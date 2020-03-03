def grabscrab(word, possible_words):
    return [x for x in possible_words if sorted(x) == sorted(word)]


print(grabscrab( "ortsp", ["sport", "parrot", "ports", "matey"] ))