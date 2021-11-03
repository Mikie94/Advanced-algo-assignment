import random
import time


def matchingSocks(_unMatched: list) -> list:
    _matched = []
    waiting = dict()

    for sock in _unMatched:
        if waiting.get(sock) == 0:
            _matched.append((sock, sock))
            waiting.pop(sock)
        else:
            waiting[sock] = 0

    return _matched


def createSocks(num: int) -> list:
    count = 1
    _unMatched = []

    while count < num:
        _unMatched.append(count)
        if count % 2 == 0:
            _unMatched.append(count)

        count += 1

    random.shuffle(_unMatched)

    return _unMatched


if __name__ == '__main__':
    # unMatched = createSocks(500000)

    unMatched = [3, 5, 7, 9, 3, 6, 5, 4, 1, 0, 1, 6, 9, 7, 9, 8, 3, 9, 0, 3]
    print(unMatched)

    start = time.time()

    matched = matchingSocks(unMatched)
    print(matched)

    print('Total Pairs: ', len(matched))

    end = time.time()

    print('\nTime Taken: ', end - start)

