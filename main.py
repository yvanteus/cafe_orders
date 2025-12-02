from utils import get_text, show_menu, get_order, save_log, get_device
from admin import new_order_notification
from menu_recommendation import menu, recommendations
from config import devices

def main():
    
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
        
    if not order_list:
            print("Вы совсем ничего не заказали")
            return
        #завершение работы программы, если покупатель ничего не купил
    
    print(f"{user_name}, ваш заказ: {', '.join(order_list).lower()}. К оплате {total_price} руб")
        
        
    save_log(name=user_name, order=','.join(order_list), price=total_price, device=device)
    new_order_notification(name=user_name, order_list=order_list)
    
if __name__ == "__main__":
    main()
    