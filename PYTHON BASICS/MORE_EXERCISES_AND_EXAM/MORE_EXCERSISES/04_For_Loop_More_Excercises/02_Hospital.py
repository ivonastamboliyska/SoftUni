period_of_time = int(input())
doctors_count = 7
patients_healed = 0
patients_sent_in_other_hospital = 0
day_of_monitoring = 0

for days in range(1, period_of_time + 1):
    patients_per_day = int(input())
    if patients_per_day <= doctors_count:
        patients_healed += patients_per_day
        day_of_monitoring += 1
        if patients_healed < patients_sent_in_other_hospital and day_of_monitoring == 2:
            doctors_count += 1

    elif patients_per_day > doctors_count:
        patients_healed += doctors_count
        patients_sent_in_other_hospital += patients_per_day - doctors_count
        day_of_monitoring += 1
        if patients_healed < patients_sent_in_other_hospital and day_of_monitoring == 2:
            doctors_count += 1


print(f"Treated patients: {patients_healed}.")
print(f"Untreated patients: {patients_sent_in_other_hospital}.")

