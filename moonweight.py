import sys

def moon_weight():
    print("Please enter your current earth weight")
    weight = int(sys.stdin.readline())
    print("Please enter the amount your weight might increase each year")
    increase = int(sys.stdin.readline())
    print("Please enter the number of years you want to spend on the moon!")
    years = int(sys.stdin.readline())
    for year in range(0, years):
        moon_weight = weight * 0.165
        weight = weight + increase
        print("On year %s I weighed %s lbs. on the moon as I gained %s earth lbs. per year" % (year + 1, moon_weight, increase))

moon_weight()
