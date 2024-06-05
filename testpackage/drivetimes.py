def get_drive_times(drive_times_input: str)-> list:
    '''
    This function takes the user input, extracts the values for each drive time
    and adds them to a list. The function will then return the list with drive times.
    Usage example: get_drive_times("100.1|80|89.9") must return [100.1|80.0|89.9]
    '''
    drive_times_str = drive_times_input.split("|")
    drive_times =[]
    for time_str in drive_times_str:
        time =float(time_str)
        drive_times.append(time)
    return drive_times
      

def get_stats(drive_times: list) -> list:
    '''
    This function takes list with drive times, calculates the min, max and average 
    drive times which are added in this order to a list. The function will then 
    return the list with min, max and average drive times.
    Usage example: get_stats([100.1,80.0,89.9]) must return [80.0,100.1,90.0]
    '''
    stats = []
    stats.append(min(drive_times))
    stats.append(max(drive_times))
    total_time = 0.0
    for time in drive_times:
        total_time += time
    stats.append(total_time / len(drive_times))
    return stats
    

def main() -> None:
    '''
    This function asks the user for the driver's name, and then asks for their
    drive times  (all values in one line and separated by |). 
    Then it calls get_drive_times and get_stats to get the min, max and average 
    drive times. Lastly it prints these values.
    '''
    drive_times_input = input(f"Enter drive times (|-separated): ")
    stats = get_stats(get_drive_times(drive_times_input))
    print(f"Average drive time: {stats[2]:.2f} seconds")
    print(f"Fastest drive: {stats[0]:.2f} seconds")
    print(f"Slowest drive: {stats[1]:.2f} seconds")
