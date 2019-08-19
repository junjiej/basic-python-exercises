''''
作者:Jason
日期：2019/08/19
功能：自动绘制小猪佩奇
来源：jackfrued/Python-100-Days
'''


from turtle import *
'''from xx import * 这种方法可以在下面调用库不用加前缀，
但一般程序中只出现一次，防止交叉使用错误'''

def nose(x,y):
    '''画鼻子'''
    penup()
    # 移动到指定位置
    goto(x,y)
    pendown()
    # 设置turtle的方向（0-东，90-北，180-西，270-南）
    setheading(-30)
    begin_fill()
    a = 0.4
    for i in range(120):
        if 0 <= i < 30 or 60 <= i <= 90:
            a = a + 0.08
            # 向左转3度
            left(3)
            # 向前走
            forward(a)
        else:
            a = a - 0.08
            #目的是在30～60之间拐弯角度比较尖锐，最终成椭圆形
            left(3)
            forward(a)
    end_fill()

    '''画眼睛'''
    penup()
    setheading(90)
    forward(25)

    setheading(0)
    forward(10)
    pendown()
    '''填充眼睛'''
    pencolor(255,155,192)
    setheading(10)
    begin_fill()
    circle(5)
    color(160,82,45)
    end_fill()

    penup()
    setheading(0)
    forward(20)
    pendown()
    pencolor(255,155,192)
    setheading(10)

    begin_fill()
    circle(5)
    color(160,82,45)
    end_fill()

def head(x,y):
    '''画头'''
    color((255,155,192),'pink')
    penup()
    goto(x,y)
    setheading(0)
    pendown()

    begin_fill()
    setheading(180)
    circle(300,-30)
    circle(100,-60)
    circle(80,-100)
    circle(150,-20)
    circle(60,-95)
    setheading(161)
    circle(-300,15)
    penup()
    goto(-100,100)
    pendown()
    setheading(-30)

    a = 0.4
    for i in range(60):
        if 0 <= i <30 or 60 <= i <90:
            a = a + 0.08
            lt(3)
            fd(a)
        else:
            a = a - 0.08
            lt(3)
            fd(a)
    end_fill()

def ears(x,y):
    '''画耳朵'''
    color((255,155,192),'pink')
    penup()
    goto(x,y)
    pendown()

    begin_fill()
    setheading(100)
    circle(-50,50)
    circle(-10,120)
    circle(-50,54)
    end_fill()

    penup()
    setheading(90)
    fd(-12)
    setheading(0)
    fd(30)
    pendown()

    begin_fill()
    setheading(100)
    circle(-50,50)
    circle(-10,120)
    circle(-50,56)
    end_fill()

def eyes(x,y):
    '''画眼睛'''
    color((255, 155, 192), "white")
    penup()
    setheading(90)
    forward(-20)
    setheading(0)
    forward(-95)
    pendown()
    begin_fill()
    circle(15)
    end_fill()
    color("black")
    penup()
    setheading(90)
    forward(12)
    setheading(0)
    forward(-3)
    pendown()
    begin_fill()
    circle(3)
    end_fill()
    color((255, 155, 192), "white")
    penup()
    seth(90)
    forward(-25)
    seth(0)
    forward(40)
    pendown()
    begin_fill()
    circle(15)
    end_fill()
    color("black")
    penup()
    setheading(90)
    forward(12)
    setheading(0)
    forward(-3)
    pendown()
    begin_fill()
    circle(3)
    end_fill()

def check(x,y):
    '''画脸颊'''
    color((255,155,192))
    penup()
    goto(x,y)
    pendown()

    setheading(0)
    begin_fill()
    circle(30)
    end_fill()

def mouth(x,y):
    '''画嘴巴'''
    color(239,69,19)
    penup()
    goto(x,y)
    pendown()
    setheading(-80)
    circle(30,40)
    circle(40,80)


def setting():
    '''设置参数'''
    pensize(4)
    hideturtle()

    colormode(255)
    color((255,155,192),'pink')

    ##设置主窗口大小和位置setup(宽（50%），高（75%），x方向（左），y方向（右）)
    setup(840,500)

    ##画笔速度0～10整数,如果不在该范围则返回0，0最快，10较快，6正常，3慢，1最慢
    speed(10)

def main():
    '''主函数'''
    setting()
    nose(-100,100)
    head(-69,167)
    ears(0,160)
    eyes(0,140)
    check(80,10)
    mouth(-20,30)


    done()


if __name__ == '__main__':
    main()

