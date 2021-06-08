V0 = 10
R = 2
a = 8
accuracy = 0.1/100

def d(n):
    if n == 0:
        return 0
    else:
        return R ** 2 / (a - d(n-1))

def q(n):
    if n == 0:
        return V0 * R
    else:
        return q(n-1) * R / (a - d(n-1))


def V(n, z):
    if z < R:
        return V0
    else:
        return q(n) / abs(z + d(n) - a/2) - q(n)/ abs(z - d(n) + a/2)

def Vtot(n, z):
    voltage = 0
    for i in range(1, n+1):
        voltage += V(i, z)
    return voltage

def calc_iter():
    i = 1
    iters = []
    while True:
        iters.append(Vtot(i, R))
        if i >= 2:
            err = abs(iters[i-1] - iters[i-2]) / abs(iters[i-2])
            if err < accuracy:
                return i
        i += 1

if __name__ == '__main__':
    print(calc_iter())






