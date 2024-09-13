'''
단순 반복 동작
robotiq 그리퍼 동작.
pip install minimalmodbus==2.1.1
'''

import minimalmodbus
import time

# Modbus 통신 설정
instrument = minimalmodbus.Instrument('COM3', 9)  # COM3 포트와 슬레이브 ID 9 설정
instrument.serial.baudrate = 115200  # 통신 속도 설정
instrument.serial.bytesize = 8
instrument.serial.parity = minimalmodbus.serial.PARITY_NONE
instrument.serial.stopbits = 1
instrument.serial.timeout = 0.5

# 그리퍼 활성화 함수
def activate_gripper():
    command = [0x0000, 0x0000, 0x0000]  # 그리퍼 활성화 명령
    instrument.write_registers(1000, command)  # 주소 1000부터 명령 전송
    print('그리퍼활성화',command)
    time.sleep(5)  # 활성화 후 잠시 대기

# 그리퍼 닫기 함수
def close_gripper():
    command = [0x0900, 0x00FF, 0xFFFF]  # 그리퍼 닫기 명령 (최대 속도, 최대 힘)
    instrument.write_registers(1000, command)  # 주소 1000부터 명령 전송
    print('그리퍼닫기',command)
    time.sleep(1)  # 동작 대기

# 그리퍼 열기 함수
def open_gripper():
    command = [0x0900, 0x0000, 0xFFFF]  # 그리퍼 열기 명령 (최대 속도, 최대 힘)
    instrument.write_registers(1000, command)  # 주소 1000부터 명령 전송
    print('그리퍼열기',command)
    time.sleep(1)  # 동작 대기

# 반복 동작
try:
    activate_gripper()  # 그리퍼 활성화
    while True:
        close_gripper()  # 그리퍼 닫기
        time.sleep(2)  # 잠시 대기
        open_gripper()  # 그리퍼 열기
        time.sleep(2)  # 잠시 대기
except KeyboardInterrupt:
    print("동작 중지")