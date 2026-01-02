from django.contrib import admin
from .models import BookReview, Comment, Europe, CommentEurope, Message

class BookReviewAdmin(admin.ModelAdmin):
    list_display=[
        "author",
        "title",
        "date",
        "body",
    ]
    
class EuropeAdmin(admin.ModelAdmin):
    list_display=[
        "author",
        "title",
        "date",
        "body",
    ]
class MessageAdmin(admin.ModelAdmin):
    list_display=[
        "First_name",
        "Last_name",
        "Email",
        "Subject",
        "Message",
]


admin.site.register(BookReview, BookReviewAdmin)
admin.site.register(Comment)
admin.site.register(Europe, EuropeAdmin)
admin.site.register(CommentEurope)
admin.site.register(Message, MessageAdmin)
# Register your models here.
 