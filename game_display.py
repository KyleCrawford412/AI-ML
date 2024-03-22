# """
# Name:                   Rotchy Moricette and Kyle Crawford
# Date:                   December 5, 2021
# Section:                001
# Assignment:             Term Project
# Due Date:               December 6, 2021
# About this project:     We were to find specific algorithm, or individual system, in the AI literature to code and study.
#                         We decided to implement the Monte Carlo Tree Search Algorithm on a well known computer game called
#                         2048. The algorithm we down was given by a YouTube personality known as Kite.
#
#                         **********************************************************************
#                                             === Monte Carlo Tree Search ===
#                         Essentially, MCTS uses Monte Carlo simulation to accumulate value
#                         estimates to guide towards highly rewarding trajectories in the
#                         search tree.
#
#                                                 === game_display.py ===
#                         This file has implementation of the graphics for the game. It displays
#                         the board and the actual animation of the 2048 game. It does all the
#                         frontend work and processes for the game.
#
#                         To the run game, run the main function within the game_display.py
#                         file. When executed, the board will appear, and you have a couple
#                         options. To play the game yourself, utilize the w,a,s,d keys on
#                         you keyboard to move the tiles. To allow the MCTS AI to play, press
#                         the 'p' key on you keyboard, then sit back and watch.
#                         **********************************************************************
#
# Assumptions:            No assumptions were made
# """
# from tkinter import Frame, Label, CENTER
# import time
# import game_ai
# import game_functions
#
# EDGE_LENGTH = 400
# CELL_COUNT = 4
# CELL_PAD = 10
#
# UP_KEY = "'w'"
# DOWN_KEY = "'s'"
# LEFT_KEY = "'a'"
# RIGHT_KEY = "'d'"
# AI_KEY = "'q'"
# AI_PLAY_KEY = "'p'"
#
# game_won = False
#
# LABEL_FONT = ("Verdana", 40, "bold")
#
# GAME_COLOR = "#a6bdbb"
#
# EMPTY_COLOR = "#8eaba8"
#
# TILE_COLORS = {2: "#daeddf", 4: "#9ae3ae", 8: "#6ce68d", 16: "#42ed71",
#                32: "#17e650", 64: "#17c246", 128: "#149938",
#                256: "#107d2e", 512: "#0e6325", 1024: "#0b4a1c",
#                2048: "#031f0a", 4096: "#000000", 8192: "#000000", }
#
# LABEL_COLORS = {2: "#011c08", 4: "#011c08", 8: "#011c08", 16: "#011c08",
#                 32: "#011c08", 64: "#f2f2f0", 128: "#f2f2f0",
#                 256: "#f2f2f0", 512: "#f2f2f0", 1024: "#f2f2f0",
#                 2048: "#f2f2f0", 4096: "#f2f2f0", 8192: "#f2f2f0", }
#
#
# class Display(Frame):
#     def __init__(self):
#         Frame.__init__(self)
#
#         self.grid()
#         self.master.title('2048')
#         self.master.bind("<Key>", self.key_press)
#
#         self.commands = {UP_KEY: game_functions.move_up,
#                          DOWN_KEY: game_functions.move_down,
#                          LEFT_KEY: game_functions.move_left,
#                          RIGHT_KEY: game_functions.move_right,
#                          AI_KEY: game_ai.ai_move,
#                          }
#
#         self.grid_cells = []
#         self.build_grid()
#         self.init_matrix()
#         self.draw_grid_cells()
#
#         self.mainloop()
#
#     def build_grid(self):
#         background = Frame(self, bg=GAME_COLOR,
#                            width=EDGE_LENGTH, height=EDGE_LENGTH)
#         background.grid()
#
#         for row in range(CELL_COUNT):
#             grid_row = []
#             for col in range(CELL_COUNT):
#                 cell = Frame(background, bg=EMPTY_COLOR,
#                              width=EDGE_LENGTH / CELL_COUNT,
#                              height=EDGE_LENGTH / CELL_COUNT)
#                 cell.grid(row=row, column=col, padx=CELL_PAD,
#                           pady=CELL_PAD)
#                 t = Label(master=cell, text="",
#                           bg=EMPTY_COLOR,
#                           justify=CENTER, font=LABEL_FONT, width=5, height=2)
#                 t.grid()
#                 grid_row.append(t)
#
#             self.grid_cells.append(grid_row)
#
#     def init_matrix(self):
#         self.matrix = game_functions.initialize_game()
#
#     def draw_grid_cells(self):
#         for row in range(CELL_COUNT):
#             for col in range(CELL_COUNT):
#                 tile_value = self.matrix[row][col]
#                 if not tile_value:
#                     self.grid_cells[row][col].configure(
#                         text="", bg=EMPTY_COLOR)
#                 else:
#                     self.grid_cells[row][col].configure(text=str(
#                         tile_value), bg=TILE_COLORS[tile_value],
#                         fg=LABEL_COLORS[tile_value])
#         self.update_idletasks()
#
#     def key_press(self, event):
#         valid_game = True
#         key = repr(event.char)
#         if key == AI_PLAY_KEY:
#             move_count = 0
#             while valid_game:
#                 self.matrix, valid_game = game_ai.ai_move(self.matrix,40, 30)
#                 if valid_game:
#                     self.matrix = game_functions.add_new_tile(self.matrix)
#                     self.draw_grid_cells()
#                 move_count += 1
#         if key == AI_KEY:
#             self.matrix, move_made = game_ai.ai_move(self.matrix, 20, 30)
#             if move_made:
#                 self.matrix = game_functions.add_new_tile(self.matrix)
#                 self.draw_grid_cells()
#                 move_made = False
#
#         elif key in self.commands:
#             self.matrix, move_made, _ = self.commands[repr(event.char)](self.matrix)
#             if move_made:
#                 self.matrix = game_functions.add_new_tile(self.matrix)
#                 self.draw_grid_cells()
#                 move_made = False
#
#
# if __name__ == "__main__":
#
#     gamegrid = Display()
#
#     # print("Game Statistics")
#     # print("===============\n")
#     # print(gamegrid.matrix)
#     # print("\nOutcome: ", end="")
#     # if gamegrid.gameWon is True:
#     #     print("WIN")
#     # else:
#     #     print("LOSE")
#     # print("Time taken:", gamegrid.timeTaken, "seconds")
#     # print("Total Moves:", gamegrid.numMoves)
#     #
#     # gamegrid.quit_game()
