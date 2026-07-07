class StockSpanner:

    def __init__(self):
        # I stored pairs of (price, span).
        # The prices in the stack stay in decreasing order.
        self.stack = []

    def next(self, price: int) -> int:

        # Today's span always starts at 1.
        span = 1

        # I merged all previous prices that were less than
        # or equal to today's price.
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]

        # I stored today's price and its span.
        self.stack.append((price, span))

        return span