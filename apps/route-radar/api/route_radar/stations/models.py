from django.contrib.gis.db import models


class Route(models.Model):
    shape_id = models.CharField(max_length=254, null=True)
    points = models.IntegerField(null=True)
    trip_id = models.CharField(max_length=10, null=True)
    head_sign = models.CharField(max_length=26, null=True)
    direction = models.IntegerField(null=True)
    route_id = models.CharField(max_length=11, null=True)
    route_name = models.CharField(max_length=6, null=True)
    route_long = models.CharField(max_length=79, null=True)
    geom = models.MultiLineStringField(srid=4326, null=True)

    class Meta:
        db_table = "route"
        verbose_name_plural = "Routes"

    def __str__(self):
        return f"{self.route_name} - {self.route_long}"


class Station(models.Model):
    stop_id = models.CharField(max_length=254, null=True)
    stop_name = models.CharField(max_length=254, null=True)
    stop_lat = models.FloatField(null=True)
    stop_long = models.FloatField(null=True)
    location_type = models.BigIntegerField(null=True)
    parent_station = models.CharField(max_length=254, null=True)
    trip_count = models.IntegerField(null=True)
    trip_ids = models.CharField(max_length=251, null=True)
    route_ids = models.CharField(max_length=254, null=True)
    route_names = models.CharField(max_length=109, null=True)
    geom = models.MultiPointField(srid=4326, null=True)

    class Meta:
        db_table = "station"
        verbose_name_plural = "Stations"

    def __str__(self):
        return f"{self.stop_name} - {self.route_names}"
