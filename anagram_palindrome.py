#Is the word an anagram of a palindrome? Determine if the given word is a rescrambling of
#a palindrome 

"""Is the word an anagram of a palindrome?

A palindrome is a word that reads the same forward and backwards
(eg, "racecar", "tacocat"). An anagram is a rescrambling of a word
(eg for "racecar", you could rescramble this as "arceace").

Determine if the given word is a re-scrambling of a palindrome.
The word will only contain lowercase letters, a-z.

Examples::

    >>> is_anagram_of_palindrome("a")
    True

    >>> is_anagram_of_palindrome("ab")
    False

    >>> is_anagram_of_palindrome("aab")
    True

    >>> is_anagram_of_palindrome("arceace")
    True

    >>> is_anagram_of_palindrome("arceaceb")
    False

"""

def is_anagram_of_palindrome(word):

    repeat_let  = {}

    #stores the occurances of each letter in the word in a dictionary 
    for letter in word:
        if repeat_let.has_key(letter):
            repeat_let[letter] += 1
        else:
            repeat_let[letter] = 1

    #this part of the code checks to see that only one letter occurs once, in odd length words
    count = 0
    for key in repeat_let:
        
        if repeat_let[key]==1: #if a letter occurs only once, it must be the middle letter of palindrome
            repeat_let[key]=0   #set this letters value to 0 and add one to the counter
            count += 1
        else:
            continue 

    if count >1:    #if there's more than one singly occurring letter, return False
            return False 
 
    #this part of the code checks to see if even length words can form a palindrome
    for val in repeat_let:
        if repeat_let[val]%2 == 0: #if each letter occurs an even amount of times return true
            continue
        else:
            return False 

    return True




if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED. AWESOMESAUCE!\n"

