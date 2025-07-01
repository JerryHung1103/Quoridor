from map import Map
from map import Pos
def swap(x):
    # Deep copy the input to avoid modifying the original
    copy = [list(coord) for coord in x]  # Explicit nested copy
    copy[0][0], copy[0][1] = copy[0][1], copy[0][0]  # Swap x/y for first coordinate
    copy[1][0], copy[1][1] = copy[1][1], copy[1][0]  # Swap x/y for second coordinate
    return copy

class Game:
  def __init__(self):
    self.map = Map(Pos(4,0), Pos(4,8), [],0)
  def is_end(self):
    if self.map.player0_pos.y == 8:
      return 1
    elif self.map.player1_pos.y == 0:
      return -1
    return 0
  def simulate(self, m, depth=0, flag = True):
    status = []
    # m.print_map()
  
    fixed_values = [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5]  # Extend this list as needed
    result = []
    for y in fixed_values:
        block = []
        for x in range(9):  # x goes from 0 to 8
            if x < 8:  # Skip the last pair if it doesn't have a next element
                block.append([[x, y], [x + 1, y]])
        result.append(block)

    # Flatten the result (if needed)
    flattened_result = [pair for block in result for pair in block]

    for x in flattened_result:
      p = m.set_barrier(x)
      if p is not None:
        status.append(p)

      p = m.set_barrier(swap(x))
      if p is not None:
        status.append(p)

    if flag:
      status += m.player0_move_down()
      status += m.player0_move_up()
      status += m.player0_move_left()
      status += m.player0_move_right()
      
    else:
      status += m.player1_move_down()
      status += m.player1_move_up()
      status += m.player1_move_left()
      status += m.player1_move_right()
     
    for s in status:
      # print(len(s.barries))
      
      if depth<2:
        # print(s.num_barries)
        self.simulate(s, depth+1, not flag)
      else:
        s.print_map()
        return

  # def player0_shortest_path(self)

