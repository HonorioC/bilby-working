from gwpy.timeseries import TimeSeries
from gwosc.datasets import event_gps

gps = event_gps("GW150414")
start = int(gps) - 