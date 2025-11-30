import random
from datetime import datetime

def get_text(text: str) -> str:
    """Единственная задача этой функции - запросить имя от покупателя"""
    return input(text).strip().title()


def show_menu(menu: dict[str, int]) -> None:
    '''Показываем меню пользователю'''
    for key, value in menu.items():
        print(f"{key}: {value} руб")
        

def get_order(menu: dict[str, int]) -> tuple[str, int]:
    '''Запрашиваем у покупателя заказ. Возвращаем кортеж из наименования позиции в меню и его стоимость'''
    while True:
        print("\nЧто хотите заказать?")
        choice = input().strip().capitalize()
        
        if choice in menu:
            price = menu[choice]
            return choice, price
        else:
            print("Такой позиции в меню нет")
            
            
def save_log(name: str, order: str, price: int, device: str) -> None:
    '''логируем поведение клиента. Как зовут, что купил, итоговая стоимость, устройство клиента'''
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("cafe_orders_logs.txt", "a", encoding="UTF-8") as file:
        file.write(f"{now} user={name} item={order} cost={price} device={device}\n")
        
        
def get_device(device_list: list[str]) -> str:
    '''для повышения интерактивности поведения кода, функция выдает разные девайсы для логов: mobile, pc, tablet, other'''
    return random.choice(device_list)