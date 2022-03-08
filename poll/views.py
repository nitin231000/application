from django.http import HttpResponse
from django.shortcuts import render,redirect
from poll.forms import PollForm
from poll.models import Poll

def home(request):
    polls = Poll.objects.all()
    context={
        'polls':polls
        }
    return render(request,'index.html',context)


def create(request):
    if request.method == 'POST':
       form = PollForm(request.POST)
       if form.is_valid():
           form.save()
           return redirect('home')
    else:
        form = PollForm()       
    context={
        'form': form
    }
    return render(request,'create.html',context)


def vote(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)

    if request.method == 'POST':
        selected_option = request.POST['poll']
        if selected_option == 'option1':
            poll.option_one_count += 1
        elif selected_option == 'option2':
            poll.option_two_count += 1
        elif selected_option == 'option3':
            poll.option_three_count += 1
        else :
            return HttpResponse(400, 'Invalid form')       
        
        poll.save()

        return redirect('results',poll.id)
    context={
        'poll':poll
    }
    return render(request,'vote.html',context)


def results(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    context={
        'poll':poll
    }
    return render(request,'results.html',context)    
