from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def main(requests):
    return HttpResponse("<h1> Hello There! <h1>")
