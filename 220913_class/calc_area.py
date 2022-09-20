num1 = int(input('첫 번째 숫자를 입력 : '))
num2 = int(input('두 번째 숫자를 입력 : '))

class calc_area:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def square(self):
        result = self.num1 * self.num2
        return result

    def triangle(self):
        result = self.num1 * self.num2 / 2
        return result

    def circle(self):
        result = (self.num1 / 2) **2 * 3.14  # 첫번째 숫자를 원의 지름(2r)으로, 𝝿r²
        return result

area = calc_area(num1, num2)

print(area.square()) # 사각형의 넓이
print(area.triangle()) # 삼각형의 넓이
print(area.circle()) # 원의 넓이