num1 = input('첫 번째 숫자를 입력 : ')
num2 = input('두 번째 숫자를 입력 : ')

class Calc:

    def set_number(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def plus(self):
        result = int(self.num1) + int(self.num2)
        return result

    def minus(self):
        result = int(self.num1) - int(self.num2)
        return result

    def multiple(self):
        result = int(self.num1) * int(self.num2)
        return result

    def divide(self):
        try:
            result = int(self.num1) / int(self.num2)
            return result
        except ZeroDivisionError:  # 0으로 나누면서 에러가 발생했을 때
            return "0으로는 나눌 수 없습니다"

calc = Calc()
calc.set_number(num1, num2)

try:
    print(calc.plus()) # 더한 값
    print(calc.minus()) # 뺀 값
    print(calc.multiple()) # 곱한 값
    print(calc.divide()) # 나눈 값

except ValueError:  # int로 변환하는 과정에서 에러가 발생했을 떄
    print(f"{num1} 혹은 {num2} 은(는) 숫자가 아닙니다.")
except Exception as e:  # 위에서 정의하지 않은 에러가 발생했을 때(권장하지 않음)
    print(f"예상하지 못한 에러가 발생했습니다. error : {e}")