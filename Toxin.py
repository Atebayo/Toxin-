#Code by Kanento
import socket 

ip_enter = input("IP scan : ")
try:
  for port in range(1,1023):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    egal = sock.connect_ex((ip_enter, port))
    if egal == 0:
      print("Port" + port + "Open")
    sock.close()
except socket.gaierror:
  print("ERROR for join the server")
  sys.exit()
except socket.error:
  print("SERVER IS NOT FOUND")
  sys.exit()


print("SCAN IS FINISHED")

#Code by Kanento
  

    
