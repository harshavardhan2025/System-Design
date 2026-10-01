class driver:

    company = "uber"
    n = "harsha"
    def __init__(self, name, id, Online):
        self.name = name
        self.id = id
        self.Online = Online

    def display(self):
        print(f"Driver Name: {self.name}")
        print(f"Driver ID: {self.id}")
        print(f"Driver Status: {'Online' if self.Online else 'Offline'}")

    @classmethod
    def company_name(s):
        #s.company = "Uber India"
        return s.company;

    @staticmethod
    def rangecal(a,l):
        return a*l
