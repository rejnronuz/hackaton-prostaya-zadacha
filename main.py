print('хакатон по программированию на языке python «Простая задача»')
choice = input('выберите задачу для просмотра:\n1 - Задача №1 Простые числа.\n2 - Задача №2 Космический кортеж\n3 - Задача №3 Бинарный поиск.\n')
def getanswr(s):
    while True:
        answer = input(s).strip().lower()
        if answer in ('да', 'нет'):
            return answer
        else:
            print("некорректный ввод, ответьте 'да'/'нет'")
def binarysearch():
    print("загадайте число от 0 до 1000\nотвечайте лишь 'да' или 'нет'")
    low = 0
    high = 1000
    while low < high:
        mid = (low + high) // 2
        answer = getanswr(f"число больше {mid}? (да/нет)")
        if answer == 'да':
            low = mid + 1
        else:
            high = mid
    print(f"вы загадали число {low}")

def isval(s):
    balance = 0
    for c in s:
        if c == '(':
            balance += 1
        elif c == ')':
            balance -= 1
            if balance < 0:
                return False
    return balance == 0

def decode(s):
    stack = []
    current_str = ''
    current_num = 0
    for c in s:
        if c.isdigit():
            current_num = current_num * 10 + int(c)
        else:
            if c == '(':
                multiplier = current_num if current_num != 0 else 1
                stack.append((current_str, multiplier))
                current_str = ''
                current_num = 0
            elif c == ')':
                if not stack:
                    return ''
                prev_str, multiplier = stack.pop()
                current_str = prev_str + current_str * multiplier
                current_num = 0
            else:
                multiplier = current_num if current_num != 0 else 1
                current_str += c * multiplier
                current_num = 0
    return current_str
def isprost(s):
    if s < 2:
        return False
    for i in range(2, int(s ** 0.5) + 1):
        if s % i == 0:
            return False
    return True

def getvalidint(s):
    while True:
        try:
            value = int(input(s))
            return value
        except ValueError:
            print("некорректный ввод: введите целое число")


if choice==('3'):
    binarysearch()
elif choice==('2'):
    while True:
        bebe = input("введите ваш код для дешифровки:\n").strip()
        if not isval(bebe):
            print("некорректный ввод: некорректные скобки")
            continue
        print(decode(bebe))
        break
elif choice==('1'):
    print("введите начало и конец диапазона")
    start = getvalidint("начало:\n")
    end = getvalidint("конец:\n")

    while start > end:
        print("некорректный ввод: начало диапазона не может быть больше конца")
        start = getvalidint("начало:\n")
        end = getvalidint("конец:\n")

    primes = [num for num in range(start, end + 1) if isprost(num)]

    print(f"простые числа в диапазоне [{start}, {end}]:\n{primes}")
else:
    print('некорректный ввод: введите соответсвующую программе цифру')