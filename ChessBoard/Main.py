"""
This is the main class for handling input of the user and the graphical (output)representation of the current state of the game(GUI)
"""

import Engine
import pygame as p

WIDTH = HEIGHT = 768 #window size. (512 or 400 would also work)
DIMENSION = 8 #chessboard is 8x8
SQ_SIZE = HEIGHT // DIMENSION #floor division (rounds to nearest whole number) (SQ_SIZE = square size)
MAX_FPS = 15 #for animations
IMAGES = {}



"""
Initializing a global dictionary of images. (only called once)
"""
def loadImages():
    pieces = ['wP', 'wN', 'wB', 'wR', 'wQ', 'wK', 'bP', 'bN', 'bB', 'bR', 'bQ', 'bK'] #bN and wN are the kNights, the K was already in use by the King
    for piece in pieces:
        image = p.image.load('ChessBoard/images/' + piece +'.png')
        IMAGES[piece] = p.transform.smoothscale(image, (SQ_SIZE, SQ_SIZE))
        #any image can be accessed by 'IMAGES['wK']' (example for accessing the 'w'hite'K'ing)



"""
Main for the code. Will handle user input and updating graphics
"""
def main():
    p.init() #initialzing pygame
    icon = p.image.load('ChessBoard/images/icon.png') #loading an image to be the icon
    p.display.set_icon(icon) #setting the icon
    p.display.set_caption('classick\'s Chess-App') #setting caption of window
    screen = p.display.set_mode((WIDTH, HEIGHT)) #creating window with certain size
    clock = p.time.Clock() #game clock
    gs = Engine.GameState() #starting/initial gamestate
    loadImages() #here is the only call, before while loop

    #LOOP
    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False #if window is exited, set running to false to stop loop
        drawGameState(screen, gs)
        clock.tick(MAX_FPS) #set tickrate
        p.display.flip() #update display
        


"""
drawGameState will handle the drawing of the current game state
"""
def drawGameState(screen, gs):
    drawBoard(screen) #draws the usual squared chess gameboard
    """ TODO: adding in the possible move and piece highlighting"""
    drawPieces(screen, gs.board) #draw pieces on top of the earlier drawn chess board 



"""
Drawing the squared board
"""
def drawBoard(screen):
    colors = [p.Color("ivory2"), p.Color("grey40")] #colors for the squares saved here. index 0 = remainder 0; index 1 = remainder 1. becomes clear a few lines down 
    #nested for loop for 8 rows x 8 columns
    for r in range(DIMENSION): #r = row
        for c in range(DIMENSION): #c = column
            #top left square of a chess board is white (chess coordinate would be (A,8) ) 
            #but we assume its (0, 0): 
            #if the row and col are summed up like we assume their position and the sum is divided by 2
            #white squares will have no remainder because their sum will be even, and dark squares will have a remainder of 1
            #(for more on how this works, check out a chessboard and try the calculation for a few squares (assuming top left is (0, 0) and 0 + 0 / 2 = 0 no remainder, white)
            #((1, 0) is 1 + 0 / 2 = 0 remainder 1 , dark), etc... 
            #and of cause since were interested in the remainder, we'll be using the modulo-operator
            #now based on the remainder we choose the color. now remainder (0) will access the color list at index 0 and choose a white/light color
            #with a remainder (1) the color at index 1 will be chosen (black/dark)
            color = colors[(r+c)%2]
            
            #now draw a square at the postion according to column(x-coord) and row(y-coord) with the calculated color
            p.draw.rect(screen, color, p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE)) #(x-posi, y-posi, width, height)



"""
Draw the pieces according to the current board of the gameState (GameState.board)
"""
def drawPieces(screen, board):
    for r in range(DIMENSION): #r = row
        for c in range(DIMENSION): #c = column
            piece = board[r][c]
            #check if there is an actual piece at this position or if its empty
            if piece != "--": #if its not an empty square
                screen.blit(IMAGES[piece], p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE)) #blit basicly means just drawing, here draw the piece at current location



if __name__ == "__main__": #this is the proper way to call this exact main function, just a safer way for when some other main class is imported for example
    main()