from django.db import models

# Create your models here.
class Post(models.Model):
    username = models.CharField(max_length=30,verbose_name='username del usuario')
    location = models.CharField(max_length=60, verbose_name='Ubicación de donde vive')
    avatar = models.ImageField(verbose_name='Imagen del usuario', upload_to='avatar')
    photo = models.ImageField(verbose_name='Imagen publicada', upload_to='publicacion')
    like= models.BooleanField(verbose_name='Se dio like', default=False)
    bookmark= models.BooleanField(verbose_name='Se guardo', default=False)
    postComment=models.CharField(verbose_name='Comentario del usuario que publico',max_length=500)
    create_at=models.DateTimeField(verbose_name='Fecha de creacion', auto_now_add=True, blank=True, null=True)
    #comments=
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    username = models.CharField(max_length=100)