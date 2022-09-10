import cv2
from imutils.video import VideoStream
from imutils.video import FPS
import time

vs = VideoStream(src=0).start()
time.sleep(2.0)
fps = FPS().start()
while True:
    frame = vs.read()
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF
    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break
    # update the FPS counter
    fps.update()
fps.stop()
print("[INFO] elapsed time: {:.2f}".format(fps.elapsed()))
print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))
cv2.destroyAllWindows()
vs.stop()