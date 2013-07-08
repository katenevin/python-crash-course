import random

# the simplest class you should define is a simple subclass of the base object that does nothing.
class NoOp(object):
    pass

# you can also do this, but you very rarely want to:
class Objectless:
    pass

# we can define a number of methods on a class.
class Animal(object):
    # the __init__ method is an important one. Define this to do all your setup steps.
    def __init__(self, name, legs=None, sound='quelp'):
        if legs is None:
            legs = random.choice(range(3, 101))
        self.name = name
        self.legs = legs
        self.sound = sound

    # an instance method is called on an instance of the class on which it is defined.
    def speak(self):
        # `self' is always the first argument of an instance method. This refers to the instance
        #   on which the method is called.
        return self.sound

    # a class method is called on the class itself and can be overridden by subclasses.
    @classmethod
    def can_fly(cls):
        return False

    # a static method is called using the class, but it does not get the class as an argument
    #   (the class is irrelevant to the method). All animals need love.
    @staticmethod
    def needs_love():
        return True

    # a property is a function that can be referenced as an attribute.
    @property
    def is_biped(self):
        return self.legs == 2

class Bird(Animal):
    def __init__(self, name, sound='tweet'):
        super(Bird, self).__init__(name, 2, sound)

    # because birds generally fly, we'll override the classmethod inherited from `Animal'.
    @classmethod
    def can_fly(cls):
        # in general, birds can fly. (Flightless subclasses should override this.)
        return True

class Ostrich(Bird):
    def __init__(self, name):
        super(Ostrich, self).__init__(name, None)

    @classmethod
    def can_fly(cls):
        return False

    # this is not really how you'd use this. I'm taking the joke too far.
    def __call__(self):
        raise NotImplementedError('An ostrich has no sound, so we cannot call it')


animal = Animal('Alice')
bird = Bird('Bob')
ostrich = Ostrich('Lewis')

assert Animal.can_fly() != Bird.can_fly()
assert Animal.needs_love() == Bird.needs_love()
assert Ostrich.can_fly() != Bird.can_fly()
assert ostrich.is_biped
assert bird.is_biped
assert not animal.is_biped
assert animal.sound == 'quelp'

class MathOperation(object):
    def __init__(self, op, arg1, arg2):
        self.op = op
        self.arg1 = arg1
        self.arg2 = arg2

    def __call__(self):
        if isinstance(self.arg1, MathOperation):
            arg1 = self.arg1()
        else:
            arg1 = self.arg1
        if isinstance(self.arg2, MathOperation):
            arg2 = self.arg2()
        else:
            arg2 = self.arg2
        return self.op(arg1, arg2)

from operator import add, sub

add_5_4 = MathOperation(add, 5, 4)
sub_5_4 = MathOperation(sub, 5, 4)

# here, we can create an operation tree that's computed at run-time
compound_add = MathOperation(add, add_5_4, sub_5_4)

assert add_5_4() == 5 + 4
assert sub_5_4() == 5 - 4
assert compound_add() == 10
