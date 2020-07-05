from problems.stacks_and_queues.max_stack import MaxStack

class TestMaxStack:
    def test_decreasing_values(self) -> None:
        values = [4,3,2,1]
        max_stack = MaxStack()

        assert(max_stack.empty())
        
        for value in values:
            max_stack.push(value)
            assert(max_stack.max() == 4)

        for i in range(len(values)):
            assert(max_stack.max() == 4)
            max_stack.pop()

        assert(max_stack.empty())

    def test_increasing_values(self) -> None:
        values = [1,2,3,4]
        max_stack = MaxStack()

        for value in values:
            max_stack.push(value)
            assert(max_stack.max() == value)

        assert(not max_stack.empty())

        for i in reversed(range(len(values))):
            assert(max_stack.max() == values[i])
            max_stack.pop()

        assert(max_stack.empty())
