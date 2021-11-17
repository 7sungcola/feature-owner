from django.shortcuts import render

# Create your views here.

import json

from django.http     import JsonResponse
from django.views    import View

from dogs.models import Owner, Dog

class OwnersView(View):
    def post(self, request):
        data    = json.loads(request.body)
        Owner.objects.create(
            name    = data['name'],
            email   = data['email'],
            age     = data['age']
        )

        return JsonResponse({'MESSAGE':'CREATED'}, status=201)

    def get(self, request):
        owners = Owner.objects.all()
        results = []
        for owner in owners:
            for dog in Dog.objects.filter(owner_id=owner.id):
                results.append(
                    {
                        "name" : dog.name,
                        "age"  : dog.age
                    }
                )
            results.append(
                {
                    "name"   : owner.name,
                    "email"  : owner.email,
                    "age"    : owner.age
                }
            )
        return JsonResponse({'results':results}, status=200)

class DogsView(View):
    def post(self, request):
        data    = json.loads(request.body)
        Dog.objects.create(
            name     = data['name'],
            age      = data['age'],
	    owner_id_id = data['owner_id']
        )

        return JsonResponse({'MESSAGE':'CREATED'}, status=201)

    def get(self, request):
        dogs = Dog.objects.all()
        results = []
        for dog in dogs:
            results.append(
                {
                    "name"   : dog.name,
                    "age"    : dog.age,
                    "owner"  : dog.owner_id.name
                }
            )
        return JsonResponse({'results':results}, status=200)
