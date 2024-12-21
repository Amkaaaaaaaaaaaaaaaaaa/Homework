#Huwisagchid utga uguh
def calc_F(A, K, L):
    F=A * (K**0.3)*(L**0.7)
    return F

A = float(input("А тоог оруулна уу: "))
K = float(input("K тоог оруулна уу: "))
L = float(input("L тоог оруулна уу: "))

F = calc_F(A, K, L)

print(F)