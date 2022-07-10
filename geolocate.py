import geocoder
import folium
from art import *
import time
import os
import webbrowser
import requests

os.system("color b")
os.system("cls")
tprint("emirtools")

time.sleep(1)

myip = requests.get('https://icanhazip.com/')
print(f'my ip addr is --> {myip.text}')
print("\n")
xx = input("ip --> ")

ip = geocoder.ip(str(xx))

location = ip.latlng

map = folium.Map(location=location, zoom_start=10)
folium.CircleMarker(location=location, radius=50, color="red").add_to(map)
folium.Marker(location).add_to(map)

map

map.save("location.html")

print(ip.city)
print(ip.latlng)

url = "file://C:/Users/lenovo/Documents/aaa/location.html" # add your location.html file path if do not change you cant see location on map!
webbrowser.open(url,new=2)

time.sleep(2)
os.remove("C:/Users/lenovo/Documents/aaa/location.html") # add location.html path needs for deleting old location.html file
