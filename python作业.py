def factorial(n):
    if not isinstance(n, int) or n < 0:
        return "请输入非负整数！"

    result = 1
    for i in range(1, n + 1):
        result *= i

    return result


def is_prime(n):
    if n < 2:
        return "False"

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return "False"

    return "True"


def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    fib_sequence = [0, 1]
    for i in range(2, n):
        next_fib = fib_sequence[i - 1] + fib_sequence[i - 2]
        fib_sequence.append(next_fib)

    return fib_sequence


while True:
    print("\n请选择一个功能：")
    print("a: 计算阶乘")
    print("b: 判断素数")
    print("c: 打印斐波那契数列")
    print("d: 退出程序")

    choice = input("请输入你的选择（a/b/c/d）：").lower()

    if choice == 'd':
        print("程序结束。")
        break

    if choice == 'a':
        while True:
            user_input = input("请输入一个非负整数（输入'R'返回选择界面）：")
            if user_input.lower() == 'r':
                break
            try:
                n = int(user_input)
                print(f"{n} 的阶乘是: {factorial(n)}")
            except ValueError:
                print("请输入非负整数！")

    elif choice == 'b':
        while True:
            user_input = input("请输入一个非负整数（输入'R'返回选择界面）：")
            if user_input.lower() == 'r':
                break
            try:
                n = int(user_input)
                print(f"{n} 是素数吗? {is_prime(n)}")
            except ValueError:
                print("请输入非负整数！")

    elif choice == 'c':
        while True:
            user_input = input("请输入一个正整数（输入'R'返回选择界面）：")
            if user_input.lower() == 'r':
                break
            try:
                n = int(user_input)
                if n < 0:
                    print("请输入一个非负整数！")
                else:
                    print(f"长度为 {n} 的斐波那契数列是: {fibonacci(n)}")
            except ValueError:
                print("请输入一个正整数！")

    else:
        print("无效选择，请重新输入！")