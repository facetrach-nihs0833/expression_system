import cv2
import matplotlib.pyplot as plt
import numpy as np
import math


bgr = cv2.imread('187.jpg')
gray = cv2.cvtColor(bgr, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (3, 3), 0)
canny = cv2.Canny(blurred, 20, 40)
kernel = np.ones((3,3), np.uint8)
dilated = cv2.dilate(canny, kernel, iterations=2)
(contours, hierarchy) = cv2.findContours(dilated.copy(),
                                         cv2.RETR_TREE,
                                         cv2.CHAIN_APPROX_SIMPLE)


candidates = []
hierarchy = hierarchy[0]

index = 0
pre_cX = 0
pre_cY = 0
center = []
for component in zip(contours, hierarchy):
    contour = component[0]
    peri = cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, 0.1 * peri, True)
    area = cv2.contourArea(contour)
    corners = len(approx)

    # compute the center of the contour
    M = cv2.moments(contour)

    if M["m00"]:
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
    else:
        cX = None
        cY = None

    if 14000 < area < 20000 and cX is not None:
        tmp = {'index': index, 'cx': cX, 'cy': cY, 'contour': contour}
        center.append(tmp)
        index += 1

center.sort(key=lambda k: (k.get('cy', 0)))
row1 = center[0:3]
row1.sort(key=lambda k: (k.get('cx', 0)))
row2 = center[3:6]
row2.sort(key=lambda k: (k.get('cx', 0)))
row3 = center[6:9]
row3.sort(key=lambda k: (k.get('cx', 0)))

center.clear()
center = row1 + row2 + row3

for component in center:
    candidates.append(component.get('contour'))

cv2.drawContours(bgr, candidates, -1, (0, 0, 255), 3)
cv2.imshow("bgr", bgr)
cv2.waitKey(0)

r_points = []
g_points = []
b_points = []
h_points = []
s_points = []
v_points = []
kx = []
ky = []
kz = []
edge = []

hsv = cv2.cvtColor(bgr,cv2.COLOR_BGR2HSV)


while True:
    cv2.imshow('bgr',bgr)

    
    key = cv2.waitKey(1) &0xFF
 
    if key == ord('s'):
        x,y,w,h = cv2.selectROI('bgr',bgr, fromCenter=False,showCrosshair=True)
        roi = bgr[int(y): int(y + h),int(x): int(x + w)]
        
        for i in range(x, x + w):
            for j in range(y, y + h):
                a = bgr[j, i]
                r_points.append(a[2])
                g_points.append(a[1])
                b_points.append(a[0])
                bgr[j, i] = [255, 255, 255]
                
        for i in range(x, x + w):
            for j in range(y, y + h):
                a = hsv[j, i]
                if i == x and j == y:
                    kx.append(a[0])
                    ky.append(a[1])
                    kx.append(a[2])
                h_points.append(a[0])
                s_points.append(a[1])
                v_points.append(a[2])
                
            fig = plt.figure()
            ax = plt.axes(projection='3d')
            ax.set_xlim(0, 255)
            ax.set_ylim(0, 255)
            ax.set_zlim(0, 255)
            ax.set_xlabel('R')
            ax.set_ylabel('G')
            ax.set_zlabel('B')
            fig_hsv = plt.figure()
            ax_hsv = plt.axes(projection='3d')
            ax_hsv.set_xlim(0, 255)
            ax_hsv.set_ylim(0, 255)
            ax_hsv.set_zlim(0, 255)
            ax_hsv.set_xlabel('H')
            ax_hsv.set_ylabel('S')
            ax_hsv.set_zlabel('V')
            ax.scatter3D(r_points, g_points, b_points)
            ax_hsv.scatter3D(h_points, s_points, v_points)
            ax_hsv.scatter3D(kx, ky, kz, c='g', s=100)
            plt.show()

    elif key == ord('r'):
            r_points =  []
            g_points =  []
            b_points =  []
            h_points =  []
            s_points =  []
            v_points =  []
            kx = []
            ky = []
            kz = []
            
    elif key ==27:
            break
            bgr = bgr[j, i]
            red_low = [0,0,200]
            red_high = [0,0,255]
            yell_low = [0,200,200]
            yell_high = [0,255,255]
            bull_low = [200,0,0]
            bull_high = [200,0,0]
            gree_low = [0,200,0]
            gree_high = [0,255,0]
            orange_low = [255,90,0]
            orange_high = [250,97,3]
            white_low = [255,255,255]
            white_high = [255,255,255]
            
           
            if red_low < bgr < red_high:
                print("1")
            elif yell_low < bgr < yell_high:
                print("2")
            elif bull_low < bgr < bull_high:
                print("3")
            elif gree_low < bgr < gree_high:
                print("4")
            elif orange_low < bgr < orange_high:
                print("5")
            elif white_low < bgr < white_high:
                print("6")
cv2.destrotALLWindows()