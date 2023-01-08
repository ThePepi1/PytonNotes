from ast import Num
from tkinter.tix import Tree
import HandTrackingModule as ht
import cv2 
import SoundPlayerModule as play
from playsound import playsound 
Hand1 =  [True, True, True, True]
Hand2 =  [True, True, True, True]
Hands = [Hand1, Hand2]
tipIds = [8, 12 , 16 , 20]
def Moving(Hand = [], HandNo = 0, orientation = False):
        for id in range(0,4):
            if Hands[HandNo][id]:
                if Hand[tipIds[id]][2] > Hand[int(tipIds[id]) - 2][2]:
                    playsound(play.SoundPlayer(HandNo, id), False)
                    Hands[HandNo][id] = False
                    print("Moving")
            else:
                if Hand[tipIds[id]][2] < Hand[int(tipIds[id]) - 2][2]:
                    Hands[HandNo][id] = True

wCam, hCam = 640, 480
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
detector =  ht.handDetectore()
FirsstHand = []
SecondHand = []
while True:
    ret, img = cap.read()
    img = detector.findHands(img, draw=True)
    if detector.results.multi_hand_landmarks:
        if len(detector.results.multi_hand_landmarks) == 1:
            FirstHand = detector.findPosition(img=img, handNo=0)
            Moving(FirstHand, 0 , False)
        if len(detector.results.multi_hand_landmarks) == 2:
            FirstHand = detector.findPosition(img=img, handNo= 0)
            SecondHand = detector.findPosition(img=img,handNo=1)
            Moving(FirstHand, 0, False)
            Moving(SecondHand, 1 , False)
    cv2.imshow('Image', img)
    if cv2.waitKey(1) == ord('q'):
        break;

cap.release()
cv2.destroyAllWindows()