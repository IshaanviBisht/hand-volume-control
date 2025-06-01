import cv2
import numpy as np
import time
import HTM.HandTrackingModule as htm
import math
import os

cap = cv2.VideoCapture(0)
pTime = 0

detector = htm.handDetector(detectionCon=0.9) #create object

while True:
    success, img = cap.read()
    img = detector.findHands(img) #detect the hands through the cam
    lmList = detector.findPosition(img, draw=False)

    if len(lmList) != 0:

        x1, y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[8][1], lmList[8][2]
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

        #circle in between the line
        cv2.circle(img, (cx, cy), 15, (255, 153, 51), cv2.FILLED)

        #to check if it is detecting both the fingers correctly
        cv2.circle(img, (x1, y1), 15, (255, 0, 0), cv2.FILLED)
        cv2.circle(img, (x2, y2), 15, (255, 0, 0), cv2.FILLED)

        # line joining thumb and index finger
        cv2.line(img ,(x1, y1), (x2, y2), (255, 153, 51), 5)

        length = math.hypot(x2-x1,y2-y1)
        print(length)
        def set_volume(vol_percent):
            vol_percent = int(np.clip(vol_percent, 0, 100))
            os.system(f"osascript -e 'set volume output volume {vol_percent}'")

        # change circle in between color
        if length<50:
            cv2.circle(img, (cx, cy), 15, (0, 0, 255), cv2.FILLED)

        # map length to volume range
        vol = np.interp(length, [90, 590], [0, 100])
        set_volume(vol)

        # draw volume bar
        cv2.rectangle(img, (50, 150), (85, 400), (153, 51, 255), 3)
        vol_bar = np.interp(length, [90, 590], [400, 150])
        cv2.rectangle(img, (50, int(vol_bar)), (85, 400), (204, 153, 255), cv2.FILLED)

        # show volume %
        cv2.putText(img, f'{int(vol)} %', (40, 450), cv2.FONT_HERSHEY_PLAIN, 4, (127, 0, 255), 3)

    #FPS
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    #SHOW NUMBER OF FPS
    cv2.putText(img, f'FPS: {int(fps)}', (40, 70), cv2.FONT_HERSHEY_PLAIN, 5,
                (153, 51, 255), 5)
    cv2.imshow("Img", img)
    cv2.waitKey(1)