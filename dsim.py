class diskSim():

    def __init__(self):
        self.locations = []
        self.algorithm = None
        self.size = 0
        self.direction = "R"
        return

    def setupParams(self):
        choice = False
        while not choice:
            print("// PARAMETER SETTINGS //\n 1. Set ssek algorithm\n 2. Set disk size\n 3. Help\n 4. Back")
            valid_responses = ["1","2","3","4"]
            res = input("Choice: ")
            if res in valid_responses:
                if res == "1":
                    self.setAlgo()
                elif res == "2":
                    self.setDiskSize()
                elif res == "3":
                    print("\n// HELP //\nHelpful info goes here.\n")
                else:
                    self.textUI()
            else:
                print("Invalid input, please enter one of the following: ")
    def textUI(self):
        choice = False
        while not choice:
            print("// MAIN MENU //\n 1. Setup disk parameters\n 2. Simulate operations\n 3. Help\n 4.Quit")
            valid_responses = ["1","2","3","4"]
            res = input("Choice: ")
            if res in valid_responses:
                if res == "1":
                    self.setupParams()
                elif res == "2":
                    self.setupSimulator()
                elif res == "3":
                    print("\n// HELP //\nHelpful info goes here.\n")
                else:
                    quit()
            else:
                print("Invalid input, please enter one of the following: ")

def main():
    ds = diskSim()
    ds.textUI()

if __name__ == "__main__":
    main()
