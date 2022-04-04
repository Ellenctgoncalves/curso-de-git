def calculate_new_duration(duration, playback_speed):
	hours, minutes, seconds = time_convertor_string_to_time(duration)
	previous_duration_in_seconds = convert_time_to_seconds(hours, minutes, seconds)

	try:
		new_duration = previous_duration_in_seconds / playback_speed
		return convert_seconds_to_time(new_duration)
	except:
		print("Tem algo de errado aqui!")

def convert_time_to_seconds(hours, minutes, seconds):
	new_seconds = seconds + (minutes * 60) + (hours * 60 * 60)
	return new_seconds

def convert_seconds_to_time(seconds_to_convert):
	seconds = seconds_to_convert % 60
	seconds_to_convert -= seconds 
	minutes = seconds_to_convert / 60
	if minutes >= 60:
		hours = minutes / 60
		minutes = minutes % 60 
	else:
		hours = 0

	seconds = time_convertor_time_to_string(seconds)
	minutes = time_convertor_time_to_string(minutes)
	hours = time_convertor_time_to_string(hours)

	return hours + ":" + minutes + ":" + seconds

def time_convertor_time_to_string(value):
	return str(int(value)).zfill(2)

def time_convertor_string_to_time(previous_time):
	if isinstance(previous_time, str):
		previous_time = previous_time.split(":")
		hours = int(previous_time[0])
		minutes = int(previous_time[1])
		seconds = int(previous_time[2])
		return hours, minutes, seconds 
	else:
		print("Hora inserida da maneira errada.")


if __name__ == "__main__":

	previous_duration = str(input("Qual a duração?  "))
	speed = float(input("Velocidade: "))

	if speed <= 0:
		print("Velocidade de reprodução inexistente.")
	else:
		new_duration = calculate_new_duration(previous_duration, speed)
		print(f'Nova duração é de {new_duration}')
	
#Próximas evoluções
#--Não aceitar valor acima de 60 para duração