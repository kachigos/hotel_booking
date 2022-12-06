# from django import forms
# from .models import Questions
#
#
# class QuestionsForm(forms.ModelForm):
#     fullname = forms.CharField(min_length=200, widget=forms.CharField(), label='ФИО')
#     email = forms.EmailField(min_length=50, widget=forms.EmailField(), label='email')
#     number = forms.CharField(min_length=50, widget=forms.CharField(), label='number')
#     text = forms.Textarea(forms.Textarea())
#
#     class Meta:
#         model = Questions
#         fields = ['fullname', 'email', 'number', 'text']
#
#     def save(self, commit=True):
#         question = Questions.objects.create()
#         question.save()
#         return question

