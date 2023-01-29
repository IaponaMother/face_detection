
import cv2
from PIL import Image
import numpy as np


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


img = cv2.imread('people.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# gray = np.array(Image.open('people.jpg').convert('L'), 'uint8')

faces = face_cascade.detectMultiScale(image=gray, minNeighbors=5, minSize=(20, 20), scaleFactor=1.1)

# def pixel_face(img,):
#     x = np.linspace(0, widht, 4, dtype="int")
#     y = np.linspace(0, height, 4, dtype="int")
#     for i in range(1, len(y)):
#         for j in range(1, len(x)):
#             X_1 = x[j - 1]
#             Y_1 = y[i - 1]
#             X_2 = x[j]
#             Y_2 = y[i]
#
#             ROI = img[Y_1:Y_2, X_1:X_2]
#             (B, G, R) = [int(k) for k in cv2.mean(ROI)[:3]]
#             cv2.rectangle(img, (X_1, Y_1), (X_2, Y_2),
#                 (B, G, R), -1)
#     return img

i = 1
for (x, y, w, h) in faces:
    # cropped = img[y:y+h, x:x+w]
    # blurred = cv2.GaussianBlur(cropped, (51, 51), 0)
    # img = cv2.addWeighted(img, 1, blurred, 1, 0)

    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    i += 1



cv2.imshow('img', img)
cv2.waitKey()