from multiprocessing import Process
import os


def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())


def f():
    info('function f')
    print('hello')


if __name__ == '__main__':
    info('main line')
    p = Process(target=f)
    p.start()
    p.join()
