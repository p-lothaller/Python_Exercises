class TicTacToe:

    def __init__(self):
        self.board = [[None, None, None],[None, None, None],[None, None, None]]
        self.turn = 'X'

    def mark_space(self, row, column):
        if 0<= row <=3 and 0 <= column <= 3 and self.board[row][column] is None:
            self.board[row][column] = self.turn
            if self.turn == 'X':
                self.turn = 'O'
            else:
                self.turn = 'X'
        else:
            return "Invalid Move"

    def get_winner(self):
        game = True

        if game is True:
            for i in range(3):
                if self.board[i].count('X') == 3 or self.board[i].count('O') == 3:
                    game = False
                    return print(self.board[i][0], 'is the winner!')
                    break
            
            for j in range(3):
                column_lst = []
                for k in range(3):
                    column_lst.append(self.board[k][j])

                if column_lst.count('X') == 3 or column_lst.count('O') == 3:
                    game = False
                    return print(column_lst[0], 'is the winner!')
                    break

            diag_lst = []
            for l in range(3):
                diag_lst.append(self.board[l][l])
                if diag_lst.count('X') == 3 or diag_lst.count('O') == 3:
                    game = False
                    return print(diag_lst[0], 'is the winner!')
                    break
                
            diag_lst1 = []
            for m in range(3):
                diag_lst1.append(self.board[m][-m-1])
                if diag_lst1.count('X') == 3 or diag_lst1.count('O') == 3:
                    game = False
                    return print(diag_lst1[0], 'is the winner!')
                    break  

            if game is True and (None in self.board[0] or None in self.board[1] or None in self.board[2]):
                return print('Ongoing')
            else:
                return print('Tie')
            

    def __str__(self):
         line_1 = (('{} | {} | {}\n'+'-----------\n').format(self.board[0][0],self.board[0][1],self.board[0][2]))
         line_2 = (('{} | {} | {}\n' + '-----------\n').format(self.board[1][0],self.board[1][1],self.board[1][2]))
         line_3 = (('{} | {} | {}\n').format(self.board[2][0],self.board[2][1],self.board[2][2]))
         return (line_1 + line_2 + line_3)

ttt = TicTacToe()
ttt = TicTacToe()
ttt.mark_space(0, 0)
ttt.mark_space(0, 1)
ttt.mark_space(1, 0)
ttt.mark_space(2, 0)
ttt.mark_space(1, 1)
ttt.mark_space(2, 2)
ttt.mark_space(2, 1)
ttt.mark_space(1, 2)
ttt.mark_space(0, 2)
ttt.get_winner()


