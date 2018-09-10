import cv2
from time import sleep
# Create a VideoCapture object
cap = cv2.VideoCapture(0)

# Check if camera opened successfully
if (cap.isOpened() == False):
  print("Unable to read camera feed")

# Default resolutions of the frame are obtained.The default resolutions are system dependent.
# We convert the resolutions from float to integer.
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

# Define the codec and create VideoWriter object.The output is stored in 'outpy.avi' file.
for i in range(2):
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cv2.imwrite('test'+str(i)+'.jpg', frame)
    # When everything done, release the video capture and video write objects
    
    sleep(2)
# Closes all the frames
cap.release()
cv2.destroyAllWindows()


# 출처: http://steki.tistory.com/entry/OpenCV와-Python을-이용한-Webcam-Capture [Let's go!]
