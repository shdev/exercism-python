def detect_anagrams(the_word, word_list):
    return [word for word in word_list
            if ''.join(sorted(the_word.lower())) ==
               ''.join(sorted(word.lower())) and
               the_word.lower() != word.lower()]
