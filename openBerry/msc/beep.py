import time
import math
import random
from openal.audio import SoundSink, SoundSource
from openal.loaders import load_wav_file

sink = SoundSink()
sink.activate()
source = SoundSource()
source.looping = False
data = load_wav_file("s.wav")
source.queue(data)

def beep(pos=[0,0,0],orintation=[0,0,0]):
    source.position = pos
    sink.play(source)
    sink.update()

if __name__=="__main__":
    while 1:
        pos=[random.randint(-2,2),random.randint(-2,2),0]#random.randint(0,3)]
        beep(pos=pos)
        print("pos",pos)
        time.sleep(0.5)