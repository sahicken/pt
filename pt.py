#!/usr/bin/python3

import json
import PySimpleGUI as sg

f=open("res/Periodic-Table-JSON/PeriodicTableJSON.json")
pt=json.load(f)
f.close()

# init layout
layout = []
for y in range(10):
    layout.append([])
    for x in range(18):
        layout[y].append(sg.Button("", size=(2,2)))
for e in pt['elements']:
    layout[e['ypos']-1][e['xpos']-1]=sg.Button(e['symbol'], size=(2,2))

def simple_gui():
    event, values = sg.Window('Periodic Table', layout).read(close=True)

if __name__=="__main__":
    simple_gui()
