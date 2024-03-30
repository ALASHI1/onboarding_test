from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from training.models import Activity, UserActivityLog, UserActivity,do_training
from training.api.serializers import ActivitySerializer, UserActivityLogSerializer, UserActivitySerializer
from django.contrib.auth.models import User

user = User.objects.get(username='Sir Hired')
class ActivityList(APIView):
    def get(self, request):
        activities = Activity.objects.all()
        serializer = ActivitySerializer(activities, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ActivitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserActivityView(APIView):
    serializer_class = UserActivitySerializer
    def get(self, request):
        user_activities = UserActivity.objects.filter(user=user, activity__name='call center Training1', completed=True).first()
        serializer = UserActivitySerializer(user_activities)
        return Response(serializer.data)

    def post(self, request):
        training_score = do_training()
        user_activity = UserActivity.objects.filter(user=user, activity__name="call center Training1",completed=False).first()
        if user_activity:
            UserActivityLog.objects.create(user_activity=user_activity, score=training_score)
            user_activity.completed = True
            user_activity.save()
            return Response({'training_score':training_score}, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
class RetakeTraining(APIView):
    serializer_class = UserActivitySerializer
    def post(self, request):
        user_activity = UserActivity.objects.filter(user=user, activity__name='call center Training1', completed=True).first()
        if user_activity:
            user_activity.completed = False
            user_activity.save()
        return Response(status=status.HTTP_200_OK)
    
class Leaderboard(APIView):
    def get(self, request):
        user_activity_logs = UserActivityLog.objects.filter(user_activity__activity__name='call center Training1',user_activity__user__username='Sir Hired').last()
        serializer = UserActivityLogSerializer(user_activity_logs)
        return Response(serializer.data)