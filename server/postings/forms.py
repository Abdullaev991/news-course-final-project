from datetime import datetime

from django import forms
from PIL import Image
from postings.models import PostModel, CommentModel


class LoginForm(forms.Form):
    username = forms.CharField(label='Имя пользователя')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['placeholder'] = 'Введите ваше имя'
        self.fields['password'].widget.attrs['placeholder'] = 'Введите ваш пароль'
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['id'] = 'usernameInput'
        self.fields['password'].widget.attrs['id'] = 'passwordInput'


class PostForm(forms.Form):
    title = forms.CharField(label='Заголовок', required=True)
    desc = forms.CharField(label='Описание', required=True,widget=forms.Textarea)
    file = forms.ImageField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['title'].widget.attrs['placeholder'] = 'Введите заголовок поста'
        self.fields['desc'].widget.attrs['placeholder'] = 'Введите описание поста'
        self.fields['title'].widget.attrs['id'] = 'titleInput'
        self.fields['desc'].widget.attrs['id'] = 'descInput'
        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['desc'].widget.attrs['class'] = 'form-control'
        self.fields['file'].widget.attrs['class'] = 'form-control'
        self.fields['file'].widget.attrs['id'] = 'fileInput'

    def save(self, user):
        if self.is_valid():
            image = Image.open(self.cleaned_data.get("file"))

            last_model_object = PostModel.objects.last()
            if last_model_object is None:
                file_number = 1
            else:
                file_number = last_model_object.id + 1

            file_name = f"{file_number}.{image.format}"
            image.save(f"static/images/{file_name}")
            image.close()

            PostModel(
                author=user,
                title=self.cleaned_data.get("title"),
                desc=self.cleaned_data.get("desc"),
                file_name=file_name,
                created = datetime.now(),
                update_author = user,

                ).save()


class CommentForm(forms.Form):
    text = forms.CharField(label='Текст комментария')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['text'].widget.attrs['class'] = 'form-control'
        self.fields['text'].widget.attrs['id'] = 'textInput'


    def save(self, photo, user):
        if self.is_valid():
            CommentModel(
                photo=photo,
                text=self.cleaned_data.get("text"),
                author=user,
                created = datetime.now()
            ).save()
