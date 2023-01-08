import imp
from matplotlib.pyplot import cla


import pyglet
import time

class Klavir():
    do = pyglet.media.load("Note\Do.mp3", streaming=False)  
    re = pyglet.media.load("Note\Re.mp3", streaming=False)  
    mi = pyglet.media.load("Note\Mi.mp3", streaming=False)
    fa = pyglet.media.load("Note\Fa.mp3", streaming=False)
    sol = pyglet.media.load("Note\Sol.mp3", streaming=False)
    la = pyglet.media.load("Note\La.mp3", streaming=False)
    si = pyglet.media.load("Note\Si.mp3", streaming=False)
    def playS(HandNo, FingerId):
        if HandNo == 0:
            if FingerId == 3:
                Klavir.do.play()
                time.sleep(1)
            if FingerId == 2:
                Klavir.re.play()
                time.sleep(1)
            if FingerId == 1:
                Klavir.mi.play()
                time.sleep(1)
            if FingerId == 0:
                Klavir.fa.play()
                time.sleep(1)

        else:
            if FingerId == 0:
                Klavir.sol.play()
                time.sleep(1)
            if FingerId == 1:
                Klavir.la.play()
                time.sleep(1)
            if FingerId == 2:
                Klavir.si.play()
                time.sleep(1)
            if FingerId == 3:
                Klavir.do.play()
                time.sleep(1)
            

