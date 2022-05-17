from Player import HumanPlayer, ComputerPlayer
from Game import TicTacToe

game = TicTacToe()

x_player = HumanPlayer('X')

o_player = ComputerPlayer('O')

game.play(game, x_player, o_player)
