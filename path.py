class P:
    def __init__(self, path):
        self.path = path

    def __truediv__(self, s):
        return P(f"{self.path}/{s}")

    def __repr__(self):
        return f"P({self.path})"

class Demo:

    def __init__(self, arg=[]):
        self.data = arg
        # WRONG - myList shared between all instances!

    def __init__(self, arg=None):
        self.data = arg or []
        # RIGHT - myList created when each object is!
