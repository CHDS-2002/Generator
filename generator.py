import os

os.system('COLOR B')


def all_variants(text):
    n = len(text)

    # Генерируем все возможные маски длины n
    for mask in range(1, 1 << n):
        # Формируем подпоследовательность по маске
        subsequence = ''.join([text[i] for i in range(n) if mask & (1 << i)])

        # Возвращаем подпоследовательность
        yield subsequence


# Пример использования
a = all_variants("abc")

for i in a:
    print(i)

try:
    os.system('PAUSE')
except:
    os.system('CLS')
