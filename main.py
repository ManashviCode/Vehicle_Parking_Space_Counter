import cv2
import numpy as np
import pickle

rectW, rectH = 107, 48

cap = cv2.VideoCapture('1207(1).mp4')

with open('carParkPos', 'rb') as f:
    posList = pickle.load(f)

frame_counter = 0

def check(imgPro):
    spaceCount = 0
    freeSlots = []  # List to store the numbers of free slots
    for idx, pos in enumerate(posList):
        x, y = pos
        crop = imgPro[y:y + rectH, x:x + rectW]
        count = cv2.countNonZero(crop)
        if count < 900:
            spaceCount += 1
            freeSlots.append(idx + 1)  # Add the slot number to the list
            color = (0, 255, 0)
            thick = 5
        else:
            color = (0, 0, 255)
            thick = 2

        # Draw rectangle and display slot number
        cv2.rectangle(img, pos, (x + rectW, y + rectH), color, thick)
        cv2.putText(img, str(idx + 1), (x + 5, y + 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

      # Display the free slots count and free slots numbers on the same line with a pink background for the text box
        cv2.rectangle(img, (0, 0), (1100, 35), (255, 105, 180), -1)  # Pink background
        freeSlotsText = f'Free: {spaceCount}/{len(posList)}   |   Free Slots: ' + ", ".join(map(str, freeSlots))

        # Set the position of the rectangle in the top-left corner
        start_x = 23  # 10px margin from the left
        start_y = 23  # 10px margin from the top
       
        cv2.putText(img, freeSlotsText, (start_x + 10, start_y ), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)





while True:
    _, img = cap.read()
    if frame_counter == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        frame_counter = 0
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (3, 3), 1)
    Thre = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 25, 16)
    blur = cv2.medianBlur(Thre, 5)
    kernel = np.ones((3, 3), np.uint8)
    dilate = cv2.dilate(blur, kernel, iterations=1)
    check(dilate)

    cv2.imshow("Image", img)
    cv2.waitKey(10)
