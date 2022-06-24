
import math

import cv2
import mediapipe as mp

class poseDetector():

    def __init__(self, mode=False, smooth=True, detectionCon=0.5, trackCon=0.6):
        self.mode = mode
        self.smooth = smooth
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        self.mpPose = mp.solutions.pose
        self.mpDraw = mp.solutions.drawing_utils
        self.pose = self.mpPose.Pose(static_image_mode=self.mode, smooth_segmentation=self.smooth, 
                                        min_detection_confidence=self.detectionCon, min_tracking_confidence=self.trackCon)

    def get_pose(self, img, draw=True):
        
        # Input from video 
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(imgRGB)

        if self.results.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(img, self.results.pose_landmarks, self.mpPose.POSE_CONNECTIONS)

        return img

    def get_position(self, img, draw=True):
        self.lmList = []
        if self.results.pose_landmarks:
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                h, w, _ = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                self.lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 15, (255,0,0), 5)
        return self.lmList

    def get_angle(self,img, p1, p2, p3, draw=True):

        # Obtain the landmarks , x and y coordinates only
        _, x1, y1 = self.lmList[p1]
        _, x2, y2 = self.lmList[p2]
        _, x3, y3 = self.lmList[p3]

        # Find the angle
        angle = math.degrees(math.atan2(y3-y2, x3-x2) - math.atan2(y1-y2, x1-x2))
        
        # Correcting range of detected angle
        if angle < 0:
            angle += 360
        if angle > 180:
            angle = 360 - angle

        # Draw the lines and angle
        if draw:
            cv2.line(img, (x1, y1), (x2, y2), (255,255,255),1)
            cv2.line(img, (x3, y3), (x2, y2), (255,255,255),1)

            cv2.circle(img, (x1, y1), 6, (255, 0, 0), 5)
            cv2.circle(img, (x2, y2), 6, (255, 0, 0), 5)
            cv2.circle(img, (x3, y3), 6, (255, 0, 0), 5)

            cv2.putText(img, str(int(angle)), (x2-20, y2+50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,0,255), 2)

        return angle

    def main():

        return 0


