from django.http import JsonResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404


from places.models import Image, Place


def index(request):
    places = Place.objects.all()
    
    geojson_places = {
        'type': 'FeatureCollection',
        'features': [],
    }

    for place in places:
        place_serialize = {
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [place.latitude, place.longitude],
            },
            'properties': {
                'title': place.title,
                'placeId': place.place_id,
                'detailsUrl': place.details_url,
            }
        }

        geojson_places['features'].append(place_serialize)

    context = {'places': geojson_places}
    return render(request, 'index.html', context=context)


def places(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    place_images = Image.objects.filter(title__contains=place.title)

    place_serialize = {
        'title': place.title,
        'imgs': [image.image.url for image in place_images],
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {
            'lng': place.longitude,
            'lat': place.latitude,
        },
    }

    return JsonResponse(place_serialize, json_dumps_params={'ensure_ascii': False})
