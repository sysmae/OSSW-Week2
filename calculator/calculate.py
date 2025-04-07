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
            print("숫자가 아닙니다. 다시 입력하세요.")
 
if __name__ == '__main__':
    while True:
        # 사용자 입력
        num1 = get_float_input('\n첫번째 숫자를 입력하세요: 입력: ')

        print('\n원하는 사칙연산 기호 중 하나를 선택하세요. (+, -, *, /)')
        act = input("기호: ")

        num2 = get_float_input('\n두번째 숫자를 입력하세요: 입력: ')

        # 연산 수행
        if act == '+':
            result = plus(num1, num2)
        elif act == '-':
            result = minus(num1, num2)
        elif act == '*':
            result = mul(num1, num2)
        elif act == '/':
            result = divide(num1, num2)
        else:
            result = "Error: Invalid operation"
       
        print(f'사칙연산 결과는 {result}입니다.')
        # 계속할지 여부 확인
        cont = input("\n계속하시겠습니까? (y/n): ")
        if cont.lower() != 'y':
            break

# def copilot_test():
#     화면이 휙휙 바껴요
#     저희 노션 워크스페이스도 마

# 근데 이거 나중에 쓸까요? 신기하긴 한데
# 보통 일찍 끝내주시지 않나요? 끝나고 시간 있으면 조금 해봐도 괜찮을거같아요
# ->네네
  
    
# 이따가 자리 있으면 모일까요? 자리 없을거 같긴한데

# 노션이랑 깃허브랑 셋팅 해놓고 기적인 이야기좀 해보면 좋을거 같아요

# 딸깍 코딩

list_operators = ['+', '-', '*', '/']

# 두수를 입력받아 사칙연산을 수행하는 함수
def calculate(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operator"