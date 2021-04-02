from machine import Pin, ADC
import array, time, sys, os, select

onboard_led = Pin(25, Pin.OUT)

temp_sensor = ADC(4)
convert = 3.3 / (65535)

def main():
    
    while True:
        time.sleep(0.1)    
     
        while sys.stdin in select.select([sys.stdin], [], [], 0)[0]:        
            ch = sys.stdin.read(1)
            
            if (ch == 't'):
                print(str(ch))
                todo_input = input("Add to your todo list: ")
                with open("todo_list.txt", "a") as td_file:
                    td_file.write("\n" + todo_input.strip(str(ch)))
                    onboard_led.value(1)
                    time.sleep(0.5)
                    print("Added to list successfully.\n")
                    onboard_led.value(0)
                    time.sleep(0.5)
                      
            elif (ch == 'r'):
                print(str(ch))
                with open("todo_list.txt", "r") as td_file:
                    lines = td_file.readlines()
                    print("\nReminder you need to: " + str(lines[0:]).strip("[]") + "\n")
                               
            elif (ch == 'g'):
                print(str(ch))
                onboard_led.value(1)
                print("Hello there!\n")
                time.sleep(0.5)
                onboard_led.value(0)

            elif (ch == "h"):
                print(str(ch))
                onboard_led.value(1)
                
            elif (ch == "l"):
                print(str(ch))
                onboard_led.value(0)
                
            elif (ch == "m"):
                curr_voltage = temp_sensor.read_u16() * convert
                temp_c = 27 - ((curr_voltage - 0.706) / 0.001721)
                temp_f = ((temp_c * 9 / 5) + 32)
                print(str(temp_f))
                
            else:
                print("No commands.")

main()