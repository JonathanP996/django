import random, re
from django.shortcuts import render, redirect, HttpResponse
import markdown2
from . import util
lists = util.list_entries()

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def searchPAGE(request):
    if request.method == 'POST':
        term = request.POST
        term = term['q']
        searchlist = []

        for page in lists:

            if re.search(term.lower(), page.lower()):  
                searchlist.append(page)
        if len(searchlist) == 0: 
            return render(request, "encyclopedia/error.html", {
                'error_message': 'no results for your search'
            })

    return render(request, "encyclopedia/search.html", {
        'entries': searchlist
    })


def wiki(request, title):
    lists = util.list_entries()

    if title in lists:
        content = util.get_entry(title)

        return render(request, "encyclopedia/page.html", {
            "title": title,
            "content": markdown2.markdown(content)
        })
    else:
        print("Sorry we could not find what your were looking for")


def editPAGE(request, title):
    title = request.GET.get('title')
    content = util.get_entry(title)
    return render(request, "encylopedia/edit.html"), {'title':title,
    'content':content, print("edit")}  )

def addPAGE(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        print(title)
        print(content)
        if title in lists:
            return render(request, "encyclopedia/add.html", {
                'available': True
            })
        else:
            print("already exists")

    })

def GETrandomPage(request):
    randompage = util.list_entries()
    random_page = random(randompage)
    title = lists[randompage]]
    return redirect(wiki, title=title) 