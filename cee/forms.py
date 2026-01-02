from django import forms
from .models import Comment, CommentEurope

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("comment",)

class CommentEuropeForm(forms.ModelForm):
    class Meta:
        model = CommentEurope
        fields = ("comment",)