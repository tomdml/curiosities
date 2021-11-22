from collections import Counter


def make_display(world: set, xsize: int, ysize: int) -> str:
    '''Create a printable str from the list of active cells and the board dimensions.'''

    def make_row(y):
        return ' '.join('#' if (x, y) in world else '.' for x in range(xsize))

    return '\n'.join(make_row(y) for y in range(ysize))


def neighbour_counts(world) -> Counter:
    '''For every cell that is active, and its neighbours, count how many cells are nearby'''

    def neighbours(cell):
        '''Return the locations of neighbouring cells.'''
        x, y = cell
        return [(x-1, y-1), (x, y-1), (x+1, y-1),
                (x-1, y  ),           (x+1, y  ),
                (x-1, y+1), (x, y+1), (x+1, y+1)]

    return Counter(nb for cell in world for nb in neighbours(cell))


def next_generation(world):
    possible_cells = counts = neighbour_counts(world)
    return {cell for cell in possible_cells
            if (counts[cell] == 3) or (counts[cell] == 2 and cell in world)}


if __name__ == '__main__':

    world = {(0, 2), (1, 2), (2, 2), (2, 1), (1, 0)}

    while True:
        print(make_display(world, 10, 10))
        world = next_generation(world)
        input()
        print('\n' * 100)
