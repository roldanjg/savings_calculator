monthly_added_capital = 500
curr = 'eur'
starting_capital = 5800
years = 17
months = years*12
annual_interest = 4.7
taxes = 0.21

daily_interest = (annual_interest/100)/365
computed_capital = starting_capital

final_profits_before_taxes = 0
final_savings = starting_capital
for month in range(1,months,1):
    profit = (computed_capital * daily_interest)*30
    final_profits_before_taxes += profit
    final_savings += monthly_added_capital

    computed_capital = computed_capital + monthly_added_capital + profit

print(
f"After {str(years)} years: \n\
Savings: {str(final_savings)} {curr}  \n\
Profits after taxes:{str((final_profits_before_taxes*(1-taxes)))} {curr}"
)

