#coding=utf-8
#类
'''class people:
    name=''
    age=0

    #定义私有属性，私有属性在类外部无法直接进行访问
    __weight=0

    #定义构造方法
    def __init__(self,n,a,w):
        self.name=n
        self.age=a
        self.weight=w

    def speak(self):
        print ('%s说：我%d岁'%(self.name,self.age))

#单类继承
class student(people):
    grade=''
    def __init__(self,n,a,w,g):
        #调用父类的构造
        people.__init__(self,n,a,w)
        self.grade=g

    #覆盖父类的方法
    def speak(self):
        print('%s说：我%d岁了，我在读%s年级'%(self.name,self.age,self.grade))

#s=student('Tom',12,40,'六')
#s.speak()

#多类继承
class speaker():
    topic=''
    name=''
    def __init__(self,n,t):
        self.topic=t
        self.name=n

    def speak(self):
        print('我叫%s,我是一个演说家，我演讲的主题是%s'%(self.name,self.topic))

class sample(speaker,student):
    a=''
    def __init__(self,n,a,w,g,t):
        student.__init__(self,n,a,w,g)
        speaker.__init__(self,n,t)
test=sample('Tom',25,80,4,"Python")
test.speak()#方法名相同，默认调用的是括号中排前的父类方法

#类方法
from time import time,localtime,sleep
class Clock(object):

    def __init__(self,hour=0,minute=0,second=0):
        self._hour=hour
        self._minute=minute
        self._second=second

    @classmethod
    def now(cls):
        ctime=localtime(time())
        return cls(ctime.tm_hour,ctime.tm_min,ctime.tm_sec)

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
        return "%02d:%02d:%02d"%(self._hour,self._minute,self._second)

def main():
#通过类方法创建对象并获取系统时间
    clock=Clock.now()
    while True:
        print(clock.show())
        sleep(1)
        clock.run()
if __name__=='__main__':
    main()

'''

#方法重写&多态
from abc import ABCMeta,abstractmethod
class Pet(object,metaclass=ABCMeta):
    def __init__(self,nickname):
        self._nickname=nickname

    @abstractmethod
    def make_voice(self):
        pass

class Dog(Pet):
    def make_voice(self):
        print('%s汪汪汪')