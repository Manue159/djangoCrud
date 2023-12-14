from django.shortcuts import render, redirect, get_object_or_404
from myapp.forms import EmployeeForm, TechnicienForm, InformaticienForm
from myapp.models import Employee, Technicien, Informaticien
from django.contrib.auth.decorators import login_required

# Create your views here.  
#employees
def employee_list(request):
    employee = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employee})


@login_required
def employee_new(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            employee = form.save(commit=False)
            employee.author = request.user
            employee.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'employee_new.html', {'form': form})


@login_required
def employee_edit(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            employee = form.save(commit=False)
            employee.author = request.user
            employee.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employee_edit.html', {'form': form})


@login_required
def employee_remove(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    employee.delete()
    return redirect('employee_list')

#techniciens
def technicien_list(request):
    technicien = Technicien.objects.all()
    return render(request, 'technicien_list.html', {'techniciens': technicien})


@login_required
def technicien_new(request):
    if request.method == "POST":
        form = TechnicienForm(request.POST)
        if form.is_valid():
            technicien = form.save(commit=False)
            technicien.author = request.user
            technicien.save()
            return redirect('technicien_list')
    else:
        form = TechnicienForm()
    return render(request, 'technicien_new.html', {'form': form})


@login_required
def technicien_edit(request, pk):
    technicien = get_object_or_404(Technicien, pk=pk)
    if request.method == "POST":
        form = TechnicienForm(request.POST, instance=technicien)
        if form.is_valid():
            technicien = form.save(commit=False)
            technicien.author = request.user
            technicien.save()
            return redirect('technicien_list')
    else:
        form = TechnicienForm(instance=technicien)
    return render(request, 'technicien_edit.html', {'form': form})


@login_required
def technicien_remove(request, pk):
    technicien = get_object_or_404(Technicien, pk=pk)
    technicien.delete()
    return redirect('technicien_list')

#informaticiens
def informaticien_list(request):
    informaticien = Informaticien.objects.all()
    return render(request, 'informaticien_list.html', {'informaticiens': informaticien})


@login_required
def informaticien_new(request):
    if request.method == "POST":
        form = InformaticienForm(request.POST)
        if form.is_valid():
            informaticien = form.save(commit=False)
            informaticien.author = request.user
            informaticien.save()
            return redirect('informaticien_list')
    else:
        form = InformaticienForm()
    return render(request, 'informaticien_new.html', {'form': form})


@login_required
def informaticien_edit(request, pk):
    informaticien = get_object_or_404(Informaticien, pk=pk)
    if request.method == "POST":
        form = InformaticienForm(request.POST, instance=informaticien)
        if form.is_valid():
            informaticien = form.save(commit=False)
            informaticien.author = request.user
            informaticien.save()
            return redirect('informaticien_list')
    else:
        form = InformaticienForm(instance=informaticien)
    return render(request, 'informaticien_edit.html', {'form': form})


@login_required
def informaticien_remove(request, pk):
    informaticien = get_object_or_404(Informaticien, pk=pk)
    informaticien.delete()
    return redirect('informaticien_list')