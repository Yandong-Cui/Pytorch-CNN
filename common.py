#生成数据集（训练集和验证集的验证码图片数据）

import os
import random
import time

captcha_array=list("0123456789abcdefghijklmnopqrstuvwxyz")
captcha_size=4
from captcha.image import ImageCaptcha
if __name__ == '__main__':
    print(captcha_array)
    image =ImageCaptcha()
    for i in range(20000):
        image_val = "".join(random.sample(captcha_array, 4))

        image_name = "D:\\app for myself\\pycharm\\验证码识别\Bili\\train\\{}_{}.png".format(image_val, int(time.time()))
        print(image_name)
        image.write(image_val,image_name)
