import math
import my_math

# Это обязательно удали!
# Все что будет написано в коментарриях на английском оставь. Инфа на русском чисто для тебя.
# Чтобы лучше понять, что тут происходит почитай о словарях, множествах и о функции eval()
# Так же я написал небольшую билиотеку с функциями, которых нет в дефолтной "math" и которые нужны тебе по ТЗ

math_dict = {
    name: exp for name, exp in math.__dict__.items() if not name.startswith("__")
}  # это словарь

my_math_dict = {
    name: exp for name, exp in my_math.__dict__.items() if not name.startswith("__") if not name.startswith("common")
}

# В данном случае "name" это диначический ключ, формируемый из функций доступных в библиотеке "math",
# а все что после ":" это соответсвенные значения ключей
# вроде как это назыается мэппинг

math_dict.update(my_math_dict)

ALLOWED_NAMES = math_dict

ARROW = "->"

WELCOME_MESSAGE = f"""
Enter the mathematical expression "{ARROW}".
Use the help command for more information.
To exit, type quit or exit.
"""

USAGE = f"""
Build a mathematical expression from numbers and operators.
You can use any of the following functions and constants:

{', '.join(ALLOWED_NAMES.keys())}
"""
# а это множество
