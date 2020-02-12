__version__ = '0.1.0'


# uvicorn 13_response_state:app --reload --host 0.0.0.0


import pygame

pygame.init()
screen = pygame.display.set_mode((880, 600))
bg_pic = pygame.image.load("贪吃蛇开始封面路径")  # 待渲染的图片路径
game_pic1 = pygame.image.load("无限模式图片路径")  # 待渲染的图片路径
game_pic2 = pygame.image.load("限时模式图片路径")  # 待渲染的图片路径
running = True

def start_game():
    """游戏开始"""
    myfont = pygame.font.Font("simhei.ttf", 20)
    text1 = myfont.render("A键进入", True, (104, 107, 38))
    text2 = myfont.render("B键进入", True, (104, 107, 38))
    screen.blit(bg_pic, (0, 0))
    screen.blit(text1, (255, 530))
    screen.blit(text2, (560, 530))

def game(game_pic):
    """
    该函数需要渲染字型及字体，以及渲染背景图并展示在窗口
    要求如下：
        - 字体为： "simhei.ttf" 字体大小为 40
        - 渲染的文字为："按【Enter】键回到首页" 字体颜色为 (255, 255, 255)
        - 字体位置为 100， 400
        - 渲染背景图 game_pic 为背景图链接，位置为 (0, 0)
    :return:
    """
    myfont = pygame.font.Font("simhei.ttf", 40)
    text_image = myfont.render("按【Enter】键回到首页", True, (255, 255, 255))
    screen.blit(game_pic, (0, 0))
    screen.blit(text_image, (100, 400))

start_game()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        #
        # 实现不同的按键得到不同的结果，按 a 键为 无限模式，b 键为 限时模式
        # enter 键（回车键） 为回到游戏开始
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                game(game_pic1)
            elif event.key == pygame.K_b:
                game(game_pic2)
            elif event.key == pygame.K_RETURN:
                start_game()

    pygame.display.update()

pygame.quit()


var ev = new KeyboardEvent('keydown', {
         key: "ArrowUp"
     });

window.dispatchEvent(ev)
