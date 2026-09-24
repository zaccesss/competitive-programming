class StockSpanner:

    def __init__(self):
        # stored pairs of (price, span).
        # the prices in the stack stay in decreasing order.
        self.stack = []

    def next(self, price: int) -> int:

        # today's span always starts at 1.
        span = 1

        # merged all previous prices that were less than
        # or equal to today's price.
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]

        # stored today's price and its span.
        self.stack.append((price, span))

        return span