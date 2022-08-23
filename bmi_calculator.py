person_height = float(input("Enter your height in centimeters: "))

person_weight = float(input("Enter your weight in kilograms: "))

height = person_height/100

weight = person_weight

body_mass_index = weight / (height ** 2)

print(f'Your body mass index is {body_mass_index}')

if (body_mass_index > 0):
    
    if (body_mass_index <= 16.5):
        print(f'You are severely underweight')
    
    elif (body_mass_index <= 18.5):
        print(f'You are underweight')

    elif (body_mass_index <= 24.5):
        print(f'You are healthy')

    elif (body_mass_index <= 29.5):
        print(f'You are overweight')

    else:
        print(f'You are severely overweight')
        
else:
    print("Enter the correct details for height and weight")






