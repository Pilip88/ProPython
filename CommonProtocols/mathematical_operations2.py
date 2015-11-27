def hours_and_minutes(minutes):
	return minutes // 60, minutes % 60

print(hours_and_minutes(36))
print(hours_and_minutes(60))
print(hours_and_minutes(137))
print(hours_and_minutes(4343433))