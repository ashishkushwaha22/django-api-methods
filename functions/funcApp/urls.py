from django.urls import path
from .views import person_list, person_detail, person_by_name, person_create, person_update, person_delete

urlpatterns = [
    path('persons/', person_list, name='person-list'),
    path('persons/<int:pk>/', person_detail, name='person-detail'),
    path('persons/<str:name>/', person_by_name, name='person-by-name'),
    path('persons/create/', person_create, name='person-create'),
    path('persons/<int:pk>/update/', person_update, name='person-update'),
    path('persons/<int:pk>/delete/', person_delete, name='person-delete'),
]
