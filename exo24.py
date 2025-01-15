def dict_char(str):
    char_counter = {}
    for char in str:
        if char in char_counter:
            char_counter[char] +=1
        else:
            char_counter[char]=1
    return char_counter


def anagrams(str1 :str,str2:str):
    if len(str1)!=len(str2):
        return False
    return dict_char(str1) == dict_char(str2)


print(anagrams("abc","der"))
print(anagrams("hii","hello"))
print(anagrams("nacb","bbb"))
