def PatterntoNumber(Pattern):
    """
    This function converts DNA pattern to quaternary numeric system for faster computation
    Input: DNA Pattern as string
    Output: Quaternary numeric system as integer
    """
    
    #First, we create a variable called result and set it's value to 0
    result = 0
    
    #Then, we loop over index and values of Pattern using enumerate function, 
    #which a and b represent index and value respectively
    for a, b in enumerate(Pattern):
        
        #Checks if value equals to Adenine
        if b == "A":
            
            #Add result by below equation which 0 represent the quaternary numeric value for Adenine
            #and 4 represent the base-4 numerical system
            #and len(Pattern) - 1 - a represent the position of base in Pattern
            result = result + 0 * 4 ** (len(Pattern) - 1 - a)
            
        #Checks if value equals to Cytosine
        elif b == "C":
            
            #Add result by below equation which 1 represent the quaternary numeric value for Cytosine
            #and 4 represent the base-4 numerical system
            #and len(Pattern) - 1 - a represent the position of base in Pattern
            result = result + 1 * 4 ** (len(Pattern) - 1 - a)
        
        #Checks if value equals to Guanine
        elif b == "G":
            
            #Add result by below equation which 2 represent the quaternary numeric value for Guanine'
            #and 4 represent the base-4 numerical system
            #and len(Pattern) - 1 - a represent the position of base in Pattern
            result = result + 2 * 4 ** (len(Pattern) - 1 - a)
        
        #Checks if value equals to Thymine
        elif b == "T":
            
            #Add result by below equation which 3 represent the quaternary numeric value for Thymine
            #and 4 represent the base-4 numerical system
            #and len(Pattern) - 1 - a represent the position of base in Pattern
            result = result + 3 * 4 ** (len(Pattern) - 1 - a)
            
    return result
