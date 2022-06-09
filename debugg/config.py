from configparser import ConfigParser
from logging import config


config_object = ConfigParser()

config_object["USERINFO"] = {
    "admin": "Chankey Pathak",
    "loginid": "chankeypathak",
    "password": "tutswiki"
}

config_object["SERVERCONFIG"] = {
    "host": "tutswiki.com",
    "port": "8080",
    "ipaddr": "8.8.8.8"
}
config_object["USERDATA"]={
    "hostname":"api12",
    "port":"8010",
    "ip":"192.123.213.12"
}
config_object["USERVALID"]={
    "hostvalid":"samirvarious",
    "port":"8120",
    "ip":"123.123.213.11"
}
config_object["DATA"]={
    "variable":"shubham"
}

with open('config.ini', 'w') as conf:
    config_object.write(conf)
