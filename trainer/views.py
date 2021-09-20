from django.shortcuts import render,redirect
from .forms import TrainerRegistrationForm
from .models import Trainer
from django.core.paginator import Paginator


# Create your views here.

# Create your views here.
#django http request content

def register_trainer(request):
    if request.method == "POST":
        form = TrainerRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('trainer:trainer_list')
            
        else:
            print(form.errors)    
    else:
        form = TrainerRegistrationForm()
    return render(request,'register_trainer.html',{'form':form})


def edit_trainer(request,id):
    trainer=Trainer.objects.get(id=id)
    if request.method=='POST':
        form=TrainerRegistrationForm(request.POST,instance=trainer)
        if form.is_valid():
            form.save()
    else:
        form=TrainerRegistrationForm(instance=trainer)
        return render(request,'edit_trainer.html',{'form':form})        
        
def trainer_profile(request,id):
    trainer=Trainer.objects.get(id=id)
    return render(request,'trainer_profile.html',{'trainer':trainer})

def delete_trainer(request,id):
    trainer=Trainer.objects.get(id=id)
    trainer.delete()
    return redirect('trainer:trainer_list')

def trainer_list(request):
    trainers=Trainer.objects.all()
    # return render(request,'trainer_list.html',{'trainers':trainers})

    paginator = Paginator(trainers, 7) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'trainer_list.html', {'page_obj': page_obj})