import time


def timer(func):
    def wrapper(n):
        start = time.time()

        result = func(n)

        end = time.time()

        print("Result:", result)
        print("Execution time:", end - start, "seconds")

        return result

    return wrapper


@timer
def create_list(n):
    return list(range(1, n + 1))


n = int(input("Enter n: "))

create_list(n)