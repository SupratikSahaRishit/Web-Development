import math

def calculate_trig_functions():
    print("--- Trigonometry Calculator (Sin, Cos, Tan) ---")
    
    try:
        degrees = float(input("Enter the angle in degrees: "))
        radians = math.radians(degrees)
        sine = math.sin(radians)
        cosine = math.cos(radians)
        tangent = math.tan(radians)
        
        print(f"\nResults for {degrees}°:")
        print(f"Sin({degrees}) = {round(sine, 4)}")
        print(f"Cos({degrees}) = {round(cosine, 4)}")
        
        if abs(cosine) < 1e-10:
            print(f"Tan({degrees}) = Undefined (Vertical Asymptote)")
        else:
            print(f"Tan({degrees}) = {round(tangent, 4)}")
            
    except ValueError:
        print("Invalid input. Please enter a numerical value.")

if __name__ == "__main__":
    while True:
        calculate_trig_functions()
        if input("\nCalculate another? (y/n): ").lower() != 'y':
            break
