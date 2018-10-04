from memory_profiler import profile


@profile
def test():
    a = [123] * (1 << 20)
    _test = [2] * (2 << 20)
    del a
    del _test
    return 1


if __name__ == '__main__':
    test()
