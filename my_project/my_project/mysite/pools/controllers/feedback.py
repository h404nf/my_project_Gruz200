from django.shortcuts import redirect, render
from pools.models import Feedback


def create(request):
    feedback = Feedback()
    feedback.email = request.POST.get("email")
    feedback.text = request.POST.get("message")
    feedback.save()

    return redirect('/')


def index(request):
    feedbacks = Feedback.objects
    content = {'feedbacks': feedbacks}

    return render(request, 'feedback.html', content)
