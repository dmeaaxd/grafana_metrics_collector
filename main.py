from prometheus_client import CollectorRegistry, Gauge, push_to_gateway
from prometheus_client.exposition import basic_auth_handler
import dotenv
import os

dotenv.load_dotenv()


def my_auth_handler(url, method, timeout, headers, data):
    username = os.getenv('USERNAME')
    password = os.getenv('PASSWORD')
    return basic_auth_handler(url, method, timeout, headers, data, username, password)


def push_gauge_metric(metric, name, documentation):
    registry = CollectorRegistry()

    g = Gauge(name=name, documentation=documentation, registry=registry)
    g.set(metric)
    push_to_gateway('0.0.0.0:9091', job='custom_metrics', registry=registry, handler=my_auth_handler)
