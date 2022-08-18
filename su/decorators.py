from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import redirect


def signin_required(fun):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("signin")
        else:
            return fun(request, *args, **kwargs)

    return wrapper


def admin_permission_required(fun):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_superuser:
            return redirect("signin")
        else:
            return fun(request, *args, **kwargs)

    return wrapper


def employee_permission_required(fun):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            if not request.user.is_superuser:
                group = request.user.groups.get()
                if not group.name == "employee":
                    return redirect("signin")
                else:
                    return fun(request, *args, **kwargs)
            return fun(request, *args, **kwargs)
        else:
            return redirect("signin")
    return wrapper


from django.http import HttpResponse

# def allowed_users(allowed_roles=[]):
#     def decorator(view_func):
#         def wrapper_func(request, *args, **kwargs):
#             group = None
#             if request.users.groups.exists() | request.user.groups.is_superuser:
#                 group = request.users.groups.all()[0].name
#
#
#     return decorator
