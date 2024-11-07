def floor_num_from_binary(binary_floor):
    '''(str) --> (int)
    Returns the decimal floor number of the blue tower from the
    4 bit binary floor number given by binary_floor.
    '''
    
    ##TODO: Write your code below by removing the None and setting up your 
    # own logic. It would be more than 1 line so think carefully. ##
    
    floor_num = 0
    for i, bit in enumerate(reversed(binary_floor)):
        floor_num += int(bit) * (2 ** i)
    
    return floor_num

def paint_binary(floor_num):
    '''(int) --> (str)
    Returns the 4-bit binary floor number given the
    actual floor number you are in.
    '''

	##TODO: Write your code below by removing the None and setting up your 
    # own logic. It would be more than 1 line so think carefully. ##

    assert 0 <= floor_num <= 15, f"Given {floor_num} is out of 4-bit binary range (0-15)"
    binary_num = ""
    for i in range(3, -1, -1):
        if floor_num >= 2 ** i:
            binary_num += "1"
            floor_num -= 2 ** i
        else:
            binary_num += "0"
    
    return binary_num

def floor_num_from_binary_v2(binary_floor):
    '''(str) --> (int)
    Makes use of Python's in-built function to convert
    binary floor number to int and returns it.
    '''
    ##TODO: Write your code below by removing the None and setting up your 
    # own logic. ##
    
    floor_num = int(binary_floor, 2)
    
    return floor_num

def paint_binary_v2(floor_num):
    '''(int) --> (str)
    Makes use of Python's in-built function to convert
    integer valued floor number you are in and returns
    it.
    '''

	##TODO: Write your code below by removing the None and setting up your 
    # own logic. It would be more than 1 line so think carefully. ##
    
    assert 0 <= floor_num <= 15, f"Given {floor_num} is out of 4-bit binary range (0-15)"
    
    binary_num = "{:0>4b}".format(floor_num)
    
    return binary_num