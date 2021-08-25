
from flask import Flask, request, render_template
import datetime as dt
import csv

# import packages
import time
import constants
from PIL import Image

# import local classes
import Plant
import Tank 
import Pump

# initialize the flask application
app = Flask(__name__)

SAVE_FILE = "plants.csv"

Plants = []

pump_time = 10

# initialize the gpio pin that 
# will control when the water pump 
# should run
#pump = Pump.Pump(pin = 17, pump_rate = 1)

# intialize the tank object
tank = Tank.Tank(0,0)

'''       
def water(pump_time):
    ''' '''function to water the plant chain by running the pump''' '''
    
    # run water for specified amount of time
    pump.run(pump_time)

    # subtract the amount of water used from the tank
    tank.currentVol = tank.currentVol - (pump.pump_rate * pump_time)

    # test if the tank is empty
    if tank.currentVol == 0:
        # call the empty tank handler when the tank is empty
        tank_empty()

    return
'''
'''
def tank_empty():
    '''''' warns when the water tank is empty''' '''

    print('Water tank is empty.')

    tank.tank_empty.on()
'''
'''def tank_reset():
    '''''' reset the tank current capacity to full when 
        the reset button is pushed ''''''

    print('The tank has been refilled.')

    # reset tank capacity to full
    tank.reset()

    # turn off the empty light
    tank.empty_light.off()
'''

@app.route("/addplant", methods=["POST"])
def addPlant(): 
    ''' adds a plant to the chain'''

    # get the information from the form
    species = request.form.get("species")
    nickname = request.form.get("nickname")
    size = request.form.get("size")

    # create new plant object
    newPlant = Plant.Plant(species, nickname, size)

    # add new plant to list
    if not Plants.append(newPlant):
        print("New plant added!")

        with open(SAVE_FILE, 'a', newline='\n') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([newPlant.species, newPlant.nickname, newPlant.size])

            csvfile.close()

        return render_template("myplants.html", Plants = Plants)

    # if anything goes wrong 
    else:
        print("Error, new plant not added to chain.")
        return render_template("error.html")
    

@app.route("/")
def index():
    ''' starts the web server at landing page '''
    # start webpage at index.html (home page)
    return render_template("index.html")

@app.route("/todo")
def todo():
    return render_template("todo.html")

@app.route("/myplants")
def myplants():
    return render_template("myplants.html", Plants = Plants)

@app.route("/add")
def add():
    return render_template("add.html")

@app.route("/readme")
def readme():
    return render_template("readme.html")

@app.route("/status")
def status():
    return render_template("status.html")

def main():
    ''' main method '''

    # initialize the main plant chain from the backup save file
    with open (SAVE_FILE, newline= '\n') as csvfile:
        reader = csv.reader(csvfile, delimiter = ',')
        for row in reader:
            newplant = Plant.Plant(row[0], row[1], row[2])
            Plants.append(newplant)
        
        csvfile.close

    app.run()

main()