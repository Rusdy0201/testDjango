from django.shortcuts import render
from django.http import HttpResponse

posts = [
	{
		'author': 'rusdy',
		'title': 'blog post 1 ',
		'content': 'first post content',
		'date_publish': 'Mei 9, 2020'
	},
	{
		'author': 'riska',
		'title': 'blog post 2 ',
		'content': 'second post content',
		'date_publish': 'Mei 9, 2020'
	}

]

about = [
	{
		'name': 'rusdiansyah',
		'contact': '+6281362745653',
		'email': 'rusdynsh@gmail.com'
		'title': 'About me'
	}
]


def home(request):
	context = {
		'posts': posts
	}

	return render(request, 'blog/home.html',context)

def about(request):
	context = {
		'about': about
	}
	return render(request, 'blog/about.html',context)
