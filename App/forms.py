from django import forms

class PostForm(forms.Form):
    title = forms.CharField(max_length=40)
    subtitle = forms.CharField(max_length=80)
    img = forms.ImageField()
    description = forms.CharField(max_length=250, widget=forms.Textarea)


class CommentForm(forms.Form):
    comment = forms.CharField(max_length=150, widget=forms.Textarea)