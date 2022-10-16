# import cv2
# from imutils.video import VideoStream
# from imutils.video import FPS
# import time

# import time
# from adafruit_extended_bus import ExtendedI2C as I2C
# import adafruit_circuitpython_pca9685


# vs = VideoStream(src=0).start()
# time.sleep(2.0)
# fps = FPS().start()
# while True:
#     frame = vs.read()
#     cv2.imshow("Frame", frame)
#     key = cv2.waitKey(1) & 0xFF
#     # if the `q` key was pressed, break from the loop
#     if key == ord("q"):
#         break
#     # update the FPS counter
#     fps.update()
# fps.stop()
# print("[INFO] elapsed time: {:.2f}".format(fps.elapsed()))
# print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))
# cv2.destroyAllWindows()
# vs.stop()
#--------------------------------------------------------------
# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time

from board import SCL, SDA
import busio
from adafruit_extended_bus import ExtendedI2C as I2C
# Import the PCA9685 module. Available in the bundle and here:
#   https://github.com/adafruit/Adafruit_CircuitPython_PCA9685
from adafruit_motor import servo
from adafruit_pca9685 import PCA9685

#i2c = I2C(8)
i2c = busio.I2C(SCL, SDA)
# Create a simple PCA9685 class instance.
pca = PCA9685(i2c)
# You can optionally provide a finer tuned reference clock speed to improve the accuracy of the
# timing pulses. This calibration will be specific to each board and its environment. See the
# calibration.py example in the PCA9685 driver.
# pca = PCA9685(i2c, reference_clock_speed=25630710)
pca.frequency = 50

# To get the full range of the servo you will likely need to adjust the min_pulse and max_pulse to
# match the stall points of the servo.
# This is an example for the Standard servo - TowerPro SG-5010 - 5010:
#   https://www.adafruit.com/product/155
servo7 = servo.Servo(pca.channels[1], min_pulse=400, max_pulse=2400)
# The pulse range is 750 - 2250 by default. This range typically gives 135 degrees of
# range, but the default is to use 180 degrees. You can specify the expected range if you wish:
# servo7 = servo.Servo(pca.channels[0], actuation_range=10)
#servo7 = servo.Servo(pca.channels[7])

# We sleep in the loops to give the servo time to move into position.
servo7.angle = 80

# while True:
#     for i in range(10):
#         servo7.angle = i
#         time.sleep(0.03)
#     for i in range(10):
#         servo7.angle = 10 - i
#         time.sleep(0.03)

# You can also specify the movement fractionally.
# fraction = 0.0
# while fraction < 1.0:
#     servo7.fraction = fraction
#     fraction += 0.01
#     time.sleep(0.03)
