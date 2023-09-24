from PPlay.window import *
from PPlay.sprite import *

janela = Window(600, 600)

janela.set_background_color([0, 0, 0])
janela.set_title("Bernardo Mendes")
ball = Sprite("pongball.png")
ball2 = Sprite("pongball.png")
iniciox = janela.width / 2 - ball.width / 2
inicioy = janela.height / 2 - ball.height / 2
ball.set_position(iniciox, inicioy)
ball2.set_position(200, 300)
velox = 400
veloy = 300
velox2 = 600
veloy2 = 500

while True:
    ball.x = ball.x + velox * janela.delta_time()
    ball.y = ball.y + veloy * janela.delta_time()

    if ball.x >= janela.width - ball.width:
        ball.x = janela.width - ball.width
        velox *= -1
    elif ball.x <= 0:
        ball.x = 0
        velox *= -1

    if ball.y >= janela.height - ball.height:
        ball.y = janela.height - ball.height
        veloy *= -1
    elif ball.y <= 0:
        ball.y = 0
        veloy *= -1
        
        
        
    ball2.x = ball2.x + velox2 * janela.delta_time()
    ball2.y = ball2.y + veloy2 * janela.delta_time()

    if ball2.x >= janela.width - ball2.width:
        ball2.x = janela.width - ball2.width
        velox2 *= -1
    elif ball2.x <= 0:
        ball2.x = 0
        velox2 *= -1

    if ball2.y >= janela.height - ball2.height:
        ball2.y = janela.height - ball2.height
        veloy2 *= -1
    elif ball2.y <= 0:
        ball2.y = 0
        veloy2 *= -1
    if(ball.collided(ball2)):
        velox *= -1
        velox2 *= -1
        veloy *= -1
        veloy2 *= -1

    janela.set_background_color([0, 100, 100])
    ball.draw()
    ball2.draw()
    janela.update()