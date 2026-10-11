n = int(input("Введіть кількість слів N: "))

words = []
for i in range(n):
    w = input("Слово " + str(i + 1) + ": ").strip()
    words.append(w)

groups = {}
for w in words:
    if w == "":
        continue
    first = w[0].lower()
    if first in groups:
        groups[first].append(w)
    else:
        groups[first] = [w]

total = 0
for letter in groups:
    if len(groups[letter]) > 1:
        print("На літеру '" + letter + "' починаються", len(groups[letter]), "слова:", ", ".join(groups[letter]))
        total += len(groups[letter])

if total == 0:
    print("Слів, що починаються з однакових символів, немає.")
else:
    print("Усього слів, які починаються з однакових символів:", total)