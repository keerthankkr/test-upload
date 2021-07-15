from monthcalc import *
    
def calculate_capital_gain(num_shares,purchase_price,sale_price):
    
    tot_purchase_price= num_shares * purchase_price        #calculate total purchase price of all shares
   
    tot_sale_price= num_shares * sale_price                #calculate total sale price of all shares
    
    capital_gain=tot_sale_price-tot_purchase_price         #calculate capital gain
    
    print("Total purchase value = ", tot_purchase_price)
    print("Total sale value     = ", tot_sale_price)
    print("Capital gains        = ", capital_gain)
    return capital_gain;

def tax_rate(gross_income):
    if(gross_income<=18200):
       tax=0
    elif(gross_income>=18201 and gross_income<=37000):
       tax=19
    elif(gross_income>=37001 and gross_income<=90000):
       tax=32.5
    elif(gross_income>=90001 and gross_income<=180000):
       tax=37
    else:
        tax=45
    return tax;    
    
def calculate_tax(taxable_capital_gain,gross_income):
    applied_tax_rate=tax_rate(gross_income)
    tax =(applied_tax_rate*taxable_capital_gain)/100
    
    print("Taxable Capital Gains:",taxable_capital_gain)
    print("Tax Due:",tax)
    

def main_func():
    
    for i in range(3):    
        
        purchase_date=input("Purchase Date(YYYY-MM-DD)")#input purchase  dates of the shares
        sale_date=input("Sale Date(YYYY-MM-DD)")#input sale dates of the shares
        num_shares=int(input("Number of shares"))#input number of shares 
        purchase_price=float(input("Purchase price per unit"))#input purchase and sale price of the shares per unit
        sale_price=float(input("Sale price per unit"))#input sale price of the shares per unit
        gross_income=float(input("Client's annual gross income")) #input Client's annual gross income
                
        capital_gain=calculate_capital_gain(num_shares,purchase_price,sale_price);
        print(capital_gain)
        
        if(capital_gain>0): 
            if(twelve_month_apart(purchase_date,sale_date)):
                print("The Stock Held for more than 12 months or more.\nClient is eligible for 50% discount on capital gains")
                taxable_capital_gain=0.5*capital_gain    #50% of capital gain is taxable
            else:
                taxable_capital_gain=capital_gain
            calculate_tax(taxable_capital_gain,gross_income)
                    
        else:
            print("Client made a capital loss. No taxes are applicable.")

    return;
    
main_func()    




 
