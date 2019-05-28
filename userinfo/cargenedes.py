# -*- coding:utf-8 -*-
__author__ = 'whr'
## This example upgrade by Tony Qu in 2019-02-27
## It includes create the car npy
## PLEASE NOTE: It is about one car ,if you upload a car, it will be run.
## to be installed only to read from your webcam.
## If you have trouble installing it, try any of the other demos
## that don't require it instead.
## And if you have any good ideas ,pls connect with me.
## My email : haominqu@hotmail.com
## My WeChat:haomin1114

import cv2
import numpy as np
import os


class GenDesc:
    ## 读取图像，解决imread不能读取中文路径的问题
    def __cv_imread(self,filePath):
        cv_img = cv2.imdecode(np.fromfile(filePath, dtype=np.uint8), -1)
        ## imdecode读取的是rgb，如果后续需要opencv处理的话，需要转换成bgr，转换后图片颜色会变化
        cv_img = cv2.cvtColor(cv_img, cv2.COLOR_RGB2BGR)
        return cv_img

    def __save_descriptor(self,folder, image_path, feature_detector):
        print("读取中... %s" % image_path)
        if image_path.endswith("npy"):
            return
        img = self.__cv_imread(os.path.join(folder, image_path))
        keypoints, descriptors = feature_detector.detectAndCompute(img, None)
        descriptor_file = image_path.replace("jpg", "npy")
        np.save(os.path.join(folder, descriptor_file), descriptors)
        return

    def create_descriptors(self,folder):
        # files = []
        # for (dirpath, dirnames, filenames) in os.walk(folder):
        #     files.extend(filenames)
        #     for f in files:
        #         print(f)
        #         self.__save_descriptor(folder, f, cv2.xfeatures2d.SIFT_create())

        self.__save_descriptor('img/car', folder, cv2.xfeatures2d.SIFT_create())





