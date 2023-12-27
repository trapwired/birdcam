# Birdcam
A quick smashing together of various components to take pictures of the birds outside my window. 
For the detection, a pretrained CNN, yoloV4 is used. Credits to the code belong to [github.com/onnx](https://github.com/onnx/models/blob/main/validated/vision/object_detection_segmentation/yolov4/dependencies/inference.ipynb), and [the parent repo](https://github.com/onnx/models/tree/main/validated/vision/object_detection_segmentation/yolov4)

# Usage
- I connected a camera via a camlink to my computer (any webcam will also do, try out the different webcam ids to find the correct webcam)
- Use requirements.txt to install the necessary python-packages
- for yoloV4 to work, you have to download the [model](https://github.com/onnx/models/tree/main/validated/vision/object_detection_segmentation/yolov4) and add it to the ./model folder
- the inference-code is trimmed to a means to be as quick as possible (you can define a threshold for confidence, and also the class to detect - 14 is birds)
- To run the while-True loop, let run the main.py file

# additional information
- on my MacbookPro, M2Max, it took about 0.2sec to infer an image, after which a 0.3 (configurable) timeout will wait before detecting the next bird, to avoid having too many pictures of one bird.
- since the stored pictures are just hdmi-grabs, the quality is not at its best - triggering a picture on the camera would definitely work better
