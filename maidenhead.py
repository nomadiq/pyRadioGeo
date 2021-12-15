import math

class Maidenhead:
    def __init__(self,loc_string: str, latlong: bool = False):
        self.loc_string = loc_string
        self.fine_loc_string = ''
        self.valid_characters_1 = "ABCDEFGHIJKLMNOPQR"
        self.valid_characters_2 = "abcdefghijklmnopqrstuvwx"
        self.valid_numbers = "0123456789"

        if len(loc_string) %2 != 0:
            raise ValueError("Invalid Maiden Location")


        if len(self.loc_string) < 2:
            raise ValueError("Invalid Maidenhead Location")

        if len(self.loc_string) == 2:
            self.loc_string = self.loc_string[:2].upper()
        else:
            self.loc_string = self.loc_string[:2].upper() + self.loc_string[2:].lower()

        maiden2 = self.loc_string[:2]
        self.m2 = ''
        if (
            maiden2[0] not in self.valid_characters_1
            or maiden2[1] not in self.valid_characters_1
        ):
            raise ValueError("Invalid Maidenhead2 Location")

        self.m2 = maiden2
        self.length = 2
        self.fine_loc_string += self.m2


        if len(self.loc_string) >= 4:

            maiden4 = self.loc_string[2:4]
            if (
                maiden4[0] not in self.valid_numbers
                or maiden4[1] not in self.valid_numbers
            ):
                raise ValueError("Invalid Maidenhead4 Location")
            self.m4 = maiden4
            self.length = 4
            self.fine_loc_string += self.m4
        else:
            self.fine_loc_string += "55"    

        if len(self.loc_string) >= 6:
            maiden6 = self.loc_string[4:6]

            if (
                maiden6[0] not in self.valid_characters_2
                or maiden6[1] not in self.valid_characters_2
            ):
                raise ValueError("Invalid Maidenhead6 Location")
            self.m6 = maiden6
            self.length = 6
            self.fine_loc_string += self.m6
        else:
            self.fine_loc_string += "ll"

        if len(self.loc_string) >= 8:
            maiden8 = self.loc_string[6:8]
            if (
                maiden8[0] not in self.valid_numbers
                or maiden8[1] not in self.valid_numbers
            ):
                raise ValueError("Invalid Maidenhead8 Location")
            self.m8 = maiden8
            self.length = 8
            self.fine_loc_string += self.m8
        else:
            self.fine_loc_string += "55"

        if len(self.loc_string) >= 10:
            maiden10 = self.loc_string[8:10]

            if (
                maiden10[0] not in self.valid_characters_2
                or maiden10[1] not in self.valid_characters_2
            ):
                raise ValueError("Invalid Maidenhead10 Location")
            self.m10 = maiden10
            self.length = 10
            self.fine_loc_string += self.m10
        else:
            self.fine_loc_string += "ll"

        if latlong:
            self.latlong()
    
    def latlong(self):
        # convert to lat/long
        # first convert self.fine_loc_string to a list of numbers
        self.fine_loc_string_list = l = [
            self.valid_characters_1.index(self.fine_loc_string[0]),
            self.valid_characters_1.index(self.fine_loc_string[1]),
            self.valid_numbers.index(self.fine_loc_string[2]),
            self.valid_numbers.index(self.fine_loc_string[3]),
            self.valid_characters_2.index(self.fine_loc_string[4]),
            self.valid_characters_2.index(self.fine_loc_string[5]),
            self.valid_numbers.index(self.fine_loc_string[6]),
            self.valid_numbers.index(self.fine_loc_string[7]),
            self.valid_characters_2.index(self.fine_loc_string[8]),
            self.valid_characters_2.index(self.fine_loc_string[9]),
        ]
        self.long = (l[0]*20 + l[2]*2 + l[4]/12 + l[6]/120 + l[8]/2880) - 180
        self.lat = (l[1]*10 + l[3] + l[5]/24 + l[7]/240 + l[9]/5760) - 90

    def __str__(self):
        return self.loc_string
    
    def __len__(self):
        return self.length

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


def latlongdistance(lat1, long1, lat2, long2):
    

    phi1 = lat1 * math.pi / 180
    phi2 = lat2 * math.pi / 180
    dphi = (lat2 - lat1) * math.pi / 180
    dlam = (long2 - long1) * math.pi / 180

    a = math.sin(dphi / 2) * math.sin(dphi / 2) + math.cos(phi1) * math.cos(phi2) * math.sin(dlam / 2) * math.sin(dlam / 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return 6371 * c

def latlongbearing(lat1, long1, lat2, long2):

    phi1 = lat1 * math.pi / 180
    phi2 = lat2 * math.pi / 180
    dphi = (lat2 - lat1) * math.pi / 180
    dlam = (long2 - long1) * math.pi / 180

    theta = math.atan2(math.sin(dlam) * math.cos(phi2), math.cos(phi1) * math.sin(phi2) - math.sin(phi1) * math.cos(phi2) * math.cos(dlam))
    return (theta * 180 / math.pi + 360) % 360