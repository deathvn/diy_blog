from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse

from blog.models import Blog, BlogAuthor, BlogComment

# Create your views here.
def index(request):
    """View function for Blog Homepage"""
    num_blogs = Blog.objects.all().count()
    num_blog_authors = BlogAuthor.objects.all().count()

    # Number of visits to this view
    num_visits = request.session.get('num_visit', 1)
    request.session['num_visit'] = num_visits + 1

    context = {
        'num_blogs': num_blogs,
        'num_blog_authors': num_blog_authors,
        'num_visits': num_visits,
    }

    return render(request, 'index.html', context=context)
    

class BlogListView(generic.ListView):
    """
    List of Blog view
    """
    model = Blog
    paginate_by = 10


class BlogAuthorListView(generic.ListView):
    """
    List of Author view
    """
    model = BlogAuthor
    paginate_by = 5


class BlogDetailView(generic.ListView):
    """
    Blog post detail view, each post has list of BlogComment paginate
    """
    model = BlogComment
    template_name = 'blog/blog_detail.html'
    paginate_by = 4

    def get_queryset(self):
        """Return all comment of the current blog"""
        target_blog = get_object_or_404(Blog, pk=self.kwargs['pk'])
        return BlogComment.objects.filter(blog=target_blog)

    def get_context_data(self, **kwargs):
        """Add Blog to context so they can display in the template"""
        # Call the base implementation first to get a context
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        # Blog for template
        context['blog'] = get_object_or_404(Blog, pk=self.kwargs['pk'])
        
        # Check delete/modifined - able?
        try:
            current_user = get_object_or_404(BlogAuthor, name=self.request.user)
            context['delete_able_comment'] = BlogComment.objects.filter(author=current_user)
        except:
            context['delete_able_comment'] = []

        return context


class BlogListbyAuthorView(generic.ListView):
    """
    Author detail view, list of blog post has paginate
    """
    model = Blog
    paginate_by = 5
    template_name ='blog/author_detail.html'

    def get_queryset(self):
        """
        Return list of Blog objects created by BlogAuthor (author id specified in URL)
        """
        target_author = get_object_or_404(BlogAuthor, pk=self.kwargs['pk'])
        return Blog.objects.filter(author=target_author)
        
    def get_context_data(self, **kwargs):
        """
        Add BlogAuthor to context so they can be displayed in the template
        """
        # Call the base implementation first to get a context
        context = super(BlogListbyAuthorView, self).get_context_data(**kwargs)
        # Get the blogger object from the "pk" URL parameter and add it to the context
        context['blogauthor'] = get_object_or_404(BlogAuthor, pk=self.kwargs['pk'])
        return context


# Comment Create, Update, Delete
class BlogCommentCreate(LoginRequiredMixin, CreateView):
    model = BlogComment
    fields = ['description']

    def get_context_data(self, **kwargs):
        """
        Add Blog to context so they can be displayed in the template
        """
        # Call the base implementation first to get a context
        context = super(BlogCommentCreate, self).get_context_data(**kwargs)
        # Get the blogger object from the "pk" URL parameter and add it to the context
        context['blog'] = get_object_or_404(Blog, pk=self.kwargs['pk'])
        return context 

    def form_valid(self, form):
        """
        Add author and associated blog to form data before setting it as valid (so it is saved to model)
        """
        #Add logged-in user as author of comment
        form.instance.author = get_object_or_404(BlogAuthor, name=self.request.user)
        #Associate comment with blog based on passed id
        form.instance.blog = get_object_or_404(Blog, pk = self.kwargs['pk'])
        # Call super-class form validation behavior
        return super(BlogCommentCreate, self).form_valid(form)

    def get_success_url(self):
        """
        Back to the blog post when commented
        """
        return reverse('blog-detail', kwargs={'pk': self.kwargs['pk']})


class BlogCommentDelete(LoginRequiredMixin, DeleteView):
    model = BlogComment

    def get_queryset(self):
        """
        Return list of comment objects created by current User
        """
        commenter = get_object_or_404(BlogAuthor, name=self.request.user)
        return BlogComment.objects.filter(author=commenter)

    def get_success_url(self):
        """
        Back to the blog post when delete comment complete
        """
        blog_id = self.get_object().blog.id
        return reverse('blog-detail', kwargs={'pk': blog_id})


class BlogCommentUpdate(LoginRequiredMixin, UpdateView):
    model = BlogComment
    fields = ['description']

    def get_queryset(self):
        """
        Return list of comment objects created by current User
        """
        commenter = get_object_or_404(BlogAuthor, name=self.request.user)
        return BlogComment.objects.filter(author=commenter)

    def get_context_data(self, **kwargs):
        """
        Add Blog to context so they can be displayed in the template
        """
        # Call the base implementation first to get a context
        context = super(BlogCommentUpdate, self).get_context_data(**kwargs)
        # Get the blogger object from the "pk" URL parameter and add it to the context
        context['blog'] = self.get_object().blog
        return context 

    def get_success_url(self):
        """
        Back to the blog post when update comment complete
        """
        blog_id = self.get_object().blog.id
        return reverse('blog-detail', kwargs={'pk': blog_id})


# Blog Create, Update, Delete
