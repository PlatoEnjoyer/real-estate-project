from django.shortcuts import render
from ml_model.get_model_from_pkl import rf
import pandas as pd
from .forms import InputParamsForm


def main_view(request):
    return render(request, 'main/base.html')


def input_apart_params(request):
    form = InputParamsForm()
    return render(request, 'main/view_of_input_apart_params.html', context={'form': form})


def calculate_apartment_price(request):
    d = {'region': request.POST['region'], 'level': request.POST['level'], 'levels': request.POST['levels'],
         'rooms': request.POST['rooms'], 'area': request.POST['area'],
         'kitchen_area': request.POST['kitchen_area']}
    data = pd.DataFrame(data=d, index=[0])
    cost = int(rf.predict(data)[0]) // 100
    return render(request, 'main/calculated_price.html', context={'res': str(cost) + '00'})


def about_view(request):
    return render(request, 'main/about_page.html')
