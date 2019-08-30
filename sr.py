import cv2
import time
import matplotlib.pyplot as plt
#from checkerboard import detect_checkerboard

vc=cv2.VideoCapture(0)
plt.ion()
size = (24, 15) # size of checkerboard
while 1:
    
    succ,image = vc.read()
    print(image.shape)
    #print(succ) # obtain checkerboard
    #corners, score =cv2.findChessboardCorners(image,size)#,verbose=1)# detect_checkerboard(image, size)#,verbose=1)
    #print(score)
    '''plt.imshow(image)
    plt.show()
    time.sleep(0.5)
    plt.close()'''