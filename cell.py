class Cell:

  def __init__(self, cells):
      self.cells = cells

  def count_cells (self):
    print(self.cells)

  def __add__(self, other): # сложение = слияние клеток в одну, поглощение
    self.cells = self.cells 
    return self


  def __sub__(self, other): # удаление одной клетки из общего колличества
    self.cells = self.cells- other.cells
    return self

  def __mul__(self, other): # добавление клеток к общему колличеству, как при делениии клеток в природе
    self.cells = (self.cells + other.cells) * 2 
    return self
  
  def __truediv__(self, other):
    self.cells = self.cells / other.cells
    self.cells= int (self.cells)
    return self


cell_1 = Cell(1)
cell_2 = Cell(1)
cell_1.count_cells()

cell_1 = cell_1 + cell_2
cell_1.count_cells()


cell_1 = cell_1 * cell_2
cell_1.count_cells()

cell_1 = cell_1 - cell_2
cell_1.count_cells()

cell_3 = Cell(2)
cell_1 = cell_1 / cell_3
cell_1.count_cells()