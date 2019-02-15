from board import *;

b = Board();
b.N = 19;
s = b.starting_state();
print (b.display(s,None))
print ("");

b = Board();
b.N = 11;
s = b.starting_state();
print (b.display(s,None));
print ("");

b = Board();
b.N = 9;
s = b.starting_state();
print (b.display(s,None));
print ("");

b = Board();
b.N = 5;
s = b.starting_state();
print (b.display(s,None));
print ("");

s = list(s);
b.play_piece(s, 1, 1, True);
b.play_piece(s, 3, 2, False);
print(b.display(s,None));
print ("");

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
    can = b.can_play(s, row, col, black);
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
    b.capture(s, row, col, p);
    can = b.can_play(s, row, col, p == 'X');
    pos = b.get_position_name(row, col);
    print(b.display(s,None));
    print("{0} captured at {1}".format(p, pos));
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
    pos = b.get_position_name(row, col);
    s2 = b.play(s, row, col, black);
    if s2:
        print(b.display(s2,None));
        print("{0} played at {1}".format('Black' if black else 'White', pos));
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
