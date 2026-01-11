from django.contrib.auth import get_user_model
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import mixins, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from core.serializers import UserSerializer


@extend_schema_view(
    list=extend_schema(tags=["usuarios"]),
    retrieve=extend_schema(tags=["usuarios"]),
    create=extend_schema(tags=["usuarios"]),
    update=extend_schema(tags=["usuarios"]),
    partial_update=extend_schema(tags=["usuarios"]),
    destroy=extend_schema(tags=["usuarios"]),
)
class UserViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = get_user_model().objects.all().order_by("id")
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action == "create":
            return [AllowAny()]
        if self.action == "me":
            return [IsAuthenticated()]
        return [IsAdminUser()]

    def perform_create(self, serializer):
        user = serializer.save()
        if not self.request.user.is_authenticated or not self.request.user.is_staff:
            user.is_staff = False
            user.is_superuser = False
            user.save(update_fields=["is_staff", "is_superuser"])
            user.groups.clear()
            user.user_permissions.clear()

    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def me(self, request):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)
