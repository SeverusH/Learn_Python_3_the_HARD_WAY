class MatchError(Exception):
    pass

class Sentence(object):

    def __init__(self, subject, verb, obj):
        self.subject = subject[1]
        self.verb = verb[1]
        self.object = obj[1]

def peek(word_list):
    if word_list:
        word = word_list[0]
        return word[0]
    else:
        return None

def match(word_list, expecting):
    if word_list:
        word = word_list.pop(0)

        if word[0] == expecting:
            return word
        else:
            raise MatchError("Expected a", expecting, "next")

    else:
        raise MatchError("Expected at least a word in word list")

def skip(word_list, word_type):
    while peek(word_list) == word_type:
        word_list.pop(0)

def parse_subject(word_list):
    skip(word_list, 'stop')
    word_type = peek(word_list)

    if word_type == 'verb':
        return ('noun','player')
    else:
        return match(word_list, 'noun')

def parse_verb(word_list):
    skip(word_list, 'stop')
    return match(word_list, 'verb')

def parse_object(word_list):
    skip(word_list, 'stop')
    word_type = peek(word_list)

    if word_type == 'noun':
        return match(word_list, 'noun')
    elif word_type == 'direction':
        return match(word_list, 'direction')
    else:
        raise MatchError("Expected a direction or noun next")

def parse_sentence(word_list):
    subject = parse_subject(word_list)
    verb = parse_verb(word_list)
    obj = parse_object(word_list)

    return Sentence(subject, verb, obj)
