import pygame
import math
import os

# Инициализация Pygame
pygame.init()

# Установка размера окна
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

# Создание группы спрайтов с поддержкой слоев
all_sprites = pygame.sprite.LayeredUpdates()

# Создание спрайта кнопки закрытия
close_button_image = pygame.image.load(os.path.join("code-solar-sys","close_button.png"))
close_button_image = pygame.transform.scale(close_button_image, (50, 50))
close_button_rect = close_button_image.get_rect()
close_button_rect.topright = (screen.get_width() - 10, 10)
close_button_sprite = pygame.sprite.Sprite()
close_button_sprite.image = close_button_image
close_button_sprite.rect = close_button_rect
all_sprites.add(close_button_sprite, layer=1)

# Создание поверхности для канваса с кнопками
canvas_width, canvas_height = 400, 400
canvas_surface = pygame.Surface((canvas_width, canvas_height))
canvas_surface.fill((255, 255, 255))    


# Загрузка изображения для планет
sun_image = pygame.image.load(os.path.join("code-solar-sys","sun.png"))
mercury_image = pygame.image.load(os.path.join("code-solar-sys","mercury.png"))
venus_image = pygame.image.load(os.path.join("code-solar-sys","venus.png"))
earth_image = pygame.image.load(os.path.join("code-solar-sys","earth.png"))
mars_image = pygame.image.load(os.path.join("code-solar-sys","mars.png"))
jupiter_image = pygame.image.load(os.path.join("code-solar-sys","jupiter.png"))
saturn_image = pygame.image.load(os.path.join("code-solar-sys","saturn.png"))
uranus_image = pygame.image.load(os.path.join("code-solar-sys","uranus.png"))
neptune_image = pygame.image.load(os.path.join("code-solar-sys","neptune.png"))

# Загрузка фонового изображения(космос)
background_image = pygame.transform.scale(pygame.image.load(os.path.join("space.png")), (screen.get_width(), screen.get_height()))

# Корректировка размера изображений планет
sun_image = pygame.transform.scale(sun_image, (88, 88))
mercury_image = pygame.transform.scale(mercury_image, (16.5, 16.5))
venus_image = pygame.transform.scale(venus_image, (27.5, 27.5))
earth_image = pygame.transform.scale(earth_image, (33, 33))
mars_image = pygame.transform.scale(mars_image, (22, 22))
saturn_image = pygame.transform.scale(saturn_image, (110, 44))
uranus_image = pygame.transform.scale(uranus_image, (38.5, 38.5))
jupiter_image = pygame.transform.scale(jupiter_image, (55, 55))
neptune_image = pygame.transform.scale(neptune_image, (44, 44))

class Planet:
    def __init__(self, name, image, angle, distance, period, radius, x, y):
        self.name = name
        self.image = image
        self.angle = angle
        self.distance = distance
        self.period = period
        self.radius = radius
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.past_positions = []

    def update_position(self, center_x, center_y):
        self.angle += 0.05 * (1 / self.period)
        self.x = center_x + math.cos(self.angle) * self.distance
        self.y = center_y + math.sin(self.angle) * self.distance
        self.past_positions.append((self.x, self.y))

    def draw(self, screen):
        image_rect = self.image.get_rect()
        image_rect.center = (int(self.x), int(self.y))
        screen.blit(self.image, image_rect)

    def draw_trail(self, screen):
        for i in range(1, len(self.past_positions)):
            pygame.draw.line(screen, (153,153,0), self.past_positions[i-1], self.past_positions[i], 1)
    
    def check_planet_clicked(self, mouse_pos):
        dx = mouse_pos[0] - self.x
        dy = mouse_pos[1] - self.y
        dist = math.sqrt(dx**2 + dy**2)
        return dist <= self.radius


sun = Planet("Sun", sun_image, 0, 0, 0, 200, screen.get_width() / 2, screen.get_height() / 2)
mercury = Planet("Mercury", mercury_image, 0, 65, 0.54, 10, sun.x + sun.radius, sun.y)
venus = Planet("Venus", venus_image, 0, 90, -0.82, 20, sun.x + sun.radius * 2, sun.y)
earth = Planet("Earth", earth_image, 0, 125, 1.2, 25, sun.x + sun.radius * 3, sun.y)
mars = Planet("Mars", mars_image, 0, 155, 1.88, 15, sun.x + sun.radius * 4, sun.y)
jupiter = Planet("Jupiter", jupiter_image, 0, 195, 11.86, 45, sun.x + sun.radius * 5, sun.y)
saturn = Planet("Saturn", saturn_image, 0, 260, 29.5, 40, sun.x + sun.radius * 6, sun.y)
uranus = Planet("Uranus", uranus_image, 0, 320, 84, 30, sun.x + sun.radius * 7, sun.y)
neptune = Planet("Neptune", neptune_image, 0, 370, 164.8, 200, sun.x + sun.radius * 8, sun.y)

planets = [sun, mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]

def show_planet_info(planet):
    # Создание поверхности для панели с информацией о планете
    info_surface = pygame.Surface((canvas_width, canvas_height))
    info_surface.fill((255, 255, 255))

    # Отображение информации о планете
    font = pygame.font.SysFont("Arial", 20)
    text = font.render("Название: " + planet.name, True, (0, 0, 0))
    info_surface.blit(text, (10, 10))
    text = font.render("Радиус: "+str(planet.radius) + " km", True, (0, 0, 0))
    info_surface.blit(text, (10, 50))
    text = font.render("Расстояние до солнца: " + str(planet.distance) + " mln km", True, (0, 0, 0))
    info_surface.blit(text, (10, 90))

    # Отображение поверхности на канвасе
    canvas_surface.blit(info_surface, (0, 0))

# Установка частоты времени
clock = pygame.time.Clock()
fps = 30

# Запуск программы в цикле
running = True

while running:
    # Обработка событий в pygame
    for event in pygame.event.get():
        # Проверка на выход
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Обработка клика на кнопке закрытия
            if close_button_rect.collidepoint(event.pos):
                running = False
            # Проверка клика по планете    
            for planet in planets:
                if planet.check_planet_clicked(event.pos):
                    show_planet_info(planet)




    # Фоновое изображение
    screen.blit(background_image, (0, 0))

    
    # Отображение солнца
    sun.draw(screen)
   
    # Рисование и обновление положение планет
    for planet in planets[1:]:
        planet.update_position(sun.x, sun.y)
        planet.draw_trail(screen)
        planet.draw(screen)

    all_sprites.draw(screen)
    screen.blit(canvas_surface, (10, 10))
    # Обновление дисплея
    pygame.display.update()

    

    # Пауза (кадры в секунду)
    clock.tick(fps)

# Выход из pygame
pygame.quit()
