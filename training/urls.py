from django.urls import path
from training.views import home, take_training, reset_training, leaderboard
urlpatterns = [
    path('', home, name='home'),
    path('take_training/', take_training, name='take_training'),
    path('reset_training/', reset_training, name='reset_training'),
    path('leaderboard/', leaderboard, name='leaderboard'),
]
