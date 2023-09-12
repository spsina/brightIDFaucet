from learntap.validators import TaskVerificationValidator
from .models import *
from .serializers import *
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.core.cache import cache


class TagsListView(ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class MissionsListView(ListAPIView):
    queryset = (
        Mission.objects.filter(is_active=True)
        .order_by("-created_at")
        .order_by("-is_promoted")
    )
    serializer_class = MissionSerializer


class MissionRetrieveView(RetrieveAPIView):
    queryset = Mission.objects.filter(is_active=True)
    serializer_class = MissionFullSerializer
    lookup_field = "pk"


class TaskVerificationView(CreateAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        # get user data
        user_data = request.data.get("data", None)
        profile = request.user.profile
        task = Task.objects.get(pk=kwargs["pk"])

        # check if its not already verified TODO

        # check if verification mutex is not locked -> {user_id: task_id}
        is_verifying = cache.get(f"task_verification:{profile.pk}")
        if is_verifying:
            return Response(
                {"error": "Verification is already in progress"}, status=400
            )
        else:
            cache.set(f"task_verification:{profile.pk}", task.pk, 120)

        # verify
        validator = TaskVerificationValidator(
            user_profile=profile,
            task=task,
        )
        validator.is_valid(user_data)

        # update user progress TODO
        # update user XP TODO

        cache.delete(f"task_verification:{profile.pk}")
        return Response({"detail": "Task verified successfully"}, status=200)
