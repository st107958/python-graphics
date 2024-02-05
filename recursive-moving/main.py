import pygame as pg

'''You can change the picture using the 'right' and 'left' on the keyboard.'''

pg.init()

window = pg.display.set_mode((500, 500))
pg.display.set_caption("moving")

def fractal(A, B, C, D, deep=100,  alpha=0.1):

    if deep < 1:
        return
    else:
        pg.draw.line(window, (100, 100, 100), A, B)
        pg.draw.line(window, (100, 100, 100), B, C)
        pg.draw.line(window, (100, 100, 100), C, D)
        pg.draw.line(window, (100, 100, 100), D, A)

        A1 = [(B[0] - A[0]) * (alpha) + A[0], (B[1] - A[1]) * (alpha) + A[1]]
        B1 = [(C[0] - B[0]) * (alpha) + B[0], (C[1] - B[1]) * (alpha) + B[1]]
        C1 = [(D[0] - C[0]) * (alpha) + C[0], (D[1] - C[1]) * (alpha) + C[1]]
        D1 = [(A[0] - D[0]) * (alpha) + D[0], (A[1] - D[1]) * (alpha) + D[1]]

        deep = deep - 1

        fractal(A1, B1, C1, D1, deep, alpha)


A = [100, 100]
B = [400, 100]
C = [400, 400]
D = [100, 400]
alpha_changing_velocity = 0.01
alpha = 0.1
deep = 50

run = True
while run:
    pg.time.delay(40)

    keys = pg.key.get_pressed()

    if keys[pg.K_RIGHT]:
        alpha += alpha_changing_velocity
    if keys[pg.K_LEFT]:
        alpha -= alpha_changing_velocity

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    window.fill((0, 0, 0))
    fractal(A, B, C, D, deep, alpha)

    pg.display.update()

pg.quit()
