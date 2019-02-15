
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

        index = 4 * row;
        bitmask = 1 << col;
        if not black:
            index = index + 1;

        # mark piece on the board
        state[index] |= bitmask;
        # this flag marks that the piece was ever played on this position
        state[index+2] |= bitmask;
        return;

    # private
    def get_piece(self, state, row, col):
        if row < 0 or row >= self.N:
            raise ValueError('bad row');

        if col < 0 or col >= self.N:
            raise ValueError('bad col');

        index = 4 * row;
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

        index = 4 * row;
        bitmask = 1 << col;
        if (state[index] & bitmask) != 0:
            return True;
        if (state[index+1] & bitmask) != 0:
            return True;
        if (state[index+2] & bitmask) != 0:
            return True;
        if (state[index+3] & bitmask) != 0:
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
        p = self.get_piece(state2, row, col);
        return self.surrounded_helper(state2, row, col, p, visited);

    # private
    def get_position_name(self, row, col):
        letter = self.column_names[col];
        row_name = str(self.N - row);
        return "{0}{1}".format(letter, row_name);

    # private
    def can_play(self, state, row, col, black):
        if self.is_occupied(state, row, col):
            return False;

        if self.check_suicide(state, row, col, black):
            return False;

        return True;

    def capture(self, state, row, col, p):
        if row < 0 or row >= self.N:
            return;

        if col < 0 or col >= self.N:
            return;

        p2 = self.get_piece(state, row, col);
        if p != p2:
            return;

        # clear the pieces from the board (offsets 0 and 1) but retain the history (offsets 3 and 4)
        bitmask = ~(1 << col);
        index = 4 * row;
        state[index] &= bitmask;
        state[index+1] &= bitmask;
        self.capture(state, row+1, col, p);
        self.capture(state, row-1, col, p);
        self.capture(state, row, col+1, p);
        self.capture(state, row, col-1, p);
        return;

    def checked_capture(self, state, row, col, p):
        if row < 0 or row >= self.N:
            return;
        if col < 0 or col >= self.N:
            return;
        if self.get_piece(state, row, col) != p:
            return;
        if not self.surrounded(state, row, col):
            return;
        self.capture(state, row, col, p);
        return;

    # private
    def play(self, state, row, col, black):
        p = 'X' if black else 'O';
        if not self.can_play(state, row, col, black):
            posname = self.get_position_name(row, col);
            piecename = 'Black' if black else 'White';
            print ("{0} at {1} is an invalid move".format(piecename, posname));
            return;

        state2 = list(state);
        self.play_piece(state2, row, col, black);
        otherpiece = 'O' if black else 'X';
        self.checked_capture(state2, row-1, col, otherpiece);
        self.checked_capture(state2, row+1, col, otherpiece);
        self.checked_capture(state2, row, col-1, otherpiece);
        self.checked_capture(state2, row, col+1, otherpiece);
        return state2;

    # required by framework
    def starting_state(self):
        # 4 bits per position:
        #   1 for Black present
        #   1 for White present
        #   1 for Black *ever* present
        #   1 for White *ever* present
        #
        # 1 boolean entry defining whether the prior action was a Pass
        #
        # 1 entry for the current player (True=Black, False=White)
        #
        return tuple([0, 0, 0, 0] * self.N + [False, True]);

    # required by framework
    def display(self, state, action, _unicode=True):
        if len(state)==2:
            state = state['state'];
        pad = ' ' if self.N > 9 else '';
        all = '   ' + pad + ' '.join([self.column_names[x] for x in range(0,self.N)]) + '\n';
        for row in range(0,self.N):
            s = str(self.N-row);
            hdr = s if len(s) > 1 else ' ' + s;
            text = pad + hdr + ' ' + ' '.join([self.get_piece(state, row, col) for col in range(0,self.N)]) + pad + hdr + '\n';
            all += text;
        all += '   ' + pad + ' '.join([self.column_names[x] for x in range(0,self.N)]) + '\n';
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
        return data;

    # required by framework
    def to_json_action(self, action):
        return action;

    # required by framework
    def from_notation(self, notation):
        s = str(notation);
        if s == "pass":
            return [False];

        if len(s) < 2:
            raise ValueError("Invalid notation [{0}]".format(s));

        colname = s[0:1];
        row = s[1:];
        if not row.isdigit():
            raise ValueError("Invalid notation [{0}".format(s));

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
            state2[-2] = True;
            return tuple(state2);

        row = action[0];
        col = action[1];
        black = state[-1];
        state2 = self.play(state, row, col, black);
        state2[-1] = not black;
        return tuple(state2);

    # required by framework
    def is_legal(self, history, action):
        if action == [False]:
            return True;

        state = history[-1]
        row = action[0];
        col = action[1];
        black = state[-1];
        return self.can_play(state, row, col, black);

    # required by framework
    def legal_actions(self, history):
        state = history[-1]
        black = state[-1];

        # passing is always a legal action
        actions = [[False]];

        # scan the board for valid plays
        for row in range(0,self.N):
            for col in range(0,self.N):
                if self.can_play(state, row, col, black):
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
        return scores;

    # required by framework
    def points_values(self, history):
        return self.win_values(history);

    # required by framework
    def winner_message(self, winners):
        black = winners[1];
        white = winners[2];
        if black==white:
            return "Draw.";
        if black > white:
            return "Winner: Player 1.";
        return "Winner: Player 2.";
