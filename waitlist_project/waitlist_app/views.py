from django.shortcuts import render
from .models import customer_collection
from django.http import HttpResponse

# Create your views here.
def reshome(request):
    return HttpResponse("hello customer")

def add_customer(request):
    records = {
        "name": "Bonnie",
        "party": 5,
        "contact": 5107598127
    }
    customer_collection.insert_one(records)
    return HttpResponse("New customer added to waitlist.")

def get_customers(request):
    customers = customer_collection.find()
    return HttpResponse(customers)
