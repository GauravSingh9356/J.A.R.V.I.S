import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd="C:\Program Files\Tesseract-OCR\\tesseract.exe"


def OCR():
    frameWidth= 640         # CAMERA RESOLUTION
    frameHeight = 480
    brightness = 180

    cap=cv2.VideoCapture(0)
    cap.set(3, frameWidth)
    cap.set(4, frameHeight)
    cap.set(10, brightness)


    # forlive video testing
    while True:
        success, img = cap.read()
        imgT = img.copy()
        textRecongized = pytesseract.image_to_string(img,lang='eng');textRecongized=textRecongized.replace("\n\x0c", "");
        print(textRecongized)
        imgT=cv2.putText(imgT,textRecongized,(img.shape[0]+120,img.shape[1]+120), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0,255,0), 1, cv2.LINE_AA)
        cv2.imshow("Image", imgT)
        
        if cv2.waitKey(1) and 0xFF == ord('q'):    
            break