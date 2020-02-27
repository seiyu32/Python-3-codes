from datetime import datetime
from dateutil import tz
local = tz.gettz()
PT = tz.gettz('US/Pacific')

dt_1 = datetime(2015, 1, 1, 12, tzinfo=local)
dt_pts = datetime(2015, 1, 1, 12, tzinfo=PT)
dt_pdt = datetime(2015, 7, 1, 12, tzinfo=PT)
# print(dt_1)
# print(dt_pst)
print(dt_pdt)