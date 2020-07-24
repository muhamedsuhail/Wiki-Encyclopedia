from django.shortcuts import render,redirect,reverse
from django.contrib import messages
from django import forms
from . import util
from markdown2 import Markdown
import random


# Markdown to Html converter

markdowner=Markdown()


# Form classes

class QueryForm(forms.Form):
    query=forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder':'Search Encyclopedia','class':'form-control'}))

class NewEntryForm(forms.Form):
    title=forms.CharField(label="Title",widget=forms.TextInput(attrs={'placeholder':'Enter a title','autofocus':True,'class':'form-control','id':'title'}))
    content=forms.CharField(label="Content",widget=forms.Textarea(attrs={'class':'form-control'}))

# View functions

#   Homepage
def index(request):
    
    # Search box handler.

    if request.method=='POST':

        # Get form data and validate.

        form=QueryForm(request.POST)
        if form.is_valid():

            query=form.cleaned_data["query"]

            # Get the list of all encyclopedia entries that have the query as a substring.

            if not util.get_entry(query):

                entries=util.get_alike_entry(query)

                if entries==[]:

                    # If no entries are found display error page

                    return render(request,"encyclopedia/error.html",{
                    "form":QueryForm(),
                    "status":"#404",
                    "msg":"The requested entry is not found"
                    })

                return render(request, "encyclopedia/index.html", {
                    "entries": entries,
                    "form":QueryForm(),
                    "head":"Search Results"
                })

            # Display entry page if an entry with the title exits.

            else:
                return redirect('encyclopedia:entry_page',query)

    # method: GET 

    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "form":QueryForm(),
        "head":"All Pages"
    })

# Entry page

def view(request,title):

    if util.get_entry(title) is None:

        # Display error message if entry does not exist.

        return render(request,"encyclopedia/error.html",{
            "form":QueryForm(),
            "status":"#404",
            "msg":"The requested entry is not found"
        })

    context={
        "entries": markdowner.convert(util.get_entry(title)),
        "title":title,
        "form":QueryForm(),
    }

    # Render entry page passing in contents of the entry.

    return render(request,"encyclopedia/entrypage.html",context)

# New Entry Page

def addEntry(request):

    # Fetch Form contents from Post request.

    if request.method=='POST':

        form=NewEntryForm(request.POST)
        
        if form.is_valid():

            title=form.cleaned_data["title"].lower().capitalize()
            content=form.cleaned_data["content"]

            # Display error message if title already exists
            
            if title in util.list_entries(): 
                
                messages.error(request, 'Title aldready exists.')
    
                return render(request,"encyclopedia/newentry.html",{
                    "form":QueryForm(),
                    "eform":NewEntryForm()
                })
            
            else:

                # Save entry if there is no file conflict.
                
                util.save_entry(title,content)
            
            return redirect('encyclopedia:entry_page',title)
    
    # method: GET 

    return render(request,"encyclopedia/newentry.html",{
        "form":QueryForm(),
        "eform":NewEntryForm()
    })

# Edit Page 

def editEntry(request,title):

    if request.method=='POST':
        
        form=NewEntryForm(request.POST)
        
        if form.is_valid():
            
            # Get the edited contents of the entry and save it.

            title=form.cleaned_data["title"]
            content=form.cleaned_data["content"]
            util.save_entry(title,content)
            return redirect('encyclopedia:entry_page',title)
    
    # method: GET 
 
    return render(request,"encyclopedia/editentry.html",{
        "form":QueryForm(),
        "eform":NewEntryForm(),
        "title":title,
        "content":util.get_entry(title)
    })

def randomPage(request):

    # Display entries randomly. 
    
    return redirect('encyclopedia:entry_page',random.choice(util.list_entries()))


# Custom Error Handlers

def handler404(request,exception):

    return render(request,"encyclopedia/error.html",{
        "form":QueryForm(),
        "status":"#404",
        "msg":"The requested url is not found"
    })

def handler500(request):
    
    return render(request,"encyclopedia/error.html",{
        "form":QueryForm(),
        "status":"#500",
        "msg":"Internal Server Error"
    })
