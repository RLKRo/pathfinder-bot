import random


def roll(message: str) -> int:
    message = message.replace(' ', '')
    queries = message.split('+')
    result = 0
    for query in queries:
        parts = query.split('d')
        if len(parts) == 1:
            result += int(parts[0])
        if len(parts) == 2:
            if parts[0] == '':
                num = 1
                dice = int(parts[1])
            else:
                num, dice = int(parts[0]), int(parts[1])
            for _ in range(num):
                result += random.randint(1, dice)

    return result
