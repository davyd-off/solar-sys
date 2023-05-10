import pygame
import math
import os

# Инициализация Pygame
pygame.init()

# Установка размера окна
size = (800, 800)
screen = pygame.display.set_mode(size)

# Заголовок окна
pygame.display.set_caption("Визуализация солнечной системы")

# Загрузка изображения для планет
sun_image = pygame.image.load(os.path.join("planets", "sun.png"))
mercury_image = pygame.image.load(os.path.join("mercury.png"))
venus_image = pygame.image.load(os.path.join("venus.png"))
earth_image = pygame.image.load(os.path.join("earth.png"))
mars_image = pygame.image.load(os.path.join("mars.png"))
jupiter_image = pygame.image.load(os.path.join("jupiter.png"))
saturn_image = pygame.image.load(os.path.join("saturn.png"))
uranus_image = pygame.image.load(os.path.join("uranus.png"))
neptune_image = pygame.image.load(os.path.join("neptune.png"))

# Загрузка фонового изображения(космос)
background_image = pygame.image.load(os.path.join("space.png"))

# Корректировка размера изображений планет
sun_image = pygame.transform.scale(sun_image, (80, 80))
mercury_image = pygame.transform.scale(mercury_image, (15, 15))
venus_image = pygame.transform.scale(venus_image, (25, 25))
earth_image = pygame.transform.scale(earth_image, (30, 30))
mars_image = pygame.transform.scale(mars_image, (20, 20))
saturn_image = pygame.transform.scale(saturn_image, (100, 40))
uranus_image = pygame.transform.scale(uranus_image, (35, 35))
jupiter_image = pygame.transform.scale(jupiter_image, (50, 50))
neptune_image = pygame.transform.scale(neptune_image, (40, 40))

# Создание словаря планет с их свойствами
planets = [
    {"name": "Sun", "image": sun_image, "radius": 200, "x": 400, "y": 390, "vx": 0, "vy": 0},
    {"name": "Mercury", "image": mercury_image, "angle": 0, "distance": 65, "period": 0.24, "radius": 10},
    {"name": "Venus", "image": venus_image, "angle": 0, "distance": 90, "period": 0.62, "radius": 20},
    {"name": "Earth", "image": earth_image, "angle": 0, "distance": 125, "period": 1, "radius": 25},
    {"name": "Mars", "image": mars_image, "angle": 0, "distance": 155, "period": 1.88, "radius": 15},
    {"name": "Jupiter", "image": jupiter_image, "angle": 0, "distance": 195, "period": 11.86, "radius": 45},
    {"name": "Saturn", "image": saturn_image, "angle": 0, "distance": 260, "period": 29.5, "radius": 40},
    {"name": "Uranus", "image": uranus_image, "angle": 0, "distance": 320, "period": 84, "radius": 30},
    {"name": "Neptune", "image": neptune_image, "angle": 0, "distance": 370, "period": 164.8, "radius": 35}
]

# Инициализация положения планет
for planet in planets[1:]:
    planet["x"] = planets[0]["x"] + math.cos(planet["angle"]) * planet["distance"]
    planet["y"] = planets[0]["y"] + math.sin(planet["angle"]) * planet["distance"]

# Создание списка прошлых позиций каждой планеты
for planet in planets[1:]:
    planet["past_positions"] = []

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

    # Фоновое изображение
    screen.blit(background_image, (0, 0))

    
    # Отображение солнца в центре
    image_rect = planets[0]["image"].get_rect()
    image_rect.center = (int(planets[0]["x"]), int(planets[0]["y"]))
    screen.blit(planets[0]["image"], image_rect)
   
    # Рисование и обновление положение планет
    for planet in planets[1:]:

        # Увеличение угла в зависимости от периода планеты
        # так, чтобы он совершил один оборот за заданный период
        planet["angle"] += 0.05 * (1 / planet["period"])

        # Рассчитать положение планеты по углу
        planet["x"] = planets[0]["x"] + math.cos(planet["angle"]) * planet["distance"]
        planet["y"] = planets[0]["y"] + math.sin(planet["angle"]) * planet["distance"]

        # Добавить текущую позицию в список прошлых позиций
        planet["past_positions"].append((planet["x"], planet["y"]))

        # Рисуем след
        for i in range(1, len(planet["past_positions"])):
            pygame.draw.line(screen, (153,153,0), planet["past_positions"][i-1], planet["past_positions"][i], 1)

        # Получение прямоугольника для изображения планеты и установка его центра в позицию планеты.
        image_rect = planet["image"].get_rect()
        image_rect.center = (int(planet["x"]), int(planet["y"]))
        
        # Изображение планеты
        screen.blit(planet["image"], image_rect)

    # Обновление дисплея
    pygame.display.update()

    # Пауза (кадры в секунду)
    clock.tick(fps)

# Выход из pygame
pygame.quit()
