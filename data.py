# заголовки для HTTP-запроса, указывающие на то, что тело запроса будет в формате JSON
headers= {
    "Content-Type": "application/json"
}

# данные заказа для создания новой записи заказа в системе
# содержат имя, фамилию заказчика, адрес доставки, ближайщую станцию метро к адресу доставки, телефон заказчика, дату заказа, срок использования, цвет заказываемого самоката и комментарий
order_body = {
    "firstName": "Марина",
    "lastName": "Иванова",
    "address": "Ленина, д. 4",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2025-03-10",
    "comment": "Нет дверного звонка и домофона",
    "color": [
        "BLACK"
    ]
}