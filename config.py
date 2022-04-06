import math
import my_math
import cmath
import fractions

math_dict = {
    name: exp for name, exp in math.__dict__.items() if not name.startswith("__")
}  # это словарь

c_math = {
    name: exp for name, exp in cmath.__dict__.items() if not name.startswith("__") if not name.startswith("__") and not name.startswith("_")
}

fractions_math = {
    name: exp for name, exp in fractions.__dict__.items() if not name.startswith("__") if not name.startswith("__") and not name.startswith("_")
}

my_math_dict = {
    name: exp for name, exp in my_math.__dict__.items() if not name.startswith("__") if not name.startswith("common")
}

math_dict.update(my_math_dict)
math_dict.update(c_math)
math_dict.update(fractions_math)

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
