import cv2 as cv
import numpy as np

image = np.zeros((500,500,3),np.uint8)
lines=[]
width = image.shape[1]
height = image.shape[0]


photo=np.zeros((500,500,3),np.uint8)
width=500
def draw_lines(event,x,y,flags,param):
    global width;global height
    global lenght_of_line
    global b,g,r

    if event == cv.EVENT_LBUTTONDOWN:
        if x<(lenght_of_line//2):
                lines.append([(0,y),((lenght_of_line),y)])
                cv.line(param,(0,y),((lenght_of_line),y),(b,g,r),8)
        elif x>width-(lenght_of_line//2):
                lines.append([(width-(lenght_of_line),y),(width,y)])
                cv.line(param,(width-(lenght_of_line),y),(width,y),(b,g,r),8)
        else:
                lines.append([(x-(lenght_of_line//2),y),(x+(lenght_of_line//2),y)])
                cv.line(param,(x-(lenght_of_line//2),y),(x+(lenght_of_line//2),y),(b,g,r),8)
        print(lines)
    image_with_text = np.copy(param)
    cv.putText(image_with_text, "Drawing mode", (width//5,height-10), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 1)
    
    cv.imshow("result",image_with_text)

def eraser(event,x,y,flags,param):
        global size_of_eraser
        if event != cv.EVENT_LBUTTONDOWN:
             return
        
        cv.rectangle(param,(x-size_of_eraser,y-size_of_eraser),(x+size_of_eraser,y+size_of_eraser),(0,0,0),-1)
        image_with_text = np.copy(param)
        cv.putText(image_with_text, "Erasing mode", (width//5,height-10), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 1)
        cv.imshow("result",image_with_text)

points = []
def crop(event,x,y,flags,param):
        if event == cv.EVENT_LBUTTONDOWN:
            points.append((x,y))
            if len(points)==4:
                cropped_image=param[points[0][1]:points[2][1],points[0][0]:points[2][0]]
                cv.namedWindow("cropped image")
                cv.imshow("cropped image",cropped_image)
        image_with_text = np.copy(param)
        cv.putText(image_with_text, "cropping mode", (width//5,height-10), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 1)
        cv.imshow("result",image_with_text)
             
        


working = True
while working :
    cv.imshow("result", image)
    key = cv.waitKey(0)

    if key == ord('d'):
        lenght_of_line=int(input("Please enter the size of your line "))
        b,g,r=(input("Please enter the BGR scale of your line ").split())
        b=int(b);g=int(g);r=int(r)
        cv.setMouseCallback("result",draw_lines,image)
    elif key == ord('e'):
        size_of_eraser=int(input("Please enter the size of your eraser "))
        cv.setMouseCallback("result",eraser,image)
    elif key == ord('c'):
        cv.setMouseCallback("result",crop,image)
    elif key == 27:
        working = False