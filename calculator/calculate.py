def plus(a, b):
    return a + b

def minus(a, b):
    return a - b

def mul(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error: Invalid input. Please enter a numeric value.")

if __name__ == '__main__':
    while True:
        # 사용자 입력
        input1 = get_float_input('\n첫번째 숫자를 입력하세요: 입력: ')

        print('\n원하는 사칙연산 기호 중 하나를 선택하세요. (+, -, *, /)')
        act = input("기호: ")

        input2 = get_float_input('\n두번째 숫자를 입력하세요: 입력: ')

        # 연산 수행
        if act == '+':
            result = plus(input1, input2)
        elif act == '-':
            result = minus(input1, input2)
        elif act == '*':
            result = mul(input1, input2)
        elif act == '/':
            result = divide(input1, input2)
        else:
            result = "Error: Invalid operation"

        print(f'사칙연산 결과는 {result}입니다.')

        # 계속할지 여부 확인
        cont = input("\n계속하시겠습니까? (y/n): ")
        if cont.lower() != 'y':
            break