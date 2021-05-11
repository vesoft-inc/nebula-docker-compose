# -*- encoding: utf-8 -*-
import datetime


def yesturday_format(value):
    yesturday = value - datetime.timedelta(days=1)
    return yesturday.strftime('%Y.%m.%d')


class FilterModule(object):
    """ jinja2 filters """

    def filters(self):
        return {
            'yesturday_format': yesturday_format,
        }
