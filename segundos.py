Segundos_str = input ("Por favor, entre com o número de segundos que deseja converter: ")

seg_total = int(Segundos_str)

dias = seg_total//86400

horas = (seg_total % 86400)//3600

minutos = ((seg_total % 86400) % 3600)//60

segundos = ((seg_total % 86400) % 3600)%60

print (dias,"dias,",horas,"horas,",minutos,"minutos e",segundos,"segundos.")
