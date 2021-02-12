import requests
import sys
import pygame
import os
api_server = "http://static-maps.yandex.ru/1.x/"

lon = f"{sys.argv[1]}"
k = lon
lat = f"{sys.argv[2]}"
t = lat
delta = f"{sys.argv[3]}"



# Инициализируем pygame
pygame.init()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        key = pygame.key.get_pressed()
        if key[pygame.K_PLUS]:
            if delta < "3":
                delta = str(float(delta) + 0.001)
        if key[pygame.K_MINUS]:
            if delta > "0.001":
                delta = str(float(delta) - 0.001)
        if key[pygame.K_LEFT]:
            if float(lon) > float(k) - 0.01:
                lon = str(float(lon) - 0.0001)
        if key[pygame.K_RIGHT]:
            if float(lon) < float(k) + 0.01:
                lon = str(float(lon) + 0.0001)
        if key[pygame.K_UP]:
            if float(lat) < float(t) + 0.01:
                lat = str(float(lat) + 0.0001)
        if key[pygame.K_DOWN]:
            if float(lat) > float(t) - 0.01:
                lat = str(float(lat) - 0.0001)
    params = {
        "ll": ",".join([lon, lat]),
        "spn": ",".join([delta, delta]),
        "l": "map"
    }
    response = requests.get(api_server, params=params)
    map_file = "map.png"
    with open(map_file, "wb") as file:
        file.write(response.content)
    screen = pygame.display.set_mode((600, 450))
    # Рисуем картинку, загружаемую из только что созданного файла.
    screen.blit(pygame.image.load(map_file), (0, 0))
    # Переключаем экран и ждем закрытия окна.
    pygame.display.flip()
pygame.quit()

# Удаляем за собой файл с изображением.
os.remove(map_file)