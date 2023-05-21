# A function is some stored code that we use. A function takes some input and produces an output
def computepay(h, r):
    if h > 40:
        regular_payment = r * 40
        overtime_payment = (h-40) * (r * 1.5)
        total_payment = regular_payment + overtime_payment
        return total_payment
hrs = float(input("Enter Hours:"))
rate = float(input("Enter rate: "))
p = computepay(hrs,rate)
print("Pay",p)