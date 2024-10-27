def get_time_timezone():
    '''(None) --> (int,int,int,float,float)
    Returns the current time trisected in hours, minutes, seconds. Along with that also returns the timezone1 and
    timezone2 as given by the user.
    '''
        
    # Prompt user to enter the current time in HH:MM:SS format
    while True:
        user_time = input("Enter the current time in 24-hour format (HH:MM:SS): ")
        
        # Check if the format is correct and parse hours, minutes, and seconds
        if len(user_time) == 8 and user_time[2] == ':' and user_time[5] == ':':
            try:
                hours = int(user_time[:2])
                minutes = int(user_time[3:5])
                seconds = int(user_time[6:])
                
                # Check if the hours, minutes, and seconds are in valid ranges
                if 0 <= hours < 24 and 0 <= minutes < 60 and 0 <= seconds < 60:
                    break
                else:
                    print("Invalid time values. Please enter a valid time.")
            except ValueError:
                print("Invalid input. Please enter time in the format HH:MM:SS using 24-hour clock.")
        else:
            print("Invalid format. Please enter time in the format HH:MM:SS using 24-hour clock.")

    # Prompt user to enter current timezone offset (e.g., UTC+2 for 2 hours ahead of UTC)
    while True:
        try:
            current_timezone = float(input("Enter the current timezone offset from UTC (e.g., -5 for UTC-5): "))
            break
        except ValueError:
            print("Invalid timezone format. Please enter a valid number for timezone offset.")

    # Prompt user to enter target timezone offset
    while True:
        try:
            target_timezone = float(input("Enter the target timezone offset from UTC (e.g., +9 for UTC+9): "))
            break
        except ValueError:
            print("Invalid timezone format. Please enter a valid number for timezone offset.")

    return hours, minutes, seconds, current_timezone, target_timezone


def time_difference(current_timezone , target_timezone):
    '''(float, float) --> float
    Return the difference between target timezone and the current timezone.
    '''

    ## Think how to calculate the difference between the target and the current ##
    ## Replace None with your code ##
    #TODO
    
    difference = target_timezone - current_timezone

    return difference


def convert_to_seconds(hours , minutes , seconds , difference):
    '''(int,int,int,float) --> (float , float)
    Returns the hours , minutes , seconds , difference all converted into seconds.
    '''

    ## Convert the current time given in hours , minutes and seconds into just seconds ##
    ## Replace None with your code ##
    #TODO

    current_time_in_sec = hours * 3600 + minutes * 60 + seconds

    ## Convert the timezone difference into seconds ##
    ## Remember: Timezones are always given in hours. Eg: +1.5 mean one and half hours ahead of ##
    ## greenwich mean time (GMT) ##
    ## Replace None with your code ##
    #TODO

    timezone_diff_in_sec = difference * 3600
    
    return current_time_in_sec, timezone_diff_in_sec
    

def target_timezone_time_in_sec(current_time_in_sec , timezone_diff_in_sec):
    '''(float,float) --> float
    Returns target time in seconds from current time and timezone difference.
    '''

    ## Think of a way to get the target time from the current_time_in_sec and timezone_diff_in_sec ##
    ## Remove the None and write your own code ##

    target_time_in_sec = current_time_in_sec + timezone_diff_in_sec

    return target_time_in_sec    
    

def reformat_target_time(target_time_in_sec):
    '''(float) --> (int , int, int)
    Return the calculated hour, minutes and seconds from the target time in seconds.
    '''
    
    # 计算小时，整除3600（每小时3600秒）
    target_hour = int(target_time_in_sec // 3600)
    # 处理小时数超过24的情况（例如，26小时应显示为2小时）
    target_hour = target_hour % 24

    # 计算剩余秒数
    remaining_sec = target_time_in_sec % 3600

    # 计算分钟数
    target_minutes = int(remaining_sec // 60)

    # 计算剩余秒数
    target_seconds = int(remaining_sec % 60)
    
    return target_hour, target_minutes, target_seconds
    

def actual_target_time(target_hour, target_minutes, target_seconds):
    '''(int,int,int) --> (str)
    Returns HH:MM:SS formated target time from the given target_hour, target_minutes, taget_seconds.
    '''

    ## Find a way to print the time in HH:MM:SS format ##
    ## Remove the pass command and fill your own code ##
    #TODO

    # formatted_time = f"{target_hour:02}:{target_minutes:02}:{target_seconds:02}"
    formatted_time = "{:02d}:{:02d}:{:02d}".format(target_hour, target_minutes, target_seconds)

    return formatted_time