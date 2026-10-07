def calculate_total(price,tax=0,discount=0):
    final_price=price+tax-discount
    return final_price
print(calculate_total(350,67,96))
