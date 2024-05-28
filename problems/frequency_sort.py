s = 'kabilan'
counts = dict()

for c in s:
    counts[c] = counts.get(c, 0) + 1

count_sorted = sorted(counts.items(), key=lambda c1: c1[1], reverse=True)
print(''.join(c2[0] * c2[1] for c2 in count_sorted))
