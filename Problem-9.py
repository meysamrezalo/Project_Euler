#AhriMAN

# Since we need three numbers
# that equal 1000, we iterate
# up to 400 to save time.
# This because we know that
# a and b will be worth less than 400
# because a < b < c
for a in range(1, 400):
    for b in range(1, 400):
    
        # Find c bysubstracting a and b from 1000
        # There is no need to loop for c.
        c = (1000 - a) - b
    
        # each number must be smaller than the next
        if a < b < c:
        
            # check if numbers are pythagorean triplet
            if a**2 + b**2 == c**2:
            
                # calculate the product
                print("The answer is the final :" , [a * b * c])