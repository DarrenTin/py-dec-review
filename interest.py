# Loan details
T = 600000
P = T * 0.9  # Loan principal in RM
r = 0.044   # Annual interest rate (4.4%)
n = 20      # Loan term in years
A = P * (r * (1 + r)*n) / ((1 + r)*n - 1)  # Annual payment

def calculate_interest_for_year(k):
    # Calculate remaining balance after k payments
    B_k = P * (1 + r)*k - (A / r) * ((1 + r)*k - 1)
    
    # Calculate interest for the k-th year
    interest_for_year = B_k * r
    return interest_for_year

print(f"Average monthly non-interest of {n} years = {T / n / 12}")

for year in range(1, n+1):
    interest = calculate_interest_for_year(year) / 12
    print(f"Year {year}: Monthly interest = RM{interest:.2f}; House payment = RM{3000 - interest:.2f}")