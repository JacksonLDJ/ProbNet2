from core.models import OS_Info, Port, Device_Data
from django.db.models import Count


#Function to retrieve data from Device_Data model to display our tables
def get_device_data():
    query = Device_Data.objects.filter(

    ).select_related(
        "Operating_System"
    ).annotate(
        port_count = Count("ports")
    ).all()

    return query


def get_ports_by_device(device_id):
    query = Port.objects.filter(device_data_id = device_id).all()
    return query