from Crypto.Cipher import DES
from timers.timer import Profiler

## Класс для кодирования данных алгоритмом DES
#  @warning не понятно почему ключь должен быть не длинне 8 байтов.
class EncDES:

    ##Конструктор с задание ключа шифрования
    def __init__(self, key):
        self.obj = DES.new(key, DES.MODE_ECB)

    ##Шифрование
    def encode(self, text):
        flag = 0
        while len(text) % 8 != 7:
            text += "H"
            flag += 1
        resText = str(flag) + text
        return self.obj.encrypt(resText)

    ##Расшифровка
    def decode(self, code):
        text = self.obj.decrypt(code)
        num = text[0] - 48
        tail = len(text) - num
        return text[1:tail].decode("utf-8")

    ##Тестирование
    def test(self, file_name):
        f = open(file_name, 'r')
        text = f.read()
        with Profiler() as p:
            obj = self
            code = obj.encode(text)
            res = obj.decode(code)
            if text == res:
                print("\ttest - OK")
            else:
                print("\ttest - FALSE")


