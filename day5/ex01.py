"Exercise 1 : CDAC Cafeteria Biling"

def calculate_cafeteria_bill(base_price, *items, tax_rate=0.05, discount=0.0, delivery_fee=0.0):
    total=0.0
    extra_order=items
    subtotal=0.0
    extra_price=0.0
    discount_subtotal=0.0
    tax=0.0
    final_total=0.0
    if len(extra_order)!=0:
        for k in extra_order:
            extra_price+=k
        subtotal=base_price +extra_price
        discount_subtotal=subtotal*(1-10/100)
        tax=discount_subtotal*tax_rate
        final_total=discount_subtotal+tax+delivery_fee
        print(final_total)
    else:
         total=base_price*tax_rate
         total+=base_price
         print(total)

def main():
    print("Standard meal, no sides, default tax, no discount, no delivery")
    total1 = calculate_cafeteria_bill(100.0)   
    # Subtotal = 100.0
    # Tax = 100.0 * 0.05 = 5.0
    # Return: 105.00  
    print("Meal with sides, custom tax rate, 10% discount, flat delivery fee")
    total2 = calculate_cafeteria_bill(100.0, 20.0, 30.0, tax_rate=0.08, discount=10.0, delivery_fee=15.0)
    # Raw Subtotal = 100.0 + (20.0 + 30.0) = 150.0
    # Discounted Subtotal = 150.0 * (1 - 10/100) = 135.0
    # Tax = 135.0 * 0.08 = 10.8
    # Final Total = 135.0 + 10.8 + 15.0 = 160.8
    # Return: 160.80
    
main()