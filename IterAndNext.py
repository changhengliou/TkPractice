class Reverse:
    """Iterator for looping over a sequence backwards."""
    par = "123456789"

    def __init__(self):
        self.data = self.par
        self.index = len(self.par)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 3
        return self.data[self.index]


def Reverse2(data):
    for index in range(len(data) - 1, -1, -1):
        yield data[index]


for char in Reverse2('golf'):
    print(char)

obj = Reverse()
for i in obj:
    print(i)
