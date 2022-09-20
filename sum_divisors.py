import math
def sum_divisors(n) : 

    # Final result of summation of divisors 
    result = 0
    
       # find all divisors which divides 'num' 
    i = 2
    while i<= (math.sqrt(n)) : 

        # if 'i' is divisor of 'num' 
        if (n % i == 0) : 

            # if both divisors are same then 
            # add it only once else add both 
            if (i == (n / i)) : 
                result = result + i; 
            else : 
                result = result +  (i + n//i); 
        i = i + 1

    # Add 1 to the result as 1 is also  
    # a divisor 
    return (result + 1); 
    

print(sum_divisors(3)) # Should sum of 1
# 1
print(sum_divisors(36)) # Should sum of 1+2+3+4+6+9+12+18
# 55
print(sum_divisors(102)) # Should be sum of 2+3+6+17+34+51
# 114
