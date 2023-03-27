import pgzrun  # 导入游戏库
import random



WIDTH = 800  # 设置窗口的宽度
HEIGHT = 600  # 设置窗口的高度
time = 0  # 经过时间


class Ball:  # 定义小球类
    x = None  # 小球的x坐标
    y = None  # 小球的y坐标
    vx = None  # 小球x方向的速度
    vy = None  # 小球y方向的速度
    radius = None  # 小球的半径
    status = None  # 对应状态，0为健康绿色，1为阳性红色

    # 使用构造函数传递参数对对象初始化
    def __init__(self, x, y, vx, vy, radius, status):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.radius = radius
        self.status = 0

    def draw(self):
        # 绘制一个填充圆，坐标(x,y)，半径radius，颜色
        if self.status == 0:  # 健康小球
            screen.draw.filled_circle((self.x, self.y), self.radius, 'green')
        elif self.status == 1:  # 阳性小球
            screen.draw.filled_circle((self.x, self.y), self.radius, 'red')

    def update(self):  # 更新小球的位置、速度
        self.x += self.vx  # 利用x方向速度更新x坐标
        self.y += self.vy  # 利用y方向速度更新y坐标
        # 当小球碰到左右边界时，x方向速度反转
        if self.x > WIDTH - self.radius or self.x < self.radius:
            self.vx = -self.vx
        # 当小球碰到上下边界时，y方向速度反转
        if self.y > HEIGHT - self.radius or self.y < self.radius:
            self.vy = -self.vy


balls = []  # 存储所有小球的信息，初始为空列表

for i in range(100):  # 随机生成100个小球
    x = random.randint(50, WIDTH - 50)  # 小球的x坐标
    y = random.randint(50, HEIGHT - 50)  # 小球的y坐标
    vx = 4 * random.random() - 2  # 小球x方向的速度
    vy = 4 * random.random() - 2  # 小球y方向的速度
    r = 5  # 小球的半径
    status = 1  # 小球的健康状态
    # 存储小球所有信息的列表
    ball = Ball(x, y, vx, vy, r, status)  # 定义ball对象
    balls.append(ball)  # 把第i号小球的信息添加到balls中
    # 将第一个小球设成阳性病例
    balls[0].status = 1


def draw():  # 绘制模块，每帧重复执行
    screen.fill('white')  # 白色背景
    # 显示传播了多场时间
    text = "Simulate Time: " + str(time // 10)
    screen.draw.text(text, (30, 30), fontsize=35, color='black')
    for ball in balls:  # 绘制所有的圆
        ball.draw()  # 绘制小球


def update():  # 更新模块，每帧重复操作
    global time
    time += 1  # 时间加一

    for ball in balls:
        ball.update()  # 更新小球的位置、速度

    ballNum = len(balls)  # 所有球的个数
    dangerDistance = 2 * balls[0].radius

    # 所有小球，两两比较，是否传播疫情
    for i in range(ballNum):
        for j in range(i, ballNum):
            # 一个小球是阳性，另一个不是阳性
            if (balls[i].status == 0 and balls[j].status == 1) or \
                    (balls[i].status == 1 and balls[j].status == 0):
                # 两个小球间距离较近
                if abs(balls[i].x - balls[j].x) < dangerDistance and abs(balls[i].y - balls[j].y) < dangerDistance:
                    # 满足一定的概率传染
                    randNum = random.random()  # 产生0到1之间的随机数
                    if randNum < 0.9:  # 两人不带口罩，传播概率90%
                        # if randNum < 0.05:  # 一人戴口罩，一人不带口罩传播概率5%
                        # if randNum < 0.015:  # 两人都戴口罩，传播概率1.5%
                        balls[i].status = 1
                        balls[j].status = 1


pgzrun.go()  # 开始执行游戏