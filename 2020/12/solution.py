from typing import List, Tuple

import math



dirs = {
    "E": (1, 0),
    "W": (-1, 0),
    "N": (0, 1),
    "S": (0, -1)
}



def load_input(input_path: str) -> str:
    with open(input_path, 'r') as input_file: return input_file.read()


def command_str_to_command(command_str: str) -> Tuple[str, int]:
    return (command_str[0], int(command_str[1:]))

def input_to_commands(inp: str) -> List[Tuple[str, int]]:
    return list(map(command_str_to_command, inp.split('\n')))


def solve_a(inp: str) -> int:
    commands = input_to_commands(inp)

    x, y = 0, 0 # east, north
    angle = 0

    for action, arg in commands:
        if action in ["E", "W", "N", "S"]:
            dir_x, dir_y = dirs[action]
            
            x += dir_x*arg
            y += dir_y*arg

        elif action == "L":
            angle += arg

        elif action == "R":
            angle -= arg

        elif action == "F":
            angle_rad = math.radians(angle)

            x += int(math.cos(angle_rad)*arg)
            y += int(math.sin(angle_rad)*arg)

    return abs(x) + abs(y)


def solve_b(inp: str) -> int:
    commands = input_to_commands(inp)

    x, y = 0, 0 # east, north
    waypoint_x, waypoint_y = 10, 1

    for action, arg in commands:
        if action in ["E", "W", "N", "S"]:
            dir_x, dir_y = dirs[action]
            
            waypoint_x += dir_x*arg
            waypoint_y += dir_y*arg

        elif action in ["L", "R"]:
            angle = math.radians(arg)
            
            if action == "R": angle *= -1

            waypoint_angle = math.atan2(waypoint_y, waypoint_x)
            waypoint_distance = (waypoint_x**2 + waypoint_y**2)**0.5

            new_waypoint_angle = waypoint_angle + angle

            waypoint_x = round(math.cos(new_waypoint_angle)*waypoint_distance) # riperino
            waypoint_y = round(math.sin(new_waypoint_angle)*waypoint_distance)

        elif action == "F":
            x += waypoint_x*arg
            y += waypoint_y*arg

    return abs(x) + abs(y)



input_ = load_input('input.txt')
test_input = load_input('test_input.txt')