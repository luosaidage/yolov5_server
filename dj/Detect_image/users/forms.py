from django import forms

# 表单类用以生成表单
class AddForm(forms.Form):
    name = forms.CharField()
    headimg = forms.FileField()