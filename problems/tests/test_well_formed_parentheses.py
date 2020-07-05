from problems.stacks_and_queues.well_formed_parentheses import is_well_formed

class TestIsWellFormed:
    def test_well_formed_parantheses(self) -> None:
        parentheses = "({(([]))}){}()(){{}}{}"
        assert(is_well_formed(parentheses=parentheses))

    def test_not_well_formed_parantheses(self) -> None:
        parentheses = "((()(]))"
        assert(not is_well_formed(parentheses=parentheses))

    def test_only_left_parentheses(self) -> None:
        parentheses = "{[({{[(("
        assert(not is_well_formed(parentheses=parentheses))

    def test_only_right_parentheses(self) -> None:
        parentheses = "}]]]))}]"
        assert(not is_well_formed(parentheses=parentheses))
