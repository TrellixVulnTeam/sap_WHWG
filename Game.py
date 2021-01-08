from Pawn import Pawn


class Game(Pawn):

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.turn = 1
        self.board = [[' '] * 8] * 4

    def start_game(self):
        if self.player1 and self.player2:
            print('Welcome to SAP')
            user_input = input('Enter Y to start a new game')
            if user_input.lower() == 'y':
                self.fill_board()
                self.display_board()
                self.display_turn()
            else:
                print('SHUT IT DOWN')

    def fill_board(self):
        self.board.insert(0, ['X'] * 8)
        self.board.insert(1, ['X'] * 8)
        self.board.append(['X'] * 8)
        self.board.append(['X'] * 8)

    def display_board(self):
        for row in self.board:
            print(row)

    def check_winning_condition(self):
        for row in self.board:
            if 'W' in row[0] or 'W' in row[1]:
                print('Player 1 Wins!')
            elif 'E' in row[6] or 'E' in row[7]:
                print('Player 2 Wins!')

    def display_turn(self):
        if self.turn % 2 != 0:
            print("Player 1 Turn:")
        else:
            print("Player 2 Turn:")

    @staticmethod
    def select_pawn():
        selected_pawn = input('Select a Pawn:')
        return int(selected_pawn)

    @staticmethod
    def start_game_message():
        print("Are you the smartest pawn?")


g1 = Game('Doak', 'Heidi')
pawn = Pawn()
g1.start_game_message()
g1.start_game()


