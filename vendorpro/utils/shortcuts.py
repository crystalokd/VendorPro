import uuid



def get_random_code():
    """
    The function `random_code` generates a random code with 12 chars using the UUID library in Python.
    :return: The code is returning the last part of a randomly generated UUID.
    """
    return str(uuid.uuid4()).split("-")[-1]

# from .models import Vendor, Order


def calculate_otd():
    total_orders = Order.objects.count()
    on_time_orders = Order.objects.filter(delivered_on_time=True).count()

    if total_orders == 0:
        otd_percentage = 0
    else:
        otd_percentage = (on_time_orders / total_orders) * 100

    # Update the OTD percentage for all vendors
    Vendor.objects.update(on_time_delivery_rate=otd_percentage)