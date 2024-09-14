from prometheus_client import CollectorRegistry, Gauge, push_to_gateway
from metrics import *
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
    push_to_gateway('pushgateway:9091', job='custom_metrics', registry=registry, handler=my_auth_handler)


if __name__ == "__main__":
    amocrm_integration_rpm, amocrm_integration_err_1, amocrm_integration_err_2 = amocrm_integration.get_metrics()
    push_gauge_metric(amocrm_integration_rpm, 'amocrm_integration RPM', 'Amocrm integration rpm')
    push_gauge_metric(amocrm_integration_err_1, 'amocrm_integration ERROR 1', 'Amocrm integration error 1')
    push_gauge_metric(amocrm_integration_err_2, 'amocrm_integration ERROR 2', 'Amocrm integration error 2')