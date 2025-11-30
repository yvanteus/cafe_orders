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
        
    }
    
    devices = ["Mobile", "PC", "Tablet", "Other"] #список девайсов для генерации в логи
    device = get_device(devices)
    
    order_list = [] #собираем итоговый заказ 
    total_price = 0 #итоговая стоимость
    
    user_name = get_text("Как вас зовут?\n")
    show_menu(menu=menu)
    
    while True:
        order, price = get_order(menu=menu)
        order_list.append(order)
        total_price += price
        
        more = input("Что нибудь еще? да/нет\n").strip().lower()
        if more != "да":
            break
        
        
    print(f"{user_name}, ваш заказ: {' '.join(order_list)}. К оплате {total_price} руб")
        
        
    save_log(name=user_name, order=' '.join(order_list), price=total_price, device=device)
    
if __name__ == "__main__":
    main()