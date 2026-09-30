import threading


class Singleton:
    _instance = None
    _lock =threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)

        return cls._instance

    def __init__(self):
        if not hasattr(self, "initialized"):
            self.initialized = True
            print("Object created")


obj1 =Singleton()
obj2 =Singleton()

print(obj1 is obj2)
