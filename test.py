import time
import random
import string


def generate_big_random_letters(filename, encoding, size):
    """
    generate big random letters/alphabets to a file
    :param filename: the filename
    :param size: the size in bytes
    :return: void
    """


    chars = ''.join([random.choice(string.ascii_letters + ' ' * 15) for i in range(size)])  # 1
    with open(filename, 'wb') as f:
        f.write(chars.encode(encoding))

    # with open(filename, 'wb') as f:
    #     for i in range(1024):
    #         chars = ''.join([random.choice(string.ascii_letters + ' ' * 15) for i in range(4*1024*1024 + 1)])
    #         f.write(chars.encode('cp1251'))
    #         print(i)
    pass


# start = time.time()
# generate_big_random_letters("50mb.txt", 50 * 1024 * 1024)
# print(time.time() - start)


def generate_file_with_diff_encodings(encodings, filename):
    foo = "привет, как дела? hi, how are you doing? Hola! Como estas?"
    f = open(filename, 'wb')
    for enc in encodings:
        f.write(foo.encode(enc))
        f.write(b' '*100)
    f.close()

#generate_file_with_diff_encodings(['cp1251', 'koi8_r', 'cp866', 'utf-8'], 'test_enc3.txt')

encodings = ['cp1251', 'koi8_r', 'cp866', 'utf-8']
sizes = range(3, 49*1024*1024+1016)

for i in range(100):
    size = random.choice(sizes)
    encoding = random.choice(encodings)
    filename = f'arch/{size}b_{encoding}.txt'
    generate_big_random_letters(filename, encoding, size)
    print(f'{i}: {size} bytes {encoding}')

