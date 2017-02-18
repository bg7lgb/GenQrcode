#-*-coding:utf-8 -*-
#
# wyf <bg7lgb@gmail.com>
#
import argparse
import qrcode
from PIL import Image, ImageDraw, ImageFont
import os
import random
import chardet


class GenQrcode(object):
#    self.qr_size = 10                # default qrcode box size 210px
#    self.text_pos = 'bottom'         # default text position
#    self.text_font = 'simhei.ttf'    # default text font
#    self.text_font_size = 40         # default text font size

    def __init__(self, size, pos, font, fontsize):
        
        self.__size = 210
        self.__pos = 'bottom'
#        self.__font = 'simhei.ttf'
        self.__font = 'wqy-zenhei.ttc'
        self.__fontsize = 40
        self.__ratio = 21            # version 1, qrcode size 21px

        if size:
            self.__size = size           # default qrcode box size, 210px
        if pos:
            self.__pos = pos             # default text position
        if font:
            self.__font = font           # default text font
        if fontsize:
            self.__fontsize = fontsize   # default text font size 

    def genFilename(self, code):
        if code is None:
            return None

        out_file = os.path.join(os.getcwd(), code) + ".png"

        if os.path.exists(out_file):
            ext = '_' + str(random.random())[-6:]
            out_file = os.path.join(os.getcwd(), code + ext) + ".png"

        return out_file
        
    def genQrcode(self, code, text):
        
        if code is None:
            print "please input code"
            return

        self.qr = qrcode.QRCode(version = 1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size = self.__size/self.__ratio,
            border = 0)

        self.qr.add_data(code)
        self.qr.make(fit = True)

        # generate qrcode image
        img = self.qr.make_image()
        w, h = img.size
        mode = img.mode

        # generate output filename
        outfile = self.genFilename(code)
        
        # generate font object
        font = ImageFont.truetype(self.__font, self.__fontsize)

        if text:
            # convert text to unicode
#            text = text.decode('utf-8')
            text = text.decode(chardet.detect(text)['encoding'])

            draw = ImageDraw.Draw(img)

            # calc text size
            textsize = draw.textsize(text, font)

            if self.__pos == 'bottom':
                # calc new image width and height
                newimg_height = h + textsize[1]
                newimg_width = w if w > textsize[0] else textsize[0]

                qr_x = 0
                qr_y = 0

                text_x = 0
                text_y = h
            elif self.__pos == 'top':
                newimg_height = h + textsize[1]
                newimg_width = w if w > textsize[0] else textsize[0]

                qr_x = 0
                qr_y = textsize[1]

                text_x = 0
                text_y = 0
            elif self.__pos == 'left':
                newimg_height = h if h > textsize[1] else textsize[1]
                newimg_width = w + textsize[0]

                qr_x = textsize[0]
                qr_y = 0

                text_x = 0
                text_y = 0
            else:   # position right
                newimg_height = h if h > textsize[1] else textsize[1]
                newimg_width = w + textsize[0]

                qr_x = 0
                qr_y = 0

                text_x = w
                text_y = 0

            # create new image
            newimg = Image.new(mode, (newimg_width, newimg_height), 255)
            newimg.paste(img, (qr_x, qr_y))

            newdraw = ImageDraw.Draw(newimg)
            newdraw.text((text_x, text_y), text , font=font, fill='black')
                
            newimg.save(outfile)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--size", type=int, help="set qrcode size, in px")
    parser.add_argument("-f", "--font", help="set text font")
    parser.add_argument("-z", "--fontsize", type=int, help="set text font size")
    parser.add_argument("-p", "--position", choices=["bottom", "top", "left", "right"], help="set text postion, left|right|top|bottom, default is bottom")
    parser.add_argument("code", help="code for qrcode")
    parser.add_argument("txt", help="append text")
    args = parser.parse_args()

    genQr = GenQrcode(size =args.size, pos=args.position,
        font=args.font, fontsize=args.fontsize)
    genQr.genQrcode(args.code, args.txt)
    
if __name__ == '__main__':
    main()
