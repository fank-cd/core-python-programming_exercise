# @Time : 2019/12/5 16:37
# @Function : 示例16-12使用try/finally块在协程终止时执行操作

from inspect import getgeneratorstate


class DemoException(Exception):
    """为这次演示定义的异常类型"""


def demo_finally():
    print("-> coroutine started")
    while True:
        try:
            x = yield
        except DemoException:
            print('***DemoException handled,Continuing')
        else:
            print('coroutine received:{!r}'.format(x))

        finally:
            print('->coroutine ending')
    raise RuntimeError("This line should never run.")


if __name__ == '__main__':
    # 激活和关闭demo_exc_handing,没有异常
    # exc_coro = demo_exc_handing()
    # next(exc_coro)
    # exc_coro.send(11)
    # exc_coro.send(22)
    # exc_coro.close()

    # 把DemoException异常传入demo_exc_handling不会导致协程终止
    # exc_coro = demo_exc_handing()
    # next(exc_coro)
    # exc_coro.send(22)
    # exc_coro.throw(DemoException)
    # print(getgeneratorstate(exc_coro))

    # 如果传入无法处理的异常，协程会终止
    exc_coro = demo_finally()
    next(exc_coro)
    exc_coro.send(11)
    exc_coro.throw(ZeroDivisionError)
    #print(getgeneratorstate(exc_coro))
