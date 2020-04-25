from ctypes import *
import pyautogui
import time
import cv2
import win32gui
import win32ui
import win32con
import win32api
import numpy as np

def window_capture(filename):
    hwnd = 0
    hwndDC = win32gui.GetWindowDC(hwnd)
    mfcDC = win32ui.CreateDCFromHandle(hwndDC)
    saveDC = mfcDC.CreateCompatibleDC()
    saveBitMap = win32ui.CreateBitmap()
    # 腾讯课堂右上角窗口化之后的大小950x509 #
    saveBitMap.CreateCompatibleBitmap(mfcDC, 950, 509)
    saveDC.SelectObject(saveBitMap)
    # 图片左上角起点在1920*1080这么大的左边的(965,6)这个位置 #
    saveDC.BitBlt((0, 0), (950, 509), mfcDC, (965, 6), win32con.SRCCOPY)
    saveBitMap.SaveBitmapFile(saveDC, filename)

# 加载模板 #
img1 = cv2.imread('./img/mask.png',0)
success_count = 0
count = 0
while 1:
    pyautogui.click(1520, 410, clicks=1, interval=0.0, button='left')
    window_capture("result.png")
    img = cv2.imread("./result.png")
    # 签到按钮灰色块块所在的区域 #
    ROI_img = img[313:444,407:701]
    img2 = ROI_img

    orb = cv2.ORB_create()
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    bf = cv2.BFMatcher(normType=cv2.NORM_HAMMING, crossCheck=True)
    if len(kp2) > 0:
        matches = bf.match(des1,des2)
        matches = sorted(matches, key = lambda x:x.distance)
        # 设置的匹配点的阈值 #
        if matches.__len__()>200:
            success_count+=1
            print("success!!!!!!!!!!!")
            cv2.imwrite("./success"+str(success_count)+".png",img)

    count += 1
    print(count)
    time.sleep(10)
