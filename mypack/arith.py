def add(x, y):
    return x + y


def sub(x, y):
    return x - y

if __name__ == "__main__":
    print(f"{add(10,20)}")
    print(f"Executed as program")
else:
    print(f"Executed as module")
