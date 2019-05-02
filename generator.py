from functions import *
from PIL import Image, ImageDraw, ImageFont
import time

text_file = 'resources/text/lorem.txt'

img_num = 100
start_index = 100
image_size = 256
dataset_path = 'dataset/' + str(image_size) + '/'

font_path = 'resources/fonts/'
fonts = getFonts(font_path)
font_size = 14
font_size_delta = 16
font_color = (0, 0, 0)

text_angle = 0
text_angle_delta = 0
text_x_offset = -20
text_x_offset_delta = 25
text_y_offset = -20
text_y_offset_delta = 5
text_line_space = 5
text_line_space_delta = 5

text = getRandomText(text_file)

for i in range(len(fonts)):
    for j in range(img_num):
        img = Image.new('RGB', (image_size, image_size), color = 'white')
        d = ImageDraw.Draw(img)

        size = round(font_size + rand()*font_size_delta)
        font = ImageFont.truetype(fonts[i]['path'], size)

        x = text_x_offset + rand()*text_x_offset_delta
        y = text_y_offset + rand()*text_y_offset_delta
        line_space = size + text_line_space + rand()*text_line_space_delta

        while(y<image_size):
            d.text((x, y), random.choice(text), font=font, fill=font_color)
            y+=line_space

        img.save(dataset_path + fonts[i]['name'] + '_' + str(start_index + j) + '.jpg')
        time.sleep(0.05)
