import random

com=random.randint(1,100)
tries=0


while True:
    tries +=1
    hum=int(input("Guess Your Number between 1 and 100:-"))
    if hum==com:
        print(f"You Won in {tries} tries")
        break
    elif hum>com:
        print("Sorry wrong guess go lower!")
    elif hum<com:
        print("Sorry wrong guess go higher!")

