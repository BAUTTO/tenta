# Author: Santiago Bautista
# Date: 2025-10-07
print("Ei-24 genrep praktiskt prov HT25")


user_input = input("Ange resistorer: ")

if not user_input.strip():
    print("Serieresistans: 0")
    print("Parallelresistans: 0")

else: 

    resistors = [float(r) for r in user_input.split()]
    r_series = sum(resistors)
    r_parallel = 1 / sum( 1 / r for r in resistors )

    print("Seriesresistans:", r_series)
    print("Parallelresistans:", r_parallel)



