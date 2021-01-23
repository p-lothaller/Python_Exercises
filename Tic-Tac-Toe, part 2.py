class TicTacToe:
    def __init__(self):
        self.turn = "X"
        self.board = [[None for i in range(3)] for j in range(3)]

    def mark_space(self, row, column):
        # TODO
        if 0 <= row <= 2 and 0 <= column <= 2:
            if self.board[row][column] is None:
                if self.turn == "X":
                    self.board[row][column] = "X"
                    self.turn = "O"
                else:
                    self.board[row][column] = "O"
                    self.turn = "X"
            else:
                raise ValueError
        else:
            raise ValueError
                    

    def get_winner(self):
        for i in range(3):
            if (self.board[i][0] == self.board[i][1]
                    and self.board[i][1] == self.board[i][2]
                    and self.board[i][0] is not None):
                return self.board[i][0]
            if (self.board[0][i] == self.board[1][i]
                    and self.board[1][i] == self.board[2][i]
                    and self.board[0][i] is not None):
                return self.board[0][i]

        if (self.board[0][0] == self.board[1][1]
                and self.board[0][0] == self.board[2][2]
                and self.board[0][0] is not None):
            return self.board[0][0]
        if (self.board[2][0] == self.board[1][1]
                and self.board[1][1] == self.board[0][2]
                and self.board[1][1] is not None):
            return self.board[1][1]

        is_full = True
        for i in range(3):
            for j in range(3):
                if self.board[i][j] is None:
                    is_full = False

        if is_full:
            return "Tie"
        else:
            return "Ongoing"

    def __str__(self):
        row_strings = []
        for row in self.board:
            row_strings.append(' ' + ' | '.join(x or ' ' for x in row) + ' \n')

        return '-----------\n'.join(row_strings)


def main():
    game = TicTacToe()
    progress = True
    while progress == True:
        print('Player {}: input the row and column of the space you want to mark (example: 0, 0):'.format(game.turn))
        try:
            player_input = input()
            row = int(player_input[0])
            column = int(player_input[-1])
            game.mark_space(row, column)
        except ValueError:
            print('Cannot mark that space.')

        print(game)

        if game.get_winner() != "Ongoing":
            progress = False
            if game.get_winner() == "Tie":
                print(" It's a tie! ")
            else:
                print('{} has won!'.format(game.get_winner()))



if __name__ == '__main__':
  main()
