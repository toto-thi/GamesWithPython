def drawField(Field):
    for row in range(5):
        getRow = int(row/2)
        if row % 2 ==0:
            for column in range(5):
                getCol = int(column/2)
                if column %2 == 0:
                    if column != 4:           
                        print(Field[getCol][getRow], end="")
                    else:
                        print(Field[getCol][getRow])
                else:
                    print("|", end="")
        else: 
            print("-----")

player = 1
currentField = [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]
drawField(currentField)

while(True):
    print("Player ",player)

    MoveRow = int(input("Please enter row: "))
    MoveCol = int(input("Please enter column: "))

    if player == 1:
        if currentField[MoveCol][MoveRow] == " ":
            currentField[MoveCol][MoveRow] = "X"
            player = 2
    else:
        if currentField[MoveCol][MoveCol] == " ":
            currentField[MoveCol][MoveRow] = "O"
            player = 1
    drawField(currentField)