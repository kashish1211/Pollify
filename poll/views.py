from django.shortcuts import render,redirect
from .forms import PollForm
from django.contrib.auth.decorators import login_required


@login_required
def CreatePoll(request):
    if request.method == 'POST':
        form = PollForm(request.POST)
        form.instance.creator = request.user
        if form.is_valid():
            form.save()
            return redirect('poll-home')
    else:
        form = PollForm
    return render(request, 'poll/createpoll.html', {'form': form})


def home(request):
    return render(request,'poll/home.html')
