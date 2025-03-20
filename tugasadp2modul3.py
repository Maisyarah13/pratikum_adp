# Input nilai
lamda_t = float(input("Masukkan nilai lamda_t: "))
m = int(input("Masukkan nilai M      : "))

# Nilai e
e = 2.71828

# Perulangan untuk menghitung P(N(t) = n) untuk n = 0, 1, 2, ..., M
factorial_n = 1  # Nilai faktorial untuk n = 0
for n in range(m + 1 ):
    p = (e ** (-lamda_t)) * ((lamda_t) ** n) / factorial_n
    print(f'P(N(t) = {n})  adalah   = {p}')
    factorial_n = factorial_n * (n + 1) #Update faktorialnya



