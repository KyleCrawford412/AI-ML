# """
# Name:                   Rotchy Moricette and Kyle Crawford
# Date:                   December 5, 2021
# Section:                001
# Assignment:             Term Project
# Due Date:               December 6, 2021
# About this project:     We were to find specific algorithm, or individual system, in the AI literature to code and study.
#                         We decided to implement the Monte Carlo Tree Search Algorithm on a well known computer game called
#                         2048. The algorithm we selected was given by a YouTube personality known as Kite.
#
#                         **********************************************************************
#                                             === Monte Carlo Tree Search ===
#                         Essentially, MCTS uses Monte Carlo simulation to accumulate value
#                         estimates to guide towards highly rewarding trajectories in the
#                         search tree.
#
#                                                 === game_ai.py ===
#                         This file has the actual implementation of the Monte Carlo Tree Search
#                         algorithm on the game 2048. The actual code that implements it is given
#                         my the function: ai_move(board, searches_per_move, search_length)
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
# import numpy as np
# import matplotlib.pyplot as plt
#
# NUMBER_OF_MOVES = 4
# SAMPLE_COUNT = 50
#
# SPM_SCALE_PARAM = 10
# SL_SCALE_PARAM = 4
# SEARCH_PARAM = 200
#
# from game_functions import initialize_game, random_move, \
#     move_down, move_left, \
#     move_right, move_up, \
#     check_for_win, add_new_tile
#
#
# def get_search_params(move_number):
#     searches_per_move = SPM_SCALE_PARAM * (1 + (move_number // SEARCH_PARAM))
#     search_length = SL_SCALE_PARAM * (1 + (move_number // SEARCH_PARAM))
#     return searches_per_move, search_length
#
#
# def ai_move(board, searches_per_move, search_length):
#     possible_first_moves = [move_left, move_up, move_down, move_right]
#     first_move_scores = np.zeros(NUMBER_OF_MOVES)
#     for first_move_index in range(NUMBER_OF_MOVES):
#         first_move_function = possible_first_moves[first_move_index]
#         board_with_first_move, first_move_made, first_move_score = first_move_function(board)
#         if first_move_made:
#             board_with_first_move = add_new_tile(board_with_first_move)
#             first_move_scores[first_move_index] += first_move_score
#         else:
#             continue
#         for _ in range(searches_per_move):
#             move_number = 1
#             search_board = np.copy(board_with_first_move)
#             game_valid = True
#             while game_valid and move_number < search_length:
#                 search_board, game_valid, score = random_move(search_board)
#                 if game_valid:
#                     search_board = add_new_tile(search_board)
#                     first_move_scores[first_move_index] += score
#                     move_number += 1
#     best_move_index = np.argmax(first_move_scores)
#     best_move = possible_first_moves[best_move_index]
#     search_board, game_valid, score = best_move(board)
#     return search_board, game_valid
#
#
# def ai_play(board):
#     move_number = 0
#     valid_game = True
#     while valid_game:
#         move_number += 1
#         number_of_simulations, search_length = get_search_params(move_number)
#         board, valid_game = ai_move(board, number_of_simulations, search_length)
#         if valid_game:
#             board = add_two(board)
#         if check_for_win(board):
#             valid_game = False
#         print(board)
#         print(move_number)
#     print(board)
#     return np.amax(board)
#
#
# def ai_plot(move_func):
#     tick_locations = np.arange(1, 12)
#     final_scores = []
#     for _ in range(SAMPLE_COUNT):
#         print('thing is ', _)
#         board = initialize_game()
#         game_is_win = ai(board)
#         final_scores.append(game_is_win)
#     all_counts = np.zeros(11)
#     unique, counts = np.unique(np.array(final_scores), return_counts=True)
#     unique = np.log2(unique).astype(int)
#     index = 0
#
#     for tick in tick_locations:
#         if tick in unique:
#             all_counts[tick - 1] = counts[index]
#             index += 1
#
#     plt.bar(tick_locations, all_counts)
#     plt.xticks(tick_locations, np.power(2, tick_locations))
#     plt.xlabel("Score of Game", fontsize=24)
#     plt.ylabel(f"Frequency per {SAMPLE_COUNT} runs", fontsize=24)
#     plt.show()