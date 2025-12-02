import cv2
import numpy as np
filepath = r'd:\anaconda\envs\object\workplace\1.jpg'
img = cv2.imread(filepath)
height, width = img.shape[:2]

b_channel = img[:,:,0]
g_channel = img[:,:,1]
r_channel = img[:,:,2]

red = np.zeros_like(img)
red[:,:,2] = r_channel 
half = width // 2
modified_img = img.copy()
right_half = modified_img[:, half:width]
right_half_red = right_half[:,:,2]
right_half_red_3channel = cv2.merge([np.zeros_like(right_half_red), np.zeros_like(right_half_red), right_half_red])
modified_img[:, half:width] = right_half_red_3channel
cv2.namedWindow('修改后', cv2.WINDOW_NORMAL)
cv2.imshow('修改后', modified_img)
cv2.namedWindow('原始图像', cv2.WINDOW_NORMAL)
cv2.imshow('原始图像', img)
print("按任意键关闭所有窗口...")
cv2.waitKey(0)
cv2.destroyAllWindows()


