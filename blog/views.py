from django.shortcuts import render
from django.utils import timezone
from .models import Post
# Le point avant models signifie dossier courant ou application courante. Les fichiers views.py et models.py sont dans le même répertoire. Cela signifie que nous pouvons utiliser . suivi par le nom du fichier (sans .py).
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect


# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

# Dans la fonction render, nous avons un paramètre request, qui désigne tout ce que nous recevons d'un utilisateur par l'intermédiaire d'Internet,
# et un autre qui signale le fichier template ('blog/post_list.html').
# Le dernier paramètre, {}, va nous permettre de glisser des informations que notre template va utiliser.
# Nous devons donner des noms à ces informations (nous allons rester sur 'posts' pour le moment). :) Ça va ressembler à ça : {'posts': posts}.
# La partie située avant : est une chaine de caractères ; vous devez donc l'entourer de guillemets : ''.

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
