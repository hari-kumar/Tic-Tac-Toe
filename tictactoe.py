from random import choice

class TicTacToe:
    def __init__(self):
        self.grid = ['-','-','-','-','-','-','-','-','-']
        self.available_blocks = [1,2,3,4,5,6,7,8,9]
        self.winning_combos = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
        self.player_symbol = 'x'
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
            print "Game Draw!"
            return True

    def gotWinner(self):
        """ Checks if the current grid snapshot has a winner or not"""
        for combo in self.winning_combos:
            if self.grid[combo[0]-1]==self.grid[combo[1]-1]==self.grid[combo[2]-1]==self.player_symbol:
                print "You have won the game!"
                return True
            if self.grid[combo[0]-1]==self.grid[combo[1]-1]==self.grid[combo[2]-1]==self.computer_symbol:
                print "You have lost the game!"
                return True
        return False

        

    def movePlayer(self):
        """ Asks and makes the player's move. Returns True if the player move was successful, else False"""
        block = raw_input("Enter block number: ")
        block = int(block)
        if self.isValidMove(block):
            self.grid[block-1] = self.player_symbol
            self.available_blocks.remove(block)
            return True
        return False
            
    def moveComputer(self):
        """ Calculates and makes the computer's move. Returns True if the computer move was successful, else False"""
        # lOGIC AS PER THE STRATEGY MENTIONED IN WIKIPEDIA. http://en.wikipedia.org/wiki/Tic-tac-toe

        # 1.If the player has two in a row, play the third to get three in a row.
        computer_symbol_list = [i+1 for i,symbol in enumerate(self.grid) if symbol == self.computer_symbol]
        for combo in self.winning_combos:
            intersect_symbol = list(set(combo).intersection(set(computer_symbol_list)))
            intersect_available =  list(set(combo).intersection(set(self.available_blocks)))
            if len(intersect_symbol) == 2 and len(intersect_available) > 0:
                difference_symbol = list(set(combo) - set(intersect_symbol))[0]
                self.grid[difference_symbol - 1] = self.computer_symbol
                self.available_blocks.remove(difference_symbol)
                return True
            else:
                pass


        # 2. If the opponent has two in a row, play the third to block them.
        player_symbol_list = [i+1 for i,symbol in enumerate(self.grid) if symbol == self.player_symbol]
        for combo in self.winning_combos:
            intersect_symbol = list(set(combo).intersection(set(player_symbol_list)))
            intersect_available =  list(set(combo).intersection(set(self.available_blocks)))
            if len(intersect_symbol) == 2 and len(intersect_available) > 0:
                difference_symbol = list(set(combo) - set(intersect_symbol))[0]
                self.grid[difference_symbol - 1] = self.computer_symbol
                self.available_blocks.remove(difference_symbol)
                return True
            else:
                pass

        # 3.  Create an opportunity where you can win in two ways.
      
        # 4. Block opponent's fork

        

        
        for corner in [6,8]:
            print "before corner case"
            print self.grid[corner], self.grid[8%corner]
            if self.grid[corner] == self.player_symbol and self.grid[8%corner] == self.player_symbol and self.grid[4] == self.computer_symbol:
                print "blocking fork"
                possible_mid = list(set(self.available_blocks).intersection([2,4,6,8]))
                try:
                    posn = choice(possible_mid)
                except:
                    posn = choice(self.available_blocks)
                self.grid[posn-1] = self.computer_symbol
                self.available_blocks.remove(posn)
                return True

        for corner in [0,2,6,8]:
            if self.grid[corner] != "-" and self.grid[8-corner] != "-":
                possible_mid = list(set(self.available_blocks).intersection([2,4,6,8]))
                possible_corner = list(set(self.available_blocks).intersection([1,3,7,9]))
                try:
                    posn = choice(possible_corner)
                except:
                    posn = choice(self.available_blocks)
                print "Corner Case aggresive"
                self.grid[posn-1] = self.computer_symbol
                self.available_blocks.remove(posn)
                return True
           
            if self.grid[corner] == "-":
                if self.grid[8-corner] == "-":
                    self.grid[8-corner] = self.computer_symbol
                    self.available_blocks.remove(9-corner)
                    return True 


        
        if self.grid[4] == "-":
            print "Center Case"
            self.grid[4] = self.computer_symbol
            self.available_blocks.remove(5)
            return True

        if self.grid[corner] == "-":
                if self.grid[8-corner] == "-":
                    self.grid[8-corner] = self.computer_symbol
                    self.available_blocks.remove(9-corner)
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
    temp = raw_input("Please enter your choice of symbol (x/0): ")
    temp = str(temp).lower()
    if temp == "x":
        t.player_symbol = "x"
        t.computer_symbol = "0"
    elif temp in ["0","o"]:
        t.player_symbol = "0"
        t.computer_symbol = "x"
    while True:
        if not t.isFullGrid() and not t.gotWinner():
            t.movePlayer()
            t.display()
        else:
            break
        if not t.isFullGrid() and not t.gotWinner():
            t.moveComputer()
            print "Computer made its move"
            t.display()
        else:
            break
            

# Computer plays first
elif player_choice == "no":
    t.computer_symbol = "x" 
    t.player_symbol = "0"
    while True:
        if not t.isFullGrid() and not t.gotWinner():
            t.moveComputer()
            print "Computer made its move"
            t.display()
        else:
            break
        if not t.isFullGrid() and not t.gotWinner():
            t.movePlayer()
            t.display()
        else:
            break
else:
    print "Game Terminated."
          

