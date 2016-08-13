import time

##Класс позволяет засекать время выполнения блока кода
#
#\code
#from timers.timer import Profiler
#
#with Profiler() as p:
#   #some Code
#\encode
class Profiler(object):
    ##Инициализируется в момент захода в нужный участок кода
    def __enter__(self):
        self._startTime = time.time()

    ##Запускается при выходе из участка кода
    def __exit__(self, type, value, traceback):
        print("Elapsed time: {:.3f} sec".format(time.time() - self._startTime))