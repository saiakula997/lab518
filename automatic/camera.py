import sys 
import cv2
import time
import argparse
import numpy as np
from vimba import *


LOWER_TH = 3.0
HIGHER_TH = 5.0

parser = argparse.ArgumentParser()
parser.add_argument('--method', type=int, required=True)
parser.add_argument('--output', type=str, required=True)
args = parser.parse_args()


def get_median(cam):
    frame = cam.get_frame()
    frame.convert_pixel_format(PixelFormat.Mono8)
    image = frame.as_opencv_image()
    return np.median(image), image

# Method 1 calibrate 
def Calibrate_Capture(cam, name):
    print("Calibrating ...")
    while True:
        gain = cam.Gain.get()
        exp_t = cam.ExposureTime.get()
        inc = cam.ExposureTime.get_increment()*10000
        median, image = get_median(cam)
        print("exp, gain, median", exp_t, gain, median)
        if median < LOWER_TH:
            exp_t +=  inc 
        elif median > HIGHER_TH:
            exp_t -= inc 
        else:
            print("Calibrated")
            cv2.imwrite(args.output+name+'.png', image)
            print("Captured image with ExposureTime {0} Gain {1}".format(exp_t, gain))
            break
        try: #[12.957, 849053.826]
            cam.ExposureTime.set(exp_t)
        except:
            print("ExposureTime Limit exceeded, Changing Gain ")
            gain += -1.0 if exp_t < 0 else 1.0
            try:
                cam.Gain.set(gain)
            except:
                print("Failed to Capture - ExposureTime {0} Gain {1}".format(exp_t, gain))
                break
        time.sleep(1.0)


# Method 0 Range Capture 
def Capture(cam,name):
    frame = cam.get_frame()
    frame.convert_pixel_format(PixelFormat.Mono8)
    cv2.imwrite(args.output+name+'.png', frame.as_opencv_image())
    print("Captured", name, np.median(frame.as_opencv_image()), cam.ExposureTime, cam.Gain)


if __name__ == "__main__":
    with Vimba.get_instance() as vimba:
        #cams = vimba.get_all_cameras() #get first camera
        with vimba.get_all_cameras()[0] as cam:
            cam.load_settings("refracted_settings_1.xml", PersistType.All)
            if args.method == 0:
                for count, gain  in enumerate(range(0, 25, 3)):
                    Capture(cam, str(count))
                    cam.Gain.set(gain)
                    time.sleep(0.5)
            elif args.method == 1:
                cam.Gain.set(10)
                Calibrate_Capture(cam, "calibrated_image")
            
    print("Done")
    sys.exit()