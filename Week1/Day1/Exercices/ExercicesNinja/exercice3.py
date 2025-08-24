paragraph = """Life is like riding a bicycle. To keep your balance, you must keep moving.
The important thing is not to stop questioning. Curiosity has its own reason for existing."""

# Count characters
char_count = len(paragraph)

# Count sentences (split on . ? !)
import re
sentences = re.split(r'[.!?]', paragraph)
sentences = [s.strip() for s in sentences if s.strip()]
sentence_count = len(sentences)

# Count words
words = paragraph.split()
word_count = len(words)

# Unique words (case-insensitive)
unique_words = set(word.lower().strip(".,!?") for word in words)
unique_word_count = len(unique_words)

# Bonus: Non-whitespace characters
non_ws_count = len(paragraph.replace(" ", "").replace("\n", ""))

# Bonus: Avg words per sentence
avg_words = word_count / sentence_count if sentence_count > 0 else 0

# Bonus: Non-unique words
non_unique = word_count - unique_word_count

# Print results nicely
print(" Paragraph Analysis:")
print("Characters:", char_count)
print("Sentences:", sentence_count)
print("Words:", word_count)
print("Unique words:", unique_word_count)
print("Non-whitespace characters:", non_ws_count)
print("Average words per sentence:", round(avg_words, 2))
print("Non-unique words:", non_unique)
