
import cv2
import mediapipe as mp
import numpy as np
import math as mt
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
cap = cv2.VideoCapture(0)

# Curl counter variables
counter = 0 
stage = None

frameWidth = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
frameHeight = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

degree = u'\N{DEGREE SIGN}'

def calculate_angle(a,b,c):
    a = np.array(a) # First
    b = np.array(b) # Mid
    c = np.array(c) # End
    
    radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
    angle = np.abs(radians*180.0/np.pi)
    
    if angle >180.0:
        angle = 360-angle
        
    return angle
## Setup mediapipe instance
with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    while cap.isOpened():
        ret, frame = cap.read()
        
        # Recolor image to RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
      
        # Make detection
        results = pose.process(image)
    
        # Recolor back to BGR
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        
        # Extract landmarks
        try:
            landmarks = results.pose_landmarks.landmark
            
            # Get coordinates
            horizon_point = [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x,
                        landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y]
            elbow = [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x,
                     landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
            wrist = [landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x,
                     landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y]
            
            # Calculate angle
            angle = calculate_angle(horizon_point, elbow, wrist)
            
            # Visualize angle
            cv2.putText(image, str(mt.log(angle)), 
                           tuple(np.multiply(elbow, [640, 480]).astype(int)), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
                                )
                
                       
        except:
            pass
        
        x_land_elbow = landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value]
        x_land_wrist = landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value]
        elbow_cord = pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(x_land_elbow.x, x_land_elbow.y, frameWidth, frameHeight)
        wrist_cord = pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(x_land_wrist.x, x_land_wrist.y, frameWidth, frameHeight)
        
        try:
            (elbow_x,elbow_y) = elbow_cord
            (wrist_x,wrist_y) = wrist_cord
            start = (elbow_x,0)
            end = (elbow_x,elbow_y)
            cv2.line(image, start, end, (0, 255, 0), 4)
            if wrist_x>elbow_x:
                stage = "Right"
            if wrist_x<elbow_x:
                stage="Left"

        except:
            pass 

        cv2.putText(image, 'Turning {} by {} degrees'.format(stage,round(angle,2)), 
                    (10,60), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2, cv2.LINE_AA)

        

        
        # Render detections
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=2), 
                                mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2) 
                                 )               
        
        cv2.imshow('Mediapipe Feed', image)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
