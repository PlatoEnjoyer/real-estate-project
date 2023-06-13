from django import forms


class InputParamsForm(forms.Form):
    region = forms.IntegerField(min_value=1, max_value=89, label='Регион')
    level = forms.IntegerField(min_value=1, max_value=100, label='Этаж')
    levels = forms.IntegerField(min_value=1, max_value=100, label='Этажей в доме')
    rooms = forms.IntegerField(min_value=1, max_value=20, label='Комнаты')
    area = forms.FloatField(min_value=1.0, label='Площадь')
    kitchen_area = forms.FloatField(min_value=1.0, label='Площадь кухни')
