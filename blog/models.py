from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model) :
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self) :
        return self.title

# models.Model signifie que Post est un modèle Django. Comme ça, Django sait qu'il doit l'enregistrer dans la base de données.
# models.ForeignKey - C'est un lien vers un autre modèle = renvoie à un identifiant spécial Django
# blank / null = blank > le champ dans le formulaire peut rester vide, null = vide aussi dans la BDD
# timezone.now = post par défaut créé à l'heure actuelle
# models.CharField - Cela nous permet de définir un champ texte avec un nombre limité de caractères. TextField = sans limite
# def signifie que nous créons une fonction/méthode qui porte le nom publish
# La règle de nommage est d'utiliser des minuscules et des tirets bas à la place des espaces. Par exemple, une méthode qui calcule le prix moyen d'un produit pourrait s'appeler calcul_prix_moyen
# Les méthodes renvoient (return) souvent quelque chose. C'est le cas de la méthode __str__.
# Dans notre tutoriel, lorsque nous appellerons la méthode __str__(), nous allons obtenir du texte (string) avec un titre de Post.
