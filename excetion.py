class vehicle:
    def fuel(self):
        return true
    def ac(self):
        pass
class car:
    def ac(self):
        return true
class bike:
    def ac(self):
        return false

class abstration:
    def main():
        c=car()
        b=bike()
        print("car fuel:",c.fuel())
        print("car ac:",c.ac())
        print("bike fuel:",b.fuel())
        print("bike ac:",b.ac)
        return
abstration.main()
        
        
