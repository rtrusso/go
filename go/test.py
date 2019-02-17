from board import *;

b = Board();
b.N = 19;
s = b.starting_state();
print (b.display(s,None))

b = Board();
b.N = 11;
s = b.starting_state();
print (b.display(s,None));

b = Board();
b.N = 9;
s = b.starting_state();
print (b.display(s,None));

b = Board();
b.N = 5;
s = b.starting_state();
print (b.display(s,None));

s = list(s);
b.play_piece(s, 1, 1, True);
b.play_piece(s, 3, 2, False);
print(b.display(s,None));

def test_surr(b, s, row, col):
    surr = b.surrounded(s, row, col);
    pos = b.get_position_name(row, col);
    p = b.get_piece(s, row, col);
    print(b.display(s,None));
    print("{2} surrounded at {1}? {0}".format(surr, pos, p));
    print("");
    return;

b = Board();
b.N = 5;
s = b.starting_state();
s = list(s);
b.play_piece(s, 1, 1, False);
b.play_piece(s, 3, 1, False);
b.play_piece(s, 1, 3, False);
b.play_piece(s, 3, 3, False);
b.play_piece(s, 2, 2, True);
test_surr(b, s, 2, 2);

b = Board();
b.N = 5;
s = b.starting_state();
s = list(s);
b.play_piece(s, 2, 1, False);
b.play_piece(s, 1, 2, False);
b.play_piece(s, 2, 3, False);
b.play_piece(s, 3, 2, False);
b.play_piece(s, 2, 2, True);
test_surr(b, s, 2, 2);

b = Board();
b.N = 5;
s = b.starting_state();
s = list(s);
b.play_piece(s, 0, 2, False);
b.play_piece(s, 1, 3, False);
b.play_piece(s, 1, 1, False);
b.play_piece(s, 2, 1, False);
b.play_piece(s, 2, 3, False);
b.play_piece(s, 3, 2, False);
b.play_piece(s, 2, 2, True);
test_surr(b, s, 2, 2);

b = Board();
b.N = 5;
s = b.starting_state();
s = list(s);
b.play_piece(s, 0, 2, False);
b.play_piece(s, 1, 3, False);
b.play_piece(s, 1, 1, False);
b.play_piece(s, 2, 1, False);
b.play_piece(s, 2, 3, False);
b.play_piece(s, 3, 2, False);
b.play_piece(s, 1, 2, True);
b.play_piece(s, 2, 2, True);
test_surr(b, s, 2, 2);

b = Board();
b.N = 5;
s = b.starting_state();
s = list(s);
b.play_piece(s, 0, 0, True);
b.play_piece(s, 1, 0, True);
b.play_piece(s, 0, 1, True);
b.play_piece(s, 0, 2, False);
b.play_piece(s, 1, 1, False);
b.play_piece(s, 2, 0, False);
test_surr(b, s, 0, 0);

b = Board();
b.N = 5;
s = b.starting_state();
s = list(s);
b.play_piece(s, 0, 0, True);
b.play_piece(s, 1, 0, True);
b.play_piece(s, 0, 1, True);
b.play_piece(s, 0, 2, False);
b.play_piece(s, 1, 1, False);
test_surr(b, s, 0, 0);

b = Board();
b.N = 5;
s = b.starting_state();
s = list(s);
b.play_piece(s, 1, 1, True);
b.play_piece(s, 3, 1, True);
b.play_piece(s, 1, 3, True);
b.play_piece(s, 3, 3, True);
b.play_piece(s, 2, 2, False);
test_surr(b, s, 2, 2);

b = Board();
b.N = 5;
s = b.starting_state();
s = list(s);
b.play_piece(s, 2, 1, True);
b.play_piece(s, 1, 2, True);
b.play_piece(s, 2, 3, True);
b.play_piece(s, 3, 2, True);
b.play_piece(s, 2, 2, False);
test_surr(b, s, 2, 2);

b = Board();
b.N = 5;
s = b.starting_state();
s = list(s);
b.play_piece(s, 0, 2, True);
b.play_piece(s, 1, 3, True);
b.play_piece(s, 1, 1, True);
b.play_piece(s, 2, 1, True);
b.play_piece(s, 2, 3, True);
b.play_piece(s, 3, 2, True);
b.play_piece(s, 2, 2, False);
test_surr(b, s, 2, 2);

b = Board();
b.N = 5;
s = b.starting_state();
s = list(s);
b.play_piece(s, 0, 2, True);
b.play_piece(s, 1, 3, True);
b.play_piece(s, 1, 1, True);
b.play_piece(s, 2, 1, True);
b.play_piece(s, 2, 3, True);
b.play_piece(s, 3, 2, True);
b.play_piece(s, 1, 2, False);
b.play_piece(s, 2, 2, False);
test_surr(b, s, 2, 2);

b = Board();
b.N = 5;
s = b.starting_state();
s = list(s);
b.play_piece(s, 0, 0, False);
b.play_piece(s, 1, 0, False);
b.play_piece(s, 0, 1, False);
b.play_piece(s, 0, 2, True);
b.play_piece(s, 1, 1, True);
b.play_piece(s, 2, 0, True);
test_surr(b, s, 0, 0);

b = Board();
b.N = 5;
s = b.starting_state();
s = list(s);
b.play_piece(s, 0, 0, False);
b.play_piece(s, 1, 0, False);
b.play_piece(s, 0, 1, False);
b.play_piece(s, 0, 2, True);
b.play_piece(s, 1, 1, True);
test_surr(b, s, 0, 0);

def test_can_play(b, s, row, col, black):
    can = b.can_play_simple(s, row, col, black);
    pos = b.get_position_name(row, col);
    print(b.display(s,None));
    print("{2} can play at {1}? {0}".format(can, pos, 'Black' if black else 'White'));
    print("");
    return;

b = Board();
b.N = 5;
s = b.starting_state();
s = list(s);
b.play_piece(s, 0, 2, True);
b.play_piece(s, 1, 3, True);
b.play_piece(s, 1, 1, True);
b.play_piece(s, 2, 1, True);
b.play_piece(s, 2, 3, True);
b.play_piece(s, 3, 2, True);
b.play_piece(s, 2, 2, False);
test_surr(b, s, 2, 2);
test_can_play(b, s, 1, 2, False);
test_can_play(b, s, 1, 2, True);
test_can_play(b, s, 4, 4, False);
test_can_play(b, s, 4, 4, True);

def test_capture(b, s, row, col):
    p = b.get_piece(s, row, col);
    s = list(s);
    capped = b.capture(s, row, col, p);
    can = b.can_play_simple(s, row, col, p == 'X');
    pos = b.get_position_name(row, col);
    print(b.display(s,None));
    print("{0} captured {2} stones at {1}".format(p, pos, capped));
    print("{2} can play at {1}? {0}".format(can, pos, 'Black' if p == 'X' else 'White'));
    print("");
    return;

b = Board();
b.N = 5;
s = b.starting_state();
s = list(s);
b.play_piece(s, 0, 2, True);
b.play_piece(s, 1, 3, True);
b.play_piece(s, 1, 1, True);
b.play_piece(s, 2, 1, True);
b.play_piece(s, 2, 3, True);
b.play_piece(s, 3, 2, True);
b.play_piece(s, 1, 2, False);
b.play_piece(s, 2, 2, False);
test_surr(b, s, 2, 2);
test_capture(b, s, 2, 2);

def test_play(b, s, row, col, black):
    player = s[-1];
    if black != player:
        s2 = list(s);
        s2[-1] = black;
        s = tuple(s2);
        print("forced turn for {0}".format('Black' if black else 'White'));
    pos = b.get_position_name(row, col);
    s2 = b.play(s, row, col, black);
    if s2:
        s2 = list(s2);
        s2[-1] = not black;
        s2 = tuple(s2);
        action = (row, col);
        print(b.display(s2,action));
        print("");
        return s2;
    else:
        print("");
        return s;

b = Board();
b.N = 5;
s = b.starting_state();
s = test_play(b, s, 0, 0, True);
s = test_play(b, s, 0, 0, True);
s = test_play(b, s, 0, 0, False);
s = test_play(b, s, 0, 1, False);
s = test_play(b, s, 1, 0, False);
print("");

history = [s];
print("legal_actions:");
legal = b.legal_actions(history);
count = 0;
for a in legal:
    j = b.to_json_action(a);
    a2 = b.to_compact_action(j);
    l = b.is_legal(history, a2);
    s2 = b.next_state(history, a2);
    player = 1;
    stats = {};
    actions_states = [(a2, s2)];
    if not all((player, S) in stats for a, S in actions_states):
        count += 1;
    print("action {2}={0} legal? {1}".format(a2, l, j));
print("");

b = Board();
b.N = 5;
s = b.starting_state();
s = test_play(b, s, 2, 4, True);
print("");

b = Board();
b.N = 11;
s = b.starting_state();
s = test_play(b, s, 1, 10, True);
print("");

b = Board();
b.N = 11;
s = b.starting_state();
s = test_play(b, s, 2, 10, True);
print("");

b = Board();
b.N = 3;
s = b.starting_state();
s = test_play(b, s, 0, 2, True);
s = test_play(b, s, 1, 1, True);
s = test_play(b, s, 2, 0, True);
s = test_play(b, s, 1, 2, False);
s = test_play(b, s, 2, 1, False);
scores = b.score_territory(s);
print("territory scores: {0}".format(scores));
print("");

b = Board();
b.N = 5;
s = b.starting_state();
s = test_play(b, s, 0, 2, True);
s = test_play(b, s, 1, 1, True);
s = test_play(b, s, 2, 0, True);
s = test_play(b, s, 1, 2, False);
s = test_play(b, s, 2, 1, False);
scores = b.score_territory(s);
print("territory scores: {0}".format(scores));
s = test_play(b, s, 3, 0, False);
s = test_play(b, s, 0, 3, False);
scores = b.score_territory(s);
print("territory scores: {0}".format(scores));
print("");

def test_sim(b, plays):
    s = b.starting_state();
    h = [s];
    iter = 0;
    for p in plays:
        iter += 1;
        a = b.from_notation(p);
        if not b.is_legal(h, a):
            black = s[-1];
            print("[SKIPPED ILLEGAL] in iter {0}, {1} is not a legal play for {2}".format(iter, p, 'Black' if black else 'White'));
            print("");
            continue;
        s = b.next_state(h, a);
        print(b.display(s, a));
        h += [s];
    ended = b.is_ended(h);
    print("After {0} iterations, game {1}ended".format(iter, '' if ended else 'not '));
    print("Territory: {0}".format(b.score_territory(s)));
    black_capped = h[-1][-4];
    white_capped = h[-1][-3];
    print("{0} black stones captured, {1} white stones captured".format(black_capped, white_capped));
    if ended:
        win = b.win_values(h);
        print("win_values: {0}".format(win));
        print("win message: {0}".format(b.winner_message(win)));

b = Board();
b.N = 11;
test_sim(b, ['E5', 'E6', 'F6', 'D5', 'G5', 'E4', 'F4', 'F5', 'E5', 'pass', 'pass']);
