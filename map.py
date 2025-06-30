class Pos:
  def __init__(self, x, y):
    self.x = x
    self.y = y

class Map:
  def __init__(self, player0_pos, player1_pos, barries):
    self.player0_pos = player0_pos
    self.player1_pos = player1_pos
    self.barries = barries

  def set_barrier(self, location):
    self.barries.append(location[0])
    self.barries.append(location[1])

  def player0_move_up(self):
    if self.player0_pos.y != 8 and [self.player0_pos.x, self.player0_pos.y + 0.5] not in self.barries:
      self.player0_pos.y+=1
      return True
    return False
  def player0_move_down(self):
    if self.player0_pos.y !=0 and [self.player0_pos.x, self.player0_pos.y - 0.5] not in self.barries:
      self.player0_pos.y-=1
      return True
    return False

  def player0_move_left(self):
    if self.player0_pos.x!=0 and [self.player0_pos.x - 0.5, self.player0_pos.y] not in self.barries:
      self.player0_pos.x-=1
      return True
    return False
  def player0_move_right(self):
    if self.player0_pos.x != 8 and [self.player0_pos.x +0.5, self.player0_pos.y] not in self.barries:
      self.player0_pos.x+=1
      return True
    return False


  def player1_move_up(self):
    if self.player1_pos.y != 8 and [self.player1_pos.x, self.player1_pos.y + 0.5] not in self.barries:
      self.player1_pos.y+=1
      return True
    return False
  def player1_move_down(self):
    if self.player1_pos.y !=0 and [self.player1_pos.x, self.player1_pos.y - 0.5] not in self.barries:
      self.player1_pos.y-=1
      return True
    return False

  def player1_move_left(self):
    if self.player1_pos.x!=0 and [self.player1_pos.x - 0.5, self.player1_pos.y] not in self.barries:
      self.player1_pos.x-=1
      return True
    return False
  def player1_move_right(self):
    if self.player1_pos.x != 8 and [self.player1_pos.x +0.5, self.player1_pos.y] not in self.barries:
      self.player1_pos.x+=1
      return True
    return False

  def print_map(self):
    for i in range(9):
      for j in range(9):
        if self.player1_pos.x == 8-i and  self.player1_pos.y == j:
          print(f'|O|', end=' ')
        elif self.player0_pos.x == 8-i and  self.player0_pos.y == j:
          print(f'|X|', end=' ')
        else:
          print(f'|_|', end=' ')
      print('')
    print()
