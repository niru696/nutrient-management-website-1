from django.shortcuts import render

from nutrients_info.models import Disease, Food, Nutrient, Season, People, \
    Geographical


def info(request):
    nutrients = Nutrient.objects.all()
    diseases = Disease.objects.all()
    foods = Food.objects.all()
    seasons = Season.objects.all()
    peoples = People.objects.all()
    geographicals = Geographical.objects.all()

    return render(request, 'nutrients_info.html', {'nutrients': nutrients,
                                                   'diseases': diseases,
                                                   'foods': foods,
                                                   'seasons': seasons,
                                                   'peoples': peoples,
                                                   'geographicals': geographicals
                                                   })
