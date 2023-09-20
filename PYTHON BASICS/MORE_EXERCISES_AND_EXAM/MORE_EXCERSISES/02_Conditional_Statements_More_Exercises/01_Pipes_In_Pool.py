volume_of_pool_in_liters = int(input())
first_pipe_debit_per_hour = int(input())
second_pipe_debit_per_hour = int(input())
hours_without_staff = float(input())

first_pipe_volume = first_pipe_debit_per_hour * hours_without_staff
second_pipe_volume = second_pipe_debit_per_hour * hours_without_staff
total_volume = first_pipe_volume + second_pipe_volume

first_pipe_volume_in_percent = first_pipe_volume / total_volume * 100
second_pipe_volume_in_percent = second_pipe_volume / total_volume * 100
total_volume_in_percent = total_volume / volume_of_pool_in_liters * 100

if total_volume < volume_of_pool_in_liters:
    print(f"The pool is {total_volume_in_percent:.2f}% full. Pipe 1: {first_pipe_volume_in_percent:.2f}%. Pipe 2: {second_pipe_volume_in_percent:.2f}%.")
elif total_volume > volume_of_pool_in_liters:
    difference = volume_of_pool_in_liters - total_volume
    print(f"For {hours_without_staff} hours the pool overflows with {abs(difference)} liters.")


