import cv2
import numpy as np

def origintl(im):
    '''
    sets the origin to the top left corner
    use for making xy pixel locations inside an img subscribe to a common sense value
    '''
    return np.flip(im,0)

def graph2sound(loc,normaxis):
    '''
    normalize from xy region location in img to locations fit for openal playing used from beep()
    '''
    loc=graphOrigin2soundOrigin(loc)
    return [loc[0]/normaxis[0],loc[1]/normaxis[1],loc[2]/normaxis[2]]

def graphOrigin2soundOrigin(loc):
    '''
    origin of the graph is bottom left
    origin of images after origintl() is top left
    origin of 3da openal is the center
    opentl does work for this purpose
    '''
    return loc