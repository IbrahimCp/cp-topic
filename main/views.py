from django.shortcuts import render, get_object_or_404
from .models import Topic, CodeSnippet, Resource, Problem


def index(request):
    return render(request, 'index.html')


def topic_list(request):
    topics = Topic.objects.all()
    return render(request, "topic_list.html", {"topics": topics})


def topic_detail(request, pk):
    topic = get_object_or_404(Topic, pk=pk)
    problems = Problem.objects.filter(topic=topic)
    resources = Resource.objects.filter(topic=topic)
    return render(request, "topic_detail.html", {"topic": topic,
                                                 "resources": resources,
                                                 "problems": problems})


def contact(request):
    return render(request, 'contact.html')


def solution(request, pk):
    sol = get_object_or_404(CodeSnippet, problem=Problem.objects.get(pk=pk))
    return render(request, 'solution_page.html', {"codesnippet": sol})
