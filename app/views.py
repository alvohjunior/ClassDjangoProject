from django.http import JsonResponse

from django.shortcuts import render, redirect

from app.models import Agents

from app.serializers import AgentSerializer


# Create your views here.
def index(request):
    data = Agents.objects.all()
    context = {'data': data}
    return render(request, 'index.html', context)


def save(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        location = request.POST.get('location')
        gender = request.POST.get('gender')
        form = Agents(name=name, email=email, age=age, gender=gender)
        form.save()
        return redirect("/")
    return render(request, 'index.html')


def edit_agents(request, id):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        location = request.POST.get('location')
        gender = request.POST.get('gender')

        editForm = Agents.objects.get(id=id)
        editForm.name = name
        editForm.email = email
        editForm.age = age
        editForm.location = location
        editForm.gender = gender
        editForm.save()
        return redirect("/")
    agent = Agents.objects.get(id=id)
    context = {'agent': agent}
    return render(request, "edit.html", context)


def delete_agents(request, id):
    agent = Agents.objects.get(id=id)
    agent.delete()
    return redirect("/")


def agents_list(request):
    agents = Agents.objects.all()
    serializer = AgentSerializer(agents, many=True)
    return JsonResponse(serializer.data, safe=False)
