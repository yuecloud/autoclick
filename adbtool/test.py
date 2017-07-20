#coding:utf-8

from tkinter.filedialog import  *
import os
from Tkinter import *
from tkinter.ttk  import *
from scriptUtils import utils
import json
import tempfile

import  get_cpu_mem_info

PATH = lambda p: os.path.abspath(p)
tempFile = tempfile.gettempdir()



def get_match_apk(package_name):
    list = []

    for packages in utils.shell("pm list packages -f %s" %package_name).stdout.readlines():
        print packages.split(":")[-1].split("=")[0]
        list.append(packages.split(":")[-1].split("=")[0])
    apk_name = list[0].split("/")[-1]

    print tempFile,apk_name


    print u"---上传App到本地temp目录----"
    if  apk_name  not in os.listdir(tempFile):
        utils.adb("pull %s %s" %(list[0], tempFile)).wait()
        print u"---上传App结束---"
    else:

        print u"---本地app已存在，不需要上传---"



    #


    return PATH("%s/%s" %(tempFile, apk_name))




    # os.popen("del %s\\*.apk" %tempFile)



def getcup_meminfo():
    entry.delete(0,END) #清空entry里面的内容
    listbox_filename.delete(1.0,END)
    listbox_filename.insert(END,u"生成的cpu和内存图标见chart目录,默认抓取20次")
    get_cpu_mem_info.line_chart()


def callback():
    entry.delete(0,END) #清空entry里面的内容
    listbox_filename.delete(1.0,END)
    global filepath


    filepath=askopenfilename()
    if filepath:
        entry.insert(0,filepath) #将选择好的路径加入到entry里面
    getdir(filepath)


def  get_app_permission():
    entry.delete(0,END) #清空entry里面的内容
    listbox_filename.delete(1.0,END)

    package_name = utils.get_current_package_name()
    permission_list = []
    result_list = utils.shell("dumpsys package %s | %s android.permission" %(package_name, utils.find_util)).stdout.readlines()

    for permission in result_list:
        permission_list.append(permission.strip())

    permission_json_file = file("permission.json")

    file_content = json.load(permission_json_file)["PermissList"]

    if utils.system is "Windows":
        listbox_filename.insert(END,"package:"+package_name)
        for permission in permission_list:
            for permission_dict in file_content:
                if permission == permission_dict["Key"]:
                    listbox_filename.insert(END,permission_dict["Key"])
                    listbox_filename.insert(END,"\n")
                    listbox_filename.insert(END,permission_dict["Memo"])
                    listbox_filename.insert(END,"\n")


    # else:
    #     print "package: %s\n" %package_name
    #     for permission in permission_list:
    #         for permission_dict in file_content:
    #             if permission == permission_dict["Key"]:
    #                 print permission_dict["Key"] + ":"
    #                 print "  " + permission_dict["Memo"]

def get_current_activity():
    entry.delete(0,END) #清空entry里面的内容
    listbox_filename.delete(1.0,END)


    listbox_filename.insert(END,"Activity:"+utils.get_focused_package_and_activity())
    listbox_filename.insert(END,"\n\n")

    package_name = utils.get_current_package_name()

    # print package_name

    # print os.popen("aapt dump badging %s" %(get_match_apk(package_name))).readlines()

    # print get_match_apk(package_name)
    for line in os.popen("aapt dump badging %s" %(get_match_apk(package_name))).readlines():
        print line
        listbox_filename.insert(END,line)

    # f = open(PATH("%s/CurrentActivity.txt" %os.getcwd()), "w")
    # f.write("Activity: \n%s\n" %utils.get_focused_package_and_activity())
    # f.close()
    # print "Completed"
    # sys.exit(0)



def getdir(filepath):

    listbox_filename.insert(END,u"App信息如下:\n")
    path1=filepath


    packagename=os.popen('aapt dump badging %s | findstr "package name:" '%path1).read().split(" ")[1].replace("name=","").replace("'","")



    activity=os.popen ('aapt dump badging %s | findstr "launchable-activity:" '%path1).read().split(" ")[1].replace("name=","").replace("'","")
    listbox_filename.insert(END,"packagename:"+packagename)

    listbox_filename.insert(END,"\n\n")
    listbox_filename.insert(END,"activity:"+activity)






root = Tk()
root.title(u"安卓获取APP信息")
root.geometry("800x800")
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=8)

entry = Entry(root, width=100)
entry.grid(sticky=W+N, row=0, column=0, columnspan=4, padx=5, pady=5)

button = Button(root,text=u"选择Apk文件",command=callback)
button.grid(sticky=W+N, row=1, column=0, padx=5, pady=5)


button1 = Button(root,text=u"获取正在运行的APP信息",command=get_current_activity)
button1.grid(sticky=W+N, row=1, column=1, padx=5, pady=5)


button2 = Button(root,text=u"获取正在运行的APP权限信息",command=get_app_permission)
button2.grid(sticky=W+N, row=1, column=2, padx=5, pady=5)


button3 = Button(root,text=u"获取运行APP的CPU和内存信息",command=getcup_meminfo)
button3.grid(sticky=W+N, row=1, column=3, padx=5, pady=5)

listbox_filename = Text(height = 30,width =100)

listbox_filename.grid(row=2, column=0, columnspan=4, rowspan=4,
                        padx=5, pady=5, sticky=W+E+S+N)

root.mainloop()