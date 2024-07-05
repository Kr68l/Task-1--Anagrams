import re

def reverse_words(text):
  def reverse_and_join(match):
    return ''.join(reversed(match.group()))
  return re.sub(r"\w+", reverse_and_join, text)

if __name__ == "__main__":
  cases = ["abcd efgh", "a1bcd efg!h"]
  for case in cases:
    reversed_text = reverse_words(case)
    print(reversed_text)

