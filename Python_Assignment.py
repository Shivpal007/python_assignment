import platform
import subprocess 
import speedtest
import pyautogui
import psutil
import socket
import math

print(" All Installed software list")
try:
    data = subprocess.check_output(['wmic', 'product', 'get', 'name'], universal_newlines=True)
    product_names = data.split('\n')[1:]  # Assuming the first line is a header and skipping it

    for product_name in product_names:
        print(product_name.strip())

except subprocess.CalledProcessError as e:
    print(f"Error: {e}")
    
print("############################################################################")  
    
print(" Internet Speed ")  
# internet speed
speed = speedtest.Speedtest();
print("Download Speed = ",speed.download())
print("Upload Speed = ",speed.upload())
print("############################################################################")  
print(" Screen resolvution")
# screen resolution
print(pyautogui.size()) 

print("############################################################################")  

print(" No of core and threads of CPU , Windows version,  CPU Model And RAM Size")
my_system = platform.uname()
print(f"OS Name: {my_system.system}")
print(f"OS Version: {my_system.version}")
print(f"CPU Model: {my_system.processor}") #CPU Model
print("Core Count= ",psutil.cpu_count())
print("Thread count= ",psutil.cpu_count()/psutil.cpu_count(logical=False))
print("RAM = ",int(psutil.virtual_memory().total/1000000000 ))

print("############################################################################")  

print("Wifi/Ethernet mac address")
for interface in psutil.net_if_addrs():
    	# Check if the interface has a valid MAC address
	if psutil.net_if_addrs()[interface][0].address:
		# Print the MAC address for the interface
		print(psutil.net_if_addrs()[interface][0].address)
		break

print("############################################################################")  

print(" Public IP address")
def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]
print(get_ip_address())

print("###############################################################")
    

def get_diagonal_size(width, height):
    diagonal_size = math.sqrt(width**2 + height**2)
    return diagonal_size

def main():
    try:
        diagonal_size = get_diagonal_size(1920, 1080)

        print(f"The diagonal size of the screen is: {diagonal_size:.2f} inches")
    except ValueError:
        print("Invalid input. Please enter valid numeric values for width and height.")

if __name__ == "__main__":
    main()


print("###############################################################")
