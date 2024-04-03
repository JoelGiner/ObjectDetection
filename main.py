from ultralytics import YOLO

from object_detection.object_detector import ObjectDetector
from config import YOLO_MODEL, VIDEO_PATH

if __name__ == "__main__":
    # Load the model
    model = YOLO(YOLO_MODEL)
    # Detect objects in the video
    detector = ObjectDetector(video_path=VIDEO_PATH, model=model)
    detector.detect()







