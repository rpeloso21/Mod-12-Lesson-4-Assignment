class OrderQueue:
    def __init__ (self):
        self.orders = []

    def add_order(self, order):
        self.orders.append(order)

    
    def remove_order(self):
        if not self.is_empty():
            self.orders.pop(0)
            print("\nOldest order removed.\n")

    def is_empty(self):
        return len(self.orders) == 0
    
    def size(self):
        return len(self.orders)
    
    def show_orders(self):
        if self.is_empty():
            print("There are no orders.")

        else:
            for order in self.orders:
                print(f"Order: {order}")


order_queue = OrderQueue()

order_queue.add_order("Grilled cheese and a coke")
order_queue.add_order("Eggs and bacon")
order_queue.add_order("Steak and cheese sandwich")
order_queue.add_order("Salad")

order_queue.show_orders()

order_queue.remove_order()

order_queue.show_orders()

