sum = 0

for d in range(0,10,0.1):
    sum += sum + 1







# import matplotlib.pyplot as plt
# import numpy as np
#
# font = {'family': 'serif',
#         'color':  'black',
#         'weight': 'normal',
#         'size': 16,
#         }
# data = [960, 715, 983, 961, 243, 973, 822, 940, 705, 829, 935, 927, 963, 960, 466, 918, 716, 953, 943, 967]
#
#
# if __name__ == '__main__':
#
#     # GAME V MOVES
#     # fig, ax = plt.subplots()
#     # ax.set_xlabel('Attempt Number')
#     # ax.set_ylabel('Total Number of Moves ')
#     # ax.set_title("Game Attempt vs. Total Number of Moves", fontdict=font)
#     #
#     # x_ticks = np.arange(0, 21, 1)
#     # plt.xticks(x_ticks)
#     # ax.plot([1, 3, 4, 6, 14, 20], [960, 983, 961, 973, 960, 967], 'o', color='green', label='Win')
#     # ax.plot([2,5,7,8,9,10,11,12,13,15,16,17,18,19], [715, 243, 822, 940, 705, 829, 935, 927, 963, 466, 918, 716, 953, 943], 'o', color='red', label='Lost')
#     # plt.legend()
#     # plt.show()
#
#     # Time chart
#     fig, ax = plt.subplots()
#     ax.set_xlabel('Attempt Number')
#     ax.set_ylabel('Total Time (seconds)')
#     ax.set_title("Game Attempt vs. Total Time in s", fontdict=font)
#
#     x_ticks = np.arange(0, 21, 1)
#     plt.xticks(x_ticks)
#     ax.plot([1, 3, 4, 6, 14, 20], [201.9726941, 208.3863702, 207.3244038, 204.3300355, 238.0315729, 202.8554593], 'o', color='green', label='Win')
#     ax.plot([2, 5, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18, 19],
#             [157.9349306, 59.5590562, 177.1946657, 197.7356983, 155.8474575, 181.4789246, 201.8582286, 201.0817164, 216.8165137, 122.7181977, 211.1986884, 163.3188293, 200.9908812, 204.2891339], 'o', color='red', label='Lost')
#     plt.legend()
#     plt.show()
#
#
#
#
#
#     # 1