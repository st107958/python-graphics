import pygame as pg

pg.init()

screen_width = 500
screen_height = 800

window = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption("lvl")


def jump(x):
    return x ** 2


def main():
    velocity = 5
    init_x = 100
    init_y = 400
    x = 100
    y = 400
    ball_radius = 10
    jump_score = 5
    jump_statement = False

    points = [(100, 100), (200, 50), (300, 100), (350, 200), (250, 250), (150, 200)]

    background_image = pg.image.load("pictures/lvl_back0.jpg")

    run = True
    while run:
        pg.time.delay(40)

        keys = pg.key.get_pressed()

        if keys[pg.K_RIGHT] and x < screen_width - ball_radius:
            x += velocity
        if keys[pg.K_LEFT] and x > ball_radius:
            x -= velocity
        if keys[pg.K_UP] and y > init_y-150:
            y -= velocity
        if keys[pg.K_DOWN] and y < init_y+200:
            y += velocity
        if not jump_statement:
            if keys[pg.K_SPACE] and y < screen_height - ball_radius:
                jump_statement = True
        else:
            if jump_score >= -5 and y < screen_height - ball_radius:
                direction = 1
                if jump_score > 0:
                    direction = -1
                y = y + (jump_score ** 2) * direction
                jump_score -= 1
            else:
                jump_statement = False
                jump_score = 5

        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

        # window.fill((100, 100, 100))
        window.blit(background_image, (0, -150))

        pg.draw.circle(window, (0, 255, 255), (x, y), ball_radius)
        # pg.draw.polygon(window, (255, 0, 0), points)

        # window.fill((100, 100, 100))

        pg.display.update()


main()

pg.quit()
