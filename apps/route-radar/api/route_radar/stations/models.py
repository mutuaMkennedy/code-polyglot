from django.contrib.gis.db import models


class Route(models.Model):
    shape_id = models.CharField(max_length=254)
    points = models.IntegerField()
    trip_id = models.CharField(max_length=10)
    head_sign = models.CharField(max_length=26)
    direction = models.IntegerField()
    route_id = models.CharField(max_length=11)
    route_name = models.CharField(max_length=6)
    route_long = models.CharField(max_length=79)
    geom = models.MultiLineStringField(srid=4326)

    class Meta:
        db_table = "route"
        verbose_name_plural = "Routes"

    def __str__(self):
        return f"{self.route_name} - {self.route_long}"


class Station(models.Model):
    stop_id = models.CharField(max_length=254)
    stop_name = models.CharField(max_length=254)
    stop_lat = models.FloatField()
    stop_long = models.FloatField()
    location_type = models.BigIntegerField()
    parent_station = models.CharField(max_length=254)
    trip_count = models.IntegerField()
    trip_ids = models.CharField(max_length=251)
    route_ids = models.CharField(max_length=254)
    route_names = models.CharField(max_length=109)
    geom = models.MultiPointField(srid=4326)

    class Meta:
        db_table = "station"
        verbose_name_plural = "Stations"

    def __str__(self):
        return f"{self.stop_name} - {self.route_names}"
