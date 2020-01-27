import os
import cv2
import numpy as np
from keras.models import load_model, model_from_json
from keras.preprocessing import image

import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
import tensorflow as tf
graph = tf.get_default_graph()

face_haar_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
model = model_from_json(open("fer.json", "r").read())
model.load_weights('fer.h5')


class VideoCamera(object):

    emotion = ""

    def __init__(self):
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        self.video.release()

    def get_frame(self):
        ret,test_img=self.video.read()# captures frame and returns boolean value and captured image
        gray_img= cv2.cvtColor(test_img, cv2.COLOR_BGR2GRAY)
        #haar cascade detector
        faces_detected = face_haar_cascade.detectMultiScale(gray_img, 1.32, 5)
        for (x,y,w,h) in faces_detected:
            cv2.rectangle(test_img,(x,y),(x+w,y+h),(255,0,0),thickness=7)
            roi_gray=gray_img[y:y+w,x:x+h]#cropping region of interest i.e. face area from  image
            roi_gray=cv2.resize(roi_gray,(48,48))
            img_pixels = image.img_to_array(roi_gray)
            img_pixels = np.expand_dims(img_pixels, axis = 0)
            img_pixels /= 255
            with graph.as_default():
                predictions = model.predict(img_pixels)
            #find max indexed array
            max_index = np.argmax(predictions[0])
            emotions = ('angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral')
            #predict from model
            predicted_emotion = emotions[max_index]
            self.emotion = predicted_emotion
        resized_img = cv2.resize(test_img, (1000, 700))
        ret,jpeg = cv2.imencode('.jpg' , resized_img)
        return (jpeg.tobytes())

    def get_emotion(self):
        return (self.emotion)
