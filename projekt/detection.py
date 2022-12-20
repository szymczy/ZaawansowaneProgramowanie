import cv2
import imutils
import time

def detection(image):

    start = time.time()

    hogcv = cv2.HOGDescriptor()
    hogcv.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    image = cv2.imread(image)

    image = imutils.resize(image, width=min(800, image.shape[1]))

    (regions, _) = hogcv.detectMultiScale(image, winStride=(4, 4), padding=(4, 4), scale=1.06)

    for (x, y, w, h) in regions:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

    cv2.putText(
        img = image,
        text = 'liczba osob: ' + str(len(regions)),
        org = (30,30),
        fontFace = cv2.FONT_HERSHEY_SIMPLEX,
        fontScale = 1,
        color = (0, 0, 255),
        thickness = 2
    )

    cv2.imshow('image.png', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    end = time.time()
    print(end - start)

detection('image.png')
