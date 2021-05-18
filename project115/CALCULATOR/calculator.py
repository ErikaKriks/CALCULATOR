class Calculator:
    def __init__(self):
        """Setting initial result in calculator's memory to 0
        this result will be updated each time you execute a calculation function
        it is possible to reset result to 0 again

        For example:
        >>> c = Calculator()
        >>> c.reset()
        0

        """

        self.result = 0

    def add(self, n: float) -> float:
        """Add number to the result, saved in calculator's memory

        add(argument for addition)

        For example:
        since initial calculaor's memory is set to 0, you get 0 + 2 = 2
        previous result is saved in calculator's memory, so you get 2 + 3 = 5
        >>> c = Calculator()
        >>> c.add(2)
        2
        >>> c.add(3)
        5

        """

        self.result = self.result + n
        return self.result

    def subtract(self, n: float) -> float:
        """Subtact number from the result, saved in calculator's memory

        subtract(argument for subtarction)

        For example:
        since initial calculaor's memory is set to 0, you get 0 - 2 = -2
        previous result is saved in calculator's memory, so you get -2 - 3 = -5
        >>> c = Calculator()
        >>> c.subtract(2)
        -2
        >>> c.subtract(3)
        -5

        """

        self.result = self.result - n
        return self.result

    def multiply(self, n: float) -> float:
        """Multiply result, saved in calculator's memory

        multiply(argument for multiplication)

        For example:
        since initial calculaor's memory is set to 0, you add 2, so that you are able to test multiplication
        previous result is saved in calculator's memory, so you get 2 * 3 = 6
        >>> c = Calculator()
        >>> c.add(2)
        2
        >>> c.multiply(3)
        6

        """

        self.result = self.result * n
        return self.result

    def divide(self, n: float) -> float:
        """Divide result, saved in calculator's memory

        divide(argument for division)

        For example:
        since initial calculaor's memory is set to 0, you add 2, so that you are able to test division
        previous result is saved in calculator's memory, so you get 2 / 4 = 0.5
        >>> c = Calculator()
        >>> c.add(2)
        2
        >>> c.divide(4)
        0.5

        """

        try:
            self.result = self.result / n
            return self.result
        except ZeroDivisionError:
            print(ZeroDivisionError)

    def root(self, n: float) -> float:
        ''' Get the root of specified degree of  result, saved in calculator's memory

        root(degree of the root)

        For example:
        since initial calculaor's memory is set to 0, you add 4, so that you are able to test root function
        previous result is saved in calculator's memory, so you get 4 ** (1/2) = 2
        >>> c = Calculator()
        >>> c.add(4)
        4
        >>> c.root(2)
        2.0

        '''


        try:
            self.result = self.result ** (1 / n)
            return self.result
        except ZeroDivisionError or ValueError:  # it is not possible to get root of negative number if n is even
            print("is it not possible to get this result")

    def reset(self):
        ''' Reset calculator's memory to be 0

        function takes no arguments

        For example:
        since initial calculaor's memory is set to 0, you add 2
        >>> c = Calculator()
        >>> c.add(2)
        2
        >>> c.reset()
        0

        '''
        self.result = 0
        return self.result


if __name__ == "__main__":
    c = Calculator()
    print(c.add(2))
    c.reset()
    print(c.reset())
    import doctest

    print(doctest.testmod())
