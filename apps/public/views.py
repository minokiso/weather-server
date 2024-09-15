from datetime import datetime

import requests
from django.db.transaction import atomic

from Utils.viewset import ModelViewSetPlus, handle_error
from apps.public.models import Weather3h


class Weather3hViewSet(ModelViewSetPlus):
    model = Weather3h
    filterset_fields = {
        "StationNameThai": ['icontains'],
        "StationNameEnglish": ['icontains'],
        "Province": ['icontains'],
        "DateTime": ['range'],
    }
    search_fields = ['StationNameThai', 'StationNameEnglish', 'Province']

    @atomic()
    @handle_error()
    def create(self, request, *args, **kwargs):
        url = "https://data.tmd.go.th/api/Weather3Hours/V2/"
        uid = "u672417591283"
        ukey = "cf81a2f0dd39dedfa42700e670b70781"
        format = 'json'
        params = {
            "uid": uid,
            "ukey": ukey,
            "format": format
        }
        response = requests.get(url, params=params)
        stations = response.json().get("Stations").get("Station")
        weather3h = []
        for station in stations:
            observation = station.pop("Observation")
            DateTime = observation.get("DateTime")
            format_datetime = datetime.strptime(DateTime, "%m/%d/%Y %H:%M:%S")
            StationPressure = observation.get("StationPressure")
            MeanSeaLevelPressure = observation.get("MeanSeaLevelPressure")
            AirTemperature = observation.get("AirTemperature")
            DewPoint = observation.get("DewPoint")
            RelativeHumidity = observation.get("RelativeHumidity")
            VaporPressure = observation.get("VaporPressure")
            LandVisibility = observation.get("LandVisibility")
            WindDirection = observation.get("WindDirection")
            WindSpeed = observation.get("WindSpeed")
            Rainfall = observation.get("Rainfall")
            Rainfall24Hr = observation.get("Rainfall24Hr")
            weather3h.append(Weather3h(
                **station,
                DateTime=format_datetime,
                StationPressure=StationPressure,
                MeanSeaLevelPressure=MeanSeaLevelPressure,
                AirTemperature=AirTemperature,
                DewPoint=DewPoint,
                RelativeHumidity=RelativeHumidity,
                VaporPressure=VaporPressure,
                LandVisibility=LandVisibility,
                WindDirection=WindDirection if not isinstance(WindDirection, dict) else None,
                WindSpeed=WindSpeed,
                Rainfall=Rainfall,
                Rainfall24Hr=Rainfall24Hr
            ))
        Weather3h.objects.bulk_create(weather3h)
        return stations
