txt1 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. God jul."
txt2 = "The quick brown fox jumps over the lazy dog. Godt nytt år."

from Levenshtein import distance

print(distance(txt1, txt2))