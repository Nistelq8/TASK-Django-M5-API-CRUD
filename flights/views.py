from datetime import datetime

from rest_framework.generics import ListAPIView,UpdateAPIView,DestroyAPIView
from rest_framework.generics import RetrieveAPIView
from .models import Booking, Flight
from .serializers import BookingDetailSerialzer, BookingListSerializer, FlightListSerializer, BookingUpdateSerializer


class FlightListView(ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightListSerializer


class BookingListView(ListAPIView):
    queryset = Booking.objects.filter(date__gte=datetime.today())
    serializer_class = BookingListSerializer

class BookingDetailedView(RetrieveAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingDetailSerialzer
    lookup_field = "id"
    lookup_url_kwarg = "booking_id"
    
class BookingUpdateView(UpdateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingUpdateSerializer
    lookup_field = "id"
    lookup_url_kwarg = "booking_id"
    
class BookingDeleteView(DestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingDetailedView
    lookup_field = "id"
    lookup_url_kwarg = "booking_id"