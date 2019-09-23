import sys
import io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
'''随机选择一个三位以内的数字作为答案。用户输入一个数字，程序会提示大了或是小了，直到用户猜中'''
import random
x=random.randint(0,1000)
A=input("请输入任一三位以内的数字:")
a=int(A)#用户输入,转为int类型
if a<0:
		print ("数字不规范，请重新输入0-999之间的整数")
elif a>999:
		print ("数字不规范，请重新输入0-999之间的整数")
else:
	if a<x:
		print ("你输入的数字小了哦~~请重新再试试。")
	elif a==x:
		print ("bingo,答对了呢。")
		print (x)
	else:
		print ("你输入的数字大了哦~~请重新再试试。")
print (x)
 

