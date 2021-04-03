from django.shortcuts import render,redirect
from .forms import PollForm
from django.contrib.auth.decorators import login_required
from .models import Poll
from users.models import Profile
from django.contrib import messages
from django.http import  HttpResponseRedirect
from django.urls import reverse
import random



@login_required
def CreatePoll(request):
    if request.method == 'POST':
        form = PollForm(request.POST)
        form.instance.creator = request.user
        if form.is_valid():
            
            bg_no = random.randint(1,15)
            form.instance.image_bg =  "back"+str(bg_no)+".jpg"
            form.save()
            return redirect('poll-home')
    else:
        form = PollForm
    return render(request, 'poll/createpoll.html', {'form': form})

@login_required
def DetailedPoll(request, pk):
    if request.method == 'POST':
        poll_connected = Poll.objects.filter(id=pk)[0]
        if poll_connected.votedBy.filter(id=request.user.id).exists():
            print("You have voted once")
            messages.error(request, "You have already voted once")
            return redirect('detail-poll', pk=pk)
        else:    
            if "option1" in request.POST:
                print("Option 1")
                o1 = Poll.objects.filter(id=pk)[0].option1_count
                o1=o1+1
                Poll.objects.filter(id=pk).update(option1_count = o1)
            else:
                print("option 2")
                o2 = Poll.objects.filter(id=pk)[0].option2_count
                o2=o2+1
                Poll.objects.filter(id=pk).update(option2_count = o2)
            poll_connected.votedBy.add(request.user) 
            p_o1 = (Poll.objects.filter(id=pk)[0].option1_count/(Poll.objects.filter(id=pk)[0].option2_count+Poll.objects.filter(id=pk)[0].option1_count))*100
            p_o2 = (Poll.objects.filter(id=pk)[0].option2_count/(Poll.objects.filter(id=pk)[0].option2_count+Poll.objects.filter(id=pk)[0].option1_count))*100
            Poll.objects.filter(id=pk).update(percentage_o1 = p_o1)
            Poll.objects.filter(id=pk).update(percentage_o2 = p_o2)
            return redirect('detail-poll', pk=pk)
        
    else:   
        poll= Poll.objects.filter(id= pk)
        return render(request, 'poll/polldetail.html',{"poll":poll[0]})



def home(request):
    context ={
    "polls": Poll.objects.all()
    }
    return render(request,'poll/home.html', context)





# def votedBy(request, pk):
#     poll = get_object_or_404(Poll, id=request.POST.get("poll_id"))
#     if poll.votedBy.filter