
def tranlate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "1"
            else:
               translation = translation + "0"
        else:
            translation = translation + letter
    return translation

print(tranlate(input("Enter a phrase: ")))

