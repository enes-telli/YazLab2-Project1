from nltk.corpus import stopwords
import testing
from collections import Counter


def find_keywords(url):

    my_dict = testing.func2(url)

    stop_words = set(stopwords.words('english'))

    delete = []

    for key, val in my_dict.items():
        if key in stop_words or key.isdigit():
            delete.append(key)

    for i in delete:
        del my_dict[i]

    return my_dict


def find_keywords_for_subdomains(result_dict, url):
    new_dict = find_keywords(url)
    for key, val in new_dict.items():
        if key in result_dict:
            result_dict[key] += new_dict[key]
        else:
            result_dict[key] = new_dict[key]
    return new_dict