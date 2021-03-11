import socket

def ports():
	try:

		a = input('Введите ip адресс, или домен->')
		b = input('До какого порта сканировать->')
		print('Это займет примерно {} секунд'.format(0.004 * int(b)))
		spis = []
		for i in range(1, int(b)):  
		    s = socket.socket()  
		    s.settimeout(0)
		    ip = a
		    response = s.connect_ex((ip, i)) 
		    if response:
		        print ('порт {} закрыт'.format(i))
		    else:
		        print ('порт {} открыт'.format(i))
		        spis.append(i)
		    s.close()
		print('Все открытые порты: {}'.format(spis))

	except:
		print('Вы ввели некоректные данные')

def one():
	try:
		a = input('Введите ip адресс, или домен->')
		b = input('Какой порт сканировать->')
		s = socket.socket()  
		s.settimeout(0)
		ip = a
		response = s.connect_ex((ip, int(b)))
	except:
		print('Вы ввели некоректные данные')

def all():
	try:
		spis = []
		a = input('Введите ip адресс, или домен->')
		for i in range(1, 65535):  
		    s = socket.socket()  
		    s.settimeout(0)
		    ip = a
		    response = s.connect_ex((ip, i)) 
		    if response:
		        print ('порт {} закрыт'.format(i))

		    else:
		        print ('порт {} открыт'.format(i))
		        spis.append(i)
		    s.close()
		print('Все открытые порты: {}'.format(spis))

	except:
		print('Вы ввели некоректные данные')

def main():
	print("Если вы хотите просканировать до определенного порта, введите цифру 1, если вы хотите просканировать отдельно один порт, введите цифру 2, если вы хотите просканировать все 65535 портов, введите цифру 3, введите 4, если хотите прекратить  работу программы")

	new = input()
	if new == '1':
		ports()
	elif new == '2':
		one()
	elif new == '3':
		all()
	else:
		print('Выберите: 1 / 2 / 3')

main()