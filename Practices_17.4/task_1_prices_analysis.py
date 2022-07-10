import random

original_prices = [random.randint(-25, 25) for price in range(5)]

new_prices = [0 if price < 0 else price for price in original_prices]

print('Список с предыдущими ценами:', original_prices)
print('Список с новыми ценами:', new_prices)

print("\nМы потеряли:", abs(sum(original_prices) - sum(new_prices)))
