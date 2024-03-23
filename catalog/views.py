from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import View, DetailView, ListView, CreateView, FormView, DeleteView, UpdateView

from catalog.forms import CommentForm, DishForm
from catalog.models import Dish, Beverages, Cook
from django.contrib.auth import logout


class IndexView(LoginRequiredMixin, ListView):
    model = Dish
    template_name = 'index.jinja'
    context_object_name = 'dishes'

    def get_queryset(self):
        query = self.request.GET.get('query')
        if query:
            return Dish.objects.filter(name__icontains=query) | Dish.objects.filter(description__icontains=query)
        else:
            return Dish.objects.all()


# class GuestIndexView(LoginRequiredMixin, ListView):
#     model = Dish
#     template_name = 'guest_page.jinja'
#     # context_object_name = 'dishes'
#
    def get_queryset(self):
        query = self.request.GET.get('query')
        if query:
            return Dish.objects.filter(name__icontains=query) | Dish.objects.filter(description__icontains=query)
        else:
            return Dish.objects.all()


class GuestPageView(View):
    template_name = 'guest_page.jinja'

    def get(self, request):
        query = request.GET.get('query')
        if query:
            dishes = Dish.objects.filter(name__icontains=query) | Dish.objects.filter(description__icontains=query)
        else:
            dishes = Dish.objects.all()
        return render(request, self.template_name, {'dishes': dishes})


class DetailsView(DetailView):
    model = Dish
    template_name = 'detail.jinja'
    context_object_name = 'details'


class DishDetailView(DetailsView):
    model = Dish
    template_name = "detail.jinja"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        dish = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = dish
            comment.save()
            return redirect('catalog:detail', pk=dish.pk)


class BeverageListView(ListView):
    model = Beverages
    template_name = "beverages.jinja"
    context_object_name = "beverage"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['query'] = self.request.GET.get('query', '')
    #     return context

    # def get_queryset(self):
    #     return Beverages.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['beverages'] = self.get_queryset()
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('query')
        if query:
            queryset = queryset.filter(name__icontains=query)
        return queryset


class UserDishesView(View):
    template_name = 'cooker_data.jinja'

    def get(self, request, user_id):
        user = get_object_or_404(Cook, pk=user_id)
        dishes = user.dishes.all()
        return render(request, self.template_name, {'user': user, 'dishes': dishes})


# class CreateDishView(View):
#     def get(self, request):
#         form = DishForm()
#         return render(request, 'create_dish.jinja', {'form': form})
#
#     def post(self, request):
#         form = DishForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('catalog:index')
#         return render(request, 'create_dish.jinja', {'form': form})

class CreateDishView(LoginRequiredMixin, View):
    def get(self, request):
        form = DishForm(initial={'cooks': [request.user.id]})
        return render(request, 'create_dish.jinja', {'form': form})

    def post(self, request):
        form = DishForm(request.POST, request.FILES)
        if form.is_valid():
            dish = form.save(commit=False)
            dish.save()
            dish.cooks.add(request.user)
            return redirect('catalog:index')
        return render(request, 'create_dish.jinja', {'form': form})


# class UpdateDishView(View):
#     template_name = 'update_dish.jinja'
#
#     def get(self, request, dish_id):
#         dish = get_object_or_404(Dish, pk=dish_id)
#         form = DishForm(instance=dish)
#         return render(request, self.template_name, {'form': form, 'dish': dish})
#
#     def post(self, request, dish_id):
#         dish = get_object_or_404(Dish, pk=dish_id)
#         form = DishForm(request.POST, request.FILES, instance=dish)
#         if form.is_valid():
#             form.save()
#             return redirect('catalog:index')
#         else:
#             return render(request, self.template_name, {'form': form, 'dish': dish})

class UpdateDishView(UpdateView):
    template_name = 'dish_form.jinja'

    form_class = DishForm
    model = Dish

    # def get(self, request, dish_id):
    #     dish = get_object_or_404(Dish, pk=dish_id)
    #     form = DishForm(instance=dish)
    #     return render(request, self.template_name, {'form': form, 'dish': dish})
    #
    # def post(self, request, dish_id):
    #     dish = get_object_or_404(Dish, pk=dish_id)
    #     form = DishForm(request.POST, request.FILES, instance=dish)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('catalog:user_dishes', user_id=request.user.id)
    #     else:
    #         return render(request, self.template_name, {'form': form, 'dish': dish})


class DeleteDishView(View):
    template_name = 'delete_dish.jinja'

    def get(self, request, dish_id):
        dish = get_object_or_404(Dish, pk=dish_id)
        return render(request, self.template_name, {'dish': dish})

    def post(self, request, dish_id):
        dish = get_object_or_404(Dish, pk=dish_id)
        dish.delete()
        return redirect('catalog:index')


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('catalog:index')
