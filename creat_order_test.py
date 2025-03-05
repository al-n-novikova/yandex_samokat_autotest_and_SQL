#Александра Новикова, 27-я когорта — Финальный проект. Инженер по тестированию плюс

# Импортируем модуль sender_stand_request, содержащий функции для отправки HTTP-запросов к API.
import sender_stand_request

# Импортируем модуль data, в котором определены данные, необходимые для HTTP-запросов.
import data

# 1. Выполняем запрос на создание заказа.
response = sender_stand_request.post_new_order(data.order_body)

# 2. Сохраняем номер трека заказа.
track_new_order = response.json()["track"]

# Функция для позитивной проверки
def positive_assert(track):
    # 3. Выполняем запрос на получения заказа по треку заказа.
    response = sender_stand_request.get_order_by_track(track)
    # 4. Проверяем, что код ответа равен 200.
    assert response.status_code == 200

# Тест 1. Проверяется, что по треку заказа можно получить данные о заказе.
def test_get_order_by_track():
    positive_assert(track_new_order)
