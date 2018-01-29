# -*- coding: utf-8 -*-

import time
import curses
from copy import deepcopy

directions = {
    0: (1, 0),
    1: (-1, 0),
    2: (0, 1),
    3: (0, -1)
}

myscreen = curses.initscr()
myscreen.border(0)

OBSTACLE = '1'

game_map = [["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"], ["1", "2", "2", "2", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "1"], ["1", "2", "0", "1", "0", "0", "0", "0", "0", "1", "0", "0", "0", "0", "0", "0", "0", "0", "1"], ["1", "1", "1", "1", "0", "0", "0", "0", "0", "1", "0", "0", "0", "0", "0", "0", "0", "0", "1"], ["1", "0", "0", "0", "0", "0", "0", "0", "0", "1", "0", "0", "0", "0", "0", "0", "0", "0", "1"], ["1", "0", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "0", "0", "0", "1"], ["1", "0", "0", "0", "0", "2", "2", "1", "2", "2", "2", "2", "2", "2", "0", "0", "0", "0", "1"], ["1", "0", "0", "0", "0", "2", "2", "1", "2", "2", "2", "2", "2", "2", "0", "0", "0", "0", "1"], ["1", "0", "0", "0", "0", "2", "2", "2", "2", "2", "2", "2", "2", "2", "0", "0", "0", "0", "1"], ["1", "0", "0", "0", "0", "2", "2", "2", "2", "2", "2", "2", "2", "2", "0", "0", "0", "0", "1"], ["1", "0", "0", "0", "0", "2", "2", "2", "2", "2", "2", "2", "2", "2", "0", "0", "0", "0", "1"], ["1", "0", "0", "0", "0", "2", "2", "2", "2", "2", "2", "1", "2", "2", "0", "0", "0", "0", "1"], ["1", "0", "0", "0", "0", "2", "2", "2", "2", "2", "2", "1", "2", "2", "0", "0", "0", "0", "1"], ["1", "0", "0", "0", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "0", "1"], ["1", "0", "0", "0", "0", "0", "0", "0", "0", "1", "0", "0", "0", "0", "0", "0", "0", "0", "1"], ["1", "0", "0", "0", "0", "0", "0", "0", "0", "1", "0", "0", "0", "0", "0", "1", "1", "1", "1"], ["1", "0", "0", "0", "0", "0", "0", "0", "0", "1", "0", "0", "0", "0", "0", "1", "0", "2", "1"], ["1", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "2", "2", "2", "1"], ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"]]


def move(node, direction, d):
    return node[0] + direction[0], node[1]+ direction[1], d


def movable(node):
    x, y = node[0], node[1]
    if x < 0 or y < 0:
        return False
    if game_map[x][y] == OBSTACLE:
        return False
    return True


def h(node, dest):
    return max(abs(dest[0] - node[0]), abs(dest[1] - node[1]))


def find_path(start_node, dest_node):
    g = {}
    f = {}
    parent = {}
    close_list = []
    open_list = []

    open_list.append(start_node)
    cur_node = start_node
    g[start_node] = 0
    f[start_node] = 0

    while not (cur_node[0] == dest_node[0] and cur_node[1] == dest_node[1]):
        open_list = sorted(open_list)
        cur_node = open_list.pop()
        for d, direction in directions.items():
            next_node = move(cur_node, direction, d)
            if not movable(next_node) or next_node in close_list:
                continue
            if next_node[2] == cur_node[2]:
                ggg = g[cur_node] + 1
            else:
                ggg = g[cur_node] + 2
            fff = ggg + h(next_node, dest_node)
            if next_node not in open_list:
                f[next_node] = fff
                g[next_node] = ggg
                parent[next_node] = cur_node
                open_list.append(next_node)
            elif next_node in open_list and f[next_node] > fff:
                f[next_node] = fff
                g[next_node] = ggg
                parent[next_node] = cur_node
        close_list.append(cur_node)

    while cur_node != start_node:
        cur_map = deepcopy(game_map)
        cur_map[cur_node[0]][cur_node[1]] = '*'
        lo_map = ''
        for y in cur_map:
            lo_map += ' '.join(y)
            lo_map += '\n'
        myscreen.addstr(10, 0, lo_map)
        myscreen.refresh()
        time.sleep(0.2)
        myscreen.clear()
        cur_node = parent[cur_node]


if __name__ == '__main__':
    find_path((1, 1, 0), (10, 10, 0))
    myscreen.getch()
