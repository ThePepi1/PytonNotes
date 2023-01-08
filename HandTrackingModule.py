from ast import Break, While
from cgitb import handler
from operator import le
from tkinter.tix import Tree
import cv2 
import mediapipe as mp
import time

class handDetectore():
    def __init__(self,  mode = False, maxHands = 2, detectionCon = 0.5, trackCon = 0.5 ) -> None:
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon;
        self.trackCon = trackCon;
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands()
        self.mpDraw = mp.solutions.drawing_utils
        
    def findHands(self, img, draw = True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        #print(results.multi_hand_landmarks)
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
        return img
    
    def findPosition(self, img, handNo =0, draw = False):
        lmlist = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):          
                h,w,c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmlist.append([id, cx , cy])
            if draw:
                self.mpDraw.draw_landmarks(img, myHand, self.mpHands.HAND_CONNECTIONS)

        return lmlist
    

 




def main():
    cap = cv2.VideoCapture(0)
    detector = handDetectore()

    while True:
        ret, img = cap.read()
        img = detector.findHands(img)
        lmList = detector.findPosition(img);
        if len(lmList) != 0:
            print(lmList[4])
        cv2.imshow('Image', img)
        if cv2.waitKey(1) == ord('q'):
            break;
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()