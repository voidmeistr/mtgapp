from django.views import generic
from .models import Post

# Create your views here.

class IndexView(generic.ListView):
	template_name = 'magic/index.html'
	context_object_name = 'all_posts'

	def get_queryset(self):
		return Post.objects.all()

class DetailView(generic.DetailView):
	model = Post
	template_name = 'magic/detail.html'
