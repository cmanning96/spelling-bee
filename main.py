import sys

def list_of_words():
  words = []
  f = open("words.txt", "r")
  for line in f.readlines():
    word = line.rstrip()
    if len(word) <= 3:
      continue
    words.append(word)
  return words

def meets_criteria(word, primary_letter, secondary_letters):
  includes_primary = False
  for char in word:
    if char == primary_letter:
      includes_primary = True
      continue
    if char not in secondary_letters:
      return False
  return includes_primary


if __name__ == "__main__":
  if len(sys.argv) < 3:
    print("ERROR: Requires one primary and at least one secondary letter")
    sys.exit()
  primary_letter = sys.argv[1]
  secondary_letters = sys.argv[2:]
  all_words = list_of_words()
  valid_words = []
  for word in all_words:
    if meets_criteria(word, primary_letter, secondary_letters):
      if word not in valid_words:
        valid_words.append(word)
  for word in valid_words:
    print(word)