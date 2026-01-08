from django.contrib.auth.models import Group
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAdminUser

from core.serializers import GroupSerializer


@extend_schema_view(
    list=extend_schema(tags=["grupos"]),
    retrieve=extend_schema(tags=["grupos"]),
    create=extend_schema(tags=["grupos"]),
    update=extend_schema(tags=["grupos"]),
    partial_update=extend_schema(tags=["grupos"]),
    destroy=extend_schema(tags=["grupos"]),
)
class GroupViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Group.objects.all().order_by("id")
    serializer_class = GroupSerializer
    permission_classes = [IsAdminUser]
