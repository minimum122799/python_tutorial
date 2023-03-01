# 함수에 인자가 존재하지 않는다면 기본값을 파라미터로 사용한다.
# 사용자가 인자를 주지 않아도 에러가 발생하지 않음.
def say_hello(name="anonymous"):
    print("hello ", name)

say_hello("min")

say_hello()


#=======================수식으로 에러 보이지 않게 하기
def plus(a=0, b=0):
    print(a + b)

plus(1, 2)
plus(1)
plus()