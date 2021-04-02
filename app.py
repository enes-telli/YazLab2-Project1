from flask import Flask, redirect, render_template, request, url_for
import testing
import nlptest
import similarities
import subdomains
import synonyms
from collections import Counter

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/page1', methods=['POST', 'GET'])
def page1():
    if request.method == "POST":
        url = request.form["input"]
        result = testing.func1(url, 0)
        return render_template('page1.html', text=url, counter=result, boolean=True)
    else:
        return render_template('page1.html')


@app.route('/page2', methods=['POST', 'GET'])
def page2():
    if request.method == "POST":
        url = request.form["input"]
        result = testing.format_text(nlptest.find_keywords(url), 25)
        return render_template('page2.html', text=url, counter=result, boolean=True)
    else:
        return render_template('page2.html')


@app.route('/page3', methods=['POST', 'GET'])
def page3():
    if request.method == "POST":
        
        url1 = request.form["input1"]
        url2 = request.form["input2"]
        urls = url2.split(" ")
        
        dicts = {}
        sim_list = []
        sim_texts = ""
        mydict = {}

        dict1 = nlptest.find_keywords(url1)
        result1 = testing.format_text(dict1, 25)
        result2 = ""

        for i in range(len(urls)):
            dicts[i] = nlptest.find_keywords(urls[i])
            sim_list.append(similarities.get_similarities(url1, urls[i]))
            mydict[urls[i]] = sim_list[i]
            result2 += urls[i] + ":\n" + testing.format_text(dicts[i], 25) + "\n\n"

        for w in sorted(mydict, key=mydict.get, reverse=True):
            sim_texts += w + ":\n" + str(mydict[w]) + "\n"

        for i in range(len(sim_list)):
            sim_list[i] = float(format(sim_list[i], '.5f'))
        
        return render_template('page3.html', text1=url1, text2=url2, counter1=result1, counter2=result2, scores=sim_texts, boolean=True)
    else:
        return render_template('page3.html')


@app.route('/page4', methods=['POST', 'GET'])
def page4():
    if request.method == "POST":
        
        url1 = request.form["input1"]
        url2 = request.form["input2"]
        urls = url2.split(" ")

        sim_list = []
        sim_texts = ""
        path = ""
        mydict = {}

        dict1 = nlptest.find_keywords(url1)
        result1 = testing.format_text(dict1, 25)

        dicts = {}
        result2 = ""

        for i in range(len(urls)):
            dicts[i], temp = subdomains.find_all_keywords(urls[i])
            result2 += temp
            sim_list.append(similarities.get_similarities2(dict1, dicts[i]))
            mydict[urls[i]] = sim_list[i]

        for w in sorted(mydict, key=mydict.get, reverse=True):
            sim_texts += w + ":\n" + str(mydict[w]) + "\n"

        for i in range(len(urls)):
            path += subdomains.print_nodes(urls[i]) + "\n\n" 

        return render_template('page4.html', text1=url1, text2=url2, counter1=result1, counter2=result2, scores=sim_texts, tree=path, boolean=True)
    else:
        return render_template('page4.html')


@app.route('/page5', methods=['POST', 'GET'])
def page5():
    if request.method == "POST":
        
        url1 = request.form["input1"]
        url2 = request.form["input2"]
        urls = url2.split(" ")

        sim_list = []
        sim_texts = ""
        path = ""
        relatives = ""
        mydict = {}

        dict1 = nlptest.find_keywords(url1)
        result1 = testing.format_text(dict1, 25)
        
        dicts = {}
        result2 = ""

        for i in range(len(urls)):
            dicts[i], temp = subdomains.find_all_keywords(urls[i])
            result2 += temp

            relatives += urls[i] + ":\n" + synonyms.find_synonyms2(dict1, dicts[i]) + "\n\n"

            sim_list.append(similarities.get_similarities2(dict1, dicts[i]))
            mydict[urls[i]] = sim_list[i]

        for w in sorted(mydict, key=mydict.get, reverse=True):
            sim_texts += w + ":\n" + str(mydict[w]) + "\n"

        for i in range(len(urls)):
            path += subdomains.print_nodes(urls[i]) + "\n\n"

        return render_template('page5.html', text1=url1, text2=url2, counter1=result1, counter2=result2, scores=sim_texts, tree=path, semantic=relatives, boolean=True)
    else:
        return render_template('page5.html')

if __name__ == "__main__":
    app.run(debug=True)
