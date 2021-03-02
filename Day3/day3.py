def calc_trees(right, down):

    tree_count = 0
    row = 0
    col = 0

    while(row < len(data)):

            if(data[row][col] == '#'):
                tree_count += 1
            #print(row, col, data[row][col], tree_count)
            if(col >= len(data[0]) - right):
                col = col % (len(data[0]) - right)
            else:
                col += right
            row += down

            
            #check spot  
            
    return tree_count       



ins = open( "path.txt", "r" )

height = 0

data = []
for line in ins:
    height += 1
    row = list(line.rstrip())
    data.append(row)

threeByOne = calc_trees(3, 1)
oneByOne = calc_trees(1, 1)
fiveByOne = calc_trees(5, 1)
sevenByOne = calc_trees(7, 1)
oneByTwo = calc_trees(1, 2)



print(threeByOne * oneByTwo * oneByOne * fiveByOne * sevenByOne)

