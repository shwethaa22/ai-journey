total_bill = int(float(input("Bill please: "))*100)
no_of_ppl = int(input("Ppl count pls: "))
tip_percentage = int(float(input("Tip Percentage pls: "))*100)
tip_amount = total_bill*tip_percentage/100
grand_total=total_bill+tip_amount
per_person_cost=grand_total//no_of_ppl
print("="*30)
print(f"{' '*7}BILL SPLITTER")
print("="*30)
print(f"Tip amount : {tip_amount:.2f}")
print(f"Grand Total : {grand_total:.2f}")
print(f"Cost of each : {per_person_cost:.2f}")
print(f"LEft over: {int(grand_total%no_of_ppl)}")
print("="*30)



