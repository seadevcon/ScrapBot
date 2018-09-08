from apistar import App, Route, Include

from routes import scrapping


def welcome(name=None):
    if name is None:
        return {'message': 'Welcome to API Star!'}
    return {'message': 'Welcome to API Star, %s!' % name}


routes = [
    Route('/', method='GET', handler=welcome),
    Include('/scrapping', name='Scrapping', routes=scrapping.routes)
]

app = App(routes=routes)


if __name__ == '__main__':
    app.serve('127.0.0.1', 8888, debug=True)