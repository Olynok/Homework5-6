import colorama
from colorama import Fore, Back

print(help(colorama))
print("Back = colorama.ansi.AnsiBack object - Этa команда имеет цветовые коды для фона")
print("Fore = colorama.ansi.AnsiFore object - Этa команда имеет цветовые коды для текса. ")
print('Style = colorama.ansi.AnsiStyle object - Этa команда имеет стили текста')
print("Style.RESET_ALL - Сброс всех стилей")
print("Fore.RESET и Back.RESET - Сброс цвета фона и текста")
print(f"Пример: {Back.RED} {Fore.BLUE} Этот фон красный, а синий ") # я знаю что вывод в консоли не очень видно
