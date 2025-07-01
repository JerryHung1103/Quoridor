import numpy as np
import copy
class Pos:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  def x_plus(self):
    if self.x+1 <=8:
      return Pos( self.x+1, self.y)
    return None

  def x_minus(self):
    if self.x-1 >=0:
      return Pos( self.x-1, self.y)
    return None

  def y_plus(self):
    if self.y+1 <=8:
      return Pos( self.x, self.y+1)
    return None
  
  def y_minus(self):
    if self.y-1 >=0:
      return Pos( self.x, self.y-1)
    return None

  def x_plus2(self):
    if self.x+2 <=8:
      return Pos( self.x+2, self.y)
    return None

  def x_minus2(self):
    if self.x-2 >=0:
      return Pos( self.x-2, self.y)
    return None

  def y_plus2(self):
    if self.y+2 <=8:
      return Pos( self.x, self.y+2)
    return None


  def y_minus2(self):
    if self.y-2 >=0:
      return Pos( self.x, self.y-2)
    return None


  def top_right(self):
    if self.x +1 <=8 and self.y +1 <= 8:
      return Pos( self.x+1, self.y+1)
    return None

  def top_left(self):
    if self.x -1 >=0 and self.y +1 <= 8:
      return Pos( self.x-1, self.y+1)
    return None

  def bottom_left(self):
    if self.x -1 >=0 and self.y -1 >= 0:
      return Pos( self.x-1, self.y-1)
    return None

  def bottom_right(self):
    if self.x +1 <=8 and self.y -1 >= 0:
      return Pos( self.x+1, self.y-1)
    return None

class Map:
  def __init__(self, player0_pos, player1_pos, barries, num_barries):
    self.player0_pos = player0_pos
    self.player1_pos = player1_pos
    self.barries = barries
    self.num_barries = num_barries

  def set_barrier(self, location):
    start = location[0]
    mid = [(location[0][0]+location[1][0])/2, (location[0][1]+location[1][1])/2 ]
    end = location[1]
    if start in self.barries or mid in self.barries or end in self.barries:
      return None
    else:
      copy = self.barries.copy()
      copy.append(start)
      copy.append(mid)
      copy.append(end)
      return Map(self.player0_pos, self.player1_pos, copy, self.num_barries+1)


  def player0_move_up(self):
    result = []
    # moveing up
    if self.player0_pos.y != 8 and [self.player0_pos.x, self.player0_pos.y + 0.5] not in self.barries:
     
      if not ((self.player0_pos.y +1 ==self.player1_pos.y) and (self.player1_pos.x == self.player0_pos.x)):
        result.append(Map(self.player0_pos.y_plus(), self.player1_pos, self.barries, self.num_barries))
      else:
        # print('???')
        new_pos = self.player0_pos.y_plus2()
        if new_pos is not None and [self.player0_pos.x, self.player0_pos.y + 1.5] not in self.barries:
          result.append(Map(new_pos, self.player1_pos, self.barries, self.num_barries))

        new_pos = self.player0_pos.top_left()
        if new_pos is not None and [self.player0_pos.x-0.5, self.player0_pos.y + 1] not in self.barries:
          result.append(Map(new_pos, self.player1_pos, self.barries, self.num_barries))

        new_pos = self.player0_pos.top_right()
        if new_pos is not None and [self.player0_pos.x+0.5, self.player0_pos.y + 1] not in self.barries:
          result.append(Map(new_pos, self.player1_pos, self.barries, self.num_barries))
    return result


  def player0_move_down(self):
    result = []
    if self.player0_pos.y !=0 and [self.player0_pos.x, self.player0_pos.y - 0.5] not in self.barries:
      if not(self.player0_pos.y -1 ==self.player1_pos.y and self.player1_pos.x == self.player0_pos.x):
        result.append(Map(self.player0_pos.y_minus(), self.player1_pos, self.barries, self.num_barries))
      else:
        new_pos = self.player0_pos.y_minus2()
        if new_pos is not None and [self.player0_pos.x, self.player0_pos.y - 1.5] not in self.barries:
          result.append(Map(new_pos, self.player1_pos, self.barries, self.num_barries))

        new_pos = self.player0_pos.bottom_left()
        if new_pos is not None and [self.player0_pos.x-0.5, self.player0_pos.y -1 ] not in self.barries:
          result.append(Map(new_pos, self.player1_pos, self.barries, self.num_barries))

        new_pos = self.player0_pos.bottom_right()
        if new_pos is not None and [self.player0_pos.x+0.5, self.player0_pos.y - 1] not in self.barries:
          result.append(Map(new_pos, self.player1_pos, self.barries, self.num_barries))
    return result

  def player0_move_left(self):
    result = []
    if self.player0_pos.x!=0 and [self.player0_pos.x - 0.5, self.player0_pos.y] not in self.barries:
      if not (self.player0_pos.y ==self.player1_pos.y and self.player0_pos.x-1 ==self.player1_pos.x):
        result.append(Map(self.player0_pos.x_minus(), self.player1_pos, self.barries, self.num_barries))
      else:
        new_pos = self.player0_pos.x_minus2()
        if new_pos is not None and [self.player0_pos.x -1.5, self.player0_pos.y] not in self.barries:
          result.append(Map(new_pos, self.player1_pos, self.barries, self.num_barries))

        new_pos = self.player0_pos.top_left()
        if new_pos is not None and [self.player0_pos.x-1, self.player0_pos.y +0.5 ] not in self.barries:
          result.append(Map(new_pos, self.player1_pos, self.barries, self.num_barries))

        new_pos = self.player0_pos.bottom_left()
        if new_pos is not None and [self.player0_pos.x-1, self.player0_pos.y -0.5 ] not in self.barries:
          result.append(Map(new_pos, self.player1_pos, self.barries, self.num_barries))
    return result
  def player0_move_right(self):
    result = []
    if self.player0_pos.x != 8 and [self.player0_pos.x +0.5, self.player0_pos.y] not in self.barries:
      if not (self.player0_pos.y ==self.player1_pos.y and self.player0_pos.x+1 ==self.player1_pos.x):
        result.append(Map(self.player0_pos.x_plus(), self.player1_pos, self.barries, self.num_barries))
      else:
        new_pos = self.player0_pos.x_plus2()
        if new_pos is not None and [self.player0_pos.x +1.5, self.player0_pos.y] not in self.barries:
          result.append(Map(new_pos, self.player1_pos, self.barries, self.num_barries))

        new_pos = self.player0_pos.top_right()
        if new_pos is not None and [self.player0_pos.x+1, self.player0_pos.y +0.5 ] not in self.barries:
          result.append(Map(new_pos, self.player1_pos, self.barries, self.num_barries))

        new_pos = self.player0_pos.bottom_left()
        if new_pos is not None and [self.player0_pos.x+1, self.player0_pos.y -0.5 ] not in self.barries:
          result.append(Map(new_pos, self.player1_pos, self.barries, self.num_barries))
    return result



  def player1_move_up(self):
    result = []
    # moveing up
    if self.player1_pos.y != 8 and [self.player1_pos.x, self.player1_pos.y + 0.5] not in self.barries:
     
      if not ((self.player1_pos.y +1 ==self.player0_pos.y) and (self.player0_pos.x == self.player1_pos.x)):
        result.append(Map(self.player0_pos, self.player1_pos.y_plus(), self.barries, self.num_barries))
      else:
        # print('???')
        new_pos = self.player1_pos.y_plus2()
        if new_pos is not None and [self.player1_pos.x, self.player1_pos.y + 1.5] not in self.barries:
          result.append(Map(self.player0_pos, new_pos, self.barries, self.num_barries))

        new_pos = self.player1_pos.top_left()
        if new_pos is not None and [self.player1_pos.x-0.5, self.player1_pos.y + 1] not in self.barries:
          result.append(Map(self.player0_pos, new_pos, self.barries, self.num_barries))

        new_pos = self.player1_pos.top_right()
        if new_pos is not None and [self.player1_pos.x+0.5, self.player1_pos.y + 1] not in self.barries:
          result.append(Map(self.player0_pos, new_pos, self.barries, self.num_barries))
    return result


  def player1_move_down(self):
    result = []
    if self.player1_pos.y !=0 and [self.player1_pos.x, self.player1_pos.y - 0.5] not in self.barries:
      if not(self.player1_pos.y -1 ==self.player0_pos.y and self.player0_pos.x == self.player1_pos.x):
        result.append(Map(self.player0_pos, self.player1_pos.y_minus(), self.barries, self.num_barries))
      else:
        new_pos = self.player1_pos.y_minus2()
        if new_pos is not None and [self.player1_pos.x, self.player1_pos.y - 1.5] not in self.barries:
          result.append(Map(self.player0_pos, new_pos, self.barries, self.num_barries))

        new_pos = self.player1_pos.bottom_left()
        if new_pos is not None and [self.player1_pos.x-0.5, self.player1_pos.y -1 ] not in self.barries:
          result.append(Map(self.player0_pos, new_pos, self.barries, self.num_barries))

        new_pos = self.player1_pos.bottom_right()
        if new_pos is not None and [self.player1_pos.x+0.5, self.player1_pos.y - 1] not in self.barries:
          result.append(Map(self.player0_pos, new_pos, self.barries, self.num_barries))
    return result

  def player1_move_left(self):
    result = []
    if self.player1_pos.x!=0 and [self.player1_pos.x - 0.5, self.player1_pos.y] not in self.barries:
      if not (self.player1_pos.y ==self.player0_pos.y and self.player1_pos.x-1 ==self.player0_pos.x):
        result.append(Map(self.player0_pos, self.player1_pos.x_minus(), self.barries, self.num_barries))
      else:
        new_pos = self.player1_pos.x_minus2()
        if new_pos is not None and [self.player1_pos.x -1.5, self.player1_pos.y] not in self.barries:
          result.append(Map(self.player0_pos, new_pos, self.barries, self.num_barries))

        new_pos = self.player1_pos.top_left()
        if new_pos is not None and [self.player1_pos.x-1, self.player1_pos.y +0.5 ] not in self.barries:
          result.append(Map( self.player0_pos, new_pos, self.barries, self.num_barries))

        new_pos = self.player1_pos.bottom_left()
        if new_pos is not None and [self.player1_pos.x-1, self.player1_pos.y -0.5 ] not in self.barries:
          result.append(Map( self.player0_pos, new_pos, self.barries, self.num_barries))
    return result
  def player1_move_right(self):
    result = []
    if self.player1_pos.x != 8 and [self.player1_pos.x +0.5, self.player1_pos.y] not in self.barries:
      if not (self.player1_pos.y ==self.player0_pos.y and self.player1_pos.x+1 ==self.player0_pos.x):
        result.append(Map( self.player0_pos, self.player1_pos.x_plus(),  self.barries, self.num_barries))
      else:
        new_pos = self.player1_pos.x_plus2()
        if new_pos is not None and [self.player1_pos.x +1.5, self.player1_pos.y] not in self.barries:
          result.append(Map( self.player0_pos, new_pos, self.barries, self.num_barries))

        new_pos = self.player1_pos.top_right()
        if new_pos is not None and [self.player1_pos.x+1, self.player1_pos.y +0.5 ] not in self.barries:
          result.append(Map( self.player0_pos, new_pos,  self.barries, self.num_barries))

        new_pos = self.player1_pos.bottom_left()
        if new_pos is not None and [self.player1_pos.x+1, self.player1_pos.y -0.5 ] not in self.barries:
          result.append(Map( self.player0_pos, new_pos,  self.barries, self.num_barries))
    return result

  def print_map(self):
    map_str = ''
    for i in np.arange(0,8.5,0.5):
      for j in np.arange(0,8.5,0.5):
        if j%1 or (8-i)%1:
          if [j, 8-i] in self.barries:
            map_str+=' ☠ ' 
          else:
            map_str+=' · '
        else:
          if self.player0_pos.x == j and  self.player0_pos.y == 8-i:
            map_str+=f' ◉ '
          elif self.player1_pos.x == j and  self.player1_pos.y == 8-i:
            map_str+=f' ⊛ '
          else:
            map_str+=f' ⬚ '
      map_str+='\n'
    print(map_str + '\n')
    