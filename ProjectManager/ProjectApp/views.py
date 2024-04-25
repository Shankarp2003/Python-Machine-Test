from django.shortcuts import render, redirect, get_object_or_404
from .models import Client
from django.contrib.auth.decorators import login_required
from .forms import ProjectForm
from .models import Project
from .forms import AssignUsersForm

@login_required
def register_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm()
    return render(request, 'register_client.html', {'form': form})
@login_required
def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = ProjectForm()
    return render(request, 'create_project.html', {'form': form})

@login_required
def project_detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    assigned_users = project.users.all()
    return render(request, 'project_detail.html', {'project': project, 'assigned_users': assigned_users})

def client_detail(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    projects = Project.objects.filter(client=client)
    return render(request, 'client_detail.html', {'client': client, 'projects': projects})



@login_required
def edit_client(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('client_info', client_id=client_id)
    else:
        form = ClientForm(instance=client)
    return render(request, 'edit_client.html', {'form': form})

@login_required
def delete_client(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    if request.method == 'POST':
        client.delete()
        return redirect('client_list')  # Redirect to client list after deletion
    return render(request, 'delete_client.html', {'client': client})


@login_required
def add_project(request, client_id):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.client_id = client_id
            project.save()
            return redirect('client_info', client_id=client_id)
    else:
        form = ProjectForm()
    return render(request, 'add_project.html', {'form': form})



@login_required
def assigned_projects(request):
    user = request.user
    assigned_projects = Project.objects.filter(users=user)
    return render(request, 'assigned_projects.html', {'assigned_projects': assigned_projects})




@login_required
def assign_users(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if request.method == 'POST':
        # Process form data to assign users to the project
        # You can implement this logic based on your requirements
        # For example:
        selected_users = request.POST.getlist('users')
        project.users.set(selected_users)
        return redirect('project_detail', project_id=project_id)
    else:
        # Display form to assign users
        users = User.objects.all()  # Assuming you have a User model
        return render(request, 'assign_users.html', {'project': project, 'users': users})



@login_required
def client_info(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    return render(request, 'client_info.html', {'client': client})

# views.py

@login_required
def assign_users_to_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if request.method == 'POST':
        form = AssignUsersForm(request.POST)
        if form.is_valid():
            selected_users = form.cleaned_data['users']
            project.users.set(selected_users)
            return redirect('project_detail', project_id=project_id)
    else:
        form = AssignUsersForm()
    return render(request, 'assign_users_to_project.html', {'form': form, 'project': project})
