class Hello:
    def __init__(self):
        pass

    @staticmethod
    def greet(a, b):
        print "I'm here...."
        result = "{} to {}".format(a, b)
        print "Result: " + result
        return result


# Hello().greet("Hello", "you!")
