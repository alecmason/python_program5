print('REQ 1: This is program 5 - Alec Jones')

print('REQ 2: This program records Austin Area Whole Foods product data.')

number_of_stores = int(input('REQ 3: Enter the number of store: '))

store_counter = 0

while store_counter < number_of_stores:
    store_name = input('REQ 4: Enter the store name: ')
    store_phone_number = input('REQ 4: Enter the store phone number: ')
    store_address = input('REQ 4: Enter the store address: ')

    veg_counter = 0
    veg_name_list = []
    veg_plu_list = []
    veg_order_quantity_list = []

    products_to_enter = int(input('REQ 5: Do you have products to enter? (-1 to end) '))

    while products_to_enter != -1:
        veg_name = input('REQ 5: Enter vegetable name: ')
        veg_name_list.append(veg_name)

        veg_plu = input('REQ 5: Enter vegetable PLU: ')
        veg_plu_list.append(veg_plu)

        veg_order_quantity = input('REQ 5: Enter amount to order: ')
        veg_order_quantity_list.append(veg_order_quantity)

        veg_counter += 1

        products_to_enter = int(input('REQ 5: Do you have products to enter? (-1 to end) '))

    print('REQ 6: {}'.format(store_name))
    print('REQ 6: {}'.format(store_phone_number))
    print('REQ 6: {}'.format(store_address))

    counter = 1
    while counter <= veg_counter:
        print('REQ 7: Vegetable Name {}: {}'.format(counter, veg_name_list[counter - 1]))
        print('REQ 7: Vegetable PLU{}: {}'.format(counter, veg_plu_list[counter - 1]))
        print('REQ 7: Amount to Order{}: {}'.format(counter, veg_order_quantity_list[counter - 1]))
        counter += 1

print('REQ 8:')
