"""Bill"""
def calculate_total_amount(price):
    """main"""
    service_charge = max(min(price * 0.10, 1000), 50)
    subtotal = price + service_charge
    vat = subtotal * 0.07
    total_amount = subtotal + vat
    print(f"{total_amount:.2f}")
calculate_total_amount(int(input()))
