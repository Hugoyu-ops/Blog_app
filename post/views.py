from django.shortcuts import render
from django.views import generic
from .models import Post
from django.shortcuts import get_object_or_404, redirect
from .forms import CommentForm
# Create your views here.
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')[:3]
    template_name = 'index.html'

#class PostDetail(generic.DetailView):
    #model = Post
    #template_name = 'post_detail.html'

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

class AllList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'all_post.html'

def post_detail(request, slug):
    template_name = 'post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(approved_comment=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})