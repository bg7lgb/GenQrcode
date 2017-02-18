# GenQrcode
写这个小工具，主要是前段时间项目需要输出大量二维码，用程序输出的二维码，不带可见的文字信息。所以才写了这个小工具，在输出二维码的同时，可以在码的周围附加上指定的文字内容。

# 使用方法
    usage: genqrcode.py [-h] [-s SIZE] [-f FONT] [-z FONTSIZE] [-p {bottom,top,left,right}] code txt

    positional arguments:
    code                  二维码内容
    txt                   二维码外面附加的信息，可以是与二维码内容相同，也可不同

    optional arguments:
    -h, --help            show this help message and exit
    -s SIZE, --size SIZE  set qrcode size, in px
    -f FONT, --font FONT  set text font
    -z FONTSIZE, --fontsize FONTSIZE set text font size
    -p {bottom,top,left,right}, --position {bottom,top,left,right} set text postion, left|right|top|bottom, default is bottom
