#coding:utf-8
#!/usr/bin/env python

'''
python-tail example.
Does a tail follow against /var/log/syslog with a time interval of 5 seconds.
Prints recieved new lines to standard out '''

# import tail
#
# def print_line(txt):
#     ''' Prints received text '''
#     print(txt.strip())
#
# t = tail.Tail('/log/testss.txt')
# t.register_callback(print_line)
# t.follow(s=1)
# -*- coding: utf-8 -*-
#
import os
import tail

def file_name(log_dir):
	list1=[]
	for root, dirs, files in os.walk(log_dir):
		list1=files
	return  os.path.join(os.path.dirname(os.path.realpath(__file__)),log_dir,list1[0])


# print file_name("log")

def print_line(txt):
	print(txt).strip()

t = tail.Tail(file_name("log"))
t.register_callback(print_line)
t.follow(s=2)