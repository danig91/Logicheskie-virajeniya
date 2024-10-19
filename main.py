# Напишите программу, которая проверяет, можно ли человеку голосовать на выборах.
# Условия:
# Возраст должен быть 18 лет или старше.
# Человек должен быть гражданином страны.
# Человек не должен быть дисквалифицирован (например, по причине уголовного наказания).
def write_do_not_vote():
    print("Вы не можете голосовать на выборах!")


def write_incorrect_input():
    print("Некорректный ввод")


try:
    age = int(input("Введите свой возраст: "))
    if age < 18:
        write_do_not_vote()
    elif age >= 18:
        is_citizen = str(input("Являетесь гражданином страны? (да/нет)\n"))
        if is_citizen == "нет":
            write_do_not_vote()
        elif is_citizen == "да":
            disqualified = str(input("Имеются причины для"
                                     " дисквалификации? (да/нет)\n"))
            if disqualified == "да":
                write_do_not_vote()
            elif disqualified == "нет":
                print("Можете приступить к голосованию!")
        else:
            write_incorrect_input()
    else:
        write_incorrect_input()
except ValueError:
    write_incorrect_input()
finally:
    print("Завершение программы")
