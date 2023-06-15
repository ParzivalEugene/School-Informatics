def f(n):
    r = bin(n)[2:]
    r += "01" if n % 2 == 0 else "10"
    return int(r, 2)


def main():
    for i in range(100):
        if f(i) > 73:
            print(i, f(i))
            return
        
main()