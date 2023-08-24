from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from .models import Blog
import csv
from .forms import ContactForm

from django.db.models import Q

# Create your views here.
def home(request):
    
    # Query all objects
    # posts = Blog.objects.all()
    
    # Query one object
    # posts = Blog.objects.get(pk=3)
    
    # Limited querying objects
    # posts = Blog.objects.all()[:3]
    
    # Reverse querying objects
    # posts = Blog.objects.order_by('-id')
    
    # Get only specific fields
    # posts = Blog.objects.values('title', 'id')
    
    # Get the first object
    # posts = Blog.objects.first()
    
    # Get the last object
    #posts = Blog.objects.last()
    
    today = datetime.now()
    
    search_post = request.GET.get('search')
    #print(search_post)
    
    if search_post:
        #posts = Blog.objects.filter(Q(title__icontains=search_post) | Q(post__icontains=search_post))
        posts = Blog.objects.filter(Q(title__icontains=search_post))
        print("Searching for", search_post)
        print("Number of items is:", posts.count())
    else:
        posts = Blog.objects.all()
    
    return render(request, "blogapp/home.html", {'today': today, 'posts': posts})

def about(request):
    
    return render(request, "blogapp/about.html")

def post_details(request, id):
    
    # Get only one post
    single_post = Blog.objects.get(pk=id)
    
    return render(request, "blogapp/post-details.html", {'single_post': single_post})

def table(request):
    
    table_obj = Blog.objects.all()
    
    return render(request, "blogapp/table.html", {'table_obj': table_obj})
    
def export_csv(request):
    # Define http entity header
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] ='attachment; filename="blog.csv"'
    
    writer = csv.writer(response)
    
    #define columns headers
    writer.writerow(['Post', 'Date Created', 'Date Updated'])
    
    #Query selected fileds to be ready saved as a csv file
    post_objs = Blog.objects.all().values_list('title', 'date_created', 'date_updated')
    
    # Finally, iterate fields, and put queried data
    # into writerow method
    for post_obj in post_objs:
        writer.writerow(post_obj)
    
    return response

def contact(request):
    form = ContactForm()
    
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            
            # return redirect('/thanks')
            return redirect('/')
        pass
    else:
        # print("This is GET")
        form = ContactForm()
    
    return render(request, 'blogapp/forms.html', {'form': form})

def thanks(request):
    return HttpResponse("Thank you so much for submitting a form")
