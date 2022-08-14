"""
This class is storing information about the current state of a chess game and checks if moves are valid.
It will also keep a log of the moves.  (e.g. for undoing moves...etc )
"""

class GameState():
    def __init__(self):
        
        #i might change how this is implemented later, for now this will be fast enough without any math libraries
        
        # board is 8x8 2D list, each element or piece of the list has a string with 2 chars.
        # first char determines the color: 'w' for white, 'b' for black
        # second char is the type of piece: 'K' King, 'Q' Queen, 'R' Rook, 'B' Bishop, 'N' kNight ('K'ing uses K already) or 'P' Pawn
        # "--" represents an empty tile on the chess board (no piece on the tile)
        self.board = [
              #a    #b    #c    #d    #e    #f    #g    #h
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],  #8
            ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],  #7
            ["--", "--", "--", "--", "--", "--", "--", "--"],  #6
            ["--", "--", "--", "--", "--", "--", "--", "--"],  #5
            ["--", "--", "--", "--", "--", "--", "--", "--"],  #4
            ["--", "--", "--", "--", "--", "--", "--", "--"],  #3
            ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],  #2
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]]  #1
              #a    #b    #c    #d    #e    #f    #g    #h
        self.whiteToMove = True
        self.moveLog = []