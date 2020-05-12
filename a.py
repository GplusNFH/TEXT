print("你有了解作者")
start = input("输入5以开始游戏：")
guess = int(start)
while guess != 5:
    start = input("认真点！再来：")
    guess = int(start)
if guess == 5:
    print("1,python")
    print("2,java")
    print("3,HTML")
    a = input("游戏开始，上面的语言中，我最喜欢的后端语言是(输入前方的数字)：")
    b = int(a)
    while b != 1:
        a = input("不对呦，在想想：")
        b = int(a)
    if b == 1:
        print("对了，没错！")
    print("********结束********")
