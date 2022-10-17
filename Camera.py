#ライブラリのインポート
import cv2
import numpy as np
#画像の読み込み

img=cv2.imread('hk.jpg',cv2.IMREAD_COLOR)#後ほどカメラ起動に切り替えます
h,w=img.shape[:2]
split_x=3
split_y=1
#画像の分割処理
cx=0
cy=0
answer = "weed"
data = []

for j in range(split_x):
    for i in range(split_y):
        split_pic=img[cy:cy+int(h/split_y),cx:cx+int(w/split_x),:]
        cy=cy+int(h/split_y)
        #画像を送る

        #結果を受け取る
        if answer == "weed":
            #除草剤の蓋をopen
            data.append(int(1))
        else:
            #何もしない
            data.append(int(0))



    cy=0
    cx=cx+int(w/split_x)

