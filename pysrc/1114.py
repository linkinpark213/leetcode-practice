class Foo:
    def __init__(self):
        self.oned = False
        self.twoed = False

    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.oned = True

    def second(self, printSecond: 'Callable[[], None]') -> None:
        while not self.oned:
            pass
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.twoed = True

    def third(self, printThird: 'Callable[[], None]') -> None:
        while not self.twoed:
            pass
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
