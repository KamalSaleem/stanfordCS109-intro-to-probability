from numpy.random import rand


        # try 1
def main():
    print(f"1. {simulate_ber()}\n")
    print(f"2. {simulate_bin()}\n")
    print(f"3. {simulate_geo()}\n")
    print(f"4. {simulate_negBin()}\n")
    print(f"5. {simulate_poi()}\n")
    print(f"6. {simulate_exp()}\n")



def simulate_ber(p = 0.4):
    if rand() < p:
        return 1
    return 0


def simulate_bin(n = 20, p = 0.4):
    result = 0
    for i in range(n):
        r = simulate_ber(p)
        if (r == 1):
            result += 1
    return result


def simulate_geo(p = 0.03):
    result = 0
    while True:
        r = simulate_ber(p)
        result += 1
        if (r == 1):
            break
    return result


def simulate_negBin(r = 5, p = 0.03):
    sum = 0
    trials = 0
    while True:
        x = simulate_ber(p)
        trials += 1
        if x == 1:
            sum += 1
            if sum == r:
                break
    return trials


def simulate_poi(l = 3.1):
    n = 60000
    return simulate_bin(n, p = l / n)


def simulate_exp(l = 3.1):
    n = 60000
    return simulate_geo(p = l / n) / n


if __name__ == "__main__":
    main()






# try 2

def main():
    print(f"1. {simulate_ber()}\n")
    print(f"2. {simulate_bin()}\n")
    print(f"3. {simulate_geo()}\n")
    print(f"4. {simulate_negBin()}\n")
    print(f"5. {simulate_poi()}\n")
    print(f"6. {simulate_exp()}\n")


def simulate_ber(p=0.4):
    if rand() < p:
        return 1
    return 0


def simulate_bin(n = 20, p = 0.4):
    result = 0
    for _ in range(n):
        result += simulate_ber(p)
    return result


def simulate_geo(p = 0.03):
    trials = 0
    while simulate_ber(p) == 0:
        trials += 1
    return trials + 1


def simulate_negBin(r = 5, p = 0.03):
    trials = 0
    successes = 0
    while successes != r:
        if simulate_ber(p) == 1:
            successes += 1
        trials += 1
    return trials


def simulate_poi(l = 3.1, i = 60000):
    result = 0
    p = l / i
    for _ in range(i):
        result += simulate_ber(p)
    return result

def simulate_exp(l = 3.1, i = 60000):
    time_in_milisecond = 0
    p = l / i
    while simulate_ber(p) == 0:
        time_in_milisecond += 1
    return time_in_milisecond / i

           

if __name__ == "__main__":
    main()