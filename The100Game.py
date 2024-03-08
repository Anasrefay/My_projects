# Purpose: Two players start from 0 and alternatively add a number from 1 to 10 to the sum
# The player who reaches 100 wins.
print("***********************************")
print("  *** Welcome to this program ***")
print("    ***************************")
print("      ***********************")
print("      ****** 100 Game *******")
print("      ***********************")
Total_num = 0
while True:
    #Function that gets a number from player 1.
    def player1_number():
        global player1_num
        #To reject any string player 1 may input.
        try:
            player1_num = int(input("Player 1: Please enter a number "))
        except ValueError:
            print()
            print("** Invalid input **")
            print()
            player1_number()
        #To check if the number is between (1-10)
        if player1_num < 1 or player1_num > 10:
            print()
            print("** Please enter a number from ( 1 - 10 ) **")
            print()
            player1_number()
    player1_number()
    #Function that adds the numbers of player 1.
    def addition_player1():
        global Total_num
        Total_num += player1_num
        if Total_num == 100:
            print()
            print("** Player 1 wins! **")
            print()
            print("*** Thank you for playing my game ^-^ ***")
            exit()
        #here if player 1 enters a number that makes Total_num more than 100.
        #then make player 1 enter another number
        elif Total_num > 100:
            if 100-(Total_num - player1_num) == 1:
                print()
                print("** ENTER THE WINNING NUMBER! **")#Note: the winning number is 1.
                print()
                Total_num -= player1_num
                player1_number()
                addition_player1()
            else:
                print()
                print("** Please enter a number from ( 1 -",100-(Total_num - player1_num),") **")
                print()
                Total_num -= player1_num
                player1_number()
                addition_player1()
    addition_player1()
    #Function that gets a number from player 2.
    def player2_number():
        global player2_num
        #To reject any string player 2 may input.
        try:
            player2_num = int(input("Player 2: Please enter a number "))
        except ValueError:
            print()
            print("** Invalid input **")
            print()
            player2_number()
        #To check if the number is between (1-10)
        if player2_num < 1 or player2_num > 10:
            print()
            print("** Please enter a number from ( 1 - 10 )**")
            print()
            player2_number()
    player2_number()
    #Function that adds the numbers of player 2.
    def addition_player2():
        global Total_num
        Total_num += player2_num
        if Total_num == 100:
            print()
            print("** Player 2 wins! **")
            print()
            print("*** Thank you for playing my game ^-^ ***")
            exit()
        #here if player 2 enters a number that makes Total_num more than 100.
        #then make player 2 enter another number
        elif Total_num > 100:
            if 100-(Total_num - player2_num) == 1:
                print()
                print("** ENTER THE WINNING NUMBER! **")#Note: the winning number is 1.
                print()
                Total_num -= player2_num
                player2_number()
                addition_player2()
            else:
                print()
                print("** Please enter a number from ( 1 -",100-(Total_num - player2_num),") **")
                print()
                Total_num -= player2_num
                player2_number()
                addition_player2()
    addition_player2()
    print()
    print("Current total: ", Total_num)
    print()

