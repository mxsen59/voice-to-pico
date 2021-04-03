from machine import Pin, ADC
import array, time, sys, os, select

onboard_led = Pin(25, Pin.OUT)

led_rgb_1 = Pin(18, Pin.OUT)
led_rgb_2 = Pin(17, Pin.OUT)
led_rgb_3 = Pin(16, Pin.OUT)

led_1 = Pin(15, Pin.OUT)
led_2 = Pin(14, Pin.OUT)
led_3 = Pin(13, Pin.OUT)

leds = [led_1, led_2, led_3]

temp_sensor = ADC(4)
convert = 3.3 / (65535)

def main():
    
    while True:
        time.sleep(0.1)
        led_rgb_1.value(0)
        led_rgb_2.value(0)
        led_rgb_3.value(1)
     
        while sys.stdin in select.select([sys.stdin], [], [], 0)[0]:        
            ch = sys.stdin.read(1)
            
            if (ch == 't'):
                print(str(ch))
                todo_input = input("Add to your todo list: ")
                with open("todo_list.txt", "a") as td_file:
                    td_file.write("\n" + todo_input.strip(str(ch)))
                    onboard_led.value(1)
                    led_rgb_2.value(1)
                    time.sleep(0.5)
                    print("Added to list successfully.\n")
                    onboard_led.value(0)
                    led_rgb_2.value(0)
                    time.sleep(0.5)
                      
            elif (ch == 'r'):
                print(str(ch))
                with open("todo_list.txt", "r") as td_file:
                    lines = td_file.readlines()
                    led_rgb_2.value(1)
                    print("\nReminder you need to: " + str(lines[0:]).strip("[]") + "\n")
                    time.sleep(0.5)
                    led_rgb_2.value(0)
                    time.sleep(0.5)
                               
            elif (ch == 'g'):
                print(str(ch))
                onboard_led.value(1)
                led_rgb_2.value(1)
                print("Hello there!\n")
                time.sleep(0.5)
                onboard_led.value(0)
                led_rgb_2.value(0)
                time.sleep(0.5)

            elif (ch == "h"):
                print(str(ch))
                onboard_led.value(1)
                
                for _ in leds:
                    _.value(1)
                
            elif (ch == "l"):
                print(str(ch))
                onboard_led.value(0)
                
                for _ in leds:
                    _.value(0)
                
            elif (ch == "m"):
                curr_voltage = temp_sensor.read_u16() * convert
                temp_c = 27 - ((curr_voltage - 0.706) / 0.001721)
                temp_f = ((temp_c * 9 / 5) + 32)
                led_rgb_2.value(1)
                print(str(temp_f))
                time.sleep(0.5)
                led_rgb_2.value(0)
                time.sleep(0.5)
                
            else:
                print("No commands.")

main()