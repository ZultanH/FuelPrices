from commandmodule import CmdNotFound, Command, commandList
from commands import helpCmd, exitCmd, summaryCmd, fuelPricesCmd, cheapestPriceCmd, mostExpensivePriceCmd
from clint.textui import colored


config = {}
config["fuel_type"] = "ulp91"

def getFuelType():
    fuelTuple = (
        "Unleaded 91", 
        "Premium Unleaded 95", 
        "Premium Unleaded 98", 
        "Diesel", 
        "Premium Diesel", 
        "LPG", 
        "e10"
    )

    fuelConversion = {
        "unleaded 91": "ulp91",
        "premium unleaded 95": "ulp95",
        "premium unleaded 98": "ulp98",
        "diesel": "diesel",
        "premium diesel": "pdiesel",
        "lpg": "lpg",
        "e10": "e10"
    }

    print("Fuel Options:\n")
    for fuelName in fuelTuple:
        print(colored.green(fuelName + "\n"))
    
    userChoice = input("Which one would you like to view prices for? ")

    if userChoice.lower() not in [name.lower() for name in fuelTuple]:
        print("Could not find fuel ... retrying.\n")
        main()
    
    userChoice = fuelConversion[userChoice.lower()]
    config["fuel_type"] = userChoice

def printBanner():
    printList = (("-" * 20), "\n", "FUEL PRICES", ("-" * 20), "\n")

    for i in range(len(printList)):
        print(colored.green(printList[i]))

def makeCmds():
    cmds = [
        ("help", helpCmd), 
        ("exit", exitCmd), 
        ("summary", summaryCmd),
        ("prices", fuelPricesCmd),
        ("cheapest", cheapestPriceCmd),
        ("mostexpensive", mostExpensivePriceCmd)
    ]

    for cmdTuple in cmds:
        cmdName = cmdTuple[0]
        cmdFunc = cmdTuple[1]
        Command(cmdName, cmdFunc)
        
def main():
    command = input("Please enter a command ")
    try:
        Command.doCmd(command, config)
    except CmdNotFound:
        print(colored.red("Incorrect Command name, retrying... "))
        main()
    main()

if __name__ == "__main__":
    printBanner()
    getFuelType()
    makeCmds()
    main()