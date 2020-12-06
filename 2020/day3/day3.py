def main():
    f = open('day3.txt', 'r')

    # 2d-array of 'rows'
    map = [list(filter(lambda c: c!= '\n', [char for char in lines])) for lines in f]

    # get num of trees encountered for the different slopes
    slope_1_1 = num_trees_encountered(map, 1, 1)
    slope_3_1 = num_trees_encountered(map, 3, 1)
    slope_5_1 = num_trees_encountered(map, 5, 1)
    slope_7_1 = num_trees_encountered(map, 7, 1)
    slope_1_2 = num_trees_encountered(map, 1, 2)

    # Resultss
    print("Num Trees (1, 1): {}".format(slope_1_1))
    print("Num Trees (3, 1): {}".format(slope_3_1))
    print("Num Trees (5, 1): {}".format(slope_5_1))
    print("Num Trees (7, 1): {}".format(slope_7_1))
    print("Num Trees (1, 2): {}".format(slope_1_2))

    print("All multiplied: {}".format(slope_1_1 * slope_3_1 * slope_5_1 * slope_7_1 * slope_1_2))


def num_trees_encountered(map, delta_x, delta_y):
    row, col = 0,0
    num_trees = 0
    while(row < len(map)):
        if col >= len(map[row]):
            col -= (len(map[row]))
        if map[row][col] == '#':
            num_trees += 1
        
        row += delta_y
        col += delta_x
    
    return num_trees

if __name__ == '__main__':
    main()