# Импортируем модуль configuration, который, мы создали выше - он содержит настройки подключения и путь к документации
import configuration

# Импортируем модуль requests, который предназначен для отправки HTTP-запросов
# Это популярная библиотека, которая позволяет взаимодействовать с веб-сервисами
import requests

# Импорт данных запроса из модуля data, в котором определены заголовки и тело запроса
import data

# Определение функции post_new_order для отправки POST-запроса на создание нового заказа
def post_new_order(body):
    # Выполнение POST-запроса с использованием URL из конфигурационного файла, тела запроса и заголовков
    # URL_SERVICE и CREATE_ORDER объединяются для формирования полного URL для запроса
    # json=body используется для отправки данных пользователя в формате JSON
    # headers=data.headers устанавливает заголовки запроса из модуля data
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=body,
                         headers=data.headers)

# Определение функции get_order_by_track для отправки get-запроса на создание нового набора пользователя
def get_order_by_track(track):
    # Выполнение POST-запроса с использованием URL из конфигурационного файла, тела запроса и заголовков
    # URL_SERVICE, GET_ORDER_BY_TRACK и номер созданного заказа track объединяются для формирования полного URL для запроса
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK + str(track))
