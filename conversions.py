from .maidenhead import Maidenhead
import math

def latlon2azimuthal(lat, lon, center_lat: float = None, center_lon: float = None, center_maiden: Maidenhead = None):
    """
    Convert latitude and longitude to azimuthal coordinates.
    """
    if center_maiden is None and (center_lat is None or center_lon is None):
        raise ValueError("Either center_lat and center_lon or center_loc must be specified.")
    elif center_lat is None or center_lon is None:
        center_maiden = Maidenhead(center_maiden)
        center_lat, center_lon = center_maiden.lat(), center_maiden.lon()
