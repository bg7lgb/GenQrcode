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

# 常见问题
1. IOError: cannot open resource
如果出现这个错误信息，并且与ImageFont有关的。这是系统没有程序中默认字体导致，可以在命令行参数上加上指定的字体文件名字。如-f simkai.ttf。
系统默认字体是文泉驿正黑wqy-zenhei.ttc。

# ChangeLog
1. 2017-3-9
修改默认字体设置方法。
修改根据系统默认编码进行转码的内容。

# ToDo
1. 增加将二维码、附加信息居中显示的内容
2. 增加二维码、附加信息对齐设置参数
