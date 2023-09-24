from django.urls import path
from . import views

urlpatterns = [
    
    #path('url-name', function_name, ref-name)
    
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    #path('post-details/<int:id>', views.post_details, name='post-details'),
    path('post-details/<slug:slug>', views.post_details, name='post_details'),
    #path('articles/<slug:slug>', views.post_details, name='post_details'),
    path('table', views.table, name="table"),
    path('export-csv', views.export_csv, name="export-csv"),
    path('contact', views.contact, name="contact"),
    path('thanks', views.thanks, name="thanks"),
    #path('search', views.search, name='search'),
    path('sign-in', views.sign_in, name='sign_in'),
    path('sign-up', views.sign_up, name='sign_up'),
    path('sign-out', views.sign_out, name='sign_out')
]
