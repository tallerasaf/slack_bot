from collections import namedtuple

from .controllers import AllAverage, UserAverage

Route = namedtuple('Route', 'resource url')


routes = [
    Route(resource=AllAverage, url='/average'),
    Route(resource=UserAverage, url='/average/<string:slack_username>'),
]


def add_routes(api):
    for route in routes:
        api.add_resource(route.resource, route.url)
