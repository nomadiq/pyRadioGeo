import shapefile as shp
import os
from .maidenhead import Maidenhead, latlongbearing, latlongdistance
import numpy as np


def latlon_10m():
    path = os.path.join(os.path.dirname(__file__), "10m_coords")
    shape = shp.Reader(path + "/ne_10m_coastline.shp")
    features = shape.shapeRecords()
    return [coord.shape.__geo_interface__["coordinates"] for coord in features]


def latlon_110m():
    path = os.path.join(os.path.dirname(__file__), "110m_coords")
    shape = shp.Reader(path + "/ne_110m_coastline.shp")
    features = shape.shapeRecords()
    return [coord.shape.__geo_interface__["coordinates"] for coord in features]


def latlon_50m():
    path = os.path.join(os.path.dirname(__file__), "50m_coords")
    shape = shp.Reader(path + "/ne_50m_coastline.shp")
    features = shape.shapeRecords()
    return [coord.shape.__geo_interface__["coordinates"] for coord in features]


def azimuthal_10m_mh(center: Maidenhead):
    center.latlong()
    coords = latlon_10m()
    center_lon = center.long
    center_lat = center.lat
    polars = []
    for land in coords:
        landmass = []
        for point in land:
            r = latlongdistance(center_lat, center_lon, point[1], point[0])
            theta = latlongbearing(center_lat, center_lon, point[1], point[0])
            landmass.append([theta * np.pi / 180, r])
        polars.append(landmass)
    return polars


def azimuthal_110m_mh(center: Maidenhead):
    center.latlong()
    coords = latlon_110m()
    center_lon = center.long
    center_lat = center.lat
    polars = []
    for land in coords:
        landmass = []
        for point in land:
            r = latlongdistance(center_lat, center_lon, point[1], point[0])
            theta = latlongbearing(center_lat, center_lon, point[1], point[0])
            landmass.append([theta * np.pi / 180, r])
        polars.append(landmass)
    return polars