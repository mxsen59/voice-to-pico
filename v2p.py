from machine import Pin, ADC
import array, time, sys, os, select

onboard_led = Pin(25, Pin.OUT)

def main():
    
    while True:
        time.sleep(0.1)
     
        while sys.stdin in select.select([sys.stdin], [], [], 0)[0]:        
            ch = sys.stdin.read(1)

            if (ch == "h"):
                print(str(ch))
                onboard_led.value(1)
                
            elif (ch == "l"):
                print(str(ch))
                onboard_led.value(0)
                
            else:
                print("No voice input.")

main()