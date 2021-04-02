import requests
import nlptest
import testing
from anytree import Node, RenderTree
from bs4 import BeautifulSoup


subdomain_limit = 3


def find_subdomains(url):
    source = requests.get(url).text
    soup = BeautifulSoup(source, 'lxml')

    texts = []

    for tag in soup.find_all('a'):
        link = tag.get('href',None)
        if link is not None and link.startswith('http') and not link.lower().endswith(('.pdf', '.gif')) and link not in texts:
            texts.append(link)
            if len(texts) == subdomain_limit:
                break
    return texts


def print_nodes(url):
    result = ""

    array = find_subdomains(url)
    root = Node(url)

    for i in range(len(array)):
        first_depth = Node(array[i], parent=root)
        array2 = find_subdomains(array[i])
        for j in range(len(array2)):
            second_depth = Node(array2[j], parent=first_depth)

    for pre, fill, node in RenderTree(root):
        result += pre + "" + node.name + "\n"
    
    return result


def find_all_keywords(url):

    result_dict = {}
    result_text = ""

    dict1 = nlptest.find_keywords_for_subdomains(result_dict, url)
    result_text += "#" + url + ":\n" + testing.format_text(dict1, 25) + "\n\n"

    urls = find_subdomains(url)

    for i in range(len(urls)):
        dict2 = nlptest.find_keywords_for_subdomains(result_dict, urls[i])
        result_text += "##" + urls[i] + ":\n" + testing.format_text(dict2, 25) + "\n\n"
        urls2 = find_subdomains(urls[i])
        for j in range(len(urls2)):
            dict3 = nlptest.find_keywords_for_subdomains(result_dict, urls2[j])
            result_text += "###" + urls2[j] + ":\n" + testing.format_text(dict3, 25) + "\n\n"
    
    return result_dict, result_text