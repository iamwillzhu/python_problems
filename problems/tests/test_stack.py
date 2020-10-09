from problems.data_structures.stack import Stack

class TestStack:
    def test_stack(self) -> None:
        values = [1,2,3,4]
        stack = Stack()

        for value in values:
            stack.push(value)
            assert(stack.peek() == value)

        for value in reversed(values):
            assert(stack.pop() == value)

        assert(stack.empty())

