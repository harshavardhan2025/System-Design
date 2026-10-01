from singleton_meta import SingletonMeta


class DBConnection(metaclass=SingletonMeta):

    def __init__(self):
        print("creating DB connection...")

        self.url = "localhost"
        self.username = "root"
        self.password = "secret"
        self.pool = []
