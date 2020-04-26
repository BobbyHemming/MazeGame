import pygame
from Vector import Vector


def collision_detection(player, walls):
    pos = player.pos
    vel = player.vel
    size = player.size

    collision_list = []

    for wall in walls:

        wall_top = wall.rect.y
        wall_bottom = wall.rect.y + wall.rect.height
        wall_right = wall.rect.x + wall.rect.width
        wall_left = wall.rect.x

        if wall_top <= pos.y <= wall_bottom or wall_top <= pos.y + size <= wall_bottom:  # or pos.y <= wall_bottom <= pos.y + size:
            if vel.x > 0 and pos.x+size/2 < wall_left:
                if pos.x + size >= wall_left:
                    collision_list.append(wall)
            if vel.x < 0 and pos.x+size/2 > wall_right:
                if pos.x <= wall_right:
                    collision_list.append(wall)

        if wall_left <= pos.x <= wall_right or wall_left <= pos.x + size <= wall_right:  # or pos.x <= wall_left <= pos.x + size:
            if vel.y > 0 and pos.y+size/2 < wall_top:
                if pos.y + size >= wall_top:
                    collision_list.append(wall)
            if vel.y < 0 and pos.y+size/2 > wall_bottom:
                if pos.y <= wall_bottom:
                    collision_list.append(wall)

        # Edge pieces, special collisions:
        if pos.x <= wall_left <= pos.x + size:
            if vel.y > 0 and pos.y < wall_top:  # Moving down and above wall
                if pos.y + size >= wall_top + 2:
                    collision_list.append(wall)
            if vel.y < 0 and pos.y + size > wall_bottom:  # Moving up and below wall
                if pos.y <= wall_bottom - 2:
                    collision_list.append(wall)

        if pos.y <= wall_bottom <= pos.y + size:
            if vel.x > 0 and pos.x < wall_left:  # Moving down and above wall
                if pos.x + size >= wall_left + 2:
                    collision_list.append(wall)
            if vel.x < 0 and pos.x + size > wall_right:
                if pos.x <= wall_right - 2:
                    collision_list.append(wall)

    collision = False
    if len(collision_list) != 0:
        collision = True
        print(f'Collision ...!  x{len(collision_list)} at {pos.x, wall.rect.x}')

    return collision_list, collision


