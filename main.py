import cvzone
import cv2
import numpy as np
import cvzone
from cvzone.HandTrackingModule import HandDetector
from cvzone import overlayPNG
import math
import random

cap = cv2.VideoCapture(0)
cap.set(3, 1920)
cap.set(4, 1080)

detector = HandDetector(detectionCon=0.8, maxHands=1)

class SnakeGameClass:
    def __init__(self, foodPath) -> None:
        self.GameOver = False
        self.points = [] # all points of the snake
        self.lengths = [] # distance between each point
        self.currentLength = 0 # total length of each snake
        self.allowedLength = 150 # total allowed length
        self.previousHead = 0, 0

        self.imgFood = cv2.imread(foodPath, cv2.IMREAD_UNCHANGED)
        self.hFood, self.wFood, _ = self.imgFood.shape
        self.foodPoint = 0, 0
        self.randomFoodLocation()
        self.score = 0

    def randomFoodLocation(self):
        self.foodPoint = random.randint(100,1000), random.randint(100,600)


    def update(self, imgMain, currentHead):

        if self.GameOver:
            cvzone.putTextRect(img, "GAME OVER!!", [300, 400], scale=7, thickness=5, offset=20)
            cvzone.putTextRect(img, f"Your Score: {self.score}", [300, 550], scale=7, thickness=5, offset=20)

        else:
            px, py = self.previousHead
            cx, cy = currentHead
            self.points.append([cx, cy]) 
            distance = math.hypot(cx - px, cy - py)
            self.lengths.append(distance)
            self.currentLength += distance
            self.previousHead = cx, cy

            # Length Reduction
            if self.currentLength > self.allowedLength:
                for i, length in enumerate(self.lengths):
                    self.currentLength -= length
                    self.points.pop(i)
                    self.lengths.pop(i)
                    if self.currentLength < self.allowedLength:
                        break 

            # Check if snake ate food
            rx, ry = self.foodPoint
            if (rx - self.wFood//2 < cx < rx + self.wFood//2) and (ry - self.hFood//2 < cy < ry + self.hFood//2):
                # print("ate")
                self.allowedLength += 50
                self.score += 1
                print(self.score)
                self.randomFoodLocation()

            # Draw Snake
            cvzone.putTextRect(img, f"Score: {self.score}", [50, 80], scale=2, thickness=3, offset=10)
            if self.points:
                for (i, point) in enumerate(self.points):
                    if i:
                        cv2.line(imgMain, self.points[i-1], point, (0,0,255), 20)
                        cv2.circle(img, self.points[-1], 20, (200, 0, 200), cv2.FILLED)
        
            # Check for collision
            pts = np.array(self.points[:-2], np.int32)
            pts = pts.reshape((-1, 1, 2))
            cv2.polylines(imgMain, [pts], False, (0, 0, 150), 3)
            minDist = cv2.pointPolygonTest(pts, (cx, cy), True)
            
            if -1 <= minDist <= 1:
                print("Hit!!")
                self.GameOver = True
                self.points = [] # all points of the snake
                self.lengths = [] # distance between each point
                self.currentLength = 0 # total length of each snake
                self.allowedLength = 150 # total allowed length
                self.previousHead = 0, 0
                

            # Draw Food
            rx, ry = self.foodPoint
            imgMain = cvzone.overlayPNG(imgMain, self.imgFood, (rx - self.wFood//2, ry - self.hFood//2))

        return imgMain

game = SnakeGameClass("Donut.png")

while 1:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img, flipType=False)

    if hands:
        lmList = hands[0]['lmList']
        pointIndex = lmList[8][0:2]
        img = game.update(img, pointIndex)

    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    if key == ord('r'):
        game.GameOver = False
        game.score = 0
    
