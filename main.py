import config as cfg


def calculate(expression):
    code = compile(expression, "<string>", "eval")
    # compiling in byte-code
    for name in code.co_names:
        if name not in cfg.ALLOWED_NAMES:
            raise NameError(f"The use of '{name}' is not allowed")
    return eval(code, {"__builtins__": {}}, cfg.ALLOWED_NAMES)


def main():
    print(cfg.WELCOME_MESSAGE)
    while True:
        # Reading user input
        try:
            expression = input(f"{cfg.ARROW} ")
        except (KeyboardInterrupt, EOFError):
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
            # Incorrect expression
            print("You entered an incorrect expression.")
            continue
        except (NameError, ValueError) as err:
            # If the user tried to use an unauthorized name
            # or an invalid value in a passed function
            print(err)
            continue
        # Output the result if there were no errors
        print(f"Result: {result}")


if __name__ == "__main__":
    main()
