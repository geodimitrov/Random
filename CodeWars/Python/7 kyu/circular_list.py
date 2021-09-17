class CircularList():
    def __init__(self, *args):
        if args:
            self.values = args
        else:
            raise Exception
        self.current_item = -1

    def next(self):
        if self.current_item + 1 == len(self.values):
            self.current_item = 0
        else:
            self.current_item += 1

        return self.values[self.current_item]

    def prev(self):
        if self.current_item - 1 < 0:
            self.current_item = len(self.values) - 1
        else:
            self.current_item -= 1

        return self.values[self.current_item]
