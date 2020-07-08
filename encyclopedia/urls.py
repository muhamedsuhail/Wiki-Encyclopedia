from django.urls import path

from . import views

app_name = 'encyclopedia'

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/create_new_entry",views.addEntry,name="new_entry"),
    path("wiki/<str:title>",views.view, name="entry_page"),
    path("wiki/edit_entry/<str:title>",views.editEntry,name="edit_entry"),
    path("random",views.randomPage,name="random_entry")
]
