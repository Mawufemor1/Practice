# array of integers (input)
# find sum of all elements
# find the average the element in the array(ages of people)
# categorize teenager , adult, child
# child(1-12), teenager(13-19), youth(20 - 40), adult(above 40)
# sort ages in both descending and ascending order
# median age , max age , min age
# standard deviation , variance

import math

child =[]
teen = []
youth = []
adult = []


# Array taking input of ages
def age() -> list[int]:
    print('Enter ages')
    ages = []
    for i in range(10):
        a = int(input())
        ages.append(a)
    
    return(ages)    


n_age = age()
new_age = n_age.copy()

# Sum of ages
sum_ages = 0
for i , old in enumerate(new_age):
    sum_ages += old


#Average of ages
average_age = sum_ages/len(new_age)


# Ages in ascending order
def ascending(new_age):
    n = len(new_age)
    for i in range(n-1):
        for j in range(n-1-i):
            if new_age[j] > new_age[j +1]:
                new_age[j] , new_age[j+1] = new_age[j+1], new_age[j]
    return new_age     

sorted_age = ascending(new_age)
sort_age = sorted_age.copy()


#Ages in descending order
def descending(new_age):
    n = len(new_age)
    for i in range(n-1):
        for j in range(n-1-i):
            if new_age[j] < new_age[j +1]:
                new_age[j] , new_age[j+1] = new_age[j+1], new_age[j]
    return new_age    


# Categorization of ages
for i, old in enumerate(new_age):
    if old in range(1,13):
        child.append(old)
    elif old in range(13,20):
        teen.append(old)
    elif old in range(20,41):
        youth.append(old)
    else:
        adult.append(old)

#Maximum and Minimum age
maximum = sort_age[-1]
minimum = sort_age[0]

#Median
n = len(sort_age)
if n % 2 == 0:
    median1 = sort_age[n//2]
    median2 = sort_age[n//2-1]
    median = (median1 + median2) / 2

else:
    median = sort_age[n//2]

# Variance and Standard Deviation
variance = sum((i - average_age) ** 2 for i in sort_age) / n
standard_deviation = math.sqrt(variance)


print("Sum of all ages: ", sum_ages)
print("Average age: ", average_age)
print("Ages categorised as a child: ", child)
print("Ages categorised as a teen: ", teen)
print("Ages categorised as a youth: ", youth)
print("Ages categorised as a adult: ", adult)
print("Ages in ascending order: ", ascending(new_age))
print("Ages in descending order: ", descending(new_age))
print("Median age: ", median)
print("Maximum age: " , maximum)
print("Minimum age: ", minimum)
print("Variance: " ,variance)
print("Standard Deviation: ", standard_deviation)
  
  

    
        


                                              
            
            



    
    

        






    

        


            

            
            
        

    

