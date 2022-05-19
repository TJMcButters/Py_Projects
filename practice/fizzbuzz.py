counter = 0
kg = True

while counter < 100:
    if counter % 2 == 0 and counter % 5 == 0 and counter != 0:
        print(f"{counter}: fizzbuzz")
    elif counter % 2 == 0 and counter != 0:
        print(f"{counter}: fizz")
    elif counter % 5 == 0 and counter != 0:
        print(f"{counter}: buzz")
    else:
        print(f"{counter}: ")
    counter += 1
    
