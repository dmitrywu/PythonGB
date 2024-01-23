from csv import DictReader, DictWriter
from os.path import exists


class LenNumberError(Exception):
    def __init__(self, txt):
        self.txt = txt


class LenNameError(Exception):
    def __init__(self, txt):
        self.txt = txt


def get_info():
    is_valid_name = False
    while not is_valid_name:
        try:
            first_name = str(input("Введите имя: "))
            if len(first_name) < 2:
                raise LenNameError("Имя должно быть больше одного символа.")
            else:
                is_valid_name = True
        except LenNameError:
            print("Некорректное имя.")
    last_name = input("Введите фамилию: ")
    is_valid_number = False
    while not is_valid_number:
        try:
            phone_number = int(input("Введите номер: "))
            if len(str(phone_number)) != 11:
                raise LenNumberError("Не валидная длина!")
            else:
                is_valid_number = True
        except ValueError:
            print = "Не валидный нмер!"
            continue
        except LenNumberError as err:
            print(err)
            continue
    return [first_name, last_name, phone_number]


def create_file(file_name):
    with open(file_name, "w", encoding="utf-8") as data:
        f_writer = DictWriter(data, fieldnames=["Имя", "Фамилия", "Телефон"])
        f_writer.writeheader()


def read_file(file_name):
    with open(file_name, "r", encoding="utf-8") as data:
        f_reader = DictReader(data)
        return list(f_reader)


def write_file(file_name):
    res = read_file(file_name)
    user_data = get_info()
    for el in res:
        if el["Телефон"] == str(user_data[2]):
            print("Такой пользователь уже существует.")
            return
    obj = {"Имя": user_data[0], "Фамилия": user_data[1], "Телефон": user_data[2]}
    res.append(obj)
    with open(file_name, "w", encoding="utf-8", newline="") as data:
        f_writer = DictWriter(data, fieldnames=["Имя", "Фамилия", "Телефон"])
        f_writer.writeheader()
        f_writer.writerows(res)


def copy_line(input_file, outfile):
    input_array = read_file(input_file)
    input_array_len = len(input_array)
    row = int(
        input(f"Введите номер строки для копирования (от 1 до {input_array_len}): ")
    )
    if row < 1 or row > input_array_len:
        print("Введите корректное значение.")
    else:
        print(input_array[row - 1])
        with open(outfile, "w", encoding="utf-8", newline="") as data:
            f_writer = DictWriter(data, fieldnames=["Имя", "Фамилия", "Телефон"])
            f_writer.writeheader()
            f_writer.writerow(input_array[row - 1])


file_name = "phone.csv"
file_name_copy = "phone_copy.csv"


def main():
    while True:
        command = input("Введите команду (q, w, r, c): ").lower()
        if command == "q":
            break
        elif command == "w":
            if not exists(file_name):
                create_file(file_name)
            write_file(file_name)
        elif command == "r":
            if not exists(file_name):
                print("Файл не существует. Создайте его.")
                continue
            print(*read_file(file_name))
        elif command == "c":
            copy_line(file_name, file_name_copy)


main()
