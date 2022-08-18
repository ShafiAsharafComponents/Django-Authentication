from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DeleteView, UpdateView
from su.forms import CustomerSignUpForm, CustomerSignInForm, EmployeeCreationForm
from su.models import User as UserModel
from django.contrib.auth.models import Group


class CustomerSignUp(TemplateView):
    def get(self, request, *args, **kwargs):
        form = CustomerSignUpForm()
        context = {'form': form}
        return render(request, 'customer_sign_up.html', context)

    def post(self, request):
        context = {}
        form = CustomerSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            print('Ashaane janga jaga jaga')
            return redirect('signin')
        else:
            context['form'] = form
            print('nahinu paranja nahi')
            return render(request, 'customer_sign_up.html', context)


class CustomerSignIn(TemplateView):
    def get(self, request, *args, **kwargs):
        form = CustomerSignInForm()
        context = {"form": form}
        return render(request, 'customer_sign_in.html', context)

    def post(self, request):
        form = CustomerSignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('index')
            else:
                return render(request, 'customer_sign_in.html', {'form': form})


def signout(request):
    logout(request)
    return redirect("signin")


# -------------------------------Employee-------------------------------------------------------

class CreateEmployeeView(TemplateView):
    def get(self, request, *args, **kwargs):
        form = EmployeeCreationForm()
        context = {}
        context["form"] = form
        return render(request, "super_employee_create.html", context)

    def post(self, request):
        context = {}
        form = EmployeeCreationForm(request.POST)
        if form.is_valid():

            first_name = request.POST.get("first_name")
            last_name = request.POST.get("last_name")
            email = request.POST.get("email")
            username = request.POST.get("username")
            password1 = make_password(request.POST.get("password1"))
            password2 = request.POST.get("password2")
            employee = True
            data = UserModel(first_name=first_name, last_name=last_name, email=email, username=username,
                             password=password1,employee=employee )
            data.save()
            doctor_group, created = Group.objects.get_or_create(name='employee')
            print(data.id)
            doctor_group.user_set.add(data.id)

            print("Employee Created successfully")
            return redirect('listemployee')

        else:
            context["form"] = form
            return render(request, "super_employee_create.html", context)


class ListEmployeeView(ListView):
    model = UserModel
    template_name = "super_employee_list.html"
    context_object_name = "employees"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["employees"] = UserModel.objects.filter(employee=True)
        return context


# @method_decorator(admin_permission_required,name="dispatch")
class UpdateEmployeeView(UpdateView):
    model = UserModel
    form_class = EmployeeCreationForm
    success_url = reverse_lazy("listemployee")
    pk_url_kwarg = "id"
    template_name = "super_employee_edit.html"


# @method_decorator(admin_permission_required,name="dispatch")
class DeleteEmployeeView(DeleteView):
    model = UserModel
    template_name = "super_employee_delete.html"
    success_url = reverse_lazy("listemployee")
    pk_url_kwarg = "id"
