import requests
import sys
import pygame
import os
api_server = "http://static-maps.yandex.ru/1.x/"

lon = "37.530887"
lat = "55.703118"
delta = "0.002"
k = "map"



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
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if 0 < pos[0] < 20 and 0 < pos[1] < 20:
                k = "map"
            if 20 < pos[0] < 40 and 0 < pos[1] < 20:
                k = "sat"
            if 40 < pos[0] < 60 and 0 < pos[1] < 20:
                k = "sat,skl"

    params = {
        "ll": ",".join([lon, lat]),
        "spn": ",".join([delta, delta]),
        "l": k
    }

    response = requests.get(api_server, params=params)
    map_file = "map.png"
    with open(map_file, "wb") as file:
        file.write(response.content)
    screen = pygame.display.set_mode((600, 450))
    # Рисуем картинку, загружаемую из только что созданного файла.
    screen.blit(pygame.image.load(map_file), (0, 0))
    font0 = pygame.font.Font(None, 20)  # слова вверху
    text0 = font0.render("Сх", True, (0, 0, 0))
    screen.blit(text0, (10, 0))
    text1 = font0.render("Сп", True, (0, 0, 0))
    screen.blit(text1, (30, 0))
    text2 = font0.render("Г", True, (0, 0, 0))
    screen.blit(text2, (50, 0))
    # Переключаем экран и ждем закрытия окна.
    pygame.display.flip()
pygame.quit()

# Удаляем за собой файл с изображением.
os.remove(map_file)