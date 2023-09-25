def fraction():
    while True:
        try:
            x = input("Fraction: ")
            a,b = x.split("/")
            y = int(a)
            z = int(b)
            return y/z
        except ValueError:
            pass
        except ZeroDivisionError:
            pass

def main():
    p = fraction()
    if p <= 0.01:
        print("E")
    elif p >= 0.99:
        print("F")
    else:
        print(p*100,"%")

main()