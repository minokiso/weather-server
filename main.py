import os
import traceback
import requests
import django
from datetime import datetime, timedelta
from apscheduler.schedulers.blocking import BlockingScheduler
from loggers import http_server_logger

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')

django.setup()
from django.db.transaction import atomic
from apps.public.models import Weather3h, Log


def get_data():
    try:
        with atomic():
            print("开始获取数据")
            http_server_logger.info("开始获取数据")
            thai_time = datetime.utcnow() + timedelta(hours=7)
            log = Log.objects.filter(last_build_time__day=thai_time.day)
            if log.exists():
                print_str = f"数据已存在, last_build_time: {log.first().last_build_time}"""
                print(print_str)
                http_server_logger.info(print_str)
                return
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
            data = response.json()
            stations = data.get("Stations").get("Station")
            last_build_time = data.get("Header").get("LastBuildDate")
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
            Log.objects.create(last_build_time=last_build_time)
            print_str = f"读取成功, last_build_time: {last_build_time}"
            print(print_str)
            http_server_logger.info(print_str)
    except Exception as e:
        err = traceback.format_exc()
        http_server_logger.error(err)
        print(err)


if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(get_data, 'cron', hour=8, minute=0)
    scheduler.add_job(get_data, 'cron', hour=8, minute=10)
    scheduler.add_job(get_data, 'cron', hour=8, minute=20)
    try:
        print("scheduler start")
        http_server_logger.debug("scheduler start")
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass
