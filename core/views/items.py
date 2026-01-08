from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import mixins, viewsets
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly

from core.models import Item
from core.permissions import IsReporterOrReadOnly
from core.serializers import ItemSerializer


@extend_schema_view(
    list=extend_schema(tags=["items"]),
    retrieve=extend_schema(tags=["items"]),
    create=extend_schema(tags=["items"]),
    update=extend_schema(tags=["items"]),
    partial_update=extend_schema(tags=["items"]),
    destroy=extend_schema(tags=["items"]),
)
class ItemViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Item.objects.select_related("reporter").all().order_by("-created_at")
    serializer_class = ItemSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly, IsReporterOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(reporter=self.request.user)
