from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.urls import reverse

from places.models import Place


def index(request) -> HttpResponse:
    geopoints = {
        'type': 'FeatureCollection',
        'features': [make_geopoint_notes(place) for place in Place.objects.all()],
    }
    context = {'places': geopoints}

    return render(request, 'index.html', context=context)


def make_geopoint_notes(place: Place) -> dict:
    geopoint_notes = {
        'type': 'Feature',
        'geometry': {
            'type': 'Point',
            'coordinates': [place.longitude, place.latitude],
        },
        'properties': {
            'title': place.title,
            'detailsUrl': reverse('places', kwargs={'place_id': place.id}),
        }
    }

    return geopoint_notes


def places(request, place_id: int) -> JsonResponse:
    place = get_object_or_404(Place, id=place_id)

    place_serialize = {
        'title': place.title,
        'imgs': [image.image.url for image in place.images.all()],
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {
            'lng': place.longitude,
            'lat': place.latitude,
        },
    }

    return JsonResponse(place_serialize, json_dumps_params={'ensure_ascii': False})
