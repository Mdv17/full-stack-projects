from typing import Any
from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from .models import Task
# So that a user can be redirected to a new page after completion of certain task
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm


class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')
    
class RegisterPage(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        user = form.save()
        # if user is not None means that if the user was successfully created
        if user is not None:
            login(self.request, user)

        return super(RegisterPage, self).form_valid(form)
    
    # This is to make sure that if a user is registered and logged in they should not see the register or logged in even if they try to do it manually
    def get(self, *args, **kwargs): 
        if self.request.user.is_authenticated:
            return redirect('tasks')
    
        return super(RegisterPage, self).get(*args, **kwargs)



def CustomLogoutView(request):
  logout(request)

  return redirect('login')



# Create your views here.
# Now we inheriting all ListView qualities. ListView returns a template of query set of data
# Same as the ListView, the DetailView gives us detail info about an item
class TaskList(LoginRequiredMixin, ListView):
    model = Task
    # to change object_list to a more readable or user name
    context_object_name = 'tasks'

    #kwargs - key word arguments
    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count()
        
        """search_input = self.GET.get('search-area') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(title__contains=search_input)"""
        
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(
                # if you want to search as you type
                title__startswith=search_input)
        
        # This is for when you press search and the page is refreshed the searched info remains
        context['search_input'] = search_input
        
        return context

class TaskDetail(LoginRequiredMixin, DetailView):
    # This view looks for a template with the prefix of model name and task 
    model = Task
    context_object_name = 'task'
    #If you want to give the name of your liking
    template_name = 'base/task.html'

class TaskCreate(LoginRequiredMixin,CreateView):
    model = Task
    # To list all items in the field
    fields = ['title', 'description', 'complete']
    # If everything goes well redirect to tasks
    success_url = reverse_lazy('tasks')
    
    def form_valid(self, form):
        # self.request.user will make sure that its the logged in user
        # assign the current user to the user attribute
        form.instance.user = self.request.user
        # call the super method to save the object and return a response
        return super(TaskCreate, self).form_valid(form)

class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks')

    

class DeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')
