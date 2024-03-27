class Car:
    car_type = 'CNG'

    def __init__(self, seats):
        self.seats = seats

    # static method
    def is_legal(age):
        if age >= 18:
            return True
        else:
            return False

def main():
    carOne = Car(4)

    print(Car.is_legal(17))

if __name__ == '__main__':
    main()
        
