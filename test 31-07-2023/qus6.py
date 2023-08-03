"""6.  Write a program to find and group anagrams in a given list of words.
 Two words are called anagrams if one word can be formed by rearranging letters of another. 
 For example 'eat', 'ate' and 'tea' are anagrams. 
Assume the list given is ['eat', 'ate', 'done', 'tea', 'soup', 'node']
 then it should return [['eat', 'ate', 'tea], ['done', 'node'], ['soup']]"""
word_list = ['eat', 'ate', 'done', 'tea', 'soup', 'node']

def group_anagrams(words):
    anagram_dict = {}
    
    for word in words:
        sorted_word = ''.join(sorted(word))
        if sorted_word in anagram_dict:
            anagram_dict[sorted_word].append(word)
        else:
            anagram_dict[sorted_word] = [word]
    return list(anagram_dict.values())
    
result = group_anagrams(word_list)
print(result)
