sentence = input("input statement: ")

countVowels = 0
countConsonants = 0

words = sentence.split()
numberWords = len(words)

print("number of words: ", numberWords, sep=" ")

vowels = ["A","E","I","O","U","a","e","i","o","u"]
for char in sentence:
    if char in vowels:
        countVowels = countVowels+1

print("number of vowels: ", countVowels)

consonants = ["B","C","D","F","G","H","J","K","L","M","N","P","Q","R","S","T","V","W","X","Y","Z","b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]
for char in sentence:
    if char in consonants:
        countConsonants = countConsonants+1

print("number of consonants: ", countConsonants)