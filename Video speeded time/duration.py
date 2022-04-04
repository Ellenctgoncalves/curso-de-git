def calculate_extra_time(hours, minutes, seconds, playback_speed):
	previous_duration_in_seconds = convert_time_to_seconds(hours, minutes, seconds)

	speeded_time = previous_duration_in_seconds/playback_speed
	extra_time = previous_duration_in_seconds - speeded_time

	return convert_seconds_to_time(extra_time)

def convert_time_to_seconds(hours, minutes, seconds):
	new_seconds = seconds + (minutes * 60) + (hours * 60 * 60)
	return new_seconds

def convert_seconds_to_time(seconds_to_convert):
	time = []
	seconds = seconds_to_convert % 60
	seconds_to_convert -= seconds 
	minutes = seconds_to_convert / 60
	if minutes>=60:
		hours = minutes / 60
		minutes = minutes % 60 
	else:
		hours = 0

	seconds = str(int(seconds))
	minutes = str(int(minutes))
	hours = str(int(hours))

	return hours+":"+minutes+":"+seconds

if __name__ == "__main__":

	previous_hours = int(input("Hora: "))
	previous_minutes = int(input("Minutos: "))
	previous_seconds = int(input("Segundos: "))
	speed = float(input("Velocidade: "))

	new_time = calculate_extra_time(previous_hours, previous_minutes, previous_seconds, speed)
	print(f'Novo tempo: {new_time}')
