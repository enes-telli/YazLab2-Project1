import math
import nlptest
from collections import Counter


def get_similarities(url1, url2):
    vector1 = url_to_vector(url1)
    vector2 = url_to_vector(url2)
    return get_cosine(vector1, vector2)


def get_similarities2(dict1, dict2):
    vector1 = Counter(dict1)
    vector2 = Counter(dict2)
    return get_cosine(vector1, vector2)


def url_to_vector(url):
    my_dict = nlptest.find_keywords(url)
    return Counter(my_dict)


def get_cosine(vec1, vec2):
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])

    sum1 = sum([vec1[x]**2 for x in vec1.keys()])
    sum2 = sum([vec2[x]**2 for x in vec2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator