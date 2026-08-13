class EvenStream(object):
    def __init__(self):
        self.current = 0

    def get_next(self):
        return self.current

    def send(self):
        self.current += 2
        return self.current


class OddStream(object):
    def __init__(self):
        self.current = -1

    def get_next(self):
        return self.current

    def send(self):
        self.current += 2
        return self.current


def print_from_stream(n, stream=EvenStream()):
    for _ in range(n):
        print(stream.send())


queries = int(input())

for _ in range(queries):
    line = input().split()
    stream_name = line[0]
    n = int(line[1])

    if stream_name == "even":
        print_from_stream(n, EvenStream())
    else:
        print_from_stream(n, OddStream())
