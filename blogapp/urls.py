from django.urls import path
from . import views

urlpatterns = [
    
    #path('url-name', function_name)
    
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('post-details/<int:id>', views.post_details, name='post-details'),
    path('table', views.table, name="table"),
    path('export-csv', views.export_csv, name="export-csv"),
    path('contact', views.contact, name="contact"),
    path('thanks', views.thanks, name="thanks")
]
