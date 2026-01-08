from django.contrib.auth.models import Permission
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAdminUser

from core.serializers import PermissionSerializer


@extend_schema_view(
    list=extend_schema(tags=["permissoes"]),
    retrieve=extend_schema(tags=["permissoes"]),
)
class PermissionViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Permission.objects.select_related("content_type").all().order_by("id")
    serializer_class = PermissionSerializer
    permission_classes = [IsAdminUser]
