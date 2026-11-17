price = float(input("input price: "))
amount = float(input("input amount: "))

total = price * amount

if total >= 50:
   #We are calculating 10 percent of the total
   discount = 0.10 * total
   final_total = total - discount
   print(final_total)
else:
    print (total)