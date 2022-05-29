from Player import HumanPlayer, ComputerPlayer,GeniusPlayer
from Game import TicTacToe

game = TicTacToe()

x_player = HumanPlayer('X')

o_player = GeniusPlayer('O')


game.play(game, x_player, o_player)
