from Vector import Vector
gridsize = 720
game_border = 10
import pygame


def reconstruct_path(current_node, node_map):
    total_path = []
    node = current_node
    while node.came_from != 0:
        total_path.append(node)
        node = node.came_from
    total_path.reverse()
    return total_path


def a_star(start, goal, node_map, win):
    """A* algoritm finds the shortest path from start to goal"""
    """Works by minimising the heuristic score + cost of path from node to node """
    start.g_score = 0
    open_set = [start]  # records nodes with minimum A* score
    came_from = []  # Records nodes that are selected in the path

    while len(open_set) != 0:
        # Select node with lowest f_score
        f_score_list = list(map(lambda node: node.f_score, open_set))
        index = f_score_list.index(min(f_score_list))
        current = open_set[index]
        if current == goal:
            print("Success")
            return reconstruct_path(current, node_map)
        del open_set[index]
        current.draw_node(win, (255, 255, 255))
        # pygame.time.wait(1)

        distance_current_neighbour = 8
        current_neighbours = get_neighbours(node_map, current)
        for neighbour in current_neighbours:
            tentative_gscore = current.g_score + distance_current_neighbour
            if tentative_gscore < neighbour.g_score:
                current_index = find_in_list_of_list(node_map, current)
                neighbour.came_from = current
                came_from.append(current_index)
                neighbour.g_score = tentative_gscore
                neighbour.f_score = neighbour.g_score + neighbour.h_value
                if neighbour not in open_set:
                    open_set.append(neighbour)

    return 0


def get_neighbours(node_map, node):
    node_index = find_in_list_of_list(node_map, node)
    neighbours_list = []
    if Vector(game_border, game_border) < (node.pos - Vector(node.squaresize, node.squaresize)) < Vector(gridsize, gridsize):
        if not node.wall == 'left':
            neighbours_list.append(node_map[node_index[0]-1][node_index[1]])  # get neighbour to the left of current
        if not node.wall == 'top':
            neighbours_list.append(node_map[node_index[0]][node_index[1]-1])  # get neighbour below current node
        else:
            print("Blocked upwards")

    if Vector(game_border, game_border) < (node.pos + Vector(node.squaresize, node.squaresize)) < Vector(gridsize, gridsize):
        if not node_map[node_index[0]+1][node_index[1]].wall == 'left':
            neighbours_list.append(node_map[node_index[0]+1][node_index[1]])  # get neighbour to the right of current node
        else:
            print('Blocked right')
        if not node_map[node_index[0]][node_index[1]+1].wall == 'top':
            neighbours_list.append(node_map[node_index[0]][node_index[1]+1])  # get neighbour above current node
        else:
            print("Blocked bottom")

    print('-----NEW NODE-----')
    return neighbours_list


def find_in_list_of_list(mylist, char):
    for sub_list in mylist:
        if char in sub_list:
            # print("yes")
            return mylist.index(sub_list), sub_list.index(char)
        # raise ValueError("'{char}' is not in list".format(char=char))

