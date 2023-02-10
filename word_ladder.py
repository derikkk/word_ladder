#!/bin/python3


def get_text(filename):  # access dictionary
    f = open(filename, encoding='latin1')
    text = f.read()
    f.close()
    return text


def word_ladder(start_word, end_word, dictionary_file='words5.dict'):

    '''
    Returns a list satisfying the following properties:

    1. the first element is `start_word`
    2. the last element is `end_word`
    3. elements at index i and i+1 are `_adjacent`
    4. all elements are entries in the `dictionary_file` file

    For example, running the command
    ```
    word_ladder('stone','money')
    ```
    may give the output
    ```
    ['stone', 'shone', 'phone', 'phony', 'peony',
    'penny', 'benny', 'bonny', 'boney', 'money']
    ```
    but the possible outputs are not unique,
    so you may also get the output
    ```
    ['stone', 'shone', 'shote', 'shots', 'soots',
    'hoots', 'hooty', 'hooey', 'honey', 'money']
    ```
    (We cannot use doctests here because the outputs are not unique.)

    Whenever it is impossible to generate a word ladder between the two words,
    the function returns `None`.
    '''

    from collections import deque
    import copy
    dictionary_file = get_text("words5.dict")
    dictionary = dictionary_file.split("\n")
    stack = []
    stack.append(start_word)
    queue = deque()
    queue.append(stack)

    if start_word == end_word:
        return queue
    if len(end_word) > len(start_word):
        return None

    while len(queue) != 0:
        dq = queue.popleft()
        dic_copy = copy.copy(dictionary)
        for word in dic_copy:
            if _adjacent(word, dq[-1]):
                if word == end_word:
                    dq.append(word)
                    return dq
                else:
                    new_stack = copy.copy(dq)
                    new_stack.append(word)
                    queue.append(new_stack)
                    dictionary.remove(word)
    return None


def verify_word_ladder(ladder):
    
    '''
    Returns True if each entry of the input list is adjacent to its neighbors;
    otherwise returns False.

    >>> verify_word_ladder(['stone', 'shone', 'phone', 'phony'])
    True
    >>> verify_word_ladder(['stone', 'shone', 'phony'])
    False
    '''
    if ladder is None:
        return False
    if ladder == []:
        return False

    for i in range(len(ladder) - 1):
        if _adjacent(ladder[i], ladder[i + 1]):
            continue
        else:
            return False
    return True


def _adjacent(word1, word2):

    '''
    Returns True if the input words differ by only a single character;
    returns False otherwise.

    >>> _adjacent('phone','phony')
    True
    >>> _adjacent('stone','money')
    False
    '''

    if len(word1) != len(word2):
        return False
    differences = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            differences += 1
            if differences > 1:
                return False
    return differences == 1
