# -*- encoding: utf-8 -*-
import datetime


def yesterday_format(value):
    yesterday = value - datetime.timedelta(days=1)
    return yesterday.strftime('%Y.%m.%d')


class FilterModule(object):
    """ jinja2 filters """

    def filters(self):
        return {
            'yesterday_format': yesterday_format,
        }
