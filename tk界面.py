#coding:utf-8
import tkinter
import tkinter.messagebox
from PIL import Image,ImageTk
#打开指定图片，缩放指定尺寸
def get_image(filename,width,height):
    im = Image.open(filename).resize((width,height))
    return ImageTk.PhotoImage(im)
root = tkinter.Tk()
root.title("背景图片")
root.geometry("800x600+300+150")
root.resizable(False,False)
#创建画布，设置要显示的图片，把画布添加到应用程序窗口
canvas_root=tkinter.Canvas(root,width=800,height=600)
im_root=get_image("1.jpg",800,600)
canvas_root.create_image(400,300,image=im_root)
canvas_root.pack()
#Label组件设置图片
im_label=get_image("201912.14.jpg",100,40)
IbImage = tkinter.Label(root,text="我是一个标签",
                        image=im_root)
IbImage.place(x=3,y=3,width=100,height=40)
#为按钮设置背景照片
def onclick():
    tkinter.messagebox.showinfo("提示","别点我,你个笨蛋")
im_button =get_image("20191214132427.jpg",100,40)
btonk = tkinter.Button(root,text="确定",
                       image=im_button,
                       compound=tkinter.CENTER,
                       command=onclick)
btonk.place(x=100,y=3,width=100,height=40)
#为复选框设置背景图片
variable_checkbutton=tkinter.IntVar(root,value=1)
im_checkbutton=get_image("3.jpg",80,40)
def checkChanged():
    msg="选中" if variable_checkbutton.get()==1 else "未选中，你处于笨蛋"
    tkinter.messagebox.showinfo("提示",f"复选框{msg}状态")
cbtnText = tkinter.Checkbutton(root,text="测试",
                               variable=variable_checkbutton,
                               onvalue=1,offvalue=0,
                               compound=tkinter.CENTER,
                               image=im_checkbutton,
                               command=checkChanged)
cbtnText.place(x=230,y=3,width=100,height=40)
root.mainloop()