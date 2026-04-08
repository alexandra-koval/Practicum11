def count_holes(word):
    """Counts the number of letters with holes in a word"""
    holes_letters = set('abdegopq')
    count = 0
    for char in word:
        if char in holes_letters:
            count += 1
    return count


def process_text(text):
    """Processes the text and returns the results"""
    words = text.split()

    total_holes = 0
    total_no_holes = 0

    words_with_holes = []

    for word in words:
        holes_count = count_holes(word)
        total_holes += holes_count
        total_no_holes += len(word) - holes_count

        if holes_count >= 2:
            words_with_holes.append(word)

    return total_holes, total_no_holes, words_with_holes


text = input()
holes, no_holes, result_words = process_text(text)

print(holes, no_holes)
print(result_words)
