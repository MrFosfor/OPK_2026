from colorama import Fore, init

import FinalProject.main as main
import FinalProject.ciphers.caesar as caesar
import FinalProject.ciphers.atbash as atbash
import FinalProject.ciphers.playfair as playfair
import FinalProject.ciphers.hash_substitution as hash_cipher

init(autoreset=True)


def _main_test():
    pass


def _test_cipher(encode_func, decode_func, text, key, language='en'):
    encrypted = encode_func(text, key, language)
    decrypted = decode_func(encrypted, key, language)
    assert decrypted == text, Fore.LIGHTRED_EX + ("Ошибка для текста '{text}' "
                                                  "(язык {language}, ключ {key}): '{decrypted}' != '{text}'")


def _caesar_test():
    _test_cipher(caesar.encode, caesar.decode, "Hello, World!", 3, 'en')
    _test_cipher(caesar.encode, caesar.decode, "abc", 1, 'en')
    _test_cipher(caesar.encode, caesar.decode, "xyz", 1, 'en')
    _test_cipher(caesar.encode, caesar.decode, "ABC", -1, 'en')
    _test_cipher(caesar.encode, caesar.decode, "Hello", 26, 'en')
    _test_cipher(caesar.encode, caesar.decode, "", 5, 'en')
    _test_cipher(caesar.encode, caesar.decode, "123!@#", 5, 'en')

    _test_cipher(caesar.encode, caesar.decode, "Привет, мир!", 3, 'ru')
    _test_cipher(caesar.encode, caesar.decode, "абвгдеёжзи", 1, 'ru')
    _test_cipher(caesar.encode, caesar.decode, "яяя", 1, 'ru')  # переход через конец
    _test_cipher(caesar.encode, caesar.decode, "ЯЯЯ", -1, 'ru')
    _test_cipher(caesar.encode, caesar.decode, "", 5, 'ru')

    assert caesar.encode("abc", 0, 'en') == "abc", (
            Fore.LIGHTRED_EX + "Сдвиг 0 должен возвращать исходный текст")
    assert caesar.decode("abc", 0, 'en') == "abc", (
            Fore.LIGHTRED_EX + "Сдвиг 0 при дешифровке")


def _atbash_test():
    _test_cipher(atbash.encode, atbash.decode, "Hello, World!", None, 'en')
    _test_cipher(atbash.encode, atbash.decode, "abc", None, 'en')
    _test_cipher(atbash.encode, atbash.decode, "ABC", None, 'en')
    _test_cipher(atbash.encode, atbash.decode, "", None, 'en')
    _test_cipher(atbash.encode, atbash.decode, "123!@#", None, 'en')

    _test_cipher(atbash.encode, atbash.decode, "Привет, мир!", None, 'ru')
    _test_cipher(atbash.encode, atbash.decode, "абвгдеёжзи", None, 'ru')
    _test_cipher(atbash.encode, atbash.decode, "АБВГД", None, 'ru')
    _test_cipher(atbash.encode, atbash.decode, "", None, 'ru')

    text = "Hello"
    assert atbash.encode(text, language='en') == atbash.decode(text, language='en'), (
            Fore.LIGHTRED_EX + "Для Атбаша шифрование и дешифрование должны давать одинаковый результат")


def _hash_substitution_test():
    pass


def _playfair_test():
    pass


def tests():
    _main_test()
    _caesar_test()
    _atbash_test()
    _hash_substitution_test()
    _playfair_test()


if __name__ == '__main__':
    tests()
