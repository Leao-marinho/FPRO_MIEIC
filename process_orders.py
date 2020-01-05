"""
 3. Process orders

Consider sales records, given as a nested list with each invoice, of a sale, 
in the format (order number, book title and author, quantity, price per item). 
Write a Python function invoice_totals(orders, min) 
which returns a list with 2-tuples. 
Each tuple consists of the order number and the total 
(the product of the price per item by the quantity). 
The total should be increased by 10€ if the value of the order 
is smaller than the min value.

Hint: use a lambda function and the function map().

Example:
    Input: [[34587, 'Always Look on the Bright, Eric Idle', 4, 40.95]], 0 	
    Output: [(34587, 163.8)]


@author: Luísa Maria Mesquita
"""
def invoice_totals(orders, min):
    
    # x corresponds to each order of list orders
    f = lambda x: (x[0], x[2]*x[3] + 10) if (x[2]*x[3]) < min else (x[0], x[2]*x[3])
        
    alist = list(map(f, orders))
 
    return alist
        
    
