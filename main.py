if __name__ == '__main__':
    n = int(input())

    simpleNumberMass = [0] * (n + 1)

    for i in range(n + 1):
        simpleNumberMass[i] = i

    simpleNumberMass[1] = 0

    i = 2
    while i <= n:
        if simpleNumberMass[i] != 0:
            j = 2 * i
            while j <= n:
                simpleNumberMass[j] = 0
                j = j + i
        i += 1

    simpleNumberMass = [i for i in simpleNumberMass if i != 0]
    print(simpleNumberMass)
