def cross(A,B):
  return [a+b for a in A for b in B]
  
alpha = 'ABCDEFGHI'
digits = '123456789'
tests = ([cross(alpha,col) for col in digits] +
          [cross(row,digits) for row in alpha] +
          [cross(col_alpha,row_digit) for col_alpha in ['ABC','DEF','GHI'] for row_digit in ['123','456','789']])
#tests = [['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9']]
squares = cross(alpha,digits) 

class Sudoku:
  def __init__(self,raw_board):
    self.raw_board = raw_board
    self.board = self.parse_board()
    self.possible_values = {key: [x for x in digits] if value == ['.'] else value for key,value in self.board.items()}
  
  def parse_board(self):
      return {key: ['.'] if self.raw_board[index] == '.' else [self.raw_board[index]] for index,key in enumerate(squares)}
      
  def parse_row_collision(self):
    for single_test_group in tests:
      digits_used,digits_used_each = [],[]
      for individual_square in single_test_group:
        if len(self.possible_values[individual_square]) == 1:
          digits_used += self.possible_values[individual_square]
        else:
          digits_used_each += self.possible_values[individual_square]
    #Determined what digits have been used (digits_used) and all possible_values stored in digits_used_each to determine if there are any that are only available to use in one square of the group.
    
      digits_used_each_once = [x for x in digits_used_each if digits_used_each.count(x) == 1]
      #Now set the squares with only 1 possible value
      for individual_square in single_test_group:
        if len(self.possible_values[individual_square]) > 1:
          

          self.possible_values[individual_square] = [x for x in self.possible_values[individual_square] if x not in digits_used]
          
          for x in digits_used_each_once:
            if x in self.possible_values[individual_square]:
              self.possible_values[individual_square] = [x]
              

          
          #Set found value on board
          if len(self.possible_values[individual_square]) == 1:
            self.board[individual_square] = self.possible_values[individual_square]
            
            
  def print_board(self):
    i = 1
    for square in squares:
      print(" " + str(self.board[square][0]) + " ",end='')
      if i % 3 == 0 and i % 9 != 0:
        print(" | ",end='')
        
      if i % 9 ==0:
        print("")
      if i % 27 == 0 and i != 81:
        print(" -  -  -  +  -  -  -  +  -  -  - ")
      i += 1
      
  def solve(self):
      old_possible_values = []
      while ['.'] in self.board.values():
        self.parse_row_collision()
        if self.possible_values == old_possible_values:
          print("Could not solve")
          #break
        old_possible_values = self.possible_values
      print("Done")
      
def test():
    assert squares == ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'E9', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9', 'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'I1', 'I2', 'I3', 'I4', 'I5', 'I6', 'I7', 'I8', 'I9']
    assert tests == [['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1', 'I1'], ['A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2', 'I2'], ['A3', 'B3', 'C3', 'D3', 'E3', 'F3', 'G3', 'H3', 'I3'], ['A4', 'B4', 'C4', 'D4', 'E4', 'F4', 'G4', 'H4', 'I4'], ['A5', 'B5', 'C5', 'D5', 'E5', 'F5', 'G5', 'H5', 'I5'], ['A6', 'B6', 'C6', 'D6', 'E6', 'F6', 'G6', 'H6', 'I6'], ['A7', 'B7', 'C7', 'D7', 'E7', 'F7', 'G7', 'H7', 'I7'], ['A8', 'B8', 'C8', 'D8', 'E8', 'F8', 'G8', 'H8', 'I8'], ['A9', 'B9', 'C9', 'D9', 'E9', 'F9', 'G9', 'H9', 'I9'], ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9'], ['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9'], ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9'], ['D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9'], ['E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'E9'], ['F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9'], ['G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9'], ['H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9'], ['I1', 'I2', 'I3', 'I4', 'I5', 'I6', 'I7', 'I8', 'I9'], ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3'], ['A4', 'A5', 'A6', 'B4', 'B5', 'B6', 'C4', 'C5', 'C6'], ['A7', 'A8', 'A9', 'B7', 'B8', 'B9', 'C7', 'C8', 'C9'], ['D1', 'D2', 'D3', 'E1', 'E2', 'E3', 'F1', 'F2', 'F3'], ['D4', 'D5', 'D6', 'E4', 'E5', 'E6', 'F4', 'F5', 'F6'], ['D7', 'D8', 'D9', 'E7', 'E8', 'E9', 'F7', 'F8', 'F9'], ['G1', 'G2', 'G3', 'H1', 'H2', 'H3', 'I1', 'I2', 'I3'], ['G4', 'G5', 'G6', 'H4', 'H5', 'H6', 'I4', 'I5', 'I6'], ['G7', 'G8', 'G9', 'H7', 'H8', 'H9', 'I7', 'I8', 'I9']]
    assert game.board == {'A1': '4', 'A2': 0, 'A3': 0, 'A4': 0, 'A5': 0, 'A6': 0, 'A7': '8', 'A8': 0, 'A9': '5', 'B1': 0, 'B2': '3', 'B3': 0, 'B4': 0, 'B5': 0, 'B6': 0, 'B7': 0, 'B8': 0, 'B9': 0, 'C1': 0, 'C2': 0, 'C3': 0, 'C4': '7', 'C5': 0, 'C6': 0, 'C7': 0, 'C8': 0, 'C9': 0, 'D1': 0, 'D2': '2', 'D3': 0, 'D4': 0, 'D5': 0, 'D6': 0, 'D7': 0, 'D8': '6', 'D9': 0, 'E1': 0, 'E2': 0, 'E3': 0, 'E4': 0, 'E5': '8', 'E6': 0, 'E7': '4', 'E8': 0, 'E9': 0, 'F1': 0, 'F2': 0, 'F3': 0, 'F4': 0, 'F5': '1', 'F6': 0, 'F7': 0, 'F8': 0, 'F9': 0, 'G1': 0, 'G2': 0, 'G3': 0, 'G4': '6', 'G5': 0, 'G6': '3', 'G7': 0, 'G8': '7', 'G9': 0, 'H1': '5', 'H2': 0, 'H3': 0, 'H4': '2', 'H5': 0, 'H6': 0, 'H7': 0, 'H8': 0, 'H9': 0, 'I1': '1', 'I2': 0, 'I3': '4', 'I4': 0, 'I5': 0, 'I6': 0, 'I7': 0, 'I8': 0, 'I9': 0}
    
game = Sudoku("1....3.8.....493.7953.7.6.2...85.......9..1.6.317....849.....6138..1.459..54..8..")
game.solve()
game.print_board()
print(game.possible_values['A1'])
print(game.possible_values['A2'])
print(game.possible_values['A3'])
print(game.possible_values['B1'])
print(game.possible_values['B2'])
print(game.possible_values['B3'])
print(game.possible_values['C1'])
print(game.possible_values['C2'])
print(game.possible_values['C3'])

