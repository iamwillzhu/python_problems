from problems.array.buy_and_sell_stock_twice import buy_and_sell_stock_twice
import pytest

class TestBuyAndSellStockTwice:
    def test_no_stocks(self) -> None:
        prices = []
        expected_result = 0

        assert(buy_and_sell_stock_twice(prices) == expected_result)

    def test_one_buy_sell(self) -> None:
        prices = [1,2,3,4,5,6,7]
        expected_result = 6

        assert(buy_and_sell_stock_twice(prices) == expected_result)

    def test_two_buy_sell(self) -> None:
        prices = [12,11,13,9,12,8,14,13,15]
        expected_result = 10

        assert(buy_and_sell_stock_twice(prices) == expected_result)


