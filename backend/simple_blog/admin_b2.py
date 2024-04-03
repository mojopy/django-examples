from django.contrib import admin
from .models import Author, Category, Tag, Post, Comment, Image, Rating, Bookmark, Like, Share, Subscription, View, Poll, NewsletterSubscription, Advertisement, FeaturedPost

# Register your models here.

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_published')
    filter_horizontal = ('categories', 'tags')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'content', 'created_at')

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('post', 'image_url')

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('post', 'user', 'rating', 'created_at')

@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('post', 'user', 'created_at')

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('post', 'user', 'created_at')

@admin.register(Share)
class ShareAdmin(admin.ModelAdmin):
    list_display = ('post', 'shared_platform', 'shared_at')

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('subscriber', 'author', 'category', 'subscribed_at')

@admin.register(View)
class ViewAdmin(admin.ModelAdmin):
    list_display = ('post', 'viewer', 'viewed_at')

@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    list_display = ('post', 'question', 'created_at')

@admin.register(NewsletterSubscription)
class NewsletterSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('email', 'subscribed_at')

@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ('image', 'link', 'created_at')

@admin.register(FeaturedPost)
class FeaturedPostAdmin(admin.ModelAdmin):
    list_display = ('post', 'featured_at')
