#bmi function

def calculate_bmi(height, weight):

    if height !=0 and isinstance(height, str) == False and isinstance(weight, str) == False and (type(height)==float or type(height)==int) and (type(weight)==float or type(weight)==int) and height>0 and weight>0 :
        bmi = weight/(height**2)
        return bmi

    else:
        return 0




