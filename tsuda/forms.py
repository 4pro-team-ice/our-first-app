from django import forms

from .models import Post

from .models import Monday1


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)


class JikannwariForm(forms.ModelForm):

    class Meta:
        model = Monday1
        fields = ('className', 'class_number' ,'profName')
