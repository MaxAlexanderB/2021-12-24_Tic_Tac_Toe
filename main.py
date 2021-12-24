

#------Variables-----#

list_1 = ['.','.','.']
list_2 = ['.','.','.']
list_3 = ['.','.','.']
list_tot = [list_1, list_2, list_3]


game_is_on = True



#------Functions-----#
#------This converts the matrix with ., O and X to 0, -1 and 1----#
def convert_list(list):
    for item in list:
        for i in range(len(item)):
            if item[i] == '.':
                item[i] = 0
            elif item[i] == 'O':
                item[i] = -1
            elif item[i] == 'X':
                item[i] = 1
    return list

#------This checks for win condition if a sum of 3 or -3 is met in a row, column or diagonally----#
def check_for_win(list):
    col0 = 0
    col1 = 0
    col2 = 0
    rows = 0
    dia1 = 0
    dia2 = 0

    for item in list:
        if sum(item) == 3:
            rows += 3
        col0 += item[0]
        col1 += item[1]
        col2 += item[2]

    for i in range(len(list_tot)):
        dia1 += list[i][i]
        dia2 += list[i][(-1)*(1+i)]


    results = [col0, col1, col2, rows, dia1, dia2]

    for result in results:
        if result == 3:
            print('Congrats X won')
            return True

        elif result == -3:
            print('Congrats O won')
            return True

#-----Startgame----#
print(list_1)
print(list_2)
print(list_3)

while game_is_on == True:
    #----- Get input-----#
    try:
        user_choice = input('Please enter a row (0,1,2) a column (0,1,2) and the symbol (X, O) separated by a space (e.g 2 0 X):\n').split()
    #------Adjust list with input X or O----#
        list_tot[int(user_choice[0])][int(user_choice[1])] = user_choice[2]

    #------Generate copies of nested lists to pass to the conversion function-----#
        list_to_pass = [list_tot[0].copy(), list_tot[1].copy(), list_tot[2].copy()]

    #-----Convert list to 0's and 1's-----#
        list_converted = convert_list(list=list_to_pass)

        print(f"{list_1[0]}|{list_1[1]}|{list_1[2]}")
        print('------')
        print(f"{list_2[0]}|{list_2[1]}|{list_2[2]}")
        print('------')
        print(f"{list_3[0]}|{list_3[1]}|{list_3[2]}")

    #-----Check if there are 3 in a row----#
        if check_for_win(list=list_converted) == True:
            game_is_on = False
    except IndexError:
        print('Sorry entry not valid')
    except TypeError:
        print('Sorry entry not valid')
