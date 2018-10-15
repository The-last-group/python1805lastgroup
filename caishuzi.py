import random

x,y,s=0,0,1
z = int(random.randint(1,1000))
print(z)
print('游戏名称:猜数字')
a = int(input('请输入一个1-1000之间的数:'))
while (a != z):
    if a > z:
        print('你输入的是',a,end='')
        a = int(input('太大了,重新输入:'))
        x = x+1
    if a < z:
        print('你输入的是', a,end='')
        a = int(input('太小了，重新输入：'))
        y = y + 1
    s = x + y + 1
else:

    if s == 1:
        print('你简直是神啊！一共只用了{}步！'.format(s))
    elif s == 2:
        print('你的智商冠绝古今！一共只用了{}步！'.format(s))
    elif s == 3:
        print('你是爱因斯坦在世！一共只用了{}步！'.format(s))
    elif 5 >= s > 3:
        print('你是个聪明的孩子!一共只用了{}步！'.format(s))
    elif 10 >= s > 5:
        print('你是个高手!一共只用了{}步!'.format(s))
    else:
        print('辛苦你了！你尝试了{}次，终于正确了！'.format(s))