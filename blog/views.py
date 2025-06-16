from django.shortcuts import render, get_object_or_404
from .models import Post

def post_list(request):
    """
    Displays a list of all blog posts.
    Includes a YouTube video ID for the background on the blog list page.
    """
    posts = Post.objects.all() # Fetch all posts from the database
    context = {
        'posts': posts,
        # Replace 'YOUR_YOUTUBE_VIDEO_ID_HERE' with your actual YouTube video ID
        # Example: For YouTube URL https://www.youtube.com/watch?v=dQw4w9WgXcQ, the ID is dQw4w9WgXcQ
        'youtube_video_id': 'sEH3pOhj0xs'
    }
    return render(request, 'blog/post_list.html', context)

def post_detail(request, slug):
    """
    Displays the detailed view of a single blog post.
    Fetches the post based on its unique slug.
    """
    # get_object_or_404 will raise a 404 Http404 exception if the post is not found
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post_detail.html', {'post': post})
