import os
import sys
import argparse
import cv2

import numpy
from yolo import YOLO, detect_video
from PIL import Image

def detect_img(yolo):
#     while True:
#         img = input('Input image filename:')
#         try:
#             image = Image.open(img)
#         except:
#             print('Open Error! Try again!')
#             continue
#         else:
#             r_image = yolo.detect_image(image)
#             r_image.show()
#     yolo.close_session()
    for i in os.listdir("./FinalGeneratedImages"):
        print(i)
        try:
            image = Image.open("./FinalGeneratedImages/" + i)
            #image = cv2.imread("./FinalGeneratedImages/" + i)
        except:
            print('Open Error! Try again!')
            continue
        else:
        
            r_image = yolo.detect_image(image)
            #r_image.show()
            cimg = numpy.array(r_image) 
            cv2.imshow("u", cimg)
            cv2.waitKey(0)
    yolo.close_session()



FLAGS = None

if __name__ == '__main__':
    # class YOLO defines the default value, so suppress any default here
    parser = argparse.ArgumentParser(argument_default=argparse.SUPPRESS)
    '''
    Command line options
    '''
    parser.add_argument(
        '--model', type=str,
        help='path to model weight file, default ' + YOLO.get_defaults("model_path")
    )

    parser.add_argument(
        '--anchors', type=str,
        help='path to anchor definitions, default ' + YOLO.get_defaults("anchors_path")
    )

    parser.add_argument(
        '--classes', type=str,
        help='path to class definitions, default ' + YOLO.get_defaults("classes_path")
    )

    parser.add_argument(
        '--gpu_num', type=int,
        help='Number of GPU to use, default ' + str(YOLO.get_defaults("gpu_num"))
    )


    FLAGS = parser.parse_args()

 
    detect_img(YOLO(**vars(FLAGS)))

