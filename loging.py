from apscheduler.schedulers.background import BackgroundScheduler as scheduler
from model.Middleware import *
import datetime


api = Middleware()
api.update()
stations = api.status_stations

stations['time-stamp'] = [datetime.datetime.now().timestamp()]*stations.shape[0]
stations.reset_index(inplace=True)

def updating():
    api.update()
    stationsBis = api.status_stations
    stationsBis['time-stamp'] = [datetime.datetime.now().timestamp()]*stationsBis.shape[0]
    stations.append(stationsBis, ignore_index = True)
    print("Got some juicy data ! Yummy in my tummy")



sch = scheduler()
sch.add_job(updating, 'interval', seconds=900)
sch.start()

# This code will be executed after the sceduler has started
try:
    print('Scheduler started, ctrl-c to exit!')
    while 1:
        input()
except KeyboardInterrupt:
    if sch.state:
        sch.shutdown()


stations.to_json(path_or_buf='./output/now.json')