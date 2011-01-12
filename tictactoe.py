class TicTacToe:
    def __init__(self):
        self.grid = ['-','-','-','-','-','-','-','-','-']
        self.available_blocks = [1,2,3,4,5,6,7,8,9]
        self.winning_combos = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
        self.player_symbol = 'X'
        self.computer_symbol = '0'
        self.dimension = 3
        self.found_winner = False

    def display(self):
        """ Displays the current grid"""
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
        """ Checks if the current move is a valid move or not """
        if block >9 or block < 1:
            return False
        if self.grid[block-1] == "-":
                return True
        return False

    def isFullGrid(self):
        """ Checks if the grid is full or not """
        try:
            # If any "-" exists in the grid, it is not full
            temp = self.grid.index("-")
            return False
        except:
            return True

    def movePlayer(self):
        """ Asks and makes the player's move. Returns True if the player move was successful, else False"""
        block = raw_input("Enter block number: ")
        if self.isValidMove(block):
            self.grid[block-1] = self.player_symbol
            return True
        return False
            
    def moveComputer(self):
        """ Calculates and makes the computer's move. Returns True if the computer move was successful, else False"""
        if self.isValidMove(block):
            self.grid[block-1] = self.computer_symbol
            return True
        return False


t = TicTacToe()
# Game begins
while True:
    player_choice = raw_input("Do you want to play first (yes/no/exit): ")
    player_choice = player_choice.lower().strip()

    if player_choice == "yes":
        print "You play first"
        break
    elif player_choice == "no":
        print "You play second"
        break
    elif player_choice == "exit":
        print "Game Terminated."
        break
    else:
        print "Invalid Choice!!!"
        pass

# Player plays first
if player_choice == "yes":
    while not t.isFullGrid() and not t.found_winner:
        temp = raw_input("Please enter your choice of symbol (X/0): ")
        temp = str(temp).lower()
        if temp == "x":
            t.player_symbol = "X"
            t.computer_symbol = "0"
        elif temp in ["0","o"]:
            t.player_symbol = "0"
            t.computer_symbol = "X"
        t.movePlayer()
        t.moveComputer()

# Computer plays first
elif player_choice == "no":
    while not t.isFullGrid() and not t.found_winner:
        t.computer_symbol = "X"
        t.player_symbol = "0"
        
        t.moveComputer()
        t.movePlayer()
else:
    print "Game Terminated."
          

