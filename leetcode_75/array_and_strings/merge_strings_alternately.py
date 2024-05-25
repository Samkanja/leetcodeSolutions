def merge_alternately(word1: str, word2: str) -> str:
    res = ''
    l = 0
    while l < len(word1) and l < len(word2):
        res += word1[l] + word2[l]
        l += 1
    return res + (word1[l:] + word2[l:])

a = 'ab'
b = 'pqrs'
print(merge_alternately(a, b))