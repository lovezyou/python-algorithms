vowels = ['a','e','i','o','u']
word_list = []

def checker(words):
    for word in words :
        for vowel in vowels :
            if vowel in word.lower() :
                word_list.append(word)
                break
            else:
                pass
    print ("\n Words that has vovels in it :",word_list)


words = input("Enter string : ").split()
checker(words)
