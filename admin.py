from datetime import datetime

def new_order_notification(name: str, order_list: list) -> None:
    '''система уведомлений повара о новых заказах'''
    now = datetime.now().strftime("%A %H:%M:%S")
    with open("admin_orders.txt", "a", encoding="UTF-8") as file:
        
        file.write(f"{now} новый заказ для клиента {name}: {order_list}\n")