import pygame
import sys
import random
from pygame_emojis import load_emoji

s_width = 600 # 游戏窗口宽
s_height = 600 # 游戏窗口高
g_size = 30 # 像素尺寸设置
g_width = s_width // g_size # 水平
g_heigh = s_height // g_size # 垂直

White = (255, 255 , 255) # 白色参数
Green = (0, 255, 255) # 绿色参数
Red = (255, 0, 0) # 红色参数
Black = (0, 0, 0) # 黑色参数

Up = (0, -1) # 上方向定义
Down = (0, 1) # 下方向定义
left = (-1, 0) # 左方向定义
Right =(1, 0) # 右方向定义

Fruits = {'🍓':'strawberry', '🥭':'mango', '🍐':'pear', '🥑':'avocado'}

class Snake: # 蛇
    def __init__(self): 
       self.len = 1 # 初始长度为1
       self.position = [((s_width // 2), (s_height // 2))] # 初始位置在中心位置
       self.direction = random.choice([Up, Down, left, Right]) # 初始方向
       self.score = 0
       self.head_image = load_emoji('🐍', (g_size,g_size)) # 蛇头的图像
       self.body_image = load_emoji('🟢', (g_size,g_size)) # 蛇身的图像
    
    def get_head(self): # 蛇头的位置
        return self.position[0] #返回蛇头坐标

    def turn(self, point): # 蛇转弯
        if self.len > 1 and (point[0] * -1, point[1] * -1) == self.direction:
            return # 禁止方向移动
        else:
            self.direction = point # 改变方向

    def move(self): # 蛇的移动
        cur = self.get_head() 
        x, y =self.direction #新的蛇头位置的 wrap-around
        new = (((cur[0]+ (x * g_size))%s_width), (cur[1] + (y * g_size)) % s_height) ##新的蛇头位置的 wrap-around
        if len (self.position) > 2 and new in self.position[2:]:
            return False # 撞到自己 游戏失败 
        else:
            self.position.insert(0,new) # 新的头部
            if len(self.position) > self.len:
                self.position.pop() # 去掉尾巴
            return True

    def reset(self): # 游戏的重新开始
        self.len = 1
        self.position = [((s_width // 2),(s_height // 2))]
        self.direction = random.choice([Up, Down, left, Right])
        self.score = 0 # 与之前类似

    def draw(self, surface): 
        head_image = self.head_image # 根据方向对蛇头进行旋转
        if self.direction == Down:
            head_image = pygame.transform.rotate(self.head_image, 180)
        elif self.direction == left:
            head_image = pygame.transform.rotate(self.head_image, 90)
        elif self.direction ==Right:
            head_image =pygame.transform.rotate(self.head_image, -90)

        surface.blit(head_image, self.get_head()) # 蛇头
        
        for p in self.position[1:]:
            surface.blit(self.body_image, p) # 蛇身

    def handle_keyboard(self): #事件选项处理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_UP: 
                       print("Up")
                       self.turn(Up) # 上
                    case pygame.K_DOWN:
                       print("Down")
                       self.turn(Down) # 下
                    case pygame.K_LEFT:
                       print("Left")
                       self.turn(left) # 左
                    case pygame.K_RIGHT:
                       print("Right")
                       self.turn(Right) # 右

class Fruit:
    def __init__(self): 
       self.pos = (0, 0) # 初始位置
       self.image = None # 水果图像
       self.emoji_char = '' # emoji
       self.random_fruit() # 水果随机生成

    def random_position(self, snake_pos): # 与蛇的位置要不同
        Flage = False
        while not Flage:
            x = random.randint(0, g_width - 1) * g_size
            y = random.randint(0, g_heigh - 1 ) * g_size
            self.pos = (x, y)

            if self.pos not in snake_pos:
                Flage = True # 确保位置不互相侵占

    def random_fruit(self):
        self.emoji_char = random.choice(list(Fruits.keys())) # 水果随机
        self.image = load_emoji(self.emoji_char, (g_size, g_size)) # 加载
    
    def draw (self,surface):
        surface.blit(self.image, self.pos) # 水果的样子及外观

def draw_grid(surface):
    for y in range(0,int(g_heigh)):
        for x in range(0,int(g_width)):
            pygame.draw.rect(surface,(200, 230, 150) if (x + y)%2 == 0 else (190, 220, 140), (x * g_size, y * g_size, g_size, g_size)) # 表格视觉效果

def show_score(surface, score):
    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {score}", True, Black) # 文本
    surface.blit(text, (10, 10)) # 使得分位于屏幕左上角

def game_over(running, surface, screen):

    while running == False:
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                pygame.quit() # 退出
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key ==pygame.K_SPACE:
                    return True # 空格键继续

        font = pygame.font.Font(None, 36)
        surface.fill(Black) # 背景黑化
        text1 = font.render("game over", True, Red)
        text2 = font. render("press SPACE to continue", True, White)
        surface.blit(text1, (235, 250))
        surface.blit(text2, (165, 300))
        screen.blit(surface, (0, 0))
        pygame.display.update()

        pygame.display.update()
        pygame.time.Clock().tick(15) # 降低帧率 减少内存占用

    return None

def main():
    print(1) 
    pygame.init()
    pygame.display.set_caption("snake") # 标题
    screen = pygame.display.set_mode((s_width, s_height), 0, 32) # 游戏窗口
    clock = pygame.time.Clock() # 频率控制
    print(2) 
    running = True
    surface = pygame.Surface(screen.get_size()) # 屏幕
    message_font = pygame.font.Font(None, 24) # 文字提示字体
    text = None # 当前提示
    mtimer = 0 # 提示
    print(4) 
    snake = Snake() 
    fruit = Fruit()
    print(5) 
    fruit.random_position(snake.position)
    print(3) 
    while running: 
        snake.handle_keyboard()
        draw_grid(surface)
        running = snake.move()
        if snake.get_head() == fruit.pos: # 吃到水果
            snake.len += 1
            snake.score += 1
            text = message_font.render(f"I like {Fruits[fruit.emoji_char]}", True, Black) # 提示语和其设置
            mposition = (fruit.pos[0], fruit.pos[1] - 20) # 现实位置在水果上方
            mtimer = 8 * 1 # 时间
            fruit.random_position(snake.position) # 新的水果位置
            fruit.random_fruit() # 随机性

        snake.draw(surface)
        fruit.draw(surface)

        if mtimer > 0:
            surface.blit(text, mposition) # 信息显示“I like 某某”
            mtimer -= 1
    
        screen.blit(surface, (0, 0))
        show_score(screen, snake.score) # 得分
        pygame.display.update()
        clock.tick(8) # 频率 随着蛇的形状增大，起速度越快 

        if running == False:
            print("Game Over")
            running = game_over(running, surface, screen)
            if running == True: 
                main() # 重新开始


if __name__ == "__main__":
    main()