#! /usr/bin/python
# -*- coding:UTF-8 -*-

flag=1;
while(flag):
	s = raw_input("请输入：")
	print "您输入的是：", s
	if (str(s) == 'out'):flag =0;
else: print "it is over"
