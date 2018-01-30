from math import radians, sin, cos, acos


def getDistance(start, lat, lon):
    slat = radians(start[0])
    slon = radians(start[1])
    elat = radians(lat)
    elon = radians(lon)
    return 6371.01 * 1000 * acos(
        sin(slat) * sin(elat) + cos(slat) * cos(elat) * cos(slon - elon))
