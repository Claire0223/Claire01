#-*- coding=utf-8 -*-
'''from translate import Translator

#英译汉
translator=Translator(to_lang="chinese")
translation=translator.translate("I hate u!")
print (translation)

#汉译英，规定中英
translator1=Translator(from_lang="chinese",to_lang="english")
translation1=translator1.translate("我想你！")
print(translation1)
'''
#太阳花
import turtle
import time

#同时设置pencolor和fillcolor
turtle.color("red","yellow")

turtle.begin_fill()
for _ in range(50):
    turtle.forward(200)
    turtle.left(170)

turtle.end_fill()

turtle.mainloop()

