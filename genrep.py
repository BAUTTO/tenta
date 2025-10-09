print('Ei24 - genrep praktiskt prov HT25')

r_string = input('Ange resistorer: ')

if r_string == '':
    print('Serieresistans: 0')
    print('Parallelresistans: 0')
else:
    r_list = r_string.split()

    r_int = []
    for i in r_list:
        r_int.append(float(i))

    r_paral = 0
    r_serie = 0

    for i in r_int:
        r_serie = r_serie + i
        r_paral = r_paral + 1 / i
    
    print(f"Serieresistans: {r_serie}")
    print(f"Parallelresistans: {1 / r_paral}")
