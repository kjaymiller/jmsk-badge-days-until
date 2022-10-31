import typing
from datetime import date, datetime, timedelta, timezone


def get_days_until(
    day_of_week: int,
    time: typing.Union[tuple[int, int, int], None] = None,
) -> tuple[str, str]:
    """Calculate days until the given day of the week"""
    today = date.today()
    days_left = today + timedelta((day_of_week - today.weekday()) % 7)
    days = (days_left - today).days
    msg = f"{days} days"

    if days == 0:
        if time != None:
            # Get 3pm in Los Angeles
            _time = (
                datetime.now()
                .astimezone(timezone("US/Pacific"))
                .replace(hour=time[0], minute=time[1], second=time[2], microsecond=0)
            )

            # Get time until 3pm in hours and minutes
            time_until = _time - datetime.now().astimezone(timezone("US/Pacific"))
            hours = time_until.seconds // 3600

            if hours == 0:
                minutes = (time_until.seconds // 60) % 60
                msg = f"{minutes} minutes"

            else:
                msg = f"{hours} hours"

    elif days > 5:
        color = "green"

    elif days >= 2:
        color = "yellow"
    else:
        color = "red"

    return msg, color
