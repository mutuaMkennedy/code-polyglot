from pathlib import Path
from django.contrib.gis.utils import LayerMapping
from .models import Route, Station

# Auto-generated `LayerMapping` dictionary for Routes model. See https://docs.djangoproject.com/en/4.2/ref/contrib/gis/tutorial/#try-ogrinspect
# Each key in the dictionary is the name of a model field, and each value is the name of a field in the shapefile.
routes_mapping = {
    "shape_id": "shape_id",
    "points": "points",
    "trip_id": "trip_id",
    "head_sign": "headsign",
    "direction": "direction",
    "route_id": "route_id",
    "route_name": "route_name",
    "route_long": "route_long",
    "geom": "MULTILINESTRING",
}

station_mapping = {
    "stop_id": "stop_id",
    "stop_name": "stop_name",
    "stop_lat": "stop_lat",
    "stop_long": "stop_lon",
    "location_type": "location_t",
    "parent_station": "parent_sta",
    "trip_count": "trip_count",
    "trip_ids": "trip_ids",
    "route_ids": "route_ids",
    "route_names": "route_nams",
    "geom": "MULTIPOINT",
}


routes_shp = Path(__file__).resolve().parent / "data" / "shapes.shp"
stations_shp = Path(__file__).resolve().parent / "data" / "stops.shp"


def run(verbose=True):
    lm_routes = LayerMapping(Route, routes_shp, routes_mapping, transform=False)
    lm_routes.save(strict=True, verbose=verbose)

    lm_stations = LayerMapping(Station, stations_shp, station_mapping, transform=False)
    lm_stations.save(strict=True, verbose=verbose)
