
import random
from search import *
from csp import *
from notebook import psource, heatmap, gaussian_kernel, show_map, final_path_colors, display_visual, plot_NQueens
import time
import tracemalloc

# start condition
case = 0

#NQueensProblem object
bfs = NQueensProblem(10)

while case != 7:
    print(f'1. Use a random starting position')
    print(f'2. Enter a starting position')
    print(f'What kind of starting position will you use: ')
    startType = input()

    if startType == '1':
        column = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'])
        row = random.randint(1, 8)
        print(f'Your random starting position is: ' + column + str(row))
    elif startType == '2':
        print(f'Please enter a column (A-H): ')
        column = input()
        print(f'Please enter a row (1-8): ')
        row = input()
        print(f'Provided starting position: ' + column + str(row))
    else:
        print(f'Invalid input.')

    print(f'1. Depth-First Search')
    print(f'2. Breadth-First Search')
    print(f'3. A*')
    print(f'4. Backtracking')
    print(f'5. Forward Checking')
    print(f'6. Arc Consistency')
    print(f'7. Exit')
    print(f'Please choose one of the search options: ')
    case = input()

    if case == '1':
        print("dpth")
    elif case == '2':
        print("brdth")
    elif case == '3':
        print("brdth")
    elif case == '4':
        print("brdth")
    elif case == '5':
        print("brdth")
    elif case == '6':
        print("brdth")
    elif case == '7':
        print(f'Ending the program.')
        break
    else:
        print(f'Please enter a valid input.')


