from django import forms
from .models import ProductAnswer


class ProductQuestionForm(forms.Form):
    question = forms.CharField(
        label="Answer",
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'question', 'placeholder': 'Ask your question!'}),
        required=True
    )


class AnswerQuestionForm(forms.ModelForm):
    class Meta:
        model = ProductAnswer
        exclude = ('user', 'product_question',)

        widgets = {
            'answer': forms.Textarea(attrs={'class': 'form-control', 'id': 'answer', 'placeholder': 'Answer here ...'}),
        }

        labels = {
            'answer': 'Answers'
        }
