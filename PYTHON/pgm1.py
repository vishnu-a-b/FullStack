unit=float(input('Enter the Unit : '))

if(unit<=50):
    result=unit*0.5
elif(unit<=150):
    result=25+(unit-50)*0.75
elif(unit<=250):
    result=100+(unit-150)*1.2
else:
    result=220+(unit-250)*1.5
print(result)