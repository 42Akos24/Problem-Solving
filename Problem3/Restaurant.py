class Restaurant:
    def __init__(self, name, menu):
        self.name = name
        self.menu = menu

    def __str__(self):
        return f"Az étterem neve: {self.name}"

    def __add__(self, other):
        self.menu.append(other)
