from retry import retry

global count
count = 0


@retry(ValueError, tries=3, delay=3)
def calc_sum(a, b):
    global count
    output = a + b
    if output > 10:
        count += 1
        print(f"Reached here {count}")
        raise ValueError("Sum is greater than 10")


calc_sum(1, 2)
