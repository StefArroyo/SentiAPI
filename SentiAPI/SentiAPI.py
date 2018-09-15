import falcon
import json
from wsgiref import simple_server

class SentimentResource(object):
    def on_post(self, req, resp):
        """Handles POST requests"""
        sentiment_data = req.stream.read()
        resp.status = falcon.HTTP_200  # This is the default status
        resp.body = sentiment_data

if __name__ == "__main__":
    # falcon.API instances are callable WSGI apps
    api = falcon.API()
    # Resources are represented by long-lived class instances
    sentiment = SentimentResource()

    # things will handle all requests to the '/things' URL path
    api.add_route('/sentiment', sentiment)

    host = "localhost"
    port = 3000

    server = simple_server.make_server(host, port, api)
    server.serve_forever()
