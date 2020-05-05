# Main Python file

''' Important:
Do not mix up .update_json() and .update_self() !!!
.update_json(): Python stays the same; json gets updated
.update_self(): Json stays the same; Python gets updated
'''

import json_stuff as jss
from random import randint
from time import sleep

# Meanings of the id-start-letters: (always followed by a 3-digit-number)
id_meanings = {
    "WL": "WhiteLamp",
    "CL": "ColorLamp",
    "TS": "TemperatureSensor",
    "QS": "AirQualitySensor",
    "HS": "HumiditySensor",
    "GR": "Group",
    "RM": "Room"
}

reverse_id_meanings = {v: k for k, v in zip(
    id_meanings.keys(), id_meanings.values())}


def create_id(type):  # generate random id and append it to used_ids.json (this function doesn't add it to devices/groups/rooms.json)
    if type in id_meanings.keys():
        used_ids = jss.read("used_ids")[type]
        while True:
            num = randint(100, 999)
            if num in used_ids:
                pass
            else:
                id = type + str(num)
                big_dict = jss.read("used_ids")
                big_dict[type].append(num)

                jss.write("used_ids", big_dict)
                return id
    else:
        raise Exception(f"Type {type} does not exist")


class Home():
    class Lamp():  # Parent class
        def __init__(self):
            self.name = ""
            self.id = ""
            self.status = ""

        def __del__(self):  # remove self from json file
            big_dict = jss.read("devices")
            del big_dict[self.name]
            jss.write("devices", big_dict)

        # Works for adding self and replacing self (json will be same as Python)
        def update_json(self):
            big_dict = jss.read("devices")
            big_dict[self.name] = {"type": str(
                type(self)), "id": self.id, "status": self.status}
            jss.write("devices", big_dict)

        def update_self(self):  # Python will be same as json
            big_dict = jss.read("devices")
            self.id = big_dict[self.name]["id"]
            self.status = big_dict[self.name]["status"]

    class WhiteLamp(Lamp):  # WL
        def __init__(self, name, id="", status=""):
            self.name = name
            self.id = create_id("WL") if id == "" else id
            self.status = "0%" if status == "" else status

            self.update_json()  # Add self to devices.json

        def change_status(self, status):
            self.status = status
            self.update_json()
            pr = self.status.split(" ")[0]
            # licht an/aus machen natürlich

    class ColorLamp(Lamp):  # CL
        def __init__(self, name, id="", status=""):
            self.name = name
            self.id = create_id("CL") if id == "" else id
            self.status = "0% (255, 255, 255)" if status == "" else status

            self.update_json()  # Add self to devices.json

        def change_status(self, status):
            self.status = status
            self.update_json()
            pr = self.status.split(" ")[0]
            rgb = self.status.split(" ")[1]
            # licht an/aus machen natürlich

    #################################################

    class Sensor():
        def __init__(self, name, id="", status=""):
            self.name = name
            self.id = create_id(
                reverse_id_meanings[str(type(self))]) if id == "" else id
            self.status = "" if status == "" else status

            self.update_json()

        # Works for adding self and replacing self (json will be same as Python)
        def update_json(self):
            big_dict = jss.read("devices")
            big_dict[self.name] = {"type": str(
                type(self)), "id": self.id, "status": self.status}
            jss.write("devices", big_dict)

        def update_self(self):  # Python will be same as json
            big_dict = jss.read("devices")
            self.id = big_dict[self.name]["id"]
            self.status = big_dict[self.name]["status"]

    class TemperatureSensor(Sensor):
        pass

    class AirQualitySensor(Sensor):
        pass

    class HumiditySensor(Sensor):
        pass

    #################################################

    class Group():
        def __init__(self, name, id="", devices=[]):
            self.name = name
            # NOT LIKE THAT! self.devices should be a dict: {name: obj, name: oj, ...}
            self.devices = devices
            self.id = create_id("GR") if id == "" else id

            self.update_json()

        # Works for adding self and replacing self (json will be same as Python)
        def update_json(self):
            big_dict = jss.read("groups")
            big_dict[self.name] = {"type": "Group",
                                   "id": self.id, "devices": self.devices}
            jss.write("groups", big_dict)

        def update_self(self):  # Python will be same as json
            big_dict = jss.read("groups")
            self.id = big_dict[self.name]["id"]
            self.devices = big_dict[self.name]["devices"]

        def __contains__(self, devicename):
            return devicename in self.devices

    class Room():
        def __init__(self, name, id="", devices=[], groups=[]):
            self.name = name
            # NOT LIKE THAT! self.devices should be a dict: {name: obj, name: oj, ...}
            self.devices = devices
            # NOT LIKE THAT! self.groups should be a dict: {name: obj, name: oj, ...}
            self.groups = groups
            self.id = create_id("GR") if id == "" else id

            self.update_json()

        # Works for adding self and replacing self (json will be same as Python)
        def update_json(self):
            big_dict = jss.read("rooms")
            big_dict[self.name] = {"type": "Room", "id": self.id,
                                   "devices": self.devices, "groups": self.groups}
            jss.write("rooms", big_dict)

        def update_self(self):  # Python will be same as json
            big_dict = jss.read("groups")
            self.id = big_dict[self.name]["id"]
            self.devices = big_dict[self.name]["devices"]
            self.groups = big_dict[self.name]["groups"]

        def __contains__(self, devicename):
            return devicename in self.devices or devicename in self.groups

    #################################################

    def __init__(self):
        self.devices = {}
        self.groups = {}
        self.rooms = {}

        # Create all existing devices/groups/rooms which are in json files:

        devices = jss.read("devices")
        for name in devices:
            if devices[name]["type"] == "WhiteLamp":
                self.add_device(
                    self.WhiteLamp(name, id=devices[name]["id"], status=devices[name]["status"]))

            elif devices[name]["type"] == "ColorLamp":
                self.add_device(
                    self.ColorLamp(name, id=devices[name]["id"], status=devices[name]["status"]))

            elif devices[name]["type"] == "TemperatureSensor":
                self.add_device(self.TemperatureSensor(
                    name, id=devices[name]["id"], status=devices[name]["status"]))

            elif devices[name]["type"] == "AirQualitySensor":
                self.add_device(self.AirQualitySensor(
                    name, id=devices[name]["id"], status=devices[name]["status"]))

            elif devices[name]["type"] == "HumiditySensor":
                self.add_device(self.HumiditySensor(
                    name, id=devices[name]["id"], status=devices[name]["status"]))

            else:
                print("Error in Home.__init__()")

        groups = jss.read("groups")
        for name in groups:
            self.create_group(self.Group(
                name, groups[name]["id"], groups[name]["devices"]))

        rooms = jss.read("rooms")
        for name in rooms:
            self.create_room(
                self.Room(name, groups[name]["id"], groups[name]["devices"]))

    def __del__(self):  # Clear all the json files
        for i in [3, 2, 1]:
            print(f"Your home is going to explode in {i} seconds ...")
            sleep(1)
        print("Home deleted. (Of course it didn't explode)")

    def add_device(self, device):
        self.devices[device.name] = device

    def create_group(self, group):
        self.groups[group.name] = group

    def create_room(self, room):
        self.rooms[room.name] = room

    def del_device(self, name):
        copy = self.devices.copy()
        del self.devices[name]
        o = copy[name]
        del o
        del copy

    def del_group(self, name):
        copy = self.groups.copy()
        del self.groups[name]
        o = copy[name]
        del o
        del copy

    def del_room(self, name):
        copy = self.rooms.copy()
        del self.rooms[name]
        o = copy[name]
        del o
        del copy
