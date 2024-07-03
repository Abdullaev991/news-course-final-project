from datetime import datetime

from PIL import Image
from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from postings.models import PostModel, CommentModel




class ProfileUpdateForm(UserChangeForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control text-bg-light'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control text-bg-light'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control text-bg-light'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control text-bg-light'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']


class LoginForm(forms.Form):
    username = forms.CharField(label='Имя пользователя')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['placeholder'] = 'Введите ваше имя'
        self.fields['password'].widget.attrs['placeholder'] = 'Введите ваш пароль'
        self.fields['username'].widget.attrs['class'] = 'form-control text-bg-light'
        self.fields['password'].widget.attrs['class'] = 'form-control text-bg-light'
        self.fields['username'].widget.attrs['id'] = 'usernameInput'
        self.fields['password'].widget.attrs['id'] = 'passwordInput'


class PostForm(forms.Form):
    title = forms.CharField(label='Заголовок', required=True)
    desc = forms.CharField(label='Описание', required=True, widget=forms.Textarea)
    file = forms.ImageField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['title'].widget.attrs['placeholder'] = 'Введите заголовок поста'
        self.fields['desc'].widget.attrs['placeholder'] = 'Введите описание поста'
        self.fields['title'].widget.attrs['id'] = 'titleInput'
        self.fields['desc'].widget.attrs['id'] = 'descInput'
        self.fields['title'].widget.attrs['class'] = 'form-control text-bg-light'
        self.fields['desc'].widget.attrs['class'] = 'form-control text-bg-light'
        self.fields['file'].widget.attrs['class'] = 'form-control text-bg-light'
        self.fields['file'].widget.attrs['id'] = 'fileInput'

    def save(self, user):
        if self.is_valid():
            if self.cleaned_data['file'] is not None:
                image = Image.open(self.cleaned_data.get("file"))

                last_model_object = PostModel.objects.last()
                if last_model_object is None:
                    file_number = 1
                else:
                    file_number = last_model_object.id + 1

                file_name = f"{file_number}.{image.format}"
                image.save(f"static/images/{file_name}")
                image.close()
            else:
                file_name = None
            PostModel(
                author=user,
                title=self.cleaned_data.get("title"),
                desc=self.cleaned_data.get("desc"),
                file_name=file_name,
                created=datetime.now(),
                update_author=user,

            ).save()


class CommentForm(forms.Form):
    text = forms.CharField(label='')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['text'].widget.attrs['class'] = 'form-control text-bg-light'
        self.fields['text'].widget.attrs['placeholder'] = 'Написать комментарий...'
        self.fields['text'].widget.attrs['id'] = 'textInput'
        self.fields['text'].widget.attrs['name'] = 'ftext'

    def save(self, photo, user):
        if self.is_valid():
            CommentModel(
                photo=photo,
                text=self.cleaned_data.get("text"),
                author=user,
                created=datetime.now()
            ).save()
