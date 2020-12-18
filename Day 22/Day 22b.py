with open('input.txt') as f:
    lines = f.read().splitlines()

lines.reverse()

def f(x):
    for line in lines:
        if 'incr' in line:
            val = int(line.split()[-1])
            x = reverse_increment(x, val)
        elif 'cut' in line:
            val = int(line.split()[-1])
            x = reverse_cut(x, val)
        elif 'deal' in line:
            x = reverse_deal(x)
    return x


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


def reverse_deal(i):
    return D - 1 - i


def reverse_cut(i, N):
    return (i + N + D) % D


def reverse_increment(i, N):
    return modinv(N, D) * i % D  # modinv is modular inverse

D = 119315717514047

X = 2020
Y = f(X)
Z = f(Y)
A = (Y-Z) * modinv(X-Y+D, D) % D
B = (Y-A*X) % D
print(A, B)

n = 101741582076661
print((pow(A, n, D)*X + (pow(A, n, D)-1) * modinv(A-1, D) * B) % D)
