from collections import Counter
import sys

# return checksum of letter frequency 2 and 3
def part_one(words):
    total_freq = [0, 0]
    for word in words:
        freq = [l for word, l in Counter(word).most_common()]
        if 2 in freq:
            total_freq[0] += 1
        if 3 in freq:
            total_freq[1] += 1
    
    return total_freq[0] * total_freq[1]

# return string of common letters
def part_two(words):
    for w1 in words:
        for w2 in words:
            diff = 0
            for i in range(0, len(w1)):
                if w1[i] is not w2[i]:
                    diff += 1

            if diff == 1:
                answer = []
                for i in range(0, len(w1)):
                    if w1[i] is w2[i]:
                        answer.append(w1[i])
                return ''.join(answer)


if __name__ == '__main__':
    data = [line.strip() for line in sys.stdin.readlines()]
    print(part_one(data))
    print(part_two(data))
