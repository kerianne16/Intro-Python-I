class Bicycle:
    def exclaim(self):
        print("I'm a bicycle")

class Specialized(Bicycle):
    pass

a_bicycle = Bicycle()

a_specialized = Specialized()


class Duck:
    def __init__(self, name, bill_description, tail_length):
        self.name = name
        self.bill = Bill(bill_description)
        self.tail = Tail(tail_length)

class Bill:
    def __init__(self, description):
        self.description = description

class Tail:
    def __init__(self, length):
        self.tail = tail 

duck = Duck("Qyackers", "wide orange", "long.")
duck.about()