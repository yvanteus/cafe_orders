from utils import get_text, show_menu, get_order, save_log, get_device

def main():
    menu = {
        "Чай": 70,
        "Кофе": 120,
        "Пепси": 110,
        "Салат": 270,
        "Панкейк": 130,
        "Какао": 190,
        "Пельмени": 145,
        "Сыр": 270,
        "Рыба": 250,
        "Тирамису": 170,
        "Хлеб": 12
        
    }
    
    recommendations = {
        "Кофе": ["Панкейк", "Тирамису"],
        "Чай": ["Панкейк", "Тирамису"],
        "Какао": ["Панкейк", "Тирамису"],
        "Салат": ["Чай", "Хлеб"],
        "Пельмени": ["Чай", "Кофе", "Хлеб"],
        "Рыба": ["Хлеб", "Чай"],
        "Тирамису": ["Какао", "Кофе", "Чай"],
        "Панкейк": ["Какао", "Кофе", "Чай"]
    }
    
    devices = ["Mobile", "PC", "Tablet", "Other"] #список девайсов для генерации в логи
    device = get_device(devices) #достаем случайный девайс из списка выше с помощью рандома
    
    order_list = [] #собираем итоговый заказ 
    total_price = 0 #итоговая стоимость
    
    user_name = get_text("Как вас зовут?\n")
    show_menu(menu=menu)
    
    while True:
        order, price = get_order(menu=menu)
        
        if order is None:
            break
        
        order_list.append(order)
        total_price += price
        
        if order in recommendations:
            recs = [r for r in recommendations[order] if r not in order_list]
            if recs: 
                print(f"\nК {order} рекомендуем {', '.join(recs)}")
        #блок кода выше делает рекомендации, исключая варианты, которые уже есть в заказе
        
        
    print(f"{user_name}, ваш заказ: {', '.join(order_list).lower()}. К оплате {total_price} руб")
        
        
    save_log(name=user_name, order=','.join(order_list), price=total_price, device=device)
    
if __name__ == "__main__":
    main()
    