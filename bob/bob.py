#
# Skeleton file for the Python "Bob" exercise.
#

ANSWER_GENERIC = "Whatever."

DATA_FOR_QUESTION = ("Sure.", lambda w: w.endswith("?"))
DATA_SHOUT = ("Whoa, chill out!", lambda w: w.isupper())
DATA_SILENCE = ("Fine. Be that way!", lambda w: len(w) == 0)

pattern_list = [
    DATA_SHOUT,
    DATA_FOR_QUESTION,
    DATA_SILENCE,
]


def hey(what):

    normalized_what = what.strip()

    for (answer, check) in pattern_list:
        if check(normalized_what):
            return answer

    return ANSWER_GENERIC
