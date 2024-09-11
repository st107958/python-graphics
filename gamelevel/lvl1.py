import pygame as pg
import os

pg.init()

screen_width = 300
screen_height = 500

window = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption("lvl1")


def jump(x):
    return x ** 2


def load_images():
    images = []
    for i in range(1, 5):
        img = pg.image.load(os.path.join("sprite", f"Sprite-000{i}.png"))
        images.append(img)
    return images


class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.images = load_images()
        self.current_image = 0
        self.image = self.images[self.current_image]
        self.rect = self.image.get_rect()
        self.rect.center = (screen_width // 2, screen_height // 2)
        self.speed = 3
        self.jump_statement = False
        self.jump_score = 5

    def update(self, keys):

        self.current_image += 0.5  # Чем больше значение, тем быстрее анимация
        if self.current_image >= len(self.images):
            self.current_image = 0
        self.image = self.images[int(self.current_image)]

        if keys[pg.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pg.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pg.K_UP]:
            self.rect.y -= self.speed
        if keys[pg.K_DOWN]:
            self.rect.y += self.speed

        if not self.jump_statement:
            if keys[pg.K_SPACE] and self.rect.y < screen_height:
                self.jump_statement = True
        else:
            if self.jump_score >= -5 and self.rect.y < screen_height:
                direction = 1
                if self.jump_score > 0:
                    direction = -1
                self.rect.y = self.rect.y + (self.jump_score ** 2) * direction
                self.jump_score -= 1
            else:
                self.jump_statement = False
                self.jump_score = 5


def main():
    # velocity = 5
    # init_x = 100
    # init_y = 400
    # x = 100
    # y = 400
    # ball_radius = 10
    # jump_score = 5
    # jump_statement = False
    #
    # run = True
    # while run:
    #     pg.time.delay(40)
    #
    #     keys = pg.key.get_pressed()
    #
    #     if keys[pg.K_RIGHT] and x < screen_width - ball_radius:
    #         x += velocity
    #     if keys[pg.K_LEFT] and x > ball_radius:
    #         x -= velocity
    #     if keys[pg.K_UP] and y > init_y-150:
    #         y -= velocity
    #     if keys[pg.K_DOWN] and y < init_y+200:
    #         y += velocity
    #     if not jump_statement:
    #         if keys[pg.K_SPACE] and y < screen_height - ball_radius:
    #             jump_statement = True
    #     else:
    #         if jump_score >= -5 and y < screen_height - ball_radius:
    #             direction = 1
    #             if jump_score > 0:
    #                 direction = -1
    #             y = y + (jump_score ** 2) * direction
    #             jump_score -= 1
    #         else:
    #             jump_statement = False
    #             jump_score = 5
    #
    #     for event in pg.event.get():
    #         if event.type == pg.QUIT:
    #             run = False
    #
    #     pg.draw.circle(window, (0, 255, 255), (x, y), ball_radius)

        background_image = pg.image.load("pictures/lvl_back0.jpg")


        # clock = pg.time.Clock()
        player = Player()
        all_sprites = pg.sprite.Group()
        all_sprites.add(player)

        running = True
        while running:
            # clock.tick(30)  # Установка FPS
            pg.time.delay(40)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False

            keys = pg.key.get_pressed()  # Получаем все нажатые клавиши
            all_sprites.update(keys)  # Обновляем все спрайты
            window.blit(background_image, (0, -150))
            all_sprites.draw(window)  # Отрисовка всех спрайтов
            pg.display.update()  # Обновление экрана


main()

pg.quit()
