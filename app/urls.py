from django.conf.urls import url

from .views import activation_list, profile_list


urlpatterns = [
    url(r'^activations$', activation_list, name='activation_list'),
    url(r'^profiles$', profile_list, name='profile_list'),
]
