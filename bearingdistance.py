from .maidenhead import Maidenhead
import math

def maidendistance(mh1: Maidenhead, mh2: Maidenhead):
    lat1 = mh1.lat
    lat2 = mh2.lat
    long1 = mh1.long
    long2 = mh2.long

    phi1 = lat1 * math.pi / 180
    phi2 = lat2 * math.pi / 180
    dphi = (lat2 - lat1) * math.pi / 180
    dlam = (long2 - long1) * math.pi / 180

    a = math.sin(dphi / 2) * math.sin(dphi / 2) + math.cos(phi1) * math.cos(phi2) * math.sin(dlam / 2) * math.sin(dlam / 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return 6371 * c

def maidenbearing(mh1: Maidenhead, mh2: Maidenhead):
    lat1 = mh1.lat
    lat2 = mh2.lat
    long1 = mh1.long
    long2 = mh2.long

    phi1 = lat1 * math.pi / 180
    phi2 = lat2 * math.pi / 180
    dphi = (lat2 - lat1) * math.pi / 180
    dlam = (long2 - long1) * math.pi / 180

    theta = math.atan2(math.sin(dlam) * math.cos(phi2), math.cos(phi1) * math.sin(phi2) - math.sin(phi1) * math.cos(phi2) * math.cos(dlam))
    return (theta * 180 / math.pi + 360) % 360


def latlondistance(lat1, lon1, lat2, lon2):
    

    phi1 = lat1 * math.pi / 180
    phi2 = lat2 * math.pi / 180
    dphi = (lat2 - lat1) * math.pi / 180
    dlam = (lon2 - lon1) * math.pi / 180

    a = math.sin(dphi / 2) * math.sin(dphi / 2) + math.cos(phi1) * math.cos(phi2) * math.sin(dlam / 2) * math.sin(dlam / 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return 6371 * c

def latlonbearing(lat1, lon1, lat2, lon2):

    phi1 = lat1 * math.pi / 180
    phi2 = lat2 * math.pi / 180
    dphi = (lat2 - lat1) * math.pi / 180
    dlam = (lon2 - lon1) * math.pi / 180

    theta = math.atan2(math.sin(dlam) * math.cos(phi2), math.cos(phi1) * math.sin(phi2) - math.sin(phi1) * math.cos(phi2) * math.cos(dlam))
    return (theta * 180 / math.pi + 360) % 360