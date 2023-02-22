def game():

    game = [[" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]]

    def print_game():
        print("The board:")
        print(f"""        | {game[0][0]} | {game[0][1]} | {game[0][2]} |
        | {game[1][0]} | {game[1][1]} | {game[1][2]} |
        | {game[2][0]} | {game[2][1]} | {game[2][2]} |""")

    def x_move():
        print("X move")
        column = int(input("enter the column you would like to make your move on (0, 1, 2): "))
        row = int(input("enter the row you would like to make your move on (0, 1, 2): "))

        game[row][column] = "X"
    
    def o_move():
        print("O move")
        column = int(input("enter the column you would like to make your move on (0, 1, 2): "))
        row = int(input("enter the row you would like to make your move on (0, 1, 2): "))

        game[row][column] = "O"
    
    def check_for_win(team):

        for i in range(0, 3):# ROW
            if game[i][0] == team and game[i][1] == team and game[i][2] == team:
                return team
        
        for i in range(0, 3): # COLUMN
            if game[0][i] == team and game[1][i] == team and game[2][i] == team:
                return team
        
        # DIAGONAL
        if game[0][0] == team and game[1][1] == team and game[2][2] == team:
            return team
        elif game[0][2] == team and game[1][1] == team and game[2][0] == team:
            return team
  
    while True:

        print_game()
        
        x_move()

        winner = check_for_win("X")
        if winner is not None:
            print_game()
            print(f"{winner} wins!")
            break
        winner = check_for_win("O")
        if winner is not None:
            print_game()
            print(f"{winner} wins!")
            break

        print_game()

        o_move()

        winner = check_for_win("X")
        if winner is not None:
            print_game()
            print(f"{winner} wins!")
            break
        winner = check_for_win("O")
        if winner is not None:
            print_game()
            print(f"{winner} wins!")
            break

def main():
    game()

if __name__ == '__main__':
    main()
