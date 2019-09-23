#coding=utf-8
'''
#练习1：定义一个类描述数字时钟
import time
class Clock(object):
    def __init__(self,hour=0,minute=0,second=0):
        self._hour=hour
        self._minute=minute
        self._second=second
    #时钟走动
    def run(self):
        self._second+=1
        if self._second==60:
            self._second=0
            self._minute+=1
            if self._minute==60:
                self._minute=0
                self._hour+=1
                if self._hour==24:
                    self._hour=0

    def show(self):
        return ('%02d:%02d:%02d'%(self._hour,self._minute,self._second))

def main():
    clock=Clock(23,59,58)
    while True:
        print(clock.show())
        time.sleep(1)
        clock.run()
main()
'''

#练习2：定义一个类描述平面上的点并提供移动点和计算到另一个点距离的方法。
