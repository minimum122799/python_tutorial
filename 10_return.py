# 함수를 실행해 값을 반환받기.
def tax_calc(money):
    print(money * 0.35)
    return money * 0.35

def pay_tax(tax):
    print("thank you for paying", tax)

pay_tax(tax_calc(10000))

to_pay = tax_calc(20000)
pay_tax(to_pay)