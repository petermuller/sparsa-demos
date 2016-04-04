"""
demo.py

Examples of some Python features I find interesting and useful.

Peter Muller
"""

__author__ = 'Peter Muller'


class DumbNode:
    """
    A simple object for comparison against the 'Node' object
    """
    def __init__(self):
        print("DumbNode object created!")


class Node:
    """
    A more interesting object that can be printed out, initialized in several
    different ways, and be called as a function.
    """
    def __init__(self, var1=1, var2=4):
        """
        Initializes the node. Has optional parameters for setting initial values
        :param var1: First parameter
        :param var2: Second Parameter
        :return: the Node object
        """
        self.p = var1
        self.q = var2
        print("Node object created!")

    def __str__(self):
        """
        Makes a human-readable string for custom objects
        :return: the string representation of the object
        """
        return "Node object with p=%d, and q=%d" % (self.p, self.q)

    def __call__(self, arg1, arg2):
        """
        Allows the object to be called as a function
        :param arg1: A number
        :param arg2: Another number
        :return: tuple containing the existing values plus the argument values
        """
        return arg1 + self.p, arg2 + self.q


def fib_r(n=100):
    """
    Makes the Fibonacci sequence. Requires an upper bound on numbers
    :param n: Number of items in the sequence to determine
    :return: a list of the first n items in the Fibonacci sequence
    """
    num1 = 0
    num2 = 1
    counter = 2
    results = [num1, num2]
    while counter < n:
        f_sum = num1 + num2
        num1 = num2
        num2 = f_sum
        results.append(f_sum)
        counter += 1
    return results


def fib_g():
    """
    Makes the Fibonacci sequence as a generator. Does not need an upper bound/
    :return: Yields the next number of the sequence when called
    """
    num1 = 0
    yield num1
    num2 = 1
    yield num2
    while True:
        f_sum = num1 + num2
        num1 = num2
        num2 = f_sum
        yield f_sum


def add(a, b):
    """
    Simple adder
    :param a:
    :param b:
    :return:
    """
    return a+b


def subtract(a, b):
    """
    Simple subtractor
    :param a:
    :param b:
    :return:
    """
    return a-b


def multiply(a, b):
    """
    Simple multiplier
    :param a:
    :param b:
    :return:
    """
    return a*b


def divide(a, b):
    """
    Simple divider
    :param a:
    :param b:
    :return:
    """
    return a/b


def class_demos():
    """
    Demo of initializing nodes, printing nodes, and calling nodes as functions
    :return:
    """
    # Let's create some objects
    dd = DumbNode()
    a = Node()
    b = Node(9)  # var1=9, var2 gets default value
    c = Node(0, 0)  # var1=0, var2=0
    d = Node(var2=5, var1=4)
    e = Node(var2=99)  # var2=99, var1 gets default value

    # And now we can print them in plain text because of __str__
    print(dd)  # prints out memory location. Python doesn't know how to make it a string.
    print(a)  # Python can make these strings because of __str__
    print(b)
    print(c)
    print(d)
    print(a(7, 8))  # called object 'a' as a function. prints the result


def generators():
    """
    Demo of iterative function vs. generator
    :return:
    """
    count = 10
    print("First Fib")
    p = fib_r(count)  # fib_r needs upper bound because return is used
    print(type(p))  # p is a list.
    for i in range(count):
        num = p[i]
    # Next line prints the last number in sequence. To get 11th number, list
    # must be regenerated with n=11. This is memory intensive with large n.
    print num
    print

    print("Second Fib")
    q = fib_g()
    print(type(q))  # q is a generator
    for i in range(count):
        # next(q) gets next number in sequence. It's a manual way of getting a
        # value instead of using a for-in loop, which is supported
        num = next(q)
    # Next line prints the same value generated from above, with the
    # difference that more values can be generated with no additional function
    # calls or memory usage than what is already used.
    print num
    print next(q)  # The 11th number
    print

    for number in fib_g():  # example using the for-in loop with a generator
        # gets the first number in the Fibonacci sequence greater than 2016
        # requires no knowledge of upper bounds and uses minimal memory
        if number > 2016:
            print number
            break


def pointers_demo():
    """
    Demo of using function pointers and some inline list generation
    :return:
    """
    # make a list of number pairs. [(1.0, 10.0), ..., (9.0, 90.0)]
    nums = [(float(i), float(i*10)) for i in range(1, 10, 1)]
    # list of functions defined above
    ops = [add, subtract, multiply, divide]
    results = []
    for function in ops:
        # makes 4x9 matrix: 4 rows for operations, 9 cols for each pair result
        # each function is called with the number pair as a parameter
        results.append([function(tup[0], tup[1]) for tup in nums])
    for row in results:  # just prints out the matrix one row at a time
        print row  # in order: results of add, subtract, multiply, divide


if __name__ == "__main__":
    """
    Run script if called from Python
    """
    # another example of function pointers
    funcs = [class_demos, generators, pointers_demo]
    for func in funcs:  # iterate over available functions
        func()  # call each function with empty arguments
        print
        raw_input("Press Enter for next demo")