import numpy as np
import scipy
import math

def load_input_file(file_name):
    with open(file_name, 'r') as file:
        n, H = map(int, file.readline().split())
        tile_types = np.zeros((n, n), dtype=int)
        tile_values = np.zeros((n, n), dtype=int)

        for i in range(n * n):
            if i == 0:
                continue  # the initial tile is zero type with zero value
            x, y, t, v = map(int, file.readline().split())
            tile_types[x][y] = t
            tile_values[x][y] = v

    return n, H, tile_types, tile_values


def print_tile_data(tile_types, tile_values):
    print("Tile Types:")
    print(tile_types)
    print("\nTile Values:")
    print(tile_values)

#########################

def DP_helper(n, H, tile_types, tile_values, i, j, jailbreak, doubleheal, memo):
    opt_1, opt_2, opt_3, opt_4 = -99999999
    if(memo[i][j] != None):
        return memo[i][j]

    if(i == n-1 and j == n-1):
        if(tile_types[i][j] == 1 or tile_types[i][j] == 2 or tile_types[i][j] == 3):
            return 0
        if(tile_types[i][j] == 0):
            return tile_values[i][j]

    #TWO OPTIONS RELATED TO MOVING RIGHT    
    if(j < n-1):
        #The next tile is damage
        if(tile_types[i][j+1] == 0):
            #Base case (not use a token to avoid damage)
            opt_1 = DP_helper(n, H, tile_types, tile_values, i, j+1, jailbreak, doubleheal, memo) - tile_values[i][j+1]
            #Potential 2nd Case if we have a jailbreak token, to use the jailbreak token
            if(jailbreak == True):
                opt_2 = DP_helper(n, H, tile_types, tile_values, i, j+1, False, doubleheal, memo)

        #The next tile is heal
        if(tile_types[i][j+1] == 1):
            #Base case (not use a token to 2x heals)
            opt_1 = DP_helper(n, H, tile_types, tile_values, i, j+1, jailbreak, doubleheal, memo) + tile_values[i][j+1]
            #Potential 2nd case if we have a doubleheal token, to use the doubleheal token
            if(doubleheal == True):
                opt_2 = DP_helper(n, H, tile_types, tile_values, i, j+1, jailbreak, False, memo) + tile_values[i][j+1]*2
        
        #The next tile is gain jailbreak token
        if(tile_types[i][j+1] == 2):
            opt_1 = DP_helper(n, H, tile_types, tile_values, i, j+1, True, doubleheal, memo)

        #The next tile is gain doubleheal token
        if(tile_types[i][j+1] == 3):
            opt_1 = DP_helper(n, H, tile_types, tile_values, i, j+1, jailbreak, True, memo)


    #TWO OPTIONS RELATED TO MOVING DOWN 
    if(i < n-1):
        #The next tile is damage
        if(tile_types[i+1][j] == 0):
            #Base case (not use a token to avoid damage)
            opt_1 = DP_helper(n, H, tile_types, tile_values, i+1, j, jailbreak, doubleheal, memo) - tile_values[i+1][j]
            #Potential 2nd Case if we have a jailbreak token, to use the jailbreak token
            if(jailbreak == True):
                opt_2 = DP_helper(n, H, tile_types, tile_values, i+1, j, False, doubleheal, memo)

        #The next tile is heal
        if(tile_types[i+1][j] == 1):
            #Base case (not use a token to 2x heals)
            opt_1 = DP_helper(n, H, tile_types, tile_values, i+1, j, jailbreak, doubleheal, memo) + tile_values[i+1][j]
            #Potential 2nd case if we have a doubleheal token, to use the doubleheal token
            if(doubleheal == True):
                opt_2 = DP_helper(n, H, tile_types, tile_values, i+1, j, jailbreak, False, memo) + tile_values[i+1][j]*2
        
        #The next tile is gain jailbreak token
        if(tile_types[i+1][j] == 2):
            opt_1 = DP_helper(n, H, tile_types, tile_values, i+1, j, True, doubleheal, memo)

        #The next tile is gain doubleheal token
        if(tile_types[i+1][j] == 3):
            opt_1 = DP_helper(n, H, tile_types, tile_values, i+1, j, jailbreak, True, memo)

    memo[i][j] = max(opt_1, opt_2, opt_3, opt_4)
    return memo[i][j]


def DP(n, H, tile_types, tile_values):
    resolution = False
    memo = []
    hp = DP_helper(n, H, tile_types, tile_values, False, False, memo)
    if(H >= hp):
        resolution = True
    return resolution

#########################

def write_output_file(output_file_name, result):
    with open(output_file_name, 'w') as file:
        file.write(str(int(result)))


def main(input_file_name):
    n, H, tile_types, tile_values = load_input_file(input_file_name)
    print_tile_data(tile_types, tile_values)
    result = DP(n, H, tile_types, tile_values)
    print("Result: " + str(result))
    output_file_name = input_file_name.replace(".txt", "_out.txt")
    write_output_file(output_file_name, result)


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python kill_Down_with_Trojans.py a_file_name.txt")
    else:
        main(sys.argv[1])
