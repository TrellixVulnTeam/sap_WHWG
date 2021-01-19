from Pawn import Pawn


class Game(Pawn):

    def __init__(self, player1, player2):
        super().__init__()
        self.player1 = player1
        self.player2 = player2
        self.turn = 1
        self.board = [[' '] * 8 for _ in range(8)]

    def start_game(self):
        print(self.board)
        if self.player1 and self.player2:
            print('Welcome to SAP')
            user_input = input('Enter Y to start a new game')
            if user_input.lower() == 'y':
                self.fill_top_board()
                self.fill_bot_board()
                self.display_board()
                self.play_game()
            else:
                print('SHUT IT DOWN')

    def fill_top_board(self):
        top = 0
        while top < 8:
            self.board[0][top] = 'W'
            top += 1
        bot = 0
        while bot < 8:
            self.board[1][bot] = 'W'
            bot += 1

    def fill_bot_board(self):
        top = 0
        while top < 8:
            self.board[6][top] = 'E'
            top += 1
        bot = 0
        while bot < 8:
            self.board[7][bot] = 'E'
            bot += 1

    def display_board(self):
        for row in self.board:
            print(row)

    def winning_condition(self):
        for row in self.board:
            if 'W' in row[0] or 'W' in row[1] or 'E' in row[6] or 'E' in row[7]:
                return True

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

    def game_over(self):
        if self.winning_condition():
            return True

    def play_game(self):
        self.game_turn()

    def game_turn(self):
        self.display_turn()
        self.select_pawn()
        print(self.board)
        self.display_board()
        self.move_pawn()
        self.display_board()

    def select_pawn(self):
        selected_row = int(input('Select a Row:'))
        selected_pawn = int(input('Select a Pawn:'))
        self.board[selected_row][selected_pawn] = 'P'

    def move_pawn(self):
        select_row = input('Select a Row:')
        select_spot = input('Select a Spot:')
        self.board[int(select_row) - 1][int(select_spot) - 1] = 'P'

    @staticmethod
    def start_game_message():
        print("Are you the smartest pawn?")


g1 = Game('Doak', 'Heidi')
pawn = Pawn()
g1.start_game_message()
g1.start_game()
