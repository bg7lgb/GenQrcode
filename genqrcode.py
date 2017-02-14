#-*-coding:utf-8 -*-
#
# wyf <bg7lgb@gmail.com>
#
import argparse
import qrcode
from PIL import Image, ImageDraw, ImageFont
import os

qr_size = 10                # default qrcode box size 210px
text_pos = 'bottom'         # default text position
text_font = 'simhei.ttf'    # default text font
text_font_size = 40         # default text font size

def make_qrcode(code, txt):
    global text_font, text_font_size, text_pos

    qr = qrcode.QRCode(version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H, 
        box_size = qr_size,
        border = 0)
    qr.add_data(code)
    qr.make(fit = True)
    img = qr.make_image()
    
    w, h = img.size 
    mode = img.mode

    out_file = os.path.join(os.getcwd(),code) + ".png"

    # 生成font对象
    font = ImageFont.truetype(text_font, text_font_size)

    if txt:
        txt = txt.decode('gbk')
        draw = ImageDraw.Draw(img)
        text_size = draw.textsize(txt, font)

        if text_pos == "bottom":
            new_height = h + text_size[1]
            new_width = w if w >text_size[0] else text_size[0]

            print w, h
            print new_width, new_height

            new_img = Image.new(mode, (new_width, new_height), (255,255,255))
            new_img.paste(img, ((new_width-w)/2, (new_height - text_size[1] - h)/2))

            new_draw = ImageDraw.Draw(new_img)
            x1 = (new_width - text_size[0])/2
            y1 = (new_height - h - text_size[1])/2 + h

            new_draw.text((x1, y1), txt, font=font, fill='black')
        
        elif text_pos == "top":
            new_height = h + text_size[1]
            new_width = w if w >text_size[0] else text_size[0]

            new_img = Image.new(mode, (new_width, new_height), (255,255,255))
            new_img.paste(img, ((new_width - w)/2, (text_size[1]+(new_height-h-text_size[1])/2)))

            new_draw = ImageDraw.Draw(new_img)
            x1 = (new_width - text_size[0])/2
            y1 = text_size[1]/2

            new_draw.text((x1, y1), txt, font=font, fill='black')
        elif text_pos == "left":
            new_height = h if h > text_size[1] else text_size[1]
            new_width = w + text_size[0]

            new_img = Image.new(mode, (new_width, new_height), (255,255,255))
            new_img.paste(img, ((new_width - text_size[0] - w)/2, (new_height - h)/2))
            new_draw = ImageDraw.Draw(new_img)

            x1 = (new_width - text_size[0] - w)/2
            y1 = (new_height -text_size[1])/2

            new_draw.text((x1, y1), txt, font=font, fill='black')
        else:  # right
            new_height = h if h > text_size[1] else text_size[1]
            new_width = w + text_size[0]

            new_img = Image.new(mode, (new_width, new_height), (255,255,255))
            new_img.paste(img, ((new_width - text_size[0] - w)/2,(new_height - h )/2))

            new_draw = ImageDraw.Draw(new_img)
            x1 = (new_width-text_size[0]-w)/2 + w
            y1 = (new_height - text_size[1])/2

            new_draw.text((x1, y1), txt , font=font, fill='black')

        new_img.save(out_file)

def main():
    global text_font, text_font_size, text_pos

    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--size", type=int, help="set qrcode size, in px")
    parser.add_argument("-f", "--font", help="set text font")
    parser.add_argument("-z", "--fontsize", type=int, help="set text font size")
    parser.add_argument("-p", "--position", choices=["bottom", "top", "left", "right"], help="set text postion, left|right|top|bottom, default is bottom")
    parser.add_argument("code", help="code for qrcode")
    parser.add_argument("txt", help="append text")
    args = parser.parse_args()

    if args.size:
        # qrcode version 1, qrcode size is 21px
        qr_size = args.size/21
        print qr_size
  
    if args.font:
        text_font = args.font

    if args.fontsize:
        text_font_size = args.fontsize

    if args.position:
        text_pos = args.position

    make_qrcode(args.code, args.txt)

if __name__ == '__main__':
    main()
