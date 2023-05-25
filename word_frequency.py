import re


def word_frequency(paragraph):
    word_stats = {}

    for line in paragraph:
        # here we remove any punctuation marks and change case of the words and split them
        words = re.findall(r'\b\w+\b', line.lower())
        # here we use dict comprehension to count frequency of word
        word_stats.update({word: (word_stats[word] + 1 if word in word_stats else 1) for word in words})

    return word_stats


paragraph = [
    "The quick brown fox",
    "jumps over the lazy dog.",
    "The dog barks,",
    "and the fox runs away."
]

frequency = word_frequency(paragraph)
print(frequency)
