print("*** Rabbit & Turtle ***")

d, Vr, Vt, Vf = [float(i) for i in input("Enter Input : ").split()]


Vt_r = Vt - Vr

D = Vf * (d/Vt_r)

print("{:.2f}".format(float(D)))