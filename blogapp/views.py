from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from .models import Blog
import csv
from .forms import ContactForm, RegisterForm
from django.db.models import Q
from django.contrib.auth import ( 
    authenticate, login, logout
)
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist

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

# @login_required(login_url='/sign-in')
# def post_details(request, id):
    
#     # Get only one post
#     single_post = Blog.objects.get(pk=id)
    
#     return render(request, "blogapp/post-details.html", {'single_post': single_post})
    
@login_required(login_url='/sign-in')
def post_details(request, slug):
    
    # single_post = Post.objects.get(slug=slug)
    # return render(request, "blog/post-detail.html", {'single_post': single_post})
    try:
        single_post = Blog.objects.get(slug=slug)
        return render(request, "blogapp/post-details.html", {'single_post': single_post})
    except Blog.DoesNotExist:
        return render(request, "blogapp/404.html", status=404)
    
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

@login_required(login_url="/sign-in")
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

# def search(request):
#     articles_search = request.GET.get('q', None)
#     #print(f' You are searching for {articles_search}')
#     if articles_search:
#         # Do somthing
#         articles = Blog.objects.filter(Q(title__icontains=articles_search))
#         article_count = articles.count()
#         print(f"Find number of articles ... {article_count}")

#     else :
#         return redirect('/')
    
#     return render(request, 'blogapp/search.html', {
#         'articles': articles, 
#         'article_count': article_count,
#         'articles_search': articles_search
#         })

# User registration
def sign_up(request):
    form = RegisterForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('/sign-in')
    else:
        # Return blank form
        form = RegisterForm()
        # print(form)
    return render(request, 'blogapp/sign-up.html', {'form': form})

# User authentication
def sign_in(request):
    
    # Get username and password from the login form
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'Successful logged in')
            # Redirect to home page
            return redirect('/')
        else:
        # return error message
            messages.error(request, 'Invalid login')
            # return redirect('/sign-in')
    
    return render(request, 'blogapp/sign-in.html')

# Log a user out
def sign_out(request):
    logout(request)
    return redirect('/sign-in')

def page_not_found_view(request, exception):
    # To enable this one, in settings.py, please s
    return render(request, "blogapp/404.html", status=404)
