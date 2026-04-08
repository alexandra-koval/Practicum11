sentence = input()
punctuation = ".,!?;:()[]{}'\""
words = [word.strip(punctuation) for word in sentence.split()]

unique_words = list(set(words))

print(unique_words)
