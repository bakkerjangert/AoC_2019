with open('input.txt') as f:
    lines = f.read().splitlines()


def deal(deck):
    return deck[::-1]


def cut(deck, n):
    return deck[n:] + deck[:n]


def increment(deck, n):
    string = '0' * len(deck)
    new_deck = list(map(int, list(string)))
    index = 0
    for card in deck:
        new_deck[index] = card
        index += n
        index = index % len(deck)
    return new_deck


cards = 10007
deck = []
for i in range(cards):
    deck.append(i)

# First step = reverse --> Not in examples; also not in Puzzle?
# deck = deal(deck)

# Test
# lst = '0123456789'
# # deck = list(map(int, list(lst)))
# print(deck)

for line in lines:
    if 'incr' in line:
        val = int(line.split()[-1])
        deck = increment(deck, val)
    elif 'cut' in line:
        val = int(line.split()[-1])
        deck = cut(deck, val)
    elif 'deal' in line:
        deck = deal(deck)

answer = deck.index(2019)
print(f'The answer is {answer}')