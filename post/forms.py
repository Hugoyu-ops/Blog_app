from .models import Comment
from django import forms

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        widgets = {
            'text': forms.Textarea(attrs={'rows':4, 'cols':40}),
        }
        fields = ('name', 'text')