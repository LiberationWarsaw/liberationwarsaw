from django import template

register = template.Library()

@register.simple_tag
def format_dates(start, end):
    if start.date() == end.date():
        date_format = "%A %b %d"
        time_format = "%I:%M%p"
        # Tuesday Jan 2, 1:00PM–4:00PM
        return "{date}, {start_time}–{end_time}".format(
            date=start.date().strftime(date_format),
            start_time=start.time().strftime(time_format),
            end_time=end.time().strftime(time_format)
        )

    elif (end.date() - start.date()).seconds <= 24*60*60:
        # If less than 24 hours difference:
        date_format = "%A %b %d"
        time_format = "%I:%M%p"

        # Tuesday Jan 2, 10:00PM – Wednesday Jan 3, 11:00PM
        return "{start_date}, {start_time} – {end_date}, {end_time}".format(
            start_date=start.date().strftime(date_format),
            start_time=start.time().strftime(time_format),
            end_date=end.date().strftime(date_format),
            end_time=end.time().strftime(time_format),
        )

    else:
        # If more than 24 hours difference:
        date_format = "%A %b %d, %Y"

        # Tuesday Jan 2, 2018 – Saturday Jan 6, 2018
        return "{start_date} – {end_date}".format(
            start_date=start.date().strftime(date_format),
            end_date=end.date().strftime(date_format),
        )
