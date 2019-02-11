from django.shortcuts import render
# Create your views here.

def index(request):
    students = Student.objects.all()
    return render(request,"student/index.html",{"students":students})
    
def new(request):
    return render(request, "student/new.html")
    
def create(request):
    title = request.POST.get("title")
    content = request.POST.get("content")
    due_date = request.POST.get("due_date")
    
    # todo = Todo(title=title, content=content,due_date=due_date)
    # todo.save()
    
    Todo.objects.create(title=title, content=content, due_date=due_date)
    
    return redirect("/students")
    
def read(request, id):
    todo = Todo.objects.get(pk=id)
    
    return render(request, "student/read.html",{"todo":todo})
    
def delete(request, id):
    todo = Todo.objects.get(pk=id)
    todo.delete()
    
    return redirect("/todos")
    
def edit(request, id):
    todo = Todo.objects.get(pk=id)
    return render(request, "student/edit.html",{"todo":todo})

def update(request, id):
    todo = Todo.objects.get(pk=id)
    
    title = request.POST.get("title")
    content = request.POST.get("content")
    due_date = request.POST.get("due_date")
    
    todo.title = title
    todo.content = content
    todo.due_date = due_date
    todo.save()
    
    return redirect(f"/students/{id}/")