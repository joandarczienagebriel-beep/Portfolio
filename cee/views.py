from django.views.generic import TemplateView, ListView, DetailView, FormView
from django.views.generic import  CreateView, DeleteView
from .models import BookReview, Europe, Message
from .forms import CommentForm, CommentEuropeForm
from django.views import View
from django.urls import reverse, reverse_lazy
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import UserPassesTestMixin,LoginRequiredMixin

class HomeView(ListView):
    template_name="home.html"
    model= BookReview

class BlogList(ListView):
    template_name="list.html"
    model= BookReview
    paginate_by = 2

    
class CommentGet(LoginRequiredMixin, DetailView):
    template_name="detail.html"
    model= BookReview

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        return context

class CommentPost(SingleObjectMixin, FormView):
    form_class= CommentForm
    template_name="detail.html"
    model= BookReview

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.bookreview = self.object
        comment.author = self.request.user
        comment.save()
        return super().form_valid(form)

    def get_success_url(self):
        bookreview = self.object
        return reverse("detail", kwargs={"pk": bookreview.pk})


class BlogDetail(LoginRequiredMixin,View):
    def get(self, request,*args, **kwargs):
        view=CommentGet.as_view()
        return view(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        view=CommentPost.as_view()
        return view(request, *args, **kwargs)

class AboutView(TemplateView):
    template_name="about.html"

class BlogCreate(CreateView):
    template_name="create.html"
    fields=["author","date","title","body"]
    model=BookReview
    success_url=reverse_lazy("list")
class BlogDelete(UserPassesTestMixin, DeleteView):
    template_name="delete.html"
    success_url=reverse_lazy("list")
    model=BookReview

    def test_func(self):
        obj=self.get_object()
        return obj.author == self.request.user


#west-europe
class EuropeList(ListView):
    template_name="Europelist.html"
    model= Europe
    paginate_by = 2


    
class EuroCommentGet(LoginRequiredMixin,DetailView):
    template_name="europedetail.html"
    model= Europe

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context["form"] = CommentEuropeForm()
        return context

class EuroCommentPost(SingleObjectMixin, FormView):
    form_class= CommentEuropeForm
    template_name="europedetail.html"
    model= Europe

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        commenteurope = form.save(commit=False)
        commenteurope.europe = self.object
        commenteurope.author = self.request.user
        commenteurope.save()
        return super().form_valid(form)

    def get_success_url(self):
        europe = self.object
        return reverse("europe_detail", kwargs={"pk": europe.pk})


class EuroBlogDetail(View):
    def get(self, request,*args, **kwargs):
        view=EuroCommentGet.as_view()
        return view(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        view=EuroCommentPost.as_view()
        return view(request, *args, **kwargs)

# Create your views here.

class MessageView(CreateView):
    model= Message
    fields=['First_name', 'Last_name', 'Email', 'Subject', 'Message']
    template_name='messages.html'