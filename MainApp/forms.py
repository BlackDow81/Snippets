from django.forms import ModelForm
from MainApp.models import Snippet
from django.forms import TextInput, Textarea


class SnippetForm(ModelForm):
    class Meta:
        model = Snippet
        # Описываем поля, которые будем заполнять в форме
        fields = ['name', 'lang', 'code']
        widgets = {
            'name': TextInput(attrs={"placeholder": "Имя сниппета"}),
            'code': Textarea(attrs={"placeholder": "Код сниппета"}),
        }
        labels = {
            'name': '',
            'lang': '',
            'code': ''
        }
