import random

def generate_number():
    num = random.randint(1, 100)
    print(f"Generated number: {num}")
    if num > 90:
        print(" Lucky! That's a great number!")

if __name__ == "__main__":
    generate_number()
