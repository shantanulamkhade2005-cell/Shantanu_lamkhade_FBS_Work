set_a = {"apple", "banana", "cherry", "mango"}
set_b = {"banana", "mango", "grapes", "kiwi"}

diff = set_a.intersection(set_b) 
for item in diff:
    set_a.discard(item)

print("Updated set_a after manual removal:", set_a)