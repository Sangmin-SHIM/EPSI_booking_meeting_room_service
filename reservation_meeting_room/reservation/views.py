from django.shortcuts import render
from .models import Reservation
from .forms import ReservationForm
from django.contrib import messages


# Create your views here.
def create_reservation(request):
    if request.method == "POST":
        reservation_form = ReservationForm(request.POST)
        reservation_form.user = request.user
        if reservation_form.is_valid():
            reservation_form.save()
            messages.success(request, "Reservation created successfully")

    reservation_form = ReservationForm()
    reservations = Reservation.objects.all()

    return render(
        request=request,
        template_name="view_reservation.html",
        context={"reservation_form": reservation_form, "reservations": reservations},
    )
