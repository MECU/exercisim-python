import string
import random


class Robot(object):
    names = []

    def __init__(self):
        self.name = ''
        self.reset()
        pass

    def reset(self):
        while self.names.__contains__(self.name):
            self.name = self.generate_name()
        self.names.append(self.name)
        pass

    @staticmethod
    def generate_name() -> str:
        return ''.join(random.choice(string.ascii_uppercase) for _ in range(2)) + random.randint(100, 999).__str__()
