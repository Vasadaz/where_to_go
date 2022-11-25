from django.shortcuts import render

from places.models import Place


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
