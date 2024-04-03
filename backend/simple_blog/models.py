from django.db import models
from django.utils import timezone

class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    bio = models.TextField()

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='posts')
    categories = models.ManyToManyField(Category)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Comment by {self.post.author.name} on {self.post.title}"

class Image(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images')
    image_url = models.URLField()

    def __str__(self):
        return f"Image for {self.post.title}"

class Rating(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    rating = models.IntegerField()
    created_at = models.DateTimeField(default=timezone.now)

class Bookmark(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='bookmarks')
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

class Share(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='shares')
    shared_platform = models.CharField(max_length=100)
    shared_at = models.DateTimeField(default=timezone.now)

class Subscription(models.Model):
    subscriber = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    subscribed_at = models.DateTimeField(default=timezone.now)

class View(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='views')
    viewer = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    viewed_at = models.DateTimeField(default=timezone.now)

class Poll(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='polls')
    question = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)

class NewsletterSubscription(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(default=timezone.now)

class Advertisement(models.Model):
    image = models.ImageField(upload_to='advertisements/')
    link = models.URLField()
    created_at = models.DateTimeField(default=timezone.now)

class FeaturedPost(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='featured_posts')
    featured_at = models.DateTimeField(default=timezone.now)
