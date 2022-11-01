import pprint

from prefect import task, get_run_logger
from faker import Faker


@task
def get_json() -> list[dict]:
    fake = Faker()
    logger = get_run_logger()
    logger.info(f'Fake user-agent: {fake.user_agent()}')

    return [
        dict(
            zip((
                'lat',
                'lon',
                'name',
                'country',
                'timezone',
            ),
                fake.location_on_land(),
            )
        ) for _ in range(10)
    ]


@task
def clean_cities(cities: list) -> list[dict]:
    logger = get_run_logger()
    logger.info(cities)
    for city in cities:
        for key in ['country', 'timezone']:
            city.pop(key)
    return cities


@task
def print_cities(cities: list) -> None:
    pprint.pprint(cities)
