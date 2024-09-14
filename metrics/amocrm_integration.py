import dotenv
import main
from requests import get
import os

dotenv.load_dotenv()
yandex_server_url = os.getenv('YANDEX_SERVER_URL')


def get_metrics():
    rpm = get(f'{yandex_server_url}/rpm').json()['rpm']
    errors_1 = get(f'{yandex_server_url}/rpm').json()['errors_1']
    errors_2 = get(f'{yandex_server_url}/rpm').json()['errors_2']

    return rpm, errors_1, errors_2


if __name__ == '__main__':
    rpm, errors_1, errors_2 = get_metrics()
    main.push_gauge_metric(rpm, 'amocrm_integration_rpm', 'Amocrm integration script RPM')
