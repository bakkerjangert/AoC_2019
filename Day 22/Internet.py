import re
import sympy
from collections import deque


# Stolen from https://www.geeksforgeeks.org/modular-exponentiation-python/
def modInverse(a, m):
    m0 = m
    y = 0
    x = 1
    if m == 1:
        return 0
    while a > 1:
        # q is quotient
        q = a // m
        t = m
        # m is remainder now, process
        # same as Euclid's algo
        m = a % m
        a = t
        t = y
        # Update x and y
        y = x - q * y
        x = t
    # Make x positive
    if x < 0:
        x = x + m0
    return x


read = open("input.txt").read().strip()
lines = read.strip().split("\n")
deck = deque(range(10007))
for i, line in enumerate(lines):
    if line == "deal into new stack":
        deck = deque(reversed(deck))
    else:
        num, = map(int, re.findall(r"-?\d+", line))
        if line.startswith("deal with increment "):
            arr = [-1] * len(deck)
            dealt = 0
            for j in range(0, 10 ** 9, num):
                arr[j % len(arr)] = deck.popleft()
                dealt += 1
                if dealt == len(arr):
                    break
            deck = deque(arr)
        elif line.startswith("cut "):
            deck.rotate(-num)
        else:
            assert False
print("Part1", deck.index(2019))


def getEquation(deckSize):
    curr = sympy.Symbol("x", integer=True)
    for line in reversed(lines):
        if line == "deal into new stack":
            curr = deckSize - 1 - curr
        else:
            num, = map(int, re.findall(r"-?\d+", line))
            if line.startswith("deal with increment "):
                # curr maps to curr * num % deckSize
                # So to undo the step need to find num^-1 % deckSize
                # Sympy can't handle simplifying the mods so we do it all at once in the end
                num_inv = modInverse(num, deckSize)
                curr = curr * num_inv
            elif line.startswith("cut "):
                curr += num
            else:
                assert False
    return sympy.simplify(curr % deckSize)


# Double check that this equation indeeds map my part 1 answer back to 2019
print(getEquation(10007))
x = 3939
assert (
        2019
        == (
                1315392026111080230451006564378314839352784895845592294250786878653195721500650716576276684844395334211426149137983383398423195398120918156699848671232000000000
                * x
                + 3517
        )
        % 10007
)

# Actual part 2
m = 119315717514047
print("Part2")
print(getEquation(m))
# So the above maps a*x + b, which we copy down here:
a = 2316501396575371573016884678972948408477118784181279403146479358987429110680017215948234886737944359959659404860298247604585300479030678380891857145974915848363346190901774010806108688385389566982151447255088144603207909635702542420948170594137083913460644529332734085415134701115605467400065023156837188485481208699186149052054077337449224873105350769960052638271121814070165393889413968776953196804435429662708235469836808282548171995262149191170173274077122837548442192037743662496368320149073154335633490074785580236768632505924285263685560816378241646170581426929350719949412438638592000000000
b = 81917208448684
N = 101741582076661
# Each a * x + b will undo one shuffle. Need to iterate N times
#
#   a * x +       b
# a^2 * x + a   * b +       b
# a^3 * x + a^2 * b + a   * b  +     b
# a^4 * x + a^3 * b + a^2 * b  + a * b + b
# ...
# a^N * x + (a^(N-1) + a^(N-2) + ... + 1) * b
#
# The geometric sum can also be simplified to (a^N - 1) / (a - 1). Thus:
print(
    "Part2", (pow(a, N, m) * 2020 + b * (pow(a, N, m) - 1) * modInverse(a - 1, m)) % m
)