
import os
import math

import pygame

# Инициализация Pygame
pygame.init()

# Установка размера окна
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen_width,screen_height = screen.get_size()

info_size_width = round(screen_width - (screen_width*((1920-400)/1920)))
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

# Создание поверхности для канваса 
info_planet_img = pygame.image.load(os.path.join("code-solar-sys","none_menu.png"))

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

# planet_img = [sun_image,mercury_image,venus_image,earth_image,mars_image,jupiter_image,saturn_image,uranus_image,neptune_image]

sun_image_info = pygame.image.load(os.path.join("code-solar-sys","sun_info.png"))
mercury_image_info = pygame.image.load(os.path.join("code-solar-sys","mercury_info.png"))
venus_image_info = pygame.image.load(os.path.join("code-solar-sys","venus_info.png"))
earth_image_info = pygame.image.load(os.path.join("code-solar-sys","earth_info.png"))
mars_image_info = pygame.image.load(os.path.join("code-solar-sys","mars_info.png"))
jupiter_image_info = pygame.image.load(os.path.join("code-solar-sys","jupiter_info.png"))
saturn_image_info = pygame.image.load(os.path.join("code-solar-sys","saturn_info.png"))
uranus_image_info = pygame.image.load(os.path.join("code-solar-sys","uranus_info.png"))
neptune_image_info = pygame.image.load(os.path.join("code-solar-sys","neptune_info.png"))

info_img = [sun_image_info,mercury_image_info,venus_image_info,earth_image_info,mars_image_info,jupiter_image_info,saturn_image_info,uranus_image_info,neptune_image_info]

#-------------------------------------------------------------------

#-------------------------------------------------------------------
# Загрузка изображения планет в нажатом состоянии
# sun_image_click = pygame.image.load(os.path.join("code-solar-sys",os.path.join("sun.png")))
# mercury_image_click = pygame.image.load(os.path.join("code-solar-sys",os.path.join("mercury.png")))
# venus_image_click = pygame.image.load(os.path.join("code-solar-sys",os.path.join("venus.png")))
# earth_image_click = pygame.image.load(os.path.join("code-solar-sys",os.path.join("earth.png")))
# mars_image_click = pygame.image.load(os.path.join("code-solar-sys",os.path.join("mars.png")))
# jupiter_image_click = pygame.image.load(os.path.join("code-solar-sys",os.path.join("jupiter.png")))
# saturn_image_click = pygame.image.load(os.path.join("code-solar-sys",os.path.join("saturn.png")))
# uranus_image_click = pygame.image.load(os.path.join("code-solar-sys",os.path.join("uranus.png")))
# neptune_image_click = pygame.image.load(os.path.join("code-solar-sys",os.path.join("neptune.png")))
#-------------------------------------------------------------------


#-------------------------------------------------------------------
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

# Загрузка фонового изображения(космос)
background_image = pygame.transform.scale(pygame.image.load(os.path.join("code-solar-sys","space.png")), (screen.get_width(), screen.get_height()))
background_way = pygame.transform.scale(pygame.image.load(os.path.join("code-solar-sys","space1.png")), (1536, 864))
background_way_rect = background_way.get_rect()
background_way_rect.centerx = screen.get_rect().centerx
background_way_rect.centery = screen.get_rect().centery

# pygame.image.load(os.path.join("code-solar-sys","space1.png"))


def print_text(message, x, y, font_color = (0,0,0), font_type = "Arial.ttf", font_size = 20):
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
		self.select = False

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
		# if len(self.past_positions) < 128*abs(self.period):
		#     self.past_positions.append((self.x, self.y))
		


	def draw(self, screen):
		"""
		Функция отвечает за отрисовку объекта на экране.
		
		Args:

		screen - объект pygame.display, на котором будет отрисован объект
		"""
		image_rect = self.image.get_rect()
		image_rect.center = (int(self.x), int(self.y))
		screen.blit(self.image, image_rect)

	# def draw_trail(self, screen):
	#     for i in range(1, len(self.past_positions)):
	#         pygame.draw.line(screen, (255, 153, 0), self.past_positions[i-1], self.past_positions[i], 2)
	
	def show_planet_info(self):
		"""
		Функция отвечает за вывод информации о планете на экран.
		"""
		global info_planet_img
		self.selected()
		info_planet_img = self.info

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

	def update_period(self):
		"""
		Функция отвечает за обновление периода вращения планеты.
		"""
		if self.name != "Earth":
			self.change_period(earth.period/(earth.std_period/self.std_period))
		elif self.period >1.17 and self.period < 1.23:
			self.change_period(self.std_period)

	def change_period(self, set_period):
		"""
		Функция отвечает за изменение периода вращения планеты на заданное значение.
		
		Args:

		set_period - новое значение периода вращения планеты
		"""
		self.period = set_period

	def selected(self):
		"""
		Функция относится к классу, описывающему графический элемент, и отвечет за выделение элемента.

		"""
		self.select = True    
	
	def un_selected(self):
		"""
		Функция относится к классу, описывающему графический элемент, и отвечет за снятие выделение элемента.

		"""
		self.select = False


sun = Planet("Sun", sun_image, sun_image_info, 0, 0, 0, 0, 100, screen.get_width() / 2, screen.get_height() / 2)
earth = Planet("Earth", earth_image, earth_image_info, 0, 125, 1.2,1.2, 25, sun.x + sun.radius * 3, sun.y)
mercury = Planet("Mercury", mercury_image, mercury_image_info, 0, 65, 0.54, earth.period/2.22, 10, sun.x + sun.radius, sun.y)
venus = Planet("Venus", venus_image,venus_image_info, 0, 90,-0.82, earth.period/-1.46, 20, sun.x + sun.radius * 2, sun.y)
mars = Planet("Mars", mars_image, mars_image_info, 0, 155, 1.88, earth.period/0.638, 15, sun.x + sun.radius * 4, sun.y)
jupiter = Planet("Jupiter", jupiter_image, jupiter_image_info, 0, 195, 11.86, earth.period/0.101, 45, sun.x + sun.radius * 5, sun.y)
saturn = Planet("Saturn", saturn_image, saturn_image_info, 0, 260, 29.5, earth.period/0.0406, 40, sun.x + sun.radius * 6, sun.y)
uranus = Planet("Uranus", uranus_image, uranus_image_info, 0, 320, 84, earth.period/0.01428, 30, sun.x + sun.radius * 7, sun.y)
neptune = Planet("Neptune", neptune_image, neptune_image_info, 0, 370, 164.8, earth.period/0.00728, 35, sun.x + sun.radius * 8, sun.y)

planets = [sun, mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]

def plus_speed():
	"""
	Функция отвечает за ускорение вращения Земли.
	"""
	if earth.period>0.25:
		earth.period -= earth.std_period*0.1 if earth.period < 1.21 else earth.std_period*0.4
		# print(neptune.period,"\n")
		print("Click ")
		print(earth.period,"\n")
def minus_speed():
	"""
	Функция отвечает за замедление вращения Земли.
	"""
	if earth.period<5:
		earth.period += earth.std_period*0.4  if earth.period > 1.19 else earth.std_period*0.1
		# print(neptune.period,"\n")
		print("Click ")
		print(earth.period,"\n")

class Button:
	def __init__(self, width, height, action = None):
		"""
		Конструктор класса Button. 

		Args:

		width - ширина кнопки
		height - высота кнопки
		action - функция, которая будет вызываться при нажатии на кнопку. По умолчанию равна None.
		"""
		self.width = width
		self.height = height
		self.color = (13,162,58)
		self.action = action
		self.butt_rect = None

	def draw(self, x, y, message):
		"""
		Функция отвечает за отображение кнопки на экране.

		Args:

		x - координата по оси X левого верхнего угла кнопки на экране
		y - координата по оси Y левого верхнего угла кнопки на экране
		message - текст, который будет отображаться на кнопке
		"""
		self.butt_rect = pygame.Rect(x, y, self.width, self.height)
		pygame.draw.rect(screen, self.color, self.butt_rect)
		print_text(message, x+20, y+12)

	def do_action(self):
		"""
		Функция отвечает за вызов функции, связанной с кнопкой, если она была передана в конструкторе.
		"""
		if self.action is not None:
			self.action()

button_plus = Button(200,50, plus_speed)
button_minus = Button(200,50, minus_speed)

plus_pos = screen.get_rect().centerx + 200
minus_pos = screen.get_rect().centerx - 400

change_procent = 0

# Установка частоты времени
clock = pygame.time.Clock()
fps = 30

# Запуск программы в цикле
running = True
canvas_show = False

clicked_time = 0
delay = 0

while running:
	# Обработка событий в pygame
	for event in pygame.event.get():
		delay = 300
		clicked = False
		for planet in planets:
			# Проверка на выход
			if event.type == pygame.QUIT:
				running = False
			elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
				if not clicked and button_plus.butt_rect.collidepoint(event.pos) and pygame.time.get_ticks() - clicked_time > delay:
					clicked = True
					button_plus.do_action()
					clicked_time = pygame.time.get_ticks()
				if not clicked and button_minus.butt_rect.collidepoint(event.pos) and pygame.time.get_ticks() - clicked_time > delay:
					clicked = True
					button_minus.do_action()
					clicked_time = pygame.time.get_ticks()
				# Обработка клика на кнопке закрытия
				if close_button_rect.collidepoint(event.pos):
					running = False
				# Проверка клика по планете    
				if planet.check_planet_clicked(event.pos):
					planet.show_planet_info()
			elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
				clicked = False            
	



	# Фоновое изображение
	screen.blit(background_image, (0, 0))
	screen.blit(background_way, background_way_rect)

	# button_minus.draw(30,640,"Замедлить")
	# button_plus.draw(250,640,"Ускорить")

	button_minus.draw(minus_pos,760,"Замедлить")
	button_plus.draw(plus_pos,760,"Ускорить")

	# Отображение солнца
	sun.draw(screen)
	# print(len(jupiter.past_positions),"\n")
	# Рисование и обновление положение планет
	for planet in planets[1:]:
		planet.update_position(sun.x, sun.y)
		planet.update_period()
		# planet.draw_trail(screen)
		planet.draw(screen)
	change_procent = 0
	all_sprites.draw(screen)
	screen.blit(info_planet_img, (40, 40))
	# Обновление дисплея
	pygame.display.update()

	

	# Пауза (кадры в секунду)
	clock.tick(fps)

# Выход из pygame
pygame.quit()
