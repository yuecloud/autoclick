#coding:utf-8


from tkinter.filedialog import  *
import time
import os
import  Consts
from Tkinter import *

from tkinter.ttk  import *

filepath=None

def show_msg(*args):
    return players.get()


def dowithfile(filepath,strtype):
    list1=[]
    f=open(filepath)
    for line in f.readlines():
        linestr=str(line).strip()
        if linestr.endswith(strtype):
        # if linestr.endswith("\\tDFTT\""):
            # print linestr
            donestr=linestr.split("\\t")
            list1.append(donestr[8])
    # list1=list(set(list1))
    return list1

def save():
    t = listbox_filename.get('0.0','10.0')
    f = open(mi.get(),'w')
    f.write(t)

# def dowithtqkb(filepath):
#     list1=[]
#     f=open(filepath)
#     for line in f.readlines():
#         linestr=str(line).strip()
#         if linestr.endswith("\\tTQKB\""):
#             # print linestr
#             donestr=linestr.split("\\t")
#             list1.append(donestr[8])
#     # list1=list(set(list1))
#     return list1


def callback():
    entry.delete(0,END) #清空entry里面的内容
    listbox_filename.delete(1.0,END)
    # listbox_filename.delete(0,END)
    #调用filedialog模块的askdirectory()函数去打开文件夹
    global filepath
    # filepath = filedialog.askdirectory()

    filepath=askopenfilename()
    if filepath:
        entry.insert(0,filepath) #将选择好的路径加入到entry里面
    print (filepath)
    getdir(filepath)

def getdir(filepath=os.getcwd()):
    """
    用于获取目录下的文件列表
    """
    # cf = os.listdir(filepath)
    # for i in cf:
    # with open(filepath,"r") as f:
    #    lines=f.readlines()
    listbox_filename.insert(END,u"打点处理结果如下:\n")


    resultlist=[]
    print show_msg()


    if show_msg()==Consts.program1:
        for value in dowithfile(filepath,Consts.field1):
            listbox_filename.insert(END,value)
            listbox_filename.insert(END,"\n")
            resultlist.append(value)

    if show_msg()==Consts.program2:
        for value in dowithfile(filepath,Consts.field2):
            listbox_filename.insert(END,value)
            listbox_filename.insert(END,"\n")
            resultlist.append(value)

    elif show_msg()==Consts.program3:
        for value in dowithfile(filepath,Consts.field3):
            listbox_filename.insert(END,value)
            listbox_filename.insert(END,"\n")
            resultlist.append(value)
    # print resultlist
    if not resultlist:
        listbox_filename.insert(END,u"打点日志中找不到按钮记录,请检查具体的日志\n")


if __name__ == "__main__":

    root = Tk()
    root.title(u"处理打点log日志")
    root.geometry("500x500")
    root.rowconfigure(1, weight=1)
    root.rowconfigure(2, weight=8)

    entry = Entry(root, width=100)
    entry.grid(sticky=W+N, row=0, column=0, columnspan=4, padx=5, pady=5)

    button = Button(root,text=u"选择日志文件",command=callback)
    button.grid(sticky=W+N, row=1, column=0, padx=5, pady=5)

    Label(root, text=u"请选择具体的项目：",font =(u"黑体", 10,"normal"),).grid(sticky=W+N, row=1, column=1, padx=5, pady=5)
    #加入下拉框
    name = StringVar()
    mi=StringVar()
    players =Combobox(root, textvariable=name)
    players.grid(sticky=W+N, row=1, column=2,columnspan=4,padx=5, pady=5)

    #创建loistbox用来显示所有文件名

    listbox_filename = Text(height = 30,width =100)
    # listbox_filename = Listbox(root, width=60)
    listbox_filename.grid(row=2, column=0, columnspan=4, rowspan=4,
                            padx=5, pady=5, sticky=W+E+S+N)



    players["values"] = (Consts.program1 ,Consts.program2,Consts.program3)
    players["state"] = "readonly"

    players.current(0)

    players.bind("<<ComboboxSelected>>")

    # players.pack()
    root.iconbitmap('111.ico')

    labe1=Label(text=u'            文件名          ')
    labe1.grid(row=3,column=0,columnspan=4, rowspan=4,
                            padx=5, pady=5, sticky=W+E+S+N)
    # Label(text=u'            文件名          ').pack(side = LEFT)

    entry1 = Entry(root, width=20,textvariable = mi)

    entry1.grid(row=3,column=1,)
    mi.set(time.strftime("%m%d_%H%M", time.localtime( time.time() ) )+".txt")


    button1=Button(text = u'保存' , command = save)
    button1.grid(row=3,column=2,)
    button2=Button(text = u'退出' , command = root.quit)
    button2.grid(row=3,column=3,)

    #
    # mi.set(time.strftime("%m%d_%H%I", time.localtime( time.time() ) )+".txt")
    root.mainloop()