def say_hello():
    print("Hello how r u?")

# 파이선은 들여쓰기 해야 해당 코드가 어디에 속해 있는지 인식할 수 있다.

say_hello()

def parent():
    print("Start parent()")
    say_hello()

parent()
