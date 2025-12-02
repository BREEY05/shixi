import cv2 as cv
import numpy as np
from PIL import ImageFont, ImageDraw, Image

img_path = r'd:\anaconda\envs\object\workplace\dengchao.png'
img = cv.imread(img_path)
print("输出图片的维度:", img.shape)
height, width = img.shape[:2]
rect_top_left = (50, 50)  # 矩形框左上角坐标
rect_bottom_right = (width - 115, height - 90)  
color = (0, 0, 255)  
thickness = 2
cv.rectangle(img, rect_top_left, rect_bottom_right, color, thickness)

font_path = r'C:\Windows\Fonts\simhei.ttf' 
text = '人工智能231:姜入文'

def put_chinese_text(img, text, position, font_path, font_size=20, color=(255, 0, 0), align='left'):
    img_pil = Image.fromarray(cv.cvtColor(img, cv.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(img_pil)
    font = ImageFont.truetype(font_path, font_size)
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    if align == 'center':
        x = position[0] - text_width // 2
        y = position[1]
        position = (x, y)
    elif align == 'right':
        x = position[0] - text_width
        y = position[1]
        position = (x, y)
    draw.text(position, text, font=font, fill=color)
    return cv.cvtColor(np.array(img_pil), cv.COLOR_RGB2BGR)

text_font_size = 15
text_position_x = (rect_top_left[0] + rect_bottom_right[0]) // 2
text_position_y = rect_top_left[1] - 20  # 矩形框上方30像素
text_position = (text_position_x, text_position_y)
img = put_chinese_text(img, text, text_position, font_path, font_size=text_font_size, color=(255, 0, 0), align='center')

watermark_path = r'd:\anaconda\envs\object\workplace\1.jpg'
watermark = cv.imread(watermark_path)

if watermark is not None:
    watermark_height = int(height * 0.30) 
    watermark_ratio = watermark_height / watermark.shape[0]
    watermark_width = int(watermark.shape[1] * watermark_ratio)
    watermark = cv.resize(watermark, (watermark_width, watermark_height))
    watermark_x = width - watermark_width 
    watermark_y = height - watermark_height
    watermark_alpha = 0.7  # 默认50%透明度
    roi = img[watermark_y:watermark_y+watermark_height, watermark_x:watermark_x+watermark_width]
  
    blended = cv.addWeighted(roi, 1-watermark_alpha, watermark, watermark_alpha, 0)
    img[watermark_y:watermark_y+watermark_height, watermark_x:watermark_x+watermark_width] = blended
    
cv.namedWindow('Result', cv.WINDOW_NORMAL)
cv.imshow('Result', img)
print("图像窗口已打开")
print("按任意键关闭窗口...")
cv.waitKey(0) 
cv.destroyAllWindows()
print("图像窗口已关闭")
