# This problem was asked by Jane Street.

# cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

# Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(pair):
    def first(a, b):
        return a
    return pair(first)

def cdr(pair):
    def second(a, b):
        return b
    return pair(second)

# Implement car and cdr.

if __name__ == "__main__":
    my_pair = cons(3, 4)
    print(car(my_pair))
    print(cdr(my_pair))
