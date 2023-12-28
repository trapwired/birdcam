import os.path
import time

import cv2

from CnnModel import CnnModel

IMAGE_COUNTER = 0
TIMEOUT = 0.3
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


def detect_birds(capture_device, cnn_model, output_directory_path):
    global IMAGE_COUNTER
    while True:
        _, start_frame = capture_device.read()
        rotated_image = cv2.rotate(start_frame, cv2.ROTATE_180)
        try:
            res = cnn_model.infer_image(rotated_image)
        except Exception as e:
            print(e)
            continue
        if res:
            img_name = "bird_picture_{}.png".format(IMAGE_COUNTER)
            path = os.path.join(output_directory_path, img_name)
            cv2.imwrite(path, rotated_image)
            IMAGE_COUNTER += 1
            time.sleep(TIMEOUT)
            if IMAGE_COUNTER > 2000:
                exit()


def create_run_directory():
    # create new folder for each run
    dir_name = time.strftime("%Y%m%d-%H%M%S")
    new_directory_path = os.path.join('out', dir_name)
    os.mkdir(new_directory_path)
    return new_directory_path


if __name__ == '__main__':
    model = CnnModel()
    cap = cv2.VideoCapture(0)

    dir_path = create_run_directory()

    detect_birds(cap, model, dir_path)
