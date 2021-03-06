
class Board(object):
    num_players = 2
    N = 5
    column_names = 'ABCDEFGHJKLMNOPQRSTUVWXYZ';

    # private
    def play_piece(self, state, row, col, black):
        if row < 0 or row >= self.N:
            raise ValueError('bad row');

        if col < 0 or col >= self.N:
            raise ValueError('bad col');

        index = 2 * row;
        bitmask = 1 << col;
        if not black:
            index = index + 1;

        # mark piece on the board
        state[index] |= bitmask;
        return;

    # private
    def get_piece(self, state, row, col):
        if row < 0 or row >= self.N:
            raise ValueError('bad row');

        if col < 0 or col >= self.N:
            raise ValueError('bad col');

        index = 2 * row;
        bitmask = 1 << col;
        black = state[index] & bitmask;
        if black != 0:
            return 'X';

        white = state[index + 1] & bitmask;
        if white != 0:
            return 'O';

        return '.';

    # private
    def is_occupied(self, state, row, col):
        if row < 0 or row >= self.N:
            raise ValueError('bad row');

        if col < 0 or col >= self.N:
            raise ValueError('bad col');

        index = 2 * row;
        bitmask = 1 << col;
        if (state[index] & bitmask) != 0:
            return True;
        if (state[index+1] & bitmask) != 0:
            return True;

        return False;

    # private
    def visit(self, visited, row, col):
        visited[row] |= 1 << col;
        return;

    # private
    def is_visited(self, visited, row, col):
        return (visited[row] & (1 << col)) != 0;

    # private
    def surrounded_helper(self, state, row, col, flag, visited):
        if row < 0 or row >= self.N:
            return True;

        if col < 0 or col >= self.N:
            return True;

        if self.is_visited(visited, row, col):
            return True;

        p = self.get_piece(state, row, col);
        if p == '.':
            return False;

        if p != flag:
            return True;

        self.visit(visited, row, col);
        p = self.surrounded_helper(state, row+1, col, flag, visited);
        if not p:
            return p;

        p = self.surrounded_helper(state, row, col+1, flag, visited);
        if not p:
            return p;

        p = self.surrounded_helper(state, row-1, col, flag, visited);
        if not p:
            return p;

        return self.surrounded_helper(state, row, col-1, flag, visited);

    # private
    def surrounded(self, state, row, col):
        visited = [0 for x in range(self.N)];
        p = self.get_piece(state, row, col);
        return self.surrounded_helper(state, row, col, p, visited);

    # private
    def check_suicide(self, state, row, col, black):
        visited = [0 for x in range(self.N)];
        state2 = list(state);
        self.play_piece(state2, row, col, black);
        otherpiece = 'O' if black else 'X';
        captured = self.checked_capture(state2, row-1, col, otherpiece);
        captured += self.checked_capture(state2, row+1, col, otherpiece);
        captured += self.checked_capture(state2, row, col-1, otherpiece);
        captured += self.checked_capture(state2, row, col+1, otherpiece);
        p = self.get_piece(state2, row, col);
        if self.surrounded_helper(state2, row, col, p, visited):
            return None;
        state2[-3 if black else -4] += captured;
        return state2;

    # private
    def get_position_name(self, row, col):
        letter = self.column_names[col];
        row_name = str(self.N - row);
        return "{0}{1}".format(letter, row_name);

    # private
    def can_play_simple(self, state, row, col, black):
        if self.is_occupied(state, row, col):
            return False;

        if not self.check_suicide(state, row, col, black):
            return False;

        return True;

    # private
    def can_play_superko(self, history, row, col, black):
        state = history[-1];
        if self.is_occupied(state, row, col):
            return False;

        state2 = self.check_suicide(state, row, col, black);
        if not state2:
            return False;

        # positional superko
        tuple_s2 = tuple(state2[0:(self.N*2)]);
        for old_s in history:
            if old_s[0:(self.N*2)] == tuple_s2:
                return False;

        return True;

    # private
    def capture(self, state, row, col, p):
        if row < 0 or row >= self.N:
            return 0;

        if col < 0 or col >= self.N:
            return 0;

        p2 = self.get_piece(state, row, col);
        if p != p2:
            return 0;

        # clear the pieces from the board (offsets 0 and 1) but retain the history (offsets 3 and 4)
        bitmask = ~(1 << col);
        index = 2 * row;
        state[index] &= bitmask;
        state[index+1] &= bitmask;
        captured = 1;
        captured += self.capture(state, row+1, col, p);
        captured += self.capture(state, row-1, col, p);
        captured += self.capture(state, row, col+1, p);
        captured += self.capture(state, row, col-1, p);
        return captured;

    def checked_capture(self, state, row, col, p):
        if row < 0 or row >= self.N:
            return 0;
        if col < 0 or col >= self.N:
            return 0;
        if self.get_piece(state, row, col) != p:
            return 0;
        if not self.surrounded(state, row, col):
            return 0;
        return self.capture(state, row, col, p);

    def score_territory(self, state):
        visited = [0 for x in range(self.N)];
        scores = {1:0,2:0};
        for row in range(0,self.N):
            for col in range(0,self.N):
                if not self.is_visited(visited, row, col) and self.get_piece(state, row, col)=='.':
                    s = [0];
                    p = self.check_territory(state, visited, row, col, 0, s);
                    if p > 0:
                        scores[p] += s[0];
        return scores;

    def check_territory(self, state, visited, row, col, player, score):
        if row < 0 or row >= self.N:
            return player;
        if col < 0 or col >= self.N:
            return player;
        if self.is_visited(visited, row, col):
            return player;
        piece = self.get_piece(state, row, col);
        if piece != '.':
            v = 1 if piece == 'X' else 2;
            if player == 0:
                return v;
            elif v != player:
                return -1;
            else:
                return player;

        self.visit(visited, row, col);
        score[0] += 1;
        player = self.check_territory(state, visited, row-1, col, player, score);
        player = self.check_territory(state, visited, row+1, col, player, score);
        player = self.check_territory(state, visited, row, col-1, player, score);
        player = self.check_territory(state, visited, row, col+1, player, score);
        return player;

    # private
    def play(self, state, row, col, black):
        occupied = self.is_occupied(state, row, col);
        state2 = self.check_suicide(state, row, col, black);
        if occupied or not state2:
            posname = self.get_position_name(row, col);
            piecename = 'Black' if black else 'White';
            print ("{0} at {1} is an invalid move".format(piecename, posname));
            return;

        return state2;

    # required by framework
    def starting_state(self):
        # 2 bits per intersection (mutually exclusive):
        #   1 for Black present
        #   1 for White present
        #
        # 1 integer for # of black stones captured
        #
        # 1 integer for # of white stones captured
        #
        # 1 boolean entry defining whether the prior action was a Pass
        #
        # 1 entry for the current player (True=Black, False=White)
        #
        return tuple([0, 0] * self.N + [0, 0, False, True]);

    # required by framework
    def display(self, state, action, _unicode=True):
        if len(state)==2:
            state = state['state'];
        if isinstance(action, str):
            action = self.to_compact_action(action);
        pad = ' ';
        width = len(str(self.N));
        all = pad + ''.join([' ']*width) + ' ' + ' '.join([self.column_names[x] for x in range(0,self.N)]) + '\n';
        for row in range(0,self.N):
            s = str(self.N-row);
            hdr = s if len(s) == width else ' ' + s;
            pad2 = pad;
            blank = ' ';
            text = '';
            for col in range(0,self.N):
                if action and action != [False] and row == action[0] and col == action[1]:
                    text += '(' + self.get_piece(state, row, col) + ')';
                    blank = '';
                    if col == self.N-1:
                        pad2 = '';
                else:
                    text += blank + self.get_piece(state, row, col);
                    blank = ' ';
            all += pad + hdr + text + pad2 + hdr + '\n';
        all += pad + ''.join([' ']*width) + ' ' + ' '.join([self.column_names[x] for x in range(0,self.N)]) + '\n';
        if action and action != [False]:
            player = 'Black' if self.previous_player(state) == 1 else 'White';
            pos = self.to_notation(action);
            all += "{0} played {1}".format(player, pos) + '\n';
        if action and action == [False]:
            player = 'Black' if self.previous_player(state) == 1 else 'White';
            all += "{0} passed".format(player) + '\n';

        return all;

    # required by framework
    def to_compact_state(self, data):
        return tuple(data['state']);

    # required by framework
    def to_json_state(self, state):
        s = list(state);
        return {'state':s,'player':self.current_player(state)};

    # required by framework
    def to_compact_action(self, data):
        return self.from_notation(data);

    # required by framework
    def to_json_action(self, action):
        return self.to_notation(action);

    # required by framework
    def from_notation(self, notation):
        s = str(notation);
        if s == "pass":
            return [False];

        if len(s) < 2:
            return None;

        colname = s[0:1];
        row = s[1:];
        if not row.isdigit():
            return None;

        c = self.column_names.find(colname);
        r = self.N - int(row);
        if c < 0 or c >= self.N or r < 0 or r >= self.N:
            return None;

        return (r, c);

    # private
    def to_notation(self, action):
        if action == [False]:
            return "pass";

        return self.get_position_name(action[0], action[1]);

    # required by framework
    def next_state(self, history, action):
        state = history[-1];
        if action == [False]:
            state2 = list(state);
            state2[-1] = not state[-1];
            state2[-2] = True;
            return tuple(state2);

        row = action[0];
        col = action[1];
        black = state[-1];
        state2 = self.play(state, row, col, black);
        state2[-1] = not black;
        state2[-2] = False;
        return tuple(state2);

    # required by framework
    def is_legal(self, history, action):
        if action == [False]:
            return True;

        row = action[0];
        col = action[1];
        state = history[-1]
        black = state[-1];
        return self.can_play_superko(history, row, col, black);

    # required by framework
    def legal_actions(self, history):
        state = history[-1]
        black = state[-1];

        # passing is always a legal action
        actions = [[False]];

        # scan the board for valid plays
        for row in range(0,self.N):
            for col in range(0,self.N):
                if self.can_play_superko(history, row, col, black):
                    actions += [(row, col)];

        return actions;

    # required by framework
    def previous_player(self, state):
        return 2 if state[-1] else 1;

    # required by framework
    def current_player(self, state):
        return 1 if state[-1] else 2;

    # required by framework
    def is_ended(self, history):
        # Currently only the 2-pass rule is implemented.
        if len(history) < 2:
            return False;

        s1 = history[-2];
        s2 = history[-1];

        s1pass = s1[-2];
        s2pass = s2[-2];

        return s1pass and s2pass;

    # required by framework
    def win_values(self, history):
        points = self.points_values(history);
        points[1] /= self.N*self.N;
        points[2] /= self.N*self.N;
        return points;

    # required by framework
    def points_values(self, history):
        state = history[-1];
        scores = {1:0, 2:0};
        # TODO: properly implement and support both Area Scoring and Territory Scoring
        for row in range(0,self.N):
            for col in range(0,self.N):
                p = self.get_piece(state, row, col);
                if p == 'X':
                    scores[1] += 1;
                if p == 'O':
                    scores[2] += 1;
                if p == '.':
                    None;

        territory = self.score_territory(state);
        scores[1] += territory[1];
        scores[2] += territory[2];

        if scores[1] > (self.N*self.N):
            raise ValueError("black scores more than board size");
        if scores[2] > (self.N*self.N):
            raise ValueError("white scores more than board size");
        if scores[1] + scores[2] > (self.N*self.N):
            raise ValueError("total score more than board size");
        return scores;

    # required by framework
    def winning_players(self, winners):
        winners = sorted((v, k) for k, v in winners.items())
        value, winner = winners[-1]
        if value == 0.5:
            return []
        return [winner]

    # required by framework
    def winner_message(self, winners):
        winners = sorted((v, k) for k, v in winners.items())
        value, winner = winners[-1]
        if value == 0.5:
            return "Draw."
        name = 'Black' if str(winner) == '1' else 'White';
        return "Winner: {0} - Player {1}.".format(name, winner)
