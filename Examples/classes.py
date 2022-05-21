class Vehicle:
    def __init__(self, make, model, year: int, color):
        self.make = make
        self.model = model
        self.year: int = year
        self.color = color

    def get_make(self):
        return self.make
    
    def get_year(self):
        return self.year
    

def main():
    v = Vehicle("Ford", "Focus", "hello", "Silver")
    print(v.get_year())

if __name__ == "__main__":
    main()