from django.urls import path
from app import views



urlpatterns = [
    path('',views.index, name="index"),
    path('delete/<int:id>/',views.deleteBook, name="deleteBook"),
    path('<int:id>/',views.updateBook, name="updateBook"),
]