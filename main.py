import os.path
import time

import cv2
import imutils

IMAGE_COUNTER = 0
TIMEOUT = 1
SENSITIVITY = 2000000


def return_camera_indexes():
    # checks the first 10 indexes.
    index = 0
    arr = []
    i = 10
    while i > 0:
        cap = cv2.VideoCapture(index)
        if cap.read()[0]:
            arr.append(index)
            cap.release()
        index += 1
        i -= 1
    return arr


if __name__ == '__main__':
    cap = cv2.VideoCapture(0)

    ret, start_frame = cap.read()

    start_frame = imutils.resize(start_frame, width=500)
    start_frame = cv2.cvtColor(start_frame, cv2.COLOR_BGR2GRAY)
    start_frame = cv2.GaussianBlur(start_frame, (21, 21), 0)

    # create new folder for each run
    dir_name = time.strftime("%Y%m%d-%H%M%S")
    dir_path = os.path.join('out', dir_name)
    os.mkdir(dir_path)

    while True:

        _, full_frame = cap.read()
        frame = imutils.resize(full_frame, width=500)

        frame_bw = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame_bw = cv2.GaussianBlur(frame_bw, (5, 5), 0)

        difference = cv2.absdiff(start_frame, frame_bw)
        threshold = cv2.threshold(difference, 25, 255, cv2.THRESH_BINARY)[1]
        start_frame = frame_bw

        if threshold.sum() > SENSITIVITY:
            print("motion detected")
            img_name = "opencv_frame_{}.png".format(IMAGE_COUNTER)
            path = os.path.join(dir_path, img_name)
            rotated_image = cv2.rotate(full_frame, cv2.ROTATE_180)
            cv2.imwrite(path, rotated_image)
            IMAGE_COUNTER += 1
            time.sleep(TIMEOUT)

    cap.release()
    cv2.destroyAllWindows()
