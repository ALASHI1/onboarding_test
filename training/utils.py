from django.contrib.auth.models import User
from training.models import Activity, UserActivity, UserActivityLog

def prefill_data():
    # create user if not exists
    if not User.objects.filter(username='Sir Hired').exists():
        User.objects.create_user('Sir Hired','sirhired@mail.com',password='password')
    # create activities if not exists
    if not Activity.objects.filter(name='call center Training1').exists():
        Activity.objects.create(name='call center Training1', description='A call center Training1 Description', start_date='2024-01-01', end_date='2024-12-31')
    # Auto enroll user to activity
    user = User.objects.get(username='Sir Hired')
    activity = Activity.objects.get(name='call center Training1')
    if not UserActivity.objects.filter(user=user, activity=activity).exists():
        UserActivity.objects.create(user=user, activity=activity)
        