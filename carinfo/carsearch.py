# -*- coding:utf-8 -*-
__author__ = 'whr'
## This example upgrade by Tony Qu in 2019-02-25
## It includes some basic function about search a car or
## a part of car in some known_car
## PLEASE NOTE: This example requires OpenCV (the `cv2` library)
## to be installed only to read from your webcam.
## And please install opencv-python==3.4.2.16 and opencv-contrib-python==3.4.2.16
## If you have trouble installing it, try any of the other demos
## that don't require it instead.

import cv2
import numpy as np
import os


class CarSearch:
    # 读取图像，解决imread不能读取中文路径的问题
    # def __cv_imread(self,filePath):
    #     cv_img = cv2.imdecode(np.fromfile(filePath, dtype=np.uint8), -1)
    #     ## imdecode读取的是rgb，如果后续需要opencv处理的话，需要转换成bgr，转换后图片颜色会变化
    #     cv_img = cv2.cvtColor(cv_img, cv2.COLOR_RGB2BGR)
    #     return cv_img

    def carSearch(self,queryImgPath,imgDBFolder):
        # qhm
        imageas= np.asarray(bytearray(queryImgPath), dtype="uint8")
        query = cv2.imdecode(imageas, cv2.IMREAD_COLOR)
        ##whr
        # query = cv2.imread(image, 0)
        # create files, images, descriptors globals
        files = []
        images = []
        descriptors = []
        for (dirpath, dirnames, filenames) in os.walk(imgDBFolder):
            files.extend(filenames)
            for f in files:
                if f.endswith("npy"):
                    descriptors.append(f)


        # create the sift detector
        sift = cv2.xfeatures2d.SIFT_create()
        query_kp, query_ds = sift.detectAndCompute(query, None)
        # 特征点, 特征描述

        # create FLANN matcher
        FLANN_INDEX_KDTREE = 0
        index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
        search_params = dict(checks=50)
        flann = cv2.FlannBasedMatcher(index_params, search_params)

        # minimum number of matches
        MIN_MATCH_COUNT = 10

        potential_fruits = {}
        potential_matches = {}

        # print(">> 初始化扫描图片...")
        for d in descriptors:
            # print("--------- 分析 %s 匹配 ------------" % d)
            matches = flann.knnMatch(query_ds, np.load(os.path.join(imgDBFolder, d)), k=2)
            good = []
            for m, n in matches:
                if m.distance < 0.7 * n.distance:
                    good.append(m)
            if len(good) > MIN_MATCH_COUNT:
                print("%s 可匹配! (%d)" % (d, len(good)))
            else:
                print("%s 不匹配" % d)
            potential_fruits[d] = len(good)
            potential_matches[d] = good

        max_matches = None
        potential_suspect = None
        well = None
        for fruit, matches in potential_fruits.items():
            if max_matches == None or matches > max_matches:
                max_matches = matches
                potential_suspect = fruit
                well = potential_matches[fruit]
        result = potential_suspect.replace(".npy", "")
        print("可能匹配的是 %s" % result.upper())
        return result