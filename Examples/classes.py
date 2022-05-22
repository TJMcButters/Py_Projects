class Vehicle:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def get_make(self):
        return self.make
    
    def get_year(self):
        return self.year
    

def main():
    v = Vehicle("Ford", "Focus", 1992, "Silver")

if __name__ == "__main__":
    main()