from django.db import models


class Weather3h(models.Model):
    WmoStationNumber = models.IntegerField(null=True, blank=True)
    StationNameThai = models.CharField(max_length=255, null=True, blank=True)
    StationNameEnglish = models.CharField(max_length=255, null=True, blank=True)
    Province = models.CharField(max_length=255, null=True, blank=True)
    Latitude = models.FloatField(null=True, blank=True)
    Longitude = models.FloatField(null=True, blank=True)
    DateTime = models.DateTimeField(null=True, blank=True)
    StationPressure = models.FloatField(null=True, blank=True)
    MeanSeaLevelPressure = models.FloatField(null=True, blank=True)
    AirTemperature = models.FloatField(null=True, blank=True)
    DewPoint = models.FloatField(null=True, blank=True)
    RelativeHumidity = models.FloatField(null=True, blank=True)
    VaporPressure = models.FloatField(null=True, blank=True)
    LandVisibility = models.FloatField(null=True, blank=True)
    WindDirection = models.IntegerField(null=True, blank=True)
    WindSpeed = models.FloatField(null=True, blank=True)
    Rainfall = models.FloatField(null=True, blank=True)
    Rainfall24Hr = models.FloatField(null=True, blank=True)

    class Meta:
        ordering = ['DateTime']
        db_table = 'weather3h'


class Log(models.Model):
    last_build_time = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['last_build_time']
        db_table = 'log'
