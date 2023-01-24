#otodollo
#empty "-" first player "x" second player "o"
#https://pastebin.com/wrPDZiDm
class GameLogic():
    def __init__(self):
        self.board = [
        ["-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-"],#second line
        ["-", "x", "-", "o", "-", "-", "-"],]#first line
        self.is_not_over = True

    def push(self,player,column):
        if self.is_not_over:
            if self.is_empty_place_column(column):
                row = self.get_options(column)
                self.board[row][column] = player
            else:
                column = input("give me a column")
                row = self.get_options(int(column))
                self.board[row][column] = player
        if self.is_over(column,row,player):
            if self.is_winner(column,row,player):
                print("the winner is{}".format(player))
                self.is_not_over = False

    def is_empty_place_column(self,column):
        for row in range(len(self.board)):
            if self.board[row][column] == "-":
                return True
        return False

    def get_options(self,column):
        for row in range(len(self.board)-1,-1,-1):
            if(self.board[row][column]) == "-":
                return row

    def is_full(self):
        count_empty = 0
        for line in self.board:
            for el in line:
                if el == "-":
                    count_empty += 1
        return count_empty == 0

    def is_over(self,column,row,player):
        return self.is_win_by_column(column, row, player) or \
            self.is_win_by_row(column,row,player) or \
            self.is_win_by_cross(column,row,player) or \
            self.is_full()

    def is_winner(self, column, row, player):
        # print("is_win_by_column{}".format(self.is_win_by_column(column,row,player)))
        # print("is_win_by_row{}".format(self.is_win_by_row(column,row,player)))
        # print("is_win_by_cross{}".format(self.is_win_by_cross(column,row,player)))
        return self.is_win_by_column(column, row,player) or self.is_win_by_row(column, row,player) or self.is_win_by_cross(column, row, player)

    def is_win_by_row(self, colum, row, player):
        all_match = self.count_right_match(colum,row,player) + self.count_right_match(colum,row,player)
        return all_match == 4

    def count_left_match(self,column,row,player):
        count_left = 0
        if(self.is_in_list(column-1,row)) and self.board[row][column-1] == player:
            count_left += 1
            if(self.is_in_list(column-2,row) and self.board[row][column-2]== player):
                count_left += 1
                if(self.is_in_list(column-3,row) and self.board[row][column-3] == player):
                    count_left += 1
                    if(self.is_in_list(column-4,row) and self.board[row][column-4] == player):
                        count_left += 1
        return count_left

    def count_right_match(self,column,row,player):
        count_right = 0
        if (self.is_in_list(column + 1, row)) and self.board[row][column + 1] == player:
            count_right += 1
            if (self.is_in_list(column + 2, row) and self.board[row][column + 2] == player):
                count_right += 1
                if (self.is_in_list(column + 3, row) and self.board[row][column + 3] == player):
                    count_right += 1
                    if (self.is_in_list(column + 4, row) and self.board[row][column + 4] == player):
                        count_right += 1
        return count_right

    def is_win_by_column(self, column, row, player):
        all_match = self.count_up_match(column, row, player) + self.count_down_match(column,row,player)
        return all_match == 4

    def count_up_match(self,column,row,player):
        count_up = 0
        if(self.is_in_list(column,row -1) and self.board[row - 1][column] == player):
            count_up += 1
            if(self.is_in_list(column,row -2) and self.board[row -2][column] == player):
                count_up += 1
                if(self.is_in_list(column,row-3) and self.board[row-3][column]):
                    count_up += 1
                    if(self.is_in_list(column,row-4)and self.board[row-4][column]):
                        count_up += 1
        return count_up

    def count_down_match(self,column,row,player):
        count_down = 0
        if (self.is_in_list(column, row + 1) and self.board[row + 1][column] == player):
             count_down += 1
             if (self.is_in_list(column, row + 2) and self.board[row + 2][column] == player):
                count_down += 1
                if (self.is_in_list(column, row + 3) and self.board[row + 3][column]):
                    count_down += 1
                    if (self.is_in_list(column, row + 4) and self.board[row + 4][column]):
                        count_down += 1
        return count_down

    def is_win_by_cross(self,colum,row,player):
        count_diagonal1 = self.count_diagonal_down_left(colum,row,player) + self.count_diagonal_up_right(colum,row,player) #left to right diagonal
        count_diagonal2 = self.count_diagonal_down_right(colum,row,player) + self.count_diagonal_up_left(colum,row,player) #right to left diagonal
        return count_diagonal1 == 4 or count_diagonal2 == 4

    def count_diagonal_up_right(self, column, row, player):
        count_up_right = 0
        if(self.is_in_list(column+1,row-1) and self.board[row-1][column+1])==player:
            count_up_right += 1
            if(self.is_in_list(column + 2, row -2 ) and self.board[row-2][column+2])==player:
                count_up_right += 1
                if(self.is_in_list(column + 3, row -3) and self.board[row -3][column+3])==player:
                    count_up_right += 1
                    if(self.is_in_list(column + 4, row -4 ) and self.board[row - 4][column+4])==player:
                        count_up_right += 1
        return count_up_right

    def count_diagonal_up_left(self,column,row,player):
        count_up_left = 0
        if (self.is_in_list(column - 1, row - 1) and self.board[row - 1][column - 1])==player:
            count_up_left += 1
            if (self.is_in_list(column - 2, row - 2) and self.board[row - 2][column - 2])==player:
                count_up_left += 1
                if (self.is_in_list(column - 3, row - 3) and self.board[row - 3][column - 3])==player:
                    count_up_left += 1
                    if (self.is_in_list(column - 4, row - 4) and self.board[row - 4][column - 4])==player:
                        count_up_left += 1
        return count_up_left

    def count_diagonal_down_right(self,column,row,player):
        count_down_right = 0
        if (self.is_in_list(column + 1, row + 1) and self.board[row + 1][column + 1])==player:
            count_down_right += 1
            if (self.is_in_list(column + 2, row + 2) and self.board[row + 2][column + 2])==player:
                count_down_right += 1
                if (self.is_in_list(column + 3, row + 3) and self.board[row + 3][column + 3])==player:
                    count_down_right += 1
                    if (self.is_in_list(column + 4, row + 4) and self.board[row + 4][column + 4])==player:
                        count_down_right += 1
        return count_down_right

    def count_diagonal_down_left(self,column,row,player):
        down_left = 0
        if (self.is_in_list(column - 1, row + 1) and self.board[row + 1][column - 1])==player:
            down_left += 1
            if (self.is_in_list(column - 2, row + 2) and self.board[row + 2][column - 2])==player:
                down_left += 1
                if (self.is_in_list(column - 3, row + 3) and self.board[row + 3][column - 3])==player:
                    down_left += 1
                    if (self.is_in_list(column - 4, row + 4) and self.board[row + 4][column - 4])==player:
                        down_left += 1
        return down_left

    def is_in_list(self,column,row):
        return column < 7 and column>=0 and row < 7 and row >= 0

game = GameLogic()
while True:
    column = int(input("column:"))
    player = input("player:")
    game.is_empty_place_column(column)
    row = game.get_options(column)
    print(row)
    game.push("o",2)
    if game.is_over(column,row,player):
        break



# game.get_options(1)
# print(game.board)
# isRun = True
# while isRun:
#     o_column = input("column position of O")
#     o_row = input("column position of O")
#     if(game.is_winner(o_column,o_row,"O")):
#         print("O player has won")
#         isRun = False
#     if(game.is_full()):
#         print("No one has won")
#         isRun = False
#     x_column = input("column position of O")
#     x_row = input("column position of O")
#     if(game.is_winner(x_column,x_row,"X")):
#         print("X player has won")
#         isRun = False
#     if(game.is_full()):
#         print("No one has won")
#         isRun = False
