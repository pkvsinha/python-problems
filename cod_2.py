def char_index(c):
    return ord(c) - ord('A')

def reduce_ballon(chars):
    for c in "BALLOON":
        if chars[char_index(c)] <= 0:
            return False
        chars[char_index(c)] -= 1
    return True

def solution(S):
    # write your code in Python 3.6
    chars = [0] * 26
    for c in S:
        chars[char_index(c)] += 1
    pass_n = 0
    while reduce_ballon(chars):
        pass_n += 1
    return pass_n
print(solution("BAONXXOLL"))