import numpy as np 
data = np.random.randint(1000,5000,size=(12,5))
all_monthes_sales = []
month = 1
for rows in data : # مبيعات كل الشهور 
    month_sales = np.array(np.sum(rows))
    print (f"total sales of all the monthe {month} => {month_sales}")
    all_monthes_sales.append(month_sales)
    month+=1
print("#"*40)
#pranches 
pranch_sales = np.sum(data,axis=0)
print ("every pranchsales => ",pranch_sales)

#highest month &  lowest pranch
highiest_month =np.max(all_monthes_sales)
lowest_pranch =np.min(pranch_sales)
print ("highiest month sales = ",highiest_month)
print ("lowest pranch sales = ", lowest_pranch)
# the average sale
the_average_sale = np.average(data).__int__()
print(the_average_sale)
pranch_list = []
pranch_numper = 1
for pranch in pranch_sales :
    pranch_list.append([int(pranch) , pranch_numper])
    pranch_numper+= 1
print (pranch_list)
branches = np.array(pranch_list)
sorted_branches =branches[:,0].argsort()[::-1]
print (sorted_branches)
