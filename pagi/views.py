from django.shortcuts import render
from django.http import HttpResponse
from pagi.models import Car, Person
import random
# Create your views here.


def create_car(request):
    car = Car(
        brand=random.choice(['b1', 'b2', 'b3']),
        model=random.choice(['x3', 'x4', 'x5']),
        color=random.choice(['Yellow', 'Black', 'Red'])
    )
    car.save()
    return HttpResponse(f'New car: {car.brand}, {car.model}')


def car_list(request):
    car_obj = Car.objects.filter(brand__contains='1')
    cars = [f'{c.id}, {c.brand}, {c.model}, {c.color} | {c.owners.count()}' for c in car_obj]
    return HttpResponse('<br>'.join(cars))


def create_person(request):
    cars = Car.objects.all()
    for car in cars:
        Person.objects.create(name='I', car=car)
    return HttpResponse("OK")


def list_person(request):
    persons_obj = Person.objects.all()
    persons = [f'{p.name}, {p.car}' for p in persons_obj]
    return HttpResponse('<br>'.join(persons))
