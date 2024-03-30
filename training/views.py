from django.shortcuts import render, redirect
from training.models import do_training, UserActivityLog, UserActivity
from training.utils import prefill_data
from django.contrib.auth.models import User


# Create your views here.
prefill_data()
user = User.objects.get(username='Sir Hired')
def home(request):
    # creates dummy data if not exists
    user_activity = UserActivity.objects.filter(user=user, activity__name='call center Training1', completed=True).first()
    if user_activity:
        return render(request, 'training/home.html', {'CourseDone': True})
    return render(request, 'training/home.html', {'CourseDone': False})

def take_training(request):
    training_score = do_training()
    user_activity = UserActivity.objects.filter(user=user, activity__name='call center Training1', completed=False).first()
    if user_activity:
        UserActivityLog.objects.create(user_activity=user_activity, score=training_score)
        user_activity.completed = True
        user_activity.save()
        return render(request, 'training/score.html', {'TrainingScore': training_score, 'CourseDone': True})
    return redirect('home')

def reset_training(request):
    user_activity = UserActivity.objects.filter(user=user, activity__name='call center Training1', completed=True).first()
    if user_activity:
        user_activity.completed = False
        user_activity.save()
    return redirect('home')
   
def leaderboard(request):
    user_activity_logs = UserActivityLog.objects.filter(user_activity__activity__name='call center Training1',user_activity__user__username='Sir Hired').last()
    return render(request, 'training/leaderboard.html', {'score': user_activity_logs.score, 'username': user_activity_logs.user_activity.user.username})

