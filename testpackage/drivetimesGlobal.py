drive_times_input = input(f"Enter drive times (|-separated): ")
drive_times_str = drive_times_input.split("|")
drive_times =[]
for time_str in drive_times_str:
   time =float(time_str)
   drive_times.append(time)


stats = []
stats.append(min(drive_times))
stats.append(max(drive_times))
total_time = 0.0
for time in drive_times:
   total_time += time
stats.append(total_time / len(drive_times))


print(f"Average drive time: {stats[2]:.2f} seconds")
print(f"Fastest drive: {stats[0]:.2f} seconds")
print(f"Slowest drive: {stats[1]:.2f} seconds")