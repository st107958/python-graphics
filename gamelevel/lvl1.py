import pygame as pg

pg.init()

screen_width = 700
screen_height = 700

window = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption("lvl")


def jump(x):
    return x ** 2


def main():
    velocity_x = 5
    x = 100
    y = 400
    ball_radius = 10
    jump_score = 5
    jump_statement = False

    run = True
    while run:
        pg.time.delay(40)

        keys = pg.key.get_pressed()

        if keys[pg.K_RIGHT] and x < screen_width - ball_radius:
            x += velocity_x
        if keys[pg.K_LEFT] and x > ball_radius:
            x -= velocity_x
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

        window.fill((100, 100, 100))

        pg.draw.circle(window, (0, 255, 255), (x, y), ball_radius)

        # window.fill((100, 100, 100))

        pg.display.update()


main()

pg.quit()
