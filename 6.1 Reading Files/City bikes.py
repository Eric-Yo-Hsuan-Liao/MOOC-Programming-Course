

def get_station_data(filename: str):
    with open(filename) as file:
        data = {}
        for line in file:
            parts = line.strip()
            parts = parts.split(';')
            if parts[0] == 'Longitude':
                continue
            names = parts[3]
            longitudes = float(parts[0])
            latitudes = float(parts[1])
            location = (longitudes, latitudes)
            data[names] = location
    return data

import math
def distance(stations: dict, station1: str, station2: str):
    longitude1 = stations[station1][0]
    longitude2 = stations[station2][0]
    latitude1 = stations[station1][1]
    latitude2 = stations[station2][1]
    x_km = (longitude1 - longitude2) * 55.26
    y_km = (latitude1 - latitude2) * 111.2
    distance_km = math.sqrt(x_km ** 2 + y_km ** 2)
    return distance_km

def greatest_distance(stations: dict):
    new = []
    for key, value in stations.items():
        new.append(key)
    max_dist = 0
    for i in range(len(new)):
        station1 = new[i]
        for j in range(i+1, len(new)):
            station2 = new[j]
            dist = distance(stations, station1, station2)
            if dist > max_dist:
                max_dist = dist
                result = (station1, station2, max_dist)
    return result


stations = get_station_data('stations1.csv')
station1, station2, greatest = greatest_distance(stations)
print(station1, station2, greatest)