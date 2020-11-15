# Move the first letter of each word to the end of it, then add "ay" 
# to the end of the word. Leave punctuation marks untouched.

def pig_it(text): #
    words = text
    punc_indx = words.find("!")
    if punc_indx != -1:
        words = text[0:punc_indx]
    words = words.split(' ')
    words_new = []
    for word in words:
        txt = word[1:len(word)] + word[0] + "ay"
        words_new.append(txt)
    words_new = " ".join(words_new)
    if punc_indx != -1:
        words_new = words_new + '!!'
    return words_new

