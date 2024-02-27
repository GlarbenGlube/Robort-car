# # from Hardware import motorstyrring as M
# from Hardware import ReadSensor as S
# from time import sleep_ms

# # def cbt():
# #     while True:
# #         M.UpdatePWM(1200,dutyL=0.4,dutyR=0.4)   
# #         print("start")
# #         b = 0
# #         distance = S.measureDistance() 
# #         while b < 25:
# #             distance = S.measureDistance()
# #             if distance < 110:
# #                 b=31
# #                 if distance < 10:
# #                     M.turnright()
# #                     sleep(0.25 - distance/100)
# #                     M.stop()
# #                 else:
# #                     M.turnleft()
# #                     sleep(distance/100)
# #                     M.stop()
# #             M.turnright()
# #             b+=1   
# #         M.UpdatePWM(1000,dutyL=0.615,dutyR=0.6)   
# #         reflection = S.measureReflection()
# #         while reflection <= 40000:
# #             print(reflection)
# #             M.forward()
# #             reflection = S.measureReflection()
# #         M.back()
# #         sleep(0.05)
# #         print("return")
# #         M.UpdatePWM(1000,dutyL=0.52,dutyR=0.5)   
# #         M.back()
# #         sleep(1)
# #         M.stop()
# #         M.turnright()
# #         sleep(0.5)
# #         M.stop()

# from machine import UART,Pin

# led = Pin("LED", Pin.OUT)

# Couldn't get UART channel 1 to work with pins 8 and 9, so after some trial and error used channel 0 and pin 16/17 instead :)


"""GY53 general mode

        from time import sleep_ms


        uart = UART(0, baudrate=9600, tx=Pin(16), rx=Pin(17))

        uart.init(bits=8, parity=None, tx=Pin(16), rx=Pin(17))

        data_to_send = bytes([0xA5, 0x51, 0xF6])   # fast mode
        data_to_send = bytes([0xA5,0x53,0xF8])     # general mode
        sleep_ms(40)
        data_to_send = bytes([0xA5,0x25,0xCA])     # save permanently to sensor

"""
# # 0xA5+0x25+0xCA
# # Write the entire bytes object to UART
# # uart.write(data_to_send)
# # sleep_ms(500)


# uart.write(data_to_send)




# while True:
#     print(S.measureDistance())  
#     sleep_ms(40)
# # # 0xA5+0x51+0xF6

# # from machine import Pin,UART
# # import time
# # uart = UART(1, baudrate=9600, tx=Pin(16), rx=Pin(17))
# # uart.init(bits=8, parity=None, stop=2)
# # led = Pin("LED", Pin.OUT)

# # while True:
# #     uart.write('t')
# #     if uart.any(): 
# #         data = uart.read() 
# #         if data== b'm':
# #             led.toggle() 
# #     time.sleep(1)