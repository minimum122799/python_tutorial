# 함수와 매개변수 return 을 활용한 예제
def make_juice(fruit):
    return f"{fruit}+🥤"
    print("return before running?")     # 해당 코드는 실행되지 않는다. 

def add_ice(juice):
    return f"{juice}+🧊"

def add_sugar(iced_juice):
    return f"{iced_juice}+🧂"

juice = make_juice("🍓")
print(juice)
iceJuice = add_ice(juice)
print(iceJuice)
sweetIceJuice = add_sugar(iceJuice)
print(sweetIceJuice)
