import curses
import time
import os


def draw_rocket(rocket) -> str:
    center_index = 30
    point_from_center = 0

    for d in range(25): # down direction
        rocket = rocket + "\n"

        for i in range(60): # right direction
            if d == 0:
                if i != center_index:
                    rocket = rocket + " "
                else:
                    rocket = rocket + "*"
            elif d == 1:
                if (i != center_index - 1) and (i != center_index + 1) and (i != center_index):
                    rocket = rocket + " "       
                else:
                    rocket = rocket + "*"
        
            if d >= 2:
                if d >= 2 and d < 6:
                    point_from_center = d
                elif d >= 6 and d < 20:
                    point_from_center = 5
                elif d >= 20 :
                    point_from_center = 7

                if (i < center_index - point_from_center) or (i > center_index + point_from_center):
                    rocket = rocket + " "
                else:
                    rocket = rocket + "*"
    return rocket


def draw_fire(fire, fm_one, fm_two, fm_three) -> str:
    center_index = 30
    point_from_center = 0

    for d in range(15): # down direction
        fire = fire + "\n"

        for i in range(60):
            if d <= 8:
                point_from_center = 5
            else:
                point_from_center = 15 - d
            
            if i < center_index - point_from_center or i > center_index + point_from_center:
                fire = fire + " "
            elif d == fm_one or d == fm_two or d == fm_three:
                fire = fire + "v"
            else:
                fire = fire + "*"

    return fire


def main(stdscr):
    curses.curs_set(0)
    stdscr.clear()
    stdscr.refresh()
    fire_move_row_one = 0
    fire_move_row_two = -2
    fire_move_row_three = -4
    blank_line = "\n" * 2

    while True:
        rocket = "\n\n"
        fire = ""
        
        rocket_str = draw_rocket(rocket)
        fire_str = draw_fire(fire, fire_move_row_one, fire_move_row_two, fire_move_row_three)
        result = f"\n\n  SpaceX TV{blank_line}{rocket_str}\n{fire_str}"

        stdscr.clear()
        stdscr.addstr(0, 0, result)
        stdscr.refresh()
        time.sleep(0.04)
        fire_move_row_one = fire_move_row_one + 1 if fire_move_row_one <= 17 else 0
        fire_move_row_two = fire_move_row_two + 1 if fire_move_row_two <= 17 else -2
        fire_move_row_three = fire_move_row_three + 1 if fire_move_row_three <= 17 else -4

curses.wrapper(main)

