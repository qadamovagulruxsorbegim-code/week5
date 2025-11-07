def add_new_orders(orders, new_orders):
    for order in new_orders:
        orders.append(order)
def process_orders(orders, num_to_process):
    processed=[]
    for _ in range(min(num_to_process, len(orders))):
        first_order= orders[0]
        processed.append(first_order)
        orders.remove(first_order)
    return processed
def cancel_order(orders, order_id):
    for order in orders:
        if order ==order_id:
            orders.remove(order)
def manage_orders(initial_orders, new_orders_to_add, orders_to_process,order_to_cancel):
    orders=initial_orders.copy()
    add_new_orders(orders,new_orders_to_add)
    cancel_order(orders, order_to_cancel)
    processed_orders=process_orders(orders,orders_to_process)
    return orders, processed_orders
    # Test Case 1
initial = [101, 102, 103, 104]
new = [105, 106]
process_count = 3
cancel_id = 103

# When you call your function, you can receive the two returned lists like this:
final_state, processed = manage_orders(initial, new, process_count, cancel_id)
print("Test case 1")
print (final_state)
print(processed)
print ( initial )

    
        