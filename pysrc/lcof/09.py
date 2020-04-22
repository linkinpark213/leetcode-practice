class CQueue:

    def __init__(self):
        self.stacks = [[], []]

    def appendTail(self, value: int) -> None:
        self.stacks[0].append(value)

    def deleteHead(self) -> int:
        if len(self.stacks[0]) == 0:
            return -1
        while len(self.stacks[0]) > 1:
            self.stacks[1].append(self.stacks[0].pop())
        head = self.stacks[0].pop()
        while len(self.stacks[1]) > 0:
            self.stacks[0].append(self.stacks[1].pop())
        return head


class CommandExecutor:
    def execute(self, commands, params):
        queue = None
        for i, command in enumerate(commands):
            param = params[i]
            if command == 'CQueue':
                queue = CQueue()
                print(None)
            elif command == 'appendTail':
                print(queue.appendTail(param[0]))
            elif command == 'deleteHead':
                print(queue.deleteHead())


if __name__ == '__main__':
    executor = CommandExecutor()
    executor.execute(["CQueue", "appendTail", "deleteHead", "deleteHead"], [[], [3], [], []])
    executor.execute(["CQueue", "deleteHead", "appendTail", "appendTail", "deleteHead", "deleteHead"],
                     [[], [], [5], [2], [], []])
