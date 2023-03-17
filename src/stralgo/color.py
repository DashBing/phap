import ctypes
from sys import stdout as __s
'''
STD_INPUT_HANDLE = -10

STD_OUTPUT_HANDLE = -11

STD_ERROR_HANDLE = -12

# 字体颜色定义 text colors

FOREGROUND_BLUE = 0x09 # blue.

FOREGROUND_GREEN = 0x0a # green.

FOREGROUND_RED = 0x0c # red.

FOREGROUND_YELLOW = 0x0e # yellow.

# 背景颜色定义 background colors

BACKGROUND_YELLOW = 0xe0 # yellow.

# get handle

std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)

def set_cmd_text_color(color, handle=std_out_handle):

    Bool = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)

    return Bool

# reset white

def resetColor():

    set_cmd_text_color(FOREGROUND_RED | FOREGROUND_GREEN | FOREGROUND_BLUE)

#blue
def blue(mess):

    set_cmd_text_color(FOREGROUND_BLUE)

    sys.stdout.write(mess + '\n')

    resetColor()

# green

def green(mess):

    set_cmd_text_color(FOREGROUND_GREEN)

    sys.stdout.write(mess + '\n')

    resetColor()

# red

def red(mess):

    set_cmd_text_color(FOREGROUND_RED)

    sys.stdout.write(mess + '\n')

    resetColor()

# yellow

def yellow(mess):

    set_cmd_text_color(FOREGROUND_YELLOW)

    sys.stdout.write(mess + '\n')

    resetColor()

# white bkground and black text

def printYellowRed(mess):

    set_cmd_text_color(BACKGROUND_YELLOW | FOREGROUND_RED)

    sys.stdout.write(mess + '\n')

if __name__ == "__main__":
    red("红")
    yellow("黄")
    blue("蓝")
    green("绿")
    print("正常")
    while True:
        pass
'''
INPUT_HANDLE = -10
OUTPUT_HANDLE = -11
ERROR_HANDLE = -12

def gethandle(handle_num):
    return(ctypes.windll.kernel32.GetStdHandle(handle_num))

out_handle = ctypes.windll.kernel32.GetStdHandle(OUTPUT_HANDLE)

BLUE = 0x09 # blue.
GREEN = 0x0a # green.
RED = 0x0c # red.
YELLOW = 0x0e # yellow.

def setcolor(color, backcolor = "none", use_hex = False, handle=out_handle):
    if use_hex:
        Bool = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
    else:
        d = {
            "none":0,
            "blue":0x09,
            "green":0x0a,
            "red":0x0c,
            "yellow":0x0e,
            "black":0x00,
            "purple":0x05,
            "white":0x07,
            "lightwhite":0x0f,
             }
        Bool = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, d[backcolor] * 0x10 + d[color])
    return Bool

def reset_color():
    return(setcolor("white"))
def reset_color_plus():
    return(setcolor("lightwhite"))
def reset_color_old():
    return(setcolor(RED | GREEN | BLUE,use_hex = True))

if __name__ == "__main__":
    setcolor("red")
    __s.write("红\n")
    setcolor("yellow")
    
    __s.write("黄\n")
    
    setcolor("blue")
    __s.write("蓝\n")
    
    setcolor("green")
    __s.write("绿\n")
    
    setcolor("purple")
    __s.write("紫\n")
    
    setcolor("black")
    __s.write("黑\n")
    
    setcolor("white")
    __s.write("白\n")
    
    setcolor("lightwhite")
    __s.write("亮白\n")
    
    setcolor(BLUE,use_hex = True)
    __s.write("hex蓝\n")

    __s.flush()

    setcolor("red")
    print("print红")
    
    while True:
        pass
