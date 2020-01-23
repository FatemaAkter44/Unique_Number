print(''' "715*46=32890 is the only unque number. Please check it Below."\n''')

def find_occurrence(num, dig):
    cnt=0
    while num>0 :
        rem=num%10
        if rem==dig:
            cnt = cnt+1
        num=int(num/10)
    return cnt

num1ok=1
num2ok=1
product_ok=1
num1 = int(input('Enter Three digit number start with 7:  '))
num2 = int(input('Enter Two digit number start with 4:  '))

if (int(num1/100)==7) and (int(num2/10)==4):
    for digit in range(0, 9):
        if find_occurrence(num1, digit)>1:
            num1ok=0
        if find_occurrence(num2, digit)>1:
            num2ok=0

    product=num1*num2

    if int(product/10000)==3 :
        for digit in range(0, 9):
            if find_occurrence(product, digit)>1:
                product_ok=0
                    
    if (num1ok==1) and (num2ok==1) and (product_ok==1):
        print("Unique five digit output  = ",product)
    else:
        print("Input or output have repeated number")
        
else:
  print("Invalid input Number")