class OrderList:
    def __init__(self, order_list):
        self.order_list = order_list

    def get_order_list(self):
        return self.order_list
    
    def append_order(self, order):
        self.order_list.append(order)
    
    def get_info(self):
        info = "Order List:\n"
        for order in self.order_list:
            info += order.get_info() + "\n"
        return info