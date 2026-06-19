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
    assert decrypted == text, f"Ошибка для текста '{text}' (язык {language}, ключ {key}): '{decrypted}' != '{text}'"


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
        "Для Атбаша шифрование и дешифрование должны давать одинаковый результат")


def _hash_substitution_test():
    _test_cipher(hash_cipher.encode, hash_cipher.decode, "Hello, World!", "key", 'en')
    _test_cipher(hash_cipher.encode, hash_cipher.decode, "abc", "secret", 'en')
    _test_cipher(hash_cipher.encode, hash_cipher.decode, "xyz", "pass", 'en')
    _test_cipher(hash_cipher.encode, hash_cipher.decode, "ABC", "test", 'en')
    _test_cipher(hash_cipher.encode, hash_cipher.decode, "", "any", 'en')
    _test_cipher(hash_cipher.encode, hash_cipher.decode, "123!@#", "key", 'en')

    _test_cipher(hash_cipher.encode, hash_cipher.decode, "Привет, мир!", "ключ", 'ru')
    _test_cipher(hash_cipher.encode, hash_cipher.decode, "абвгдеёжзи", "секрет", 'ru')
    _test_cipher(hash_cipher.encode, hash_cipher.decode, "ЯЯЯ", "ключ", 'ru')
    _test_cipher(hash_cipher.encode, hash_cipher.decode, "", "ключ", 'ru')

    text = "Hello"
    key = "test"
    enc1 = hash_cipher.encode(text, key, 'en')
    enc2 = hash_cipher.encode(text, key, 'en')
    assert enc1 == enc2, "Хеш-подстановка должна быть детерминированной при одинаковом ключе"

    enc3 = hash_cipher.encode(text, "other", 'en')
    assert enc1 != enc3, "Разные ключи должны давать разные шифры (хотя бы в большинстве случаев)"


def _playfair_test():
    _test_cipher(playfair.encode, playfair.decode, "HELLO", "KEY", 'en')
    _test_cipher(playfair.encode, playfair.decode, "WORLD", "SECRET", 'en')
    _test_cipher(playfair.encode, playfair.decode, "ATTACK", "MONARCHY", 'en')
    _test_cipher(playfair.encode, playfair.decode, "TEST", "CIPHER", 'en')
    _test_cipher(playfair.encode, playfair.decode, "A", "SINGLE", 'en')
    _test_cipher(playfair.encode, playfair.decode, "AA", "DOUBLE", 'en')
    _test_cipher(playfair.encode, playfair.decode, "ABCDE", "KEY", 'en')
    _test_cipher(playfair.encode, playfair.decode, "", "ANY", 'en')

    _test_cipher(playfair.encode, playfair.decode, "ПРИВЕТ", "КЛЮЧ", 'ru')
    _test_cipher(playfair.encode, playfair.decode, "МИР", "СЕКРЕТ", 'ru')
    _test_cipher(playfair.encode, playfair.decode, "ААА", "КЛЮЧ", 'ru')
    _test_cipher(playfair.encode, playfair.decode, "АБВГД", "КЛЮЧ", 'ru')
    _test_cipher(playfair.encode, playfair.decode, "", "КЛЮЧ", 'ru')
    _test_cipher(playfair.encode, playfair.decode, "А,Б.В-Г/Д", "КЛЮЧ", 'ru')

    _test_cipher(playfair.encode, playfair.decode, "HELLO", "A", 'en')
    _test_cipher(playfair.encode, playfair.decode, "ПРИВЕТ", "Я", 'ru')

    text = "HELLO"
    key = "KEY"
    enc1 = playfair.encode(text, key, 'en')
    enc2 = playfair.encode(text, key, 'en')
    assert enc1 == enc2, "Плейфер должен быть детерминирован при одинаковом ключе"

    enc3 = playfair.encode(text, "OTHER", 'en')
    assert enc1 != enc3, "Разные ключи должны давать разные шифры (в большинстве случаев)"

    def tests():
        _main_test()
        _caesar_test()
        _atbash_test()
        _hash_substitution_test()
        _playfair_test()

    if __name__ == '__main__':
        tests()
