import pytest
from stations.models import Route, Station
from typing import Type, Dict
from django.db.models import Model


class BaseTest:
    """
    Base class containing reusable helper methods
    Methods:
        create_instance(model, data)
    """

    @staticmethod
    def create_instance(model: Type[Model], data: dict) -> Model:
        """
        Creates a model instance.

        Args:
            model (Type[Model]): The Django model class to create an instance of.
            data (dict): A dictionary containing data to initialize the model instance.

        Returns:
            The created model instance.
        """
        return model.objects.create(**data)


@pytest.mark.django_db
class TestRoute(BaseTest):
    """
    Test class for Route model.
    """

    @pytest.mark.parametrize(
        "data",
        [
            (
                {
                    "shape_id": "123",
                    "points": 5,
                    "trip_id": "456",
                    "head_sign": "Test Head Sign",
                    "direction": 1,
                    "route_id": "789",
                    "route_name": "Test",
                    "route_long": "Test Route Long",
                    "geom": "MULTILINESTRING((0 0,1 1,2 2))",
                }
            ),
            (
                {
                    "shape_id": None,
                    "points": None,
                    "trip_id": None,
                    "head_sign": None,
                    "direction": None,
                    "route_id": None,
                    "route_name": None,
                    "route_long": None,
                    "geom": None,
                }
            ),
        ],
    )
    def test_instance_creation(self, data: Dict[str, any]) -> None:
        """
        Test case to verify instance creation for Route model.

        Args:
            data (dict): Dictionary containing data for the model instance creation.
        """
        route = self.create_instance(Route, data)
        assert route.pk is not None

    def test_route_string_representation(self) -> None:
        """
        Test case to verify string representation of Route model.
        """
        route = Route(route_name="Test", route_long="Test Route Long")
        assert str(route) == "Test - Test Route Long"


@pytest.mark.django_db
class TestStation(BaseTest):
    """
    Test class for Station model.
    """

    @pytest.mark.parametrize(
        "data",
        [
            (
                {
                    "stop_id": "123",
                    "stop_name": "Test Station",
                    "stop_lat": 0.0,
                    "stop_long": 0.0,
                    "location_type": 0,
                    "parent_station": "Test Parent Station",
                    "trip_count": 1,
                    "trip_ids": "1",
                    "route_ids": "1",
                    "route_names": "Test",
                    "geom": "MULTIPOINT(0 0)",
                }
            ),
            (
                {
                    "stop_id": None,
                    "stop_name": None,
                    "stop_lat": None,
                    "stop_long": None,
                    "location_type": None,
                    "parent_station": None,
                    "trip_count": None,
                    "trip_ids": None,
                    "route_ids": None,
                    "route_names": None,
                    "geom": None,
                }
            ),
        ],
    )
    def test_instance_creation(self, data: Dict[str, any]) -> None:
        """
        Test case to verify instance creation for Station model.

        Args:
            data (dict): Dictionary containing data for the model instance creation.
        """
        station = self.create_instance(Station, data)
        assert station.pk is not None

    def test_station_string_representation(self):
        """
        Test case to verify string representation of Station model.
        """
        station = Station(stop_name="Test Station", route_names="Test")
        assert str(station) == "Test Station - Test"
