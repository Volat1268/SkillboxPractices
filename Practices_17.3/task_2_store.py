original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
new_lst = [(price if price >= 0 else 0) for price in original_prices]

print(new_lst)