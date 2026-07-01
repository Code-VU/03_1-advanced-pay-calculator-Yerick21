def calculatePay():
    # This first line is provided for you

    try:
        hours = input("Enter Hours: ")
        hours = float(hours)

        hourlyRate = input("Enter Rate: ")
        hourlyRate = float(hourlyRate)
        
    except ValueError:
        print("Error, please enter numeric input")
        return


    if hours > 40:
        overtimeHours = hours - 40
        overtimePay = hourlyRate * 1.5 * overtimeHours
        hours = hours - overtimeHours
    else:
        overtimePay = 0
    print("Pay:", (hours * hourlyRate) + overtimePay)
        
 

    
    # end assignment

## if you want to test locally before you try to sync
## run > python payCalculator.py

#Ignore this for now. 
if __name__ == "__main__":
    calculatePay()
