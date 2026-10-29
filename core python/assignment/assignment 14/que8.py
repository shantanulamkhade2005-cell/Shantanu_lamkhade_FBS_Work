a = ["eat", "tea", "tan", "ate", "nat", "bat"]
d = {}

for s in a:
    key = "".join(sorted(s))
    d.setdefault(key, []).append(s)

print(list(d.values()))