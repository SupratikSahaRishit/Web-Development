def total_calc(bill_amount,trip_perc):
    total = bill_amount*(1 + 0.01*trip_perc)
    total = round(total,2)

    print(f"Please pay $[total]")

total_calc(150,20)
