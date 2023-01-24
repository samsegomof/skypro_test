from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated

from .models import Participant, Supplier

from .serializers import ParticipantSerializer, ParticipantCreateSerializer, SupplierSerializer, \
    SupplierCreateSerializer

from .permissions import IfUserEmployee


class ParticipantCreateView(CreateAPIView):
    """Создать участника"""
    model = Participant
    permission_classes = [IsAuthenticated, IfUserEmployee]
    serializer_class = ParticipantCreateSerializer


class ParticipantListView(ListAPIView):
    """Показать список всех участников"""
    queryset = Participant.objects.all()
    permission_classes = [IsAuthenticated, IfUserEmployee]
    pagination_class = LimitOffsetPagination
    serializer_class = ParticipantSerializer

    def get_queryset(self):
        queryset = Participant.objects.all()
        country = self.request.query_params.get('country')
        if country is not None:
            queryset = queryset.filter(contact__country__contains=country)
        return queryset


class ParticipantView(RetrieveUpdateDestroyAPIView):
    """Представление участника"""
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer
    permission_classes = [IsAuthenticated, IfUserEmployee]

    def get_queryset(self):
        return super().get_queryset()


class SupplierCreateView(CreateAPIView):
    """Создать поставщика"""
    model = Supplier
    permission_classes = [IsAuthenticated, IfUserEmployee]
    serializer_class = SupplierCreateSerializer


class SupplierListView(ListAPIView):
    """Показать список всех поставщиков"""
    queryset = Supplier.objects.all()
    permission_classes = [IsAuthenticated, IfUserEmployee]
    pagination_class = LimitOffsetPagination
    serializer_class = SupplierSerializer

    def get_queryset(self):
        return super().get_queryset()


class SupplierView(RetrieveUpdateDestroyAPIView):
    """Представление поставщика"""
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = [IsAuthenticated, IfUserEmployee]

    def get_queryset(self):
        return super().get_queryset()
