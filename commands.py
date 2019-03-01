from commandmodule import CmdNotFound, Command, commandList
from fuelmodule import FuelModule
from clint.textui import colored

import sys

def helpCmd(config):
    for cmdName in commandList: 
        print("Command: {}\n".format(cmdName))

def exitCmd(config):
    print(colored.red("Goodbye ... \n"))
    sys.exit()

def summaryCmd(config):
    newModule   = config["fuel_type"] is "ulp91" and FuelModule() or FuelModule(fuel_type=config["fuel_type"])
    fuelObject  = newModule.createObject()
    fuelSummary = fuelObject["summary"]

    print(colored.green("Summary:\n{}\n".format(fuelSummary)))

def fuelPricesCmd(config):
    newModule       = config["fuel_type"] is "ulp91" and FuelModule() or FuelModule(fuel_type=config["fuel_type"])
    fuelObject      = newModule.createObject()
    sortedPrices    = fuelObject["sorted_prices"]

    for fuelTuple in sortedPrices:
        location    = fuelTuple[0]
        price       = fuelTuple[1]

        print(colored.green("Location: {}\nPrice: ${}/L\n\n".format(location, str(price))))

def cheapestPriceCmd(config):
    newModule       = config["fuel_type"] is "ulp91" and FuelModule() or FuelModule(fuel_type=config["fuel_type"])
    fuelObject      = newModule.createObject()
    sortedPrices    = fuelObject["sorted_prices"]
    cheapestPrices  = [fuelTuple for fuelTuple in sortedPrices if fuelTuple[1] == sortedPrices[0][1]]
    
    for fuelTuple in cheapestPrices:
        location    = fuelTuple[0]
        price       = fuelTuple[1]

        print(colored.green("Cheapest Prices:\nLocation: {}\nPrice: ${}/L\n\n".format(location, str(price))))


def mostExpensivePriceCmd(config):
    newModule       = config["fuel_type"] is "ulp91" and FuelModule() or FuelModule(fuel_type=config["fuel_type"])
    fuelObject      = newModule.createObject()
    sortedPrices    = fuelObject["sorted_prices"]
    expensivePrices = [fuelTuple for fuelTuple in sortedPrices if fuelTuple[1] == sortedPrices[-1][1]]
    
    for fuelTuple in expensivePrices:
        location    = fuelTuple[0]
        price       = fuelTuple[1]

        print(colored.green("Most Expensive Prices:\nLocation: {}\nPrice: ${}/L\n\n".format(location, str(price))))