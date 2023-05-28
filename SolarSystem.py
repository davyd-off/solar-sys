
import os
import math

import pygame

# Инициализация Pygame
pygame.init()

# Установка размера окна
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen_width,screen_height = screen.get_size()

# Вычисление размеров информаионного окна
info_size_width =  math.ceil(screen_width - (screen_width*((1920-400)/1920)))
info_size_height = info_size_width+info_size_width*0.5

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

# Загрузка idol картинки для информаионного окна
info_std_img = pygame.image.load(os.path.join("code-solar-sys","none_menu.png"))
info_planet_img = info_std_img

# Вычисление координат кнопки закрытия информаионного окна
info_close_butt_width = info_size_width-info_size_width*0.9075
info_close_butt_height = info_size_height-info_size_height*0.9383

# Создание объекта закрытия информаионного окна
info_close_butt = pygame.Rect(info_size_width-info_close_butt_width+40, 40, info_close_butt_width , info_close_butt_height)

#-------------------------------------------------------------------
# Загрузка изображении планет и информации
sun_image = pygame.image.load(os.path.join("code-solar-sys","sun.png"))
mercury_image = pygame.image.load(os.path.join("code-solar-sys","mercury.png"))
venus_image = pygame.image.load(os.path.join("code-solar-sys","venus.png"))
earth_image = pygame.image.load(os.path.join("code-solar-sys","earth.png"))
mars_image = pygame.image.load(os.path.join("code-solar-sys","mars.png"))
jupiter_image = pygame.image.load(os.path.join("code-solar-sys","jupiter.png"))
saturn_image = pygame.image.load(os.path.join("code-solar-sys","saturn.png"))
uranus_image = pygame.image.load(os.path.join("code-solar-sys","uranus.png"))
neptune_image = pygame.image.load(os.path.join("code-solar-sys","neptune.png"))

sun_image_info = pygame.image.load(os.path.join("code-solar-sys","sun_info.png"))
mercury_image_info = pygame.image.load(os.path.join("code-solar-sys","mercury_info.png"))
venus_image_info = pygame.image.load(os.path.join("code-solar-sys","venus_info.png"))
earth_image_info = pygame.image.load(os.path.join("code-solar-sys","earth_info.png"))
mars_image_info = pygame.image.load(os.path.join("code-solar-sys","mars_info.png"))
jupiter_image_info = pygame.image.load(os.path.join("code-solar-sys","jupiter_info.png"))
saturn_image_info = pygame.image.load(os.path.join("code-solar-sys","saturn_info.png"))
uranus_image_info = pygame.image.load(os.path.join("code-solar-sys","uranus_info.png"))
neptune_image_info = pygame.image.load(os.path.join("code-solar-sys","neptune_info.png"))

#-------------------------------------------------------------------

#-------------------------------------------------------------------
# Корректировка размера изображении планет и информации
sun_image = pygame.transform.scale(sun_image, (88, 88))
mercury_image = pygame.transform.scale(mercury_image, (16.5, 16.5))
venus_image = pygame.transform.scale(venus_image, (27.5, 27.5))
earth_image = pygame.transform.scale(earth_image, (33, 33))
mars_image = pygame.transform.scale(mars_image, (22, 22))
saturn_image = pygame.transform.scale(saturn_image, (110, 44))
uranus_image = pygame.transform.scale(uranus_image, (38.5, 38.5))
jupiter_image = pygame.transform.scale(jupiter_image, (55, 55))
neptune_image = pygame.transform.scale(neptune_image, (44, 44))

sun_image_info = pygame.transform.scale(sun_image_info, (info_size_width, info_size_height))
mercury_image_info = pygame.transform.scale(mercury_image_info, (info_size_width, info_size_height))
venus_image_info = pygame.transform.scale(venus_image_info, (info_size_width, info_size_height))
earth_image_info = pygame.transform.scale(earth_image_info, (info_size_width, info_size_height))
mars_image_info = pygame.transform.scale(mars_image_info, (info_size_width, info_size_height))
jupiter_image_info = pygame.transform.scale(jupiter_image_info, (info_size_width, info_size_height))
saturn_image_info = pygame.transform.scale(saturn_image_info, (info_size_width, info_size_height))
uranus_image_info = pygame.transform.scale(uranus_image_info, (info_size_width, info_size_height))
neptune_image_info = pygame.transform.scale(neptune_image_info, (info_size_width, info_size_height))

#-------------------------------------------------------------------

# Загрузка фонового изображения(космос) и траектории
background_image = pygame.transform.scale(pygame.image.load(os.path.join("code-solar-sys","space.png")), (screen.get_width(), screen.get_height()))
background_way = pygame.transform.scale(pygame.image.load(os.path.join("code-solar-sys","space1.png")), (1536, 864))
background_way_rect = background_way.get_rect()
background_way_rect.centerx = screen.get_rect().centerx
background_way_rect.centery = screen.get_rect().centery

# Функция написания текста на экране
def print_text(message, x, y, font_color = (0,0,0), font_type = "Arial.ttf", font_size = 30):
    """
    Функция отвечает за вывод текста на экран.

    Args:
        message - текст, который нужно вывести на экран
        x - координата по оси X, где должен быть расположен левый край текста
        y - координата по оси Y, где должен быть расположен верхний край текста
        font_color - цвет текста. По умолчанию равен черному цвету (0, 0, 0)
        font_type - тип шрифта. По умолчанию равен "Arial.ttf"
        font_size - размер шрифта. По умолчанию равен 20 
    """
    font_type = pygame.font.SysFont(font_type, font_size)
    text = font_type.render(message, True, font_color)    
    screen.blit(text, (x, y))
    

# Класс планет
class Planet:
    def __init__(self, name, image, info, angle, distance, std_period, period, radius, x, y):
        """
        Конструктор класса Planet
        
        Args:

        name - имя объекта
        image - изображение объекта
        info - дополнительная информация об объекте
        angle - начальный угол объекта (в радианах)
        distance - расстояние от центра координат до объекта
        std_period - стандартный период обновления позиции объекта
        period - текущий период обновления позиции объекта
        radius - радиус объекта
        x - координата x объекта
        y - координата y объекта
        """
        self.name = name
        self.image = image
        self.info = info
        self.angle = angle
        self.distance = distance
        self.std_period = std_period
        self.period = period
        self.radius = radius
        self.x = x
        self.y = y

    # Обновление позиции планеты
    def update_position(self, center_x, center_y):
        """
        Функция обновляет позицию объекта, который движется по окружности с центром в (center_x, center_y) 
        и радиусом self.distance.
        
        Args:

        center_x - координата x центра окружности
        center_y - координата y центра окружности
        """
        self.angle += 0.05 * (1 / self.period)
        self.x = center_x + math.cos(self.angle) * self.distance
        self.y = center_y + math.sin(self.angle) * self.distance

    # Отображение планеты
    def draw(self, screen):
        """
        Функция отвечает за отрисовку объекта на экране.
        
        Args:

        screen - объект pygame.display, на котором будет отрисован объект
        """
        image_rect = self.image.get_rect()
        image_rect.center = (int(self.x), int(self.y))
        screen.blit(self.image, image_rect)
    
    # Отображение информации о планете
    def show_planet_info(self):
        """
        Функция отвечает за вывод информации о планете на экран.
        """
        global info_planet_img
        info_planet_img = self.info

    # Проверка нажатия на планету
    def check_planet_clicked(self, mouse_pos):
        """
        Функция отвечает за проверку, была ли планета кликнута мышью.
        
        Args:

        mouse_pos - кортеж координат мыши (x, y)

        Returns:

        Возвращает значение True, если расстояние между планетой и точкой, в которой была кликнута мышь, меньше или равно радиусу планеты. 
        В противном случае возвращает значение False.
        """
        dx = mouse_pos[0] - self.x
        dy = mouse_pos[1] - self.y
        dist = math.sqrt(dx**2 + dy**2)
        
        return dist <= self.radius

    # Обновление периуда(скорости) планеты
    def update_period(self):
        """
        Функция отвечает за обновление периода вращения планеты.
        """
        if self.name != "Earth":
            self.change_period(earth.period/(earth.std_period/self.std_period))
        elif self.period >1.17 and self.period < 1.23:
            self.change_period(self.std_period)

    # Изменение периуда планеты
    def change_period(self, set_period):
        """
        Функция отвечает за изменение периода вращения планеты на заданное значение.
        
        Args:

        set_period - новое значение периода вращения планеты
        """
        self.period = set_period


# Создание объектов с классам планета 
sun = Planet("Sun", sun_image, sun_image_info, 0, 0, 0, 0, 100, screen.get_width() / 2, screen.get_height() / 2)
earth = Planet("Earth", earth_image, earth_image_info, 0, 125, 1.2,1.2, 25, sun.x + sun.radius * 3, sun.y)
mercury = Planet("Mercury", mercury_image, mercury_image_info, 0, 65, 0.54, earth.period/2.22, 10, sun.x + sun.radius, sun.y)
venus = Planet("Venus", venus_image,venus_image_info, 0, 90,-0.82, earth.period/-1.46, 20, sun.x + sun.radius * 2, sun.y)
mars = Planet("Mars", mars_image, mars_image_info, 0, 155, 1.88, earth.period/0.638, 15, sun.x + sun.radius * 4, sun.y)
jupiter = Planet("Jupiter", jupiter_image, jupiter_image_info, 0, 195, 11.86, earth.period/0.101, 45, sun.x + sun.radius * 5, sun.y)
saturn = Planet("Saturn", saturn_image, saturn_image_info, 0, 260, 29.5, earth.period/0.0406, 40, sun.x + sun.radius * 6, sun.y)
uranus = Planet("Uranus", uranus_image, uranus_image_info, 0, 320, 84, earth.period/0.01428, 30, sun.x + sun.radius * 7, sun.y)
neptune = Planet("Neptune", neptune_image, neptune_image_info, 0, 370, 164.8, earth.period/0.00728, 35, sun.x + sun.radius * 8, sun.y)

# Объявление массива планет
planets = [sun, mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]

# Функция добавления скорости вращения планеты
def plus_speed():
    """
    Функция отвечает за ускорение вращения Земли.
    """
    global kof_value
    if kof_value == 0:
        earth.period = 5.04
    if earth.period>0.25:
        earth.period -= earth.std_period*0.2 if earth.period < 1.21 else earth.std_period*0.8
        # print(neptune.period,"\n")
        kof_value += 25
        print(kof_value)
        print("Click ")
        print(earth.period,"\n")

# Функция отнимания скорости вращения планеты
def minus_speed():
    """
    Функция отвечает за замедление вращения Земли.
    """
    global kof_value
    if earth.period<5:
        kof_value -= 25
        print(kof_value)
        if kof_value != 0:
            earth.period += earth.std_period*0.8  if earth.period > 1.19 else earth.std_period*0.2
            # print(neptune.period,"\n")
            print("Click ")
            print(earth.period,"\n")
        else:
            earth.period = float('inf')

# Класс кнопка
class Button:
    def __init__(self, width, height, action = None, regional_butt = False):
        """
        Конструктор класса Button. 

        Args:

        width - ширина кнопки
        height - высота кнопки
        action - функция, которая будет вызываться при нажатии на кнопку. По умолчанию равна None.
        regional_butt=False - булево значение, указывающее, является ли кнопка региональной.И свойство butt_rect будет использоваться для определения местоположения кнопки на экране.
        """
        self.width = width
        self.height = height
        self.color = (13,162,58)
        self.action = action
        self.image = regional_butt
        self.butt_rect = None

    # Отображение кнопки
    def draw(self, x, y, message=None):
        """
        Функция отвечает за отображение кнопки на экране.

        Args:

        x - координата по оси X левого верхнего угла кнопки на экране
        y - координата по оси Y левого верхнего угла кнопки на экране
        message=None - текст, который будет отображаться на кнопке
        """
        if self.image is False:
            self.butt_rect = pygame.Rect(x, y, self.width, self.height)
            pygame.draw.rect(screen, self.color, self.butt_rect)
            print_text(message, x+50, y+30)
        else:
            self.butt_rect = self.image.get_rect(x, y, self.width, self.height)
            
    # Выполнение функции копки(если такая присутствует)
    def do_action(self):
        """
        Функция отвечает за вызов функции, связанной с кнопкой, если она была передана в конструкторе.
        """
        if self.action is not None:
            self.action()

# Создание объектов с классом кнопка
button_plus = Button(220,70, plus_speed)
button_minus = Button(220,70, minus_speed)

# Вычисление позиции, кнопок
plus_pos_x = screen.get_rect().centerx + 200
minus_pos_x = screen.get_rect().centerx - 400

plus_pos_y = screen.get_rect().centery + 400
minus_pos_y = screen.get_rect().centery + 400

# Вычисление позиции, коэфицента скорости планет
kof_pos_x = screen.get_rect().centerx - 44
kof_pos_y = screen.get_rect().centery + 400
kof_value = 100


# Установка частоты времени
clock = pygame.time.Clock()
fps = 60

# Запуск программы в цикле
running = True


while running:
    # Обработка событий в pygame
    for event in pygame.event.get():
        clicked = False
        for planet in planets:
            # Проверка на выход
            if event.type == pygame.QUIT:
                running = False
            # Проверка на нажатие ЛКМ
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # Провеврка на поподание координат мыши, в область кнопки добавления скорости 
                if not clicked and button_plus.butt_rect.collidepoint(event.pos):
                    clicked = True
                    button_plus.do_action()
                # Провеврка на поподание координат мыши, в область кнопки вычистания скорости 
                if not clicked and button_minus.butt_rect.collidepoint(event.pos):   
                    clicked = True
                    button_minus.do_action()
                # Обработка клика на кнопке закрытия программы
                if close_button_rect.collidepoint(event.pos):
                    running = False
                # Обработка клика на кнопке закрытия информационной панели
                if info_close_butt.collidepoint(event.pos):
                    info_planet_img = info_std_img
                # Проверка клика по планете    
                if planet.check_planet_clicked(event.pos):
                    planet.show_planet_info()
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                clicked = False            
    



    # Фоновое изображение
    screen.blit(background_image, (0, 0))
    screen.blit(background_way, background_way_rect)

    # Кнопки "Замедленить", "Ускорить"
    button_minus.draw(minus_pos_x,minus_pos_y,"Замедлить")
    button_plus.draw(plus_pos_x,plus_pos_y,"Ускорить")

    # Отображение солнца
    sun.draw(screen)

    # Отображение и обновление положения планет
    for planet in planets[1:]:
        planet.update_position(sun.x, sun.y)
        planet.update_period()
        # planet.draw_trail(screen)
        planet.draw(screen)
    all_sprites.draw(screen)

    # Отображение информационной панели
    screen.blit(info_planet_img, (40, 40))

    # Отображение коэффициента скорости планет
    print_text(str(kof_value)+'%',kof_pos_x,kof_pos_y, font_color = (255, 153, 0), font_size = 50)

    # Обновление дисплея
    pygame.display.update()

    

    # Пауза (кадры в секунду)
    clock.tick(fps)

# Выход из pygame
pygame.quit()
