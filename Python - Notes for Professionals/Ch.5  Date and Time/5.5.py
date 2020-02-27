from datetime import datetime
from dateutil import tz

utc = tz.tzutc()
local = tz.tzlocal()

utc_now = datetime.utcnow()
utc_now

utc_now = utc_now.replace(tzinfo=utc)
utc_now

local_now = utc_now.astimezone(local)
local_now