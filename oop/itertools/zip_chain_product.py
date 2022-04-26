"""Module with reorganized functions"""


class Chain:
    """Class represent chain method"""

    def __init__(self, *args):
        self.arg = args
        self.counter = 0

    def __iter__(self):
        return self._chaining()

    def _chaining(self):
        return (i for j in self.arg for i in j)


class Zip:
    """Class represent zip method"""

    def __init__(self, *args):
        self.args = args
        self.min_lenght = min(len(l) for l in args)
        self.counter = -1

    def zipper(self):
        """Return custom zip func"""
        for i in range(self.min_lenght):
            zipper = []
            for j in self.args:
                zipper.append(j[i])
            yield tuple(zipper)

    def __iter__(self):
        return self.zipper()

    def __next__(self):
        try:
            if self.counter <= self.min_lenght:
                zipper = list(self.zipper())
                self.counter += 1
                return zipper[self.counter]
        except Exception:
            raise StopIteration


class Product:
    """Class represent product method"""

    def __init__(self, *args):
        self.args = args
        self.counter = -1

    def __iter__(self):
        return self

    def product(self):
        """Return cartesian value"""
        products = []
        for arr in self.args:
            products.append([x + [y] for x in self.args for y in arr])
        return products

    def __next__(self):
        try:
            for i in self.product():
                self.counter += 0
                return i[self.counter]
        except Exception:
            raise StopIteration

# players = ["Sachin", "Sehwag", "Gambhir", "Dravid", "Raina"]
# scores = [100, 15, 17, 28]
# # c = Chain(players, scores)
# # for i in c:
# #     print(i)
# z = Zip(players,scores)
# print(next(z))
# print(next(z))
# print(next(z))
# print(next(z))
# # p = Product(players, scores)
# # print(next(p))
# # print(next(p))
