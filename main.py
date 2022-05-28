# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(star, rats):

    # [assignment] Add your code here
    if (sorted(star) == sorted(rats)):
        answer = True
    else:
        answer= False
    print(answer)

no1 = input("please enter the first word: ")
no2 = input("please enter the second number: ")
find_anagram(no1, no2)

