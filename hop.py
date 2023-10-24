def sentence_maker(phrase):
    interogatives = ("how","what","why")
    capitalized = phrase.capitalize()
    if phrase.startswith(interogatives):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)
print(sentence_maker("how are you"))

result=[]
while True:
    worde = input("say a word")
    if worde == "end":
        break
    else:
        result.append(sentence_maker(worde))


print(result)        