from colorama import Fore, init

from utils import file_io
import ciphers.caesar as caesar
import ciphers.atbash as atbash
import ciphers.playfair as playfair
import ciphers.hash_substitution as hash_cipher

CIPHERS = {
    'caesar': caesar,
    'atbash': atbash,
    'hash': hash_cipher,
    'playfair': playfair
}

init(autoreset=True)


def get_language():
    while True:
        print(Fore.LIGHTGREEN_EX + "Выберите язык текста:")
        print("1. Русский")
        print("2. Английский")
        choice = input("Ваш выбор: ").strip()
        if choice not in ('1', '2'):
            print(Fore.LIGHTRED_EX + "Неверный выбор.")
        else:
            return 'ru' if choice == '1' else 'en'


def get_mode():
    print(Fore.LIGHTGREEN_EX + "Действия:")
    print("1. Зашифровать")
    print("2. Расшифровать")
    print("0. Выход")
    choice = input("Выберите действие: ").strip()
    if choice not in ('1', '2', '0'):
        print(Fore.LIGHTRED_EX + "Неверный выбор.")
        return -1
    else:
        return int(choice)


def get_cipher_name():
    while True:
        print(Fore.LIGHTGREEN_EX + "Доступные Шифры: ")
        print("1. Цезарь")
        print("2. Обратный (Atbash)")
        print("3. Хеш-подстановка")
        print("4. Квадрат Плейфера")
        cipher_choice = input("Выберите Шифр: ").strip()
        cipher_map = {'1': 'caesar', '2': 'atbash', '3': 'hash', '4': 'playfair'}
        if cipher_choice not in cipher_map:
            print(Fore.LIGHTRED_EX + "Неверный выбор.")
            continue
        else:
            return cipher_map[cipher_choice]


def get_key(cipher_name):
    if cipher_name == 'atbash':
        return None
    while True:
        print(Fore.LIGHTGREEN_EX + "Источник ключа:")
        print("1. Ввести с консоли")
        print("2. Загрузить из файла")
        src = input("Выберите: ").strip()
        if src not in ('1', '2'):
            print(Fore.LIGHTRED_EX + "Неверный выбор.")
            continue
        if src == '1':
            if cipher_name == 'caesar':
                while True:
                    try:
                        return int(input("Введите сдвиг (целое число): "))
                    except ValueError:
                        print(Fore.LIGHTRED_EX + "Введите целое число.")
            else:
                key_str = input("Введите ключ (строка): ").strip()
                if cipher_name == 'playfair':
                    if len(key_str) > 0:
                        return key_str
                    else:
                        print(Fore.LIGHTRED_EX + "Ключ должен быть не нулевой длины.")
                        continue
                else:
                    return key_str
        else:
            filename = input("Имя файла с ключом: ").strip()
            try:
                content = file_io.read_text(filename)
                if not content.strip():
                    print(Fore.LIGHTRED_EX + "Файл пуст. Попробуйте снова.")
                    continue
                key_str = content.splitlines()[0].strip()
                if cipher_name == 'caesar':
                    try:
                        return int(key_str)
                    except ValueError:
                        print(Fore.LIGHTRED_EX + "В файле должно быть целое число. Попробуйте снова.")
                        continue
                elif cipher_name == 'playfair':
                    if len(key_str) > 0:
                        return key_str
                    else:
                        print(Fore.LIGHTRED_EX + "Ключ должен быть не нулевой длины.")
                        continue
                else:
                    return key_str
            except FileNotFoundError:
                print(Fore.LIGHTRED_EX + f"Файл {filename} не найден.")
            except Exception as e:
                print(Fore.LIGHTRED_EX + f"Ошибка чтения файла: {e}")


def get_text_source():
    while True:
        print(Fore.LIGHTGREEN_EX + "Ввод текста из:")
        print("1. Консоль")
        print("2. Файл")
        src = input("Выберите: ").strip()
        if src == '1':
            text = input("Введите текст: ")
            if len(text) != 0:
                return text
            else:
                print(Fore.LIGHTRED_EX + "Текст должен быть ненулевой длины.")
        elif src == '2':
            filename = input("Имя файла для чтения: ")
            try:
                text = file_io.read_text(filename)
                if len(text) != 0:
                    return text
                else:
                    print(Fore.LIGHTRED_EX + "Текст должен быть ненулевой длины.")
            except Exception as e:
                print(Fore.LIGHTRED_EX + f"Ошибка чтения файла: {e}")
        else:
            print(Fore.LIGHTRED_EX + "Неверный выбор.")


def print_result(result):
    while True:
        print(Fore.LIGHTGREEN_EX + "Вывод текста в:")
        print("1. Консоль")
        print("2. Файл")
        dst = input("Выберите: ").strip()
        if dst == '1':
            print("Результат: ", end='')
            print(Fore.LIGHTBLUE_EX + result + '\n')
            break
        elif dst == '2':
            filename = input("Имя файла для записи: ")
            try:
                file_io.write_text(filename, result)
                print(Fore.LIGHTBLUE_EX + "\nРезультат записан в файл.")
                print(Fore.BLUE + f"Файл: {filename}\n")
                break
            except Exception as e:
                print(Fore.LIGHTRED_EX + f"Ошибка записи файла: {e}")
        else:
            print(Fore.LIGHTRED_EX + "Неверный выбор.")


def get_result(mode, language, cipher, key, text):
    try:
        if mode == 'encode':
            if key is None:
                result = cipher.encode(text, language=language)
            else:
                result = cipher.encode(text, key, language)
        else:
            if key is None:
                result = cipher.decode(text, language=language)
            else:
                result = cipher.decode(text, key, language)
        return result
    except ValueError as e:
        print(Fore.LIGHTRED_EX + f"Ошибка: {e}")
        return None
    except Exception as e:
        print(Fore.LIGHTRED_EX + f"Непредвиденная ошибка: {e}")
        return None


def main():
    print(Fore.LIGHTWHITE_EX + '=' * 35)
    print(Fore.LIGHTWHITE_EX + "=== Универсальный кодер/декодер ===")
    print(Fore.LIGHTWHITE_EX + '=' * 35)

    try:

        mode_int = get_mode()
        if mode_int not in (1, 2):
            return mode_int
        mode = 'encode' if mode_int == 1 else 'decode'
        cipher = get_cipher_name()
        result = get_result(mode, get_language(), CIPHERS[cipher], get_key(cipher), get_text_source())
        if result is None:
            return -1
        print_result(result)

        return True
    except KeyboardInterrupt:
        print(Fore.LIGHTRED_EX + "\nПрервано пользователем.")
        return False


if __name__ == '__main__':
    while main():
        pass
