import cv2 as cv
import numpy as np
width,height=(input("Please enter the width and the height of your image ").split())
width=int(width);height=int(height)
b,g,r=(input("Please enter the BGR scale of your image ").split())
b=int(b);g=int(g);r=int(r)


image = np.zeros((width,height,3),np.uint8)
image[:]=(b,g,r)

circleCenter = None
circleRadius = 0
isDrawing = False

def circle(event,x,y,flags,param):
    global width,height,circleCenter,circleRadius,isDrawing
    global b_c,g_c,r_c

    if event == cv.EVENT_LBUTTONDOWN:
        isDrawing = True
        circleCenter = (x, y)
        circleRadius = 0

    elif event == cv.EVENT_LBUTTONUP:
            isDrawing = False

    elif event == cv.EVENT_MOUSEMOVE:
        if isDrawing:
            dx = x - circleCenter[0]
            dy = y - circleCenter[1]
            circleRadius = int((dx**2 + dy**2)**0.5)


    image_with_text = np.copy(param)
    cv.circle(param,circleCenter,circleRadius,(b_c,g_c,r_c),-1)
    cv.putText(image_with_text, "Circle mode", (width//5,height-10), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 1)
    cv.imshow("result",image_with_text)

startX, startY = None, None

def rectangle(event,x,y,flags,param):
        global width,height,isDrawing,startX,startY
        global b_r,g_r,r_r
        if event == cv.EVENT_LBUTTONDOWN:
            isDrawing = True
            startX,startY=x,y
        elif event == cv.EVENT_MOUSEMOVE:
            if isDrawing:
                cv.rectangle(param,(startX,startY),(x,y),(b_r,g_r,r_r),10)
        elif event == cv.EVENT_LBUTTONUP:
            isDrawing = False
        
        image_with_text = np.copy(param)

        cv.putText(image_with_text, "Rectangle mode", (width//5,height-10), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 1)
        cv.imshow("result",image_with_text)

drawing_mode = False
polygon_points = []  
polygons = []  

def draw_polygons(param):
    global b_p,g_p,r_p
    for polygon in polygons:
        if len(polygon) > 1:
            cv.polylines(param, [np.array(polygon)], isClosed=True, color=(b_p, g_p, r_p), thickness=2)
 
def draw_temp_polygon(param):
    if len(polygon_points) > 1:
        cv.polylines(param, [np.array(polygon_points)], isClosed=True, color=(b_p, g_p, r_p), thickness=2)

def polygon(event, x, y, flags, param):
    global drawing_mode, polygon_points

    if drawing_mode:
        if event == cv.EVENT_LBUTTONDOWN:
            polygon_points.append((x, y))
        image_with_text = np.copy(param)
        cv.putText(image_with_text, "Polygon mode", (width//5,height-10), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 1)
        cv.imshow("result",image_with_text)
cv.namedWindow("result")
working = True
while working :
    draw_polygons(image)  
    draw_temp_polygon(image)

    cv.imshow("result", image)
    key = cv.waitKey(0)

    if key == ord('c'):
        b_c,g_c,r_c=(input("Please enter the BGR scale of your Circle ").split())
        b_c=int(b_c);g_c=int(g_c);r_c=int(r_c)
        cv.setMouseCallback("result",circle,image)
        
    if key == ord('r'):
        b_r,g_r,r_r=(input("Please enter the BGR scale of your Rectangle ").split())
        b_r=int(b_r);g_r=int(g_r);r_r=int(r_r)
        cv.setMouseCallback("result",rectangle,image)

    if key == ord('p'):
        drawing_mode = not drawing_mode
        if not drawing_mode:
            b_p,g_p,r_p=(input("Please enter the BGR scale of your Polygon ").split())
            b_p=int(b_p);g_p=int(g_p);r_p=int(r_p)
            cv.setMouseCallback("result",polygon,image)

            if len(polygon_points) > 1:
                polygons.append(polygon_points.copy())
            polygon_points.clear()
    if key == ord('e'):
        if drawing_mode:
            if len(polygon_points) > 1:
                polygons.append(polygon_points.copy())
            polygon_points.clear()
            drawing_mode = False

    elif key == 27:
        working = False