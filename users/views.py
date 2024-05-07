from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView
from django.shortcuts import redirect, render

from users.forms import UserRegisterForm, UserProfileForm
from users.models import User
from users.services import create_payment_session


class UserLoginView(LoginView):
    """Обработка входа пользователя"""
    template_name = 'users/login.html'


class UserLogoutView(View):
    """Обработка выхода пользователя"""

    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('blog:home')


class UserRegisterView(CreateView):
    """Регистрация пользователя"""
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'

    def form_valid(self, form):
        """Валидная форма регистрации пользователя"""
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password1'])
        user.save()
        return redirect('users:verify_message')

    def get_success_url(self):
        """Получение URL для перенаправления после успешной регистрации"""
        return reverse('users:verify_message')


class UserProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:success_message')

    def get_object(self, queryset=None):  # отвязываемся от pk
        return self.request.user


def create_subscription(request):
    """Создание оплаты подписки"""
    if request.user.is_authenticated:
        user = request.user
        if not user.is_subscription:
            session = create_payment_session(request)
            return redirect(session.url)
        else:
            messages.info(request, 'У вас уже есть активная подписка.')
            return redirect('blog:home')

def cancel_subscription(request):
    """URL для перенаправления в случае отмены платежа"""
    return render(request, 'users/cancel_payment.html')

def success_subscription(request):
    """Обработка оплаты подписки"""
    if request.user.is_authenticated:
        user = request.user
        user.is_subscription = True
        user.save()
        messages.success(request, 'Подписка успешно оформлена!')
        return redirect('blog:home')

    else:
        messages.error(request, 'Что-то пошло не так. Пожалуйста, повторите попытку.')
        return redirect('users:login')

# class UserUpdateView(PermissionRequiredMixin, UpdateView):
#     """Обновление информации о пользователе"""
#     model = User
#     form_class = UserRegisterForm
#     success_url = 'users:users_list'
#
#     def get_success_url(self):
#         """Получение URL для перенаправления после успешного обновления"""
#         return reverse('users:list_view')
