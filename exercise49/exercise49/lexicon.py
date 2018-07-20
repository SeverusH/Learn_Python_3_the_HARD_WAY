lexicons = {
    'east'  : 'direction',
    'south' : 'direction',
    'west'  : 'direction',
    'north' : 'direction',
    'go'    : 'verb',
    'stop'  : 'verb',
    'kill'  : 'verb',
    'eat'   : 'verb',
    'the'   : 'stop',
    'in'    : 'stop',
    'of'    : 'stop',
    'from'  : 'stop',
    'at'    : 'stop',
    'it'    : 'stop',
    'door'  : 'noun',
    'bear'  : 'noun',
    'princess': 'noun',
    'cabinet': 'noun'
}

def scan(input):
    words = input.split()
    results = []
    for word in words:

        try:
            word = int(word)
            token = 'number'
        except ValueError:
            word = word.casefold()
            token = lexicons.get(word, 'error')
        finally:
            results.append((token, word))

    return results
