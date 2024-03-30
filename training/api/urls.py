from django.urls import path

from training.api.views import ActivityList, UserActivityView, RetakeTraining, Leaderboard

urlpatterns = [
    path('activities/', ActivityList.as_view(), name='activity_list'),
    path('user-activity/', UserActivityView.as_view(), name='user_activity'),
    path('retake-training/', RetakeTraining.as_view(), name='retake_training'),
    path('leaderboard/', Leaderboard.as_view(), name='api_leaderboard'),
]