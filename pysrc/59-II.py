class MaxQueue:

    def __init__(self):
        self.q = []
        self.max_values = []

    def max_value(self) -> int:
        if len(self.q) == 0:
            return -1
        return self.max_values[0]

    def push_back(self, value: int) -> None:
        self.q.append(value)
        while len(self.max_values) > 0 and value > self.max_values[-1]:
            self.max_values.pop(-1)
        self.max_values.append(value)

    def pop_front(self) -> int:
        if len(self.q) == 0:
            return -1
        if self.max_values[0] == self.q[0]:
            self.max_values.pop(0)
        return self.q.pop(0)

    def print(self):
        print('Queue: ', self.q)
        print('Maximums: ', self.max_values)


if __name__ == '__main__':
    # Your MaxQueue object will be instantiated and called as such:
    obj = MaxQueue()
    cmds = ["MaxQueue", "max_value", "pop_front", "max_value", "push_back", "max_value", "pop_front", "max_value",
            "pop_front", "push_back", "pop_front", "pop_front", "pop_front", "push_back", "pop_front", "max_value",
            "pop_front", "max_value", "push_back", "push_back", "max_value", "push_back", "max_value", "max_value",
            "max_value", "push_back", "pop_front", "max_value", "push_back", "max_value", "max_value", "max_value",
            "pop_front", "push_back", "push_back", "push_back", "push_back", "pop_front", "pop_front", "max_value",
            "pop_front", "pop_front", "max_value", "push_back", "push_back", "pop_front", "push_back", "push_back",
            "push_back", "push_back", "pop_front", "max_value", "push_back", "max_value", "max_value", "pop_front",
            "max_value", "max_value", "max_value", "push_back", "pop_front", "push_back", "pop_front", "max_value",
            "max_value", "max_value", "push_back", "pop_front", "push_back", "push_back", "push_back", "pop_front",
            "max_value", "pop_front", "max_value", "max_value", "max_value", "pop_front", "push_back", "pop_front",
            "push_back", "push_back", "pop_front", "push_back", "pop_front", "push_back", "pop_front", "pop_front",
            "push_back", "pop_front", "pop_front", "pop_front", "push_back", "push_back", "max_value", "push_back",
            "pop_front", "push_back", "push_back", "pop_front"]
    params = [[], [], [], [], [46], [], [], [], [], [868], [], [], [], [525], [], [], [], [], [123], [646], [], [229],
              [], [], [], [871], [], [], [285], [], [], [], [], [45], [140], [837], [545], [], [], [], [], [], [],
              [561], [237], [], [633], [98], [806], [717], [], [], [186], [], [], [], [], [], [], [268], [], [29], [],
              [], [], [], [866], [], [239], [3], [850], [], [], [], [], [], [], [], [310], [], [674], [770], [], [525],
              [], [425], [], [], [720], [], [], [], [373], [411], [], [831], [], [765], [701], []]

    for cmd, param in zip(cmds, params):
        print(cmd, param)
        if cmd == 'MaxQueue':
            obj = MaxQueue()
            obj.print()
        elif cmd == 'max_value':
            print('Max value: ', obj.max_value())
            obj.print()
        elif cmd == 'pop_front':
            obj.pop_front()
            obj.print()
        elif cmd == 'push_back':
            obj.push_back(param[0])
            obj.print()
