class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        res = 0
        if iterations == 0:
            return init
        for i in range(iterations):
            res = init - learning_rate * 2 * init
            init = res
        return round(res,5)
        # Objective function: f(x) = x^2
        # Derivative:         f'(x) = 2x
        # Update rule:        x = x - learning_rate * f'(x)
        # Round final answer to 5 decimal places
        pass
