from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Person
from .serializers import PersonSerializer
from django.http import Http404

# get all
@api_view(['GET'])
def person_list(request):
    persons = Person.objects.all()
    serializer = PersonSerializer(persons, many=True)
    return Response(serializer.data)

# get by id
@api_view(['GET'])
def person_detail(request, pk):
    person = Person.objects.get(pk=pk)
    serializer = PersonSerializer(person)
    return Response(serializer.data)

# get by name
@api_view(['GET'])
def person_by_name(request, name):
    try:
        person = Person.objects.get(name=name)
    except Person.DoesNotExist:
        return Response(status=404)
    
    # except Person.DoesNotExist:
        # raise Http404

    # except Person.DoesNotExist:
        # error = {'error': 'Person not found.'}
        # return Response(error, status=404)
        
    serializer = PersonSerializer(person)
    return Response(serializer.data)

@api_view(['POST'])
def person_create(request):
    serializer = PersonSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)

@api_view(['PUT'])
def person_update(request, pk):
    person = Person.objects.get(pk=pk)
    serializer = PersonSerializer(instance=person, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)

@api_view(['DELETE'])
def person_delete(request, pk):
    person = Person.objects.get(pk=pk)
    person.delete()
    return Response(status=204)

'''
# crud operations using name and age

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Person
from .serializers import PersonSerializer

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def person_detail(request, name, age):
    try:
        person = Person.objects.get(name=name, age=age)
    except Person.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = PersonSerializer(person)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    elif request.method == 'PUT':
        serializer = PersonSerializer(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        person.delete()
        return Response(status=204)
'''

