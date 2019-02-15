from board import *;
from time import time;
from random import choice

t1 = time();
b = Board();
b.N = 11;
s = b.starting_state();
history = [s];
legal = b.legal_actions(history);
iter = 0;
while len(legal) > 1:
    iter += 1;
    a = choice(legal);
    j = b.to_json_action(a);
    a2 = b.to_compact_action(j);
    l = b.is_legal(history, a2);
    if not l:
        print("unexpected illegal move {0}, {1}, {2}, {3}", a, j, a2, l);
        raise ValueError("illegal move");

    stats = {};
    actions_states = [(a2, s)];
    player = b.current_player(s);
    count = 0;
    if not all((player, S) in stats for a, S in actions_states):
        count += 1;

    s = b.next_state(history, a2);

    print(b.display(s,None));
    print("{0} legal moves".format(len(legal)));
    print("{0} played at {1}".format('Black' if player == 1 else 'White', j));

    history += [s];
    legal = b.legal_actions(history);

    points = b.points_values(history);
    print("points: {0}".format(points));
    print("");

print("Legal moves: {0}".format(b.to_json_action(legal[0])));

s = b.next_state(history, legal[0]);
history += [s];
s = b.next_state(history, legal[0]);
history += [s];

ended = b.is_ended(history);
if not ended:
    print("Game not ended as expected");
print("Game ends after {0} iterations".format(iter));

win = b.win_values(history);
print("time: {0:.3f}s".format(time()-t1));
print("win_values: {0}".format(win));
print("win message: {0}".format(b.winner_message(win)));
print("");
