class TicTacToe:
    def __init__(self):
        self.grid = ['-','-','-','-','-','-','-','-','-']
        self.available_blocks = [1,2,3,4,5,6,7,8,9]
        self.winning_combos = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
        self.player_symbol = 'X'
        self.computer_symbol = '0'
        self.dimension = 3

    def display(self):
        import sys
        increment = 0
        while increment < 3:
            for eno, element in enumerate(self.grid[self.dimension*increment:self.dimension*increment+3]):
                sys.stdout.write(element)
                if eno < 2:
                    sys.stdout.write(" | ")
            if increment <2:
                sys.stdout.write('\n--|---|--\n')
            increment+=1 
        sys.stdout.write("\n")

    def isValidMove(self, block):
        if block >9 or block < 1:
            return False
        if self.grid[block-1] == "-":
                return True
        return False

    def isEmptyGrid(self):
        try:
            # If any "-" exists in the grid, it is not empty
            temp = self.grid.index("-")
            return False
        except:
            return True

    def movePlayer(self,block):
        """ Returns True if the move was successful, else False"""
        if self.isValidMove(block):
            self.grid[block-1] = self.player_symbol
            return True
        return False
            


t = TicTacToe()
t.movePlayer(2)
t.display()
