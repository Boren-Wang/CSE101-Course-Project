# your name
# your NetID
# your SBU ID number
# CSE 101
# Course Project

# In this part of the file it is very important that you write code inside
# the functions only. If you write code in between the functions, then the
# grading system will not be able to read your code or grade your work!

from battleship import *


# Part I
def is_valid_location(board, row, col):
    return None


# Part II
def place_ship(board, row, col):
    return None


# Part III
def attack(defender_board, row, col):
    return None


# Part IV
def game_status(player_board, ai_board):
    return None


# Part V
def move_ship(board, current_location, new_location):
    return None


# Part VI
def air_strike(attacker_board, defender_board, col):
    return None


# Main program
if __name__ == '__main__':
    print("PART 1: ")
    part1_board = Board(4, 6)
    row = 2
    col = 3
    print("Testing is_valid_location() with board = 4X6, row = " + str(row) + ", col = " + str(col) + " " + str(
        is_valid_location(part1_board, row, col)))
    part1_board = Board(6, 7)
    row = -3
    col = 3
    print("Testing is_valid_location() with board = 6X7, row = " + str(row) + ", col = " + str(col) + " " + str(
        is_valid_location(part1_board, row, col)))
    part1_board = Board(5, 5)
    row = 6
    col = 6
    print("Testing is_valid_location() with board = 5X5, row = " + str(row) + ", col = " + str(col) + " " + str(
        is_valid_location(part1_board, row, col)))
    print()
    print("PART 2: ")
    part2_board = Board(4, 6)
    part2_board.cells[2][2] = SHIP
    part2_board.cells[3][3] = SHIP
    row = 3
    col = 2
    print("Testing place_ship() with board = 4X6, row = " + str(row) + ", col = " + str(col) + " " + str(
        place_ship(part2_board, row, col)))
    print(str(part2_board))
    part2_board = Board(6, 7)
    part2_board.cells[3][3] = SHIP
    part2_board.cells[4][4] = SHIP
    row = 7
    col = 6
    print("Testing place_ship() with board = 6X7, row = " + str(row) + ", col = " + str(col) + " " + str(
        place_ship(part2_board, row, col)))
    print(str(part2_board))
    part2_board = Board(5, 5)
    part2_board.cells[2][2] = SHIP
    part2_board.cells[3][3] = SHIP
    part2_board.cells[4][4] = SHIP
    row = 3
    col = 3
    print("Testing place_ship() with board = 5X5, row = " + str(row) + ", col = " + str(col) + " " + str(
        place_ship(part2_board, row, col)))
    print(str(part2_board))
    print()
    print("PART 3: ")
    part3_board = Board(4, 6)
    part3_board.cells[2][2] = SHIP
    part3_board.cells[3][3] = SHIP
    part3_board.cells[0][0] = SHIP
    row = 3
    col = 2
    print("Testing attack() with board = 4X6, row = " + str(row) + ", col = " + str(col) + " " + str(
        attack(part3_board, row, col)))
    print("Board:\n" + str(part3_board))
    part3_board = Board(6, 7)
    part3_board.cells[2][2] = SHIP
    part3_board.cells[3][3] = SHIP
    part3_board.cells[4][4] = SHIP
    row = 7
    col = 6
    print("Testing attack() with board = 6X7, row = " + str(row) + ", col = " + str(col) + " " + str(
        attack(part3_board, row, col)))
    print("Board:\n" + str(part3_board))
    part3_board = Board(5, 5)
    part3_board.cells[2][2] = SHIP
    part3_board.cells[3][3] = SHIP
    part3_board.cells[4][4] = SHIP
    row = 3
    col = 3
    print("Testing attack() with board = 5X5, row = " + str(row) + ", col = " + str(col) + " " + str(
        attack(part3_board, row, col)))
    print("Board:\n" + str(part3_board))
    print()
    print("PART 4: ")
    part4_board_player = Board(4, 6)
    part4_board_player.cells[2][2] = BOMB
    part4_board_player.cells[3][3] = BOMB
    part4_board_player.cells[0][0] = BOMB
    part4_board_ai = Board(4, 6)
    part4_board_ai.cells[2][2] = SHIP
    part4_board_ai.cells[3][3] = BOMB
    part4_board_ai.cells[0][0] = SHIP
    print("Testing game_status() with\nPlayer Board:\n" + str(part4_board_player) + "\n AI Board:\n" + str(
        part4_board_ai) + "\nYour Solution: " + str(game_status(part4_board_player, part4_board_ai)))
    print()
    part4_board_player = Board(6, 7)
    part4_board_player.cells[2][2] = BOMB
    part4_board_player.cells[3][3] = SHIP
    part4_board_player.cells[0][0] = BOMB
    part4_board_ai = Board(4, 6)
    part4_board_ai.cells[2][2] = BOMB
    part4_board_ai.cells[3][3] = BOMB
    part4_board_ai.cells[0][0] = BOMB
    print("Testing game_status() with\nPlayer Board:\n" + str(part4_board_player) + "\n AI Board:\n" + str(
        part4_board_ai) + "\nYour Solution: " + str(game_status(part4_board_player, part4_board_ai)))
    print()
    part4_board_player = Board(5, 5)
    part4_board_player.cells[2][2] = BOMB
    part4_board_player.cells[3][3] = SHIP
    part4_board_player.cells[0][0] = BOMB
    part4_board_ai = Board(4, 6)
    part4_board_ai.cells[2][2] = SHIP
    part4_board_ai.cells[3][3] = BOMB
    part4_board_ai.cells[0][0] = BOMB
    print("Testing game_status() with\nPlayer Board:\n" + str(part4_board_player) + "\n AI Board:\n" + str(
        part4_board_ai) + "\nYour Solution: " + str(game_status(part4_board_player, part4_board_ai)))
    print()
    print("PART 5: ")
    part5_board = Board(4, 6)
    part5_board.cells[2][2] = SHIP
    part5_board.cells[3][3] = BOMB
    part5_board.cells[0][0] = SHIP
    cur_loc = (3, 3)
    new_loc = (4, 6)
    print("Testing move_ship() with\nPlayer Board:\n" + str(part5_board) + "\nCurrent Location = " + str(
        cur_loc) + "\nNew Location = " + str(new_loc) + "\nYour Solution: " + str(
        move_ship(part5_board, cur_loc, new_loc)))
    print("Board:\n" + str(part5_board))
    print("move_ability: " + str(part5_board.move_ability))
    print()
    part5_board = Board(6, 7)
    part5_board.cells[2][2] = SHIP
    part5_board.cells[3][3] = SHIP
    part5_board.cells[0][0] = SHIP
    cur_loc = (3, 3)
    new_loc = (7, 6)
    print("Testing move_ship() with\nPlayer Board:\n" + str(part5_board) + "Current Location = " + str(
        cur_loc) + "\nNew Location = " + str(new_loc) + "\nYour Solution: " + str(
        move_ship(part5_board, cur_loc, new_loc)))
    print("Board:\n" + str(part5_board))
    print("move_ability: " + str(part5_board.move_ability))
    print()
    part5_board = Board(5, 5)
    part5_board.cells[2][2] = SHIP
    part5_board.cells[3][3] = SHIP
    part5_board.cells[0][0] = SHIP
    cur_loc = (2, 2)
    new_loc = (5, 5)
    print("Testing move_ship() with\nPlayer Board:\n" + str(part5_board) + "Current Location = " + str(
        cur_loc) + "\nNew Location = " + str(new_loc) + "\nYour Solution: " + str(
        move_ship(part5_board, cur_loc, new_loc)))
    print("Board:\n" + str(part5_board))
    print("move_ability: " + str(part5_board.move_ability))
    print()
    print("PART 6: ")
    part6_board_defender = Board(4, 6)
    part6_board_defender.cells[2][2] = SHIP
    part6_board_defender.cells[3][3] = BOMB
    part6_board_defender.cells[0][0] = SHIP
    part6_board_attacker = Board(4, 6)
    print("Testing air_strike() with\nDefender Board:\n" + str(
        part6_board_defender) + "\nCol = 3 \nYour Solution: " + str(
        air_strike(part6_board_attacker, part6_board_defender, 3)))
    print("Defender Board:\n" + str(part6_board_defender))
    print("Attacker air_strike_ability: " + str(part6_board_attacker.air_strike_ability))
    print()
    part6_board_defender = Board(6, 7)
    part6_board_defender.cells[2][2] = SHIP
    part6_board_defender.cells[3][3] = BOMB
    part6_board_defender.cells[0][0] = SHIP
    part6_board_attacker = Board(4, 6)
    print("Testing air_strike() with\nDefender Board:\n" + str(
        part6_board_defender) + "\nCol = 6 \nYour Solution: " + str(
        air_strike(part6_board_attacker, part6_board_defender, 6)))
    print("Defender Board:\n" + str(part6_board_defender))
    print("Attacker air_strike_ability: " + str(part6_board_attacker.air_strike_ability))
    print()
    part6_board_defender = Board(6, 7)
    part6_board_defender.cells[2][2] = SHIP
    part6_board_defender.cells[3][3] = BOMB
    part6_board_defender.cells[0][0] = SHIP
    part6_board_attacker = Board(4, 6)
    print("Testing air_strike() with\nDefender Board:\n" + str(
        part6_board_defender) + "\nCol = 8 \nYour Solution: " + str(
        air_strike(part6_board_attacker, part6_board_defender, 8)))
    print("Defender Board:\n" + str(part6_board_defender))
    print("Attacker air_strike_ability: " + str(part6_board_attacker.air_strike_ability))
