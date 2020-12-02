import os
from threading import Thread
import cv2
# opencv-python
import keyboard
import numpy as np
import pyautogui as pg
from tensorflow.keras.models import model_from_json
# tanserfow-2.3.0

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'


class MyThread(Thread):
    deth = False

    def __init__(self, name, flag=True):
        Thread.__init__(self)
        self.name = name
        self.flag = flag
        self.deth = False
        self.model = self.open_model_json('my_model')
        self.model.load_weights('weights.h5')

    def run(self):
        while not self.deth:
            if self.flag:
                try:
                    pg.sleep(1)
                    img = pg.screenshot()
                    img = np.array(img)
                    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    gray_image = self.resizeIMG(gray_image, 25)
                    ret, threshold_image = cv2.threshold(gray_image, 127, 255, 0)
                    # self.showCV2File(threshold_image,'333')
                    input_img = []
                    input_img.append(threshold_image)
                    input_img = np.expand_dims(input_img, axis=3)
                    out_model = self.model.predict(input_img)

                    # print(out_model, int(out_model[0][0]) == 1)
                    if (int(out_model[0][0]) == 1):
                        keyboard.send("Enter")
                        print("Я играю в доту и я принимаю это :(")
                        pg.sleep(1)

                except IndexError:
                    False
            else:
                pg.sleep(1)

    def swich_flag(self):
        self.flag = not self.flag
        if (self.flag):
            print("Поиск включен")
        else:
            print("Поиск отключен")

    def deth_Thread(self):
        self.deth = True

    def open_model_json(self, name):
        with open(f'{name}.json', 'r') as f:
            loaded_model = model_from_json(f.read())
        return loaded_model

    def resizeIMG(self, image, procent):
        scale_percent = procent  # Процент от изначального размера
        width = int(image.shape[1] * scale_percent / 100)
        height = int(image.shape[0] * scale_percent / 100)
        dim = (width, height)
        return cv2.resize(image, dim, interpolation=cv2.INTER_AREA)

    def showCV2File(self, image, text):
        cv2.namedWindow(text, cv2.WINDOW_NORMAL)
        cv2.imshow(text, image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
