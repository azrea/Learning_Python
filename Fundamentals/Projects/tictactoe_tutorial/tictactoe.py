from Player import HumanPlayer, ComputerPlayer,GeniusPlayer
from Game import TicTacToe

game = TicTacToe()

x_player = GeniusPlayer('X')

o_player = HumanPlayer('O')


game.play(game, x_player, o_player)
