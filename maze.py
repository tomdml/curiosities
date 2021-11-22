from random import shuffle, randrange
from dataclasses import dataclass


@dataclass
class Cell:
    up: bool
    down: bool
    left: bool
    right: bool
    visited: bool


def make_maze(w=16, h=8):
    cells = [[Cell(up=1, down=1, left=1, right=1, visited=0) for x in range(w)]
                                                             for y in range(h)]

 #for x in range(w):
  #      cells[0][x].up = 1
  #      cells[h-1][x].down = 1
  #  for y in range(h):
  #      cells[y][0].left = 1
  #      cells[y][w-1].right = 1

    # vis = [[0] * w + [1] for _ in range(h)] + [[1] * (w + 1)]
    # ver = [["|  "] * w + ['|'] for _ in range(h)] + [[]]
    # hor = [["+--"] * w + ['+'] for _ in range(h + 1)]

    def walk(x, y):
        cells[y][x].visited = 1

        d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
        shuffle(d)

        for (newx, newy) in d:
            print(newx, ' ', newy)
            if newx > w-1 or newx < 0 or newy > h-1 or newy < 0:
                print('breaking: invalid coord')
                continue
            if cells[newy][newx].visited:
                print('breaking: cell visited')
                continue
            if newx == x:
                if newy > y:
                    cells[y][x].up = 0
                    cells[newy][x].down = 0
                else:
                    cells[y][x].down = 0
                    cells[newy][x].up = 0
            else:
                if newx > x:
                    cells[y][x].left = 0
                    cells[y][newx].right = 0
                else:
                    cells[y][x].right = 0
                    cells[y][newx].left = 0
            walk(newx, newy)

  #  walk(randrange(w), randrange(h))
    walk(0, 0)

    return cells
  #  s = ""
  #  for (a, b) in zip(hor, ver):
  #      s += ''.join(a + ['\n'] + b + ['\n'])
  #  return s


if __name__ == '__main__':
    for row in make_maze():
        print(''.join(['|  ' if cell.left else '   ' for cell in row]))
        print(''.join(['___' if cell.down else '   ' for cell in row]))

