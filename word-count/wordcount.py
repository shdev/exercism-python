def word_count(sentence):
    return_dict = {}

    words = sentence.split()

    for word in words:
        if word != '':
            if word in return_dict:
                return_dict[word] += 1
            else:
                return_dict[word] = 1

    return return_dict
