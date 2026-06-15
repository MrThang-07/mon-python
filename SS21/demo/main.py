def calculate_payment(amount : float, rate : float) -> float:
    if amount < 0:
        print("Số tiền k9hông được phép âm !")
        raise ValueError("Số tiền âm")
    return amount * (1 - rate)
result =calculate_payment(100.0,0.1)

print(result)