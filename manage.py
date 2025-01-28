from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import Group, Permission
from django.utils import timezone

# Models
class User(AbstractUser):
    pass

class Table(models.Model):
    table_number = models.IntegerField(unique=True)
    capacity = models.IntegerField()

    def __str__(self):
        return f"Table {self.table_number} (Capacity: {self.capacity})"

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    guests = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('table', 'date', 'time')

    def __str__(self):
        return f"Booking by {self.user.username} on {self.date} at {self.time}"

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

# Admin Registration
from django.contrib import admin

@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('table_number', 'capacity')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'table', 'date', 'time', 'guests')
    list_filter = ('date', 'time')

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')

### Views
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Table, Booking, MenuItem
from django.views.decorators.csrf import csrf_exempt
from django.utils.dateparse import parse_date, parse_time

@login_required
def home(request):
    menu = MenuItem.objects.all()
    return render(request, 'home.html', {'menu': menu})

@login_required
def book_table(request):
    if request.method == 'POST':
        table_id = request.POST['table_id']
        date = parse_date(request.POST['date'])
        time = parse_time(request.POST['time'])
        guests = int(request.POST['guests'])

        # Check for double bookings
        if Booking.objects.filter(table_id=table_id, date=date, time=time).exists():
            return JsonResponse({'success': False, 'message': 'Table is already booked for this time.'})

        table = Table.objects.get(id=table_id)
        if guests > table.capacity:
            return JsonResponse({'success': False, 'message': 'Guest count exceeds table capacity.'})

        booking = Booking(user=request.user, table=table, date=date, time=time, guests=guests)
        booking.save()
        return JsonResponse({'success': True, 'message': 'Booking confirmed!'})

    tables = Table.objects.all()
    return render(request, 'book_table.html', {'tables': tables})

