from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.simple_tag
def format_dates(start, end, multiline=False):
    if multiline == "true":
        multiline = True

    if start.date() == end.date():
        date_format = "%A %b %d"
        time_format = "%I:%M%p"
        # Tuesday Jan 2, 1:00PM–4:00PM
        template_string = "{date}, {start_time} – {end_time}"
        if multiline:
            template_string = "{date}<br>{start_time} – {end_time}"
        return mark_safe(template_string.format(
            date=start.date().strftime(date_format),
            start_time=start.time().strftime(time_format).lower(),
            end_time=end.time().strftime(time_format).lower()
        ))

    elif (end.date() - start.date()).seconds <= 24*60*60:
        # If less than 24 hours difference:
        date_format = "%A %b %d"
        time_format = "%I:%M%p"

        # Tuesday Jan 2, 10:00PM – Wednesday Jan 3, 11:00PM
        template_string = "{start_date}, {start_time} – {end_date}, {end_time}"
        if multiline:
            template_string = "{start_date}, {start_time}<br>{end_date}, {end_time}"
        return mark_safe(template_string.format(
            start_date=start.date().strftime(date_format),
            start_time=start.time().strftime(time_format).lower(),
            end_date=end.date().strftime(date_format),
            end_time=end.time().strftime(time_format).lower(),
        ))

    else:
        # If more than 24 hours difference:
        date_format = "%A %b %d, %Y"

        # Tuesday Jan 2, 2018 – Saturday Jan 6, 2018
        template_string = "{start_date} – {end_date}"
        if multiline:
            template_string = "{start_date}<br>{end_date}"
        return mark_safe(template_string.format(
            start_date=start.date().strftime(date_format),
            end_date=end.date().strftime(date_format),
        ))
