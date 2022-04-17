"""File with mro task for oop theme"""
import random


class Transport:
    """Class initializing transport object"""

    def __init__(self, model=None):
        self.name = 'Transport'
        self.model = model
        self._gas = 0
        self.status = 'Stop'

    def fuel(self):
        """Fill the fuel for object"""
        self._gas = 100

    def __str__(self):
        return f"{self.name} - {self.model} - {self._gas} - {self.status}"


class Engine:
    """Class initializing engine object"""

    def __init__(self, size, weight):
        self.size = size
        self.weight = weight

    @classmethod
    def craft_default_engine(cls):
        """Return example of default engine object"""
        return Engine(5, 200)


class Plane(Transport, Engine):
    """Class that return ready plane object"""

    def __init__(self, version='Plane', weight=10000, size=2000):
        Transport.__init__(self)
        Engine.__init__(self, size, weight)
        self._gas = 100
        self.version = version
        self.weight = weight
        self.size = size

    def __eq__(self, other):
        if isinstance(self, Plane) == isinstance(other, Plane) \
                and self.version == other.version:
            return True
        return False

    def __ne__(self, other):
        if not isinstance(self, Plane) == isinstance(other, Plane) \
                and self.version == other.version:
            return True
        return False

    def __hash__(self):
        return hash(self.version)

    def __unicode__(self):
        return random.randint(3000, 4000)

    def fuel(self):
        """Fill the fuel for object"""
        super().fuel()
        self._gas = 1000

    def launch(self):
        """Launching Transport object , change status to work """
        self.status = "Launch"

    @classmethod
    def build_example(cls):
        """Return example of default plane object"""
        example = cls()
        example.fuel()
        return example

    @staticmethod
    def info():
        """Return price info of default plane object"""
        print("Cost $170 000")

    @property
    def owner(self):
        """Return the company of default plane object"""
        self.model = 'Aurora'
        return self.model


print(Plane().build_example())


class Car(Transport, Engine):
    """Class that return ready car object"""

    def __init__(self, version='Car', weight=2000, size=200):
        Transport.__init__(self)
        Engine.__init__(self, size, weight)
        self._gas = 100
        self.version = version
        self.weight = weight
        self.size = size

    def __eq__(self, other):
        if isinstance(self, Plane) == isinstance(other, Plane) and self.version == other.version:
            return True
        return False

    def __getitem__(self, item):
        print(self.__dict__[item])

    def __hash__(self):
        return hash(self.version)

    def __unicode__(self):
        return random.randint(1000, 2000)

    def launch(self):
        """Launching Transport object , change status to work """
        self.status = "Launch"

    def fuel(self):
        """Fill the fuel for object"""
        super().fuel()
        self._gas = 60

    @classmethod
    def build_example(cls):
        """Return default car object"""
        example = cls()
        example.fuel()
        return example

    @staticmethod
    def info():
        """Return price of car object"""
        print("Cost $10 000")

    @property
    def owner(self):
        """Return company of car object"""
        self.model = 'Zaz'
        return self.model


class Bus(Transport):
    """Class that return ready bus object"""

    def __init__(self, version='Car', weight=2000, size=200):
        Transport.__init__(self)
        self._gas = 100
        self.version = version
        self.weight = weight
        self.size = size

    def __eq__(self, other):
        if isinstance(self, Plane) == isinstance(other, Plane) \
                and self.version == other.version:
            return True
        return False

    def __ne__(self, other):
        if not isinstance(self, Plane) == isinstance(other, Plane) \
                and self.version == other.version:
            return True
        return False

    def __hash__(self):
        return hash(self.version)

    def __unicode__(self):
        return random.randint(1,1000)

    def launch(self):
        """Launching Transport object , change status to work """
        self.status = 'Launch'

    def fuel(self):
        """Fill the fuel for object"""
        super().fuel()
        self._gas = 500

    @classmethod
    def build_example(cls):
        """Fill the fuel for object"""
        example = cls()
        example.fuel()
        return example

    @staticmethod
    def info():
        """Return price of bus object"""
        print("Cost $20 000")

    @property
    def owner(self):
        """Return company of bus object"""
        self.model = 'Ikarus'
        return self.model


class Boat(Transport):
    """Class that return ready boat object"""

    def __init__(self, version='Boat', weight=4000, size=500):
        Transport.__init__(self)
        self._gas = 240
        self.version = version
        self.weight = weight
        self.size = size

    def __eq__(self, other):
        if isinstance(self, Plane) == isinstance(other, Plane) \
                and self.version == other.version:
            return True
        return False

    def __ge__(self, other):
        if self._gas > other:
            return True
        return False

    def __reversed__(self):
        return reversed(self.__dict__)

    def launch(self):
        """Launching Transport object , change status to work """
        self.status = "Launch"

    def fuel(self):
        """Fill the fuel for object"""
        super().fuel()
        self._gas = 300

    @classmethod
    def build_example(cls):
        """Return example of boat object"""
        example = cls()
        example.fuel()
        return example

    @staticmethod
    def info():
        """Return price of boat object"""
        print("Cost $50 000")

    @property
    def owner(self):
        """Return company of boat object"""
        self.model = 'Yamaha'
        return self.model
