
from map import Map, Pos
print("=== Test Case 1: Basic Movement ===")
m = Map(Pos(4,4), Pos(4,6), [], 0)
print("Initial map:")
m.print_map()

# Player 0 moves
print("Player 0 moves up:")
for c in m.player0_move_up():
    c.print_map()

print("Player 0 moves right:")
for c in m.player0_move_right():
    c.print_map()

# Player 1 moves
print("Player 1 moves down:")
for c in m.player1_move_down():
    c.print_map()

print("Player 1 moves left:")
for c in m.player1_move_left():
    c.print_map()


print("\n=== Test Case 2: Jump Over Opponent ===")
m = Map(Pos(4,4), Pos(4,5), [], 0)
print("Initial map:")
m.print_map()

print("Player 0 jumps up over Player 1:")
for c in m.player0_move_up():
    c.print_map()

print("Player 1 jumps down over Player 0:")
for c in m.player1_move_down():
    c.print_map()


print("\n=== Test Case 3: Blocked by Barrier ===")
m = Map(Pos(2,2), Pos(6,6), [], 0)
m = m.set_barrier([[2,2.5], [2.5,2.5]])  # Barrier to right of Player 0
m = m.set_barrier([[6,5.5], [6.5,5.5]])  # Barrier above Player 1
print("Initial map:")
m.print_map()

print("Player 0 blocked right:")
for c in m.player0_move_right():
    c.print_map()  # Should be empty

print("Player 1 blocked up:")
for c in m.player1_move_up():
    c.print_map()  # Should be empty

print("\n=== Test Case 4: Diagonal Alternatives ===")
m = Map(Pos(3,3), Pos(3,4), [], 0)
m = m.set_barrier([[3,3.5], [3.5,3.5]])  # Barrier above Player 0
print("Initial map:")
m.print_map()

print("Player 0 diagonal options when blocked straight up:")
for c in m.player0_move_up():
    c.print_map()  # Should show top-left and top-right moves

print("\n=== Test Case 5: Edge Cases ===")
m = Map(Pos(0,0), Pos(8,8), [], 0)  # Players in corners
print("Initial map:")
m.print_map()

print("Player 0 at (0,0) attempts left and down:")
print("Left moves:", len(m.player0_move_left()))  # Should be 0
print("Down moves:", len(m.player0_move_down()))  # Should be 0

print("Player 1 at (8,8) attempts right and up:")
print("Right moves:", len(m.player1_move_right()))  # Should be 0
print("Up moves:", len(m.player1_move_up()))  # Should be 0


print("\n=== Test Case 8: Barrier Between Players ===")
m = Map(Pos(4,4), Pos(4,5), [], 0)
m = m.set_barrier([[4,4.5], [4.5,4.5]])
print("Initial map:")
m.print_map()

print("Player 0 attempts to jump up through barrier:")
for c in m.player0_move_up():
    c.print_map()  # Should be empty - completely blocked