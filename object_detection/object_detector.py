from ultralytics import YOLO
import cv2


class ObjectDetector:
    """
    Class to detect objects from a video
    :param video_path: path to the video file:
    :param model: YOLO object to detect the objects
    """
    def __init__(self, video_path: str, model: YOLO):
        self.video_path = video_path
        self.model = model

    def detect(self):
        """
        Detecting the objects
        :return:
        """
        video = cv2.VideoCapture(self.video_path)

        flag = True

        while flag:
            # Reading the actual frame
            flag, frame = video.read()
            # frame = self.preprocess_frame(frame)
            # TODO: Preprocesar el frame

            if flag:
                # We detect existing objects in the frame
                # Persist True to track movement
                detection = self.model.track(frame, persist=True)

                frame_ = detection[0].plot()

                # We visualize the detection
                cv2.imshow(f"Video: {self.video_path}", frame_)
                # Exit if 'q' key is pressed
                if cv2.waitKey(25) & 0xFF == ord("q"):
                    break

    def preprocess_frame(self, frame):
        """

        :param frame:
        :return:
        """
        # TODO: completar
        return
