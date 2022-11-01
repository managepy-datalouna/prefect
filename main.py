from prefect import flow

from tasks import (
    clean_cities,
    print_cities,
    get_json,
)


@flow(name='City extraction')
def extract_cities():
    json = get_json()
    cleaned_cities = clean_cities(json)
    print_cities(cleaned_cities)


if __name__ == '__main__':
    extract_cities()
