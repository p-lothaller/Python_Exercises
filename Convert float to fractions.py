import math

# Convert floats to fractions.
def float2fraction(f, max_denominator):
    if math.isinf(f) != True and math.isnan(f) != True:
        print('x')
        g = abs(f)
        lst = []
        denominator = 1
        numerator = 1
        num = numerator/denominator
        while denominator < max_denominator:
            if g < num:
                denominator += 1
                numerator = round(denominator*f)
                num = numerator/denominator
                if math.isclose(f, num, rel_tol=0.01):
                    lst.append((numerator,denominator))
            elif g > num:
                numerator += 1
                num = numerator/denominator
                if math.isclose(f, num, rel_tol=0.01):
                    lst.append((numerator, denominator))
            elif g == num:
                lst.append((numerator, denominator))
                break    
        while len(lst)!=1:
            if abs( g - lst[0][0]/lst[0][1]) <= abs( g - lst[1][0]/lst[1][1]):
                del lst[1]
            else:
                del lst[0]
        if f < 0:
            tuple_change = list(lst[0])
            lst = [(-tuple_change[0], tuple_change[1])]
            
        return print(lst[0])
    else: 
        return print(None)
print(math.isnan(float('nan')))   
float2fraction(0.333, 100)

