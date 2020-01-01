from collections import Counter, defaultdict, deque, OrderedDict

# Counter - Most Common
def most_common_characters(s):
    chars = Counter(sorted(s))
    for char, count in chars.most_common(3):
        print(char, count)

# DefaultDict
n, m = map(int, input().split())
d = defaultdict(list)
for i in range(n):
    d[input()].append(i + 1)
for i in range(m):
    word = input()
    if word in d:
        print(' '.join(map(str, d[word])))
    else:
        print(-1)
