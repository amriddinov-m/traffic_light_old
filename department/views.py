from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from department.models import Department
from department.serializer import DepartmentListSerializer


class DepartamentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects\
        .select_related('entity', 'parent')
    serializer_class = DepartmentListSerializer
    permission_classes = [AllowAny]
    http_method_names = ['get']
