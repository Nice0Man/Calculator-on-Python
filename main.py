import config as cfg


def calculate(expression):
    code = compile(expression, "<string>", "eval")
    # компилируем введенную строку в код
    # compiling in byte-code
    for name in code.co_names:
        # проходим по списку математических действий
        if name not in cfg.ALLOWED_NAMES:
            # если действия нет, то возвращаем NameError, в котором говорим,
            # что данного действия нет в списке доступных
            raise NameError(f"The use of '{name}' is not allowed")
    return eval(code, {"__builtins__": {}}, cfg.ALLOWED_NAMES)
    # Если все окей, возвращем результат выполнения функции


def main():
    print(cfg.WELCOME_MESSAGE)
    while True:
        # Запускаем бесконечный цикл
        # Reading user input
        try:
            expression = input(f"{cfg.ARROW} ")
        except (KeyboardInterrupt, EOFError):
            # В этом блоке мы проверяем правильность данных и не прерван ли поток
            # ввода, если прерван и вылезают эти ошибки, мы завершаем выполнение программы
            raise SystemExit()

        # Custom commands support
        if expression.strip().lower() == "help":
            print(cfg.USAGE)
            continue
        if expression.strip().lower() in {"quit", "exit"}:
            raise SystemExit()

        # Expression calculation and error handling
        try:
            result = calculate(expression)
        except SyntaxError:
            # Если юзер не умеет писать, обрабатываем SyntaxError
            # Incorrect expression
            print("You entered an incorrect expression.")
            continue
        except (NameError, ValueError) as err:
            # Если юзер умеет писать, но не умеет думать (99.9% что это так)
            # обрабатываем NameError и ValueError
            # If the user tried to use an unauthorized name
            # or an invalid value in a passed function
            print(err)
            continue
        # Output the result if there were no errors
        print(f"Result: {result}")


if __name__ == "__main__":
    main()
