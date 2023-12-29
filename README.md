# Birdcam
A quick smashing together of various components to take pictures of the birds outside my window. 
For the detection, a pretrained CNN, yoloV4 is used. Credits to the code belong to [github.com/onnx](https://github.com/onnx/models/blob/main/validated/vision/object_detection_segmentation/yolov4/dependencies/inference.ipynb), and [the parent repo](https://github.com/onnx/models/tree/main/validated/vision/object_detection_segmentation/yolov4), as well as [this object detection repository](https://github.com/ezhil56x/Motion-Detection-Alarm-OpenCV/tree/main), and these two repositories for the yoloV4 parameters: [Coco.names](https://github.com/hunglc007/tensorflow-yolov4-tflite/blob/master/data/classes/coco.names), [yolov4_anchors.txt](https://github.com/hunglc007/tensorflow-yolov4-tflite/blob/master/data/anchors/yolov4_anchors.txt)

# Usage
- I connected a camera via a camlink to my computer (any webcam will also do, try out the different webcam ids to find the correct webcam)
- Use requirements.txt to install the necessary python-packages
- for yoloV4 to work, you have to download the [model](https://github.com/onnx/models/tree/main/validated/vision/object_detection_segmentation/yolov4) and add it to the ./model folder
- the inference-code is trimmed to a means to be as quick as possible (you can define a threshold for confidence, and also the class to detect - 14 is birds)
- To run the while-True loop, let run the main.py file

# additional information
- on my MacbookPro (M2Max), as well as my windows computer, it took about 0.2sec to infer an image, after which a 0.3 (configurable) timeout will wait before detecting the next bird, to avoid having too many pictures of one bird.
  - I left in the timing code (main.py, L:34ff) to uncomment, if you want to run your own timing tests
- since the stored pictures are just hdmi-grabs, the quality is not at its best - triggering a picture on the camera would definitely work better
