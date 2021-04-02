from nltk.corpus import wordnet

def find_synonyms(my_dict):

    result = ""
    
    for key,value in my_dict.items():
        my_list = []
        for word in find_word(key):
            if word in my_dict:
                my_list.append(word)
        if my_list:
            result += key + " => " + ", ".join(my_list) + "\n"
    
    return result

  
def find_synonyms2(dict1, dict2):
    
    result = ""
    
    for key,value in dict1.items():
        my_list = []
        for word in find_word(key):
            if word in dict2:
                my_list.append(word)
        if my_list:
            result += key + " => " + ", ".join(my_list) + "\n"
    
    return result


def find_word(key):
    result = []
    for syn in wordnet.synsets(key):
        for lemma in syn.lemmas():
            if key != str(lemma.name()).lower():
                result.append(lemma.name())
    
    return set(result)