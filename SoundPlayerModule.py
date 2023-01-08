from playsound import playsound
import winsound 
#Note\Do.mp3

def SoundPlayer(HandNo, FingerId):
    if HandNo == 0:
        if FingerId == 3:
            Folder = "Note\Do.mp3"
        if FingerId == 2:
            Folder =  "Note\Re.mp3"
        if FingerId == 1:
            Folder = "Note\Mi.mp3"
        if FingerId == 0:
            Folder = "Note\Fa.mp3"

    else :
        if FingerId == 0:
            Folder = "Note\Sol.mp3"
        if FingerId == 1:
            Folder =  "Note\La.mp3"
        if FingerId == 2:
            Folder = "Note\Si.mp3"
        if FingerId == 3:
            Folder = "Note\Do.mp3"
        
    return Folder


def SoundPlayer2(HandNo, Fingerid):
    winsound.PlaySound("Do",winsound.SND_FILENAME)
