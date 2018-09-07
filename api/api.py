from apistar import App, Route

from routes import scrap_event


def welcome(name=None):
    if name is None:
        return {'message': 'Welcome to API Star!'}
    return {'message': 'Welcome to API Star, %s!' % name}


routes = [
    Route('/', method='GET', handler=welcome),
    Route('/', method='GET', handler=scrap_event)
]

app = App(routes=routes)


if __name__ == '__main__':
    app.serve('127.0.0.1', 8888, debug=True)