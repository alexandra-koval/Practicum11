words = []
counts = []
line = input()
while line != "":
    parts = line.split()
    for i in parts:
        i = i.lower()
        if i[-1].isalpha() == 0:
            i = i[:-1]
        if i not in words:
            words.append(i)
            counts.append(1)
        else:
            index = words.index(i)
            counts[index] = counts[index] + 1
    line = input()

while words != []:
    max_index = counts.index(max(counts))
    print(words.pop(max_index))
    counts.pop(max_index)
