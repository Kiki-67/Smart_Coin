from django.urls import path
from . import views

app_name = 'records'

urlpatterns = [
    # path("", views.IndexView.as_view(), name='index'),
    path("login/", views.user_login, name='login'),
    path("logout/", views.user_logout, name='user_logout'),
    path('register/', views.user_register, name='register'),
    path('edit/<int:id>/', views.profile_edit, name='edit'),
    path('home/<int:id>/', views.home, name='home'),
    path('expense_add/<int:id>/', views.expense_add, name='expense_add'),
    path('income_add/<int:id>/', views.income_add, name='income_add'),
    path('budget_add/<int:id>/', views.budget_add, name='budget_add'),
    path('<int:user_id>/expense-delete/<int:id>/', views.expense_delete, name='expense_delete'),
    path('<int:user_id>/income-delete/<int:id>/', views.income_delete, name='income_delete'),
    path('<int:user_id>/budget-delete/<int:id>/', views.budget_delete, name='budget_delete'),
    path('<int:user_id>/expense-change/<int:id>/', views.expense_change, name='expense_change'),
    path('<int:user_id>/income-change/<int:id>/', views.income_change, name='income_change'),
    path('<int:user_id>/budget-change/<int:id>/', views.budget_change, name='budget_change'),
    path('search/<int:id>/', views.search, name='search'),
    path('summary/<int:id>/', views.summary, name='summary')

]