from django.shortcuts import render
from .models import User
from .forms import AddForm

# Create your views here.
def add(request):
    # 判断是否为 post 方法提交 
    if request.method == "POST":
        af = AddForm(request.POST, request.FILES)
        # 判断表单值是否和法
        if af.is_valid():
            name = af.cleaned_data['name']
            headimg = af.cleaned_data['headimg']
            user = User(name=name, headimg=headimg)
            user.save()
            return render(request, 'users/index.html', context={"user":user}) 
    else:
        af = AddForm()
        return render(request, 'users/add.html', context={"af":af})
