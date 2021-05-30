from django.shortcuts import render

posts = [
    {
        'author': 'Osama',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'May 17, 2021'

    },
    {
        'author': 'Bobo',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'May 18, 2021'

    },
]

def home(request):
    context = {
        'posts': posts,
    }
    return render(request,'blog/home.html', context)
def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
