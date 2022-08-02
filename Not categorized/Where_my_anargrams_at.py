def anagrams(word, words):
    dict_root = {}
    dict_each = {}
    result = []
    for char in word:
        if char in dict_root:
            dict_root[char] += 1
        else:
            dict_root[char] = 1
    for words_e in words:
        dict_each = {}
        for char in words_e:
            if char in dict_each:
                dict_each[char] += 1
            else:
                dict_each[char] = 1
        if dict_each == dict_root:
            result.append(words_e)
    return result
print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))
print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))