from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='todo_home'),
    path('delete/<list_id>', views.delete, name="delete"),
    path('mark-complete/<list_id>', views.mark_complete, name="mark_complete"),
    path('mark-open/<list_id>', views.mark_open, name="mark_open"),
    path('edit-item/<list_id>', views.edit_item, name="edit_item")
]
