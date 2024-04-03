from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import Author, Category, Tag, Post, Comment, Image, Rating, Bookmark, Like, Share, Subscription, View, Poll, NewsletterSubscription, Advertisement, FeaturedPost

# Create a custom AdminSite instance for the "simple_blog" section
class SimpleBlogAdminSite(AdminSite):
    site_header = "Simple Blog Administration"
    site_title = "Simple Blog Admin"
    index_title = "Welcome to the Simple Blog Admin Panel"

simple_blog_admin_site = SimpleBlogAdminSite(name='simple_blog_admin')

# Register your models here.
simple_blog_admin_site.register(Author)
simple_blog_admin_site.register(Category)
simple_blog_admin_site.register(Tag)
simple_blog_admin_site.register(Post)
simple_blog_admin_site.register(Comment)
simple_blog_admin_site.register(Image)
simple_blog_admin_site.register(Rating)
simple_blog_admin_site.register(Bookmark)
simple_blog_admin_site.register(Like)
simple_blog_admin_site.register(Share)
simple_blog_admin_site.register(Subscription)
simple_blog_admin_site.register(View)
simple_blog_admin_site.register(Poll)
simple_blog_admin_site.register(NewsletterSubscription)
simple_blog_admin_site.register(Advertisement)
simple_blog_admin_site.register(FeaturedPost)
