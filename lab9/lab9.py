import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
img1 = cv2.imread('img1.png')
img2 = cv2.imread('img2.jpg')
img3 = cv2.imread('img3.jpg')
img4 = cv2.imread('img4.jpg')
img5 = cv2.imread('img5.jpg')

#print(img1) - piksele

#cv2.imshow('img1', img1)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

def read_from_image(img):
    bnw = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cv2.imshow('',bnw)
    cv2.waitKey(0)

    return pytesseract.image_to_string(bnw)

print(read_from_image(img4))