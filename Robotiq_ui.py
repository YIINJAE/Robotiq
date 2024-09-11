'''
단순 반복 동작
robotiq 그리퍼 동작.
pip install minimalmodbus==2.1.1

단순화면 추가
'''

import tkinter as tk
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
    command = [0x0100, 0x0000, 0x0000]  # 그리퍼 활성화 명령
    instrument.write_registers(1000, command)  # 주소 1000부터 명령 전송
    time.sleep(1)  # 활성화 후 잠시 대기
    status_label.config(text="Gripper Activated")

# 그리퍼 동작 함수
def move_gripper():
    position = position_scale.get()  # 위치 값
    speed = speed_scale.get()        # 속도 값
    force = force_scale.get()        # 힘 값
    command = [0x0900, position, (speed << 8) | force]  # 명령 생성
    instrument.write_registers(1000, command)  # 주소 1000부터 명령 전송
    time.sleep(1)
    status_label.config(text=f"Moved: Position={position}, Speed={speed}, Force={force}")

# GUI 생성
root = tk.Tk()
root.title("Gripper Control")

# 위치 조정 스크롤바
tk.Label(root, text="Position (0-255):").pack()
position_scale = tk.Scale(root, from_=0, to=255, orient="horizontal")
position_scale.pack()

# 속도 조정 스크롤바
tk.Label(root, text="Speed (0-255):").pack()
speed_scale = tk.Scale(root, from_=0, to=255, orient="horizontal")
speed_scale.pack()

# 힘 조정 스크롤바
tk.Label(root, text="Force (0-255):").pack()
force_scale = tk.Scale(root, from_=0, to=255, orient="horizontal")
force_scale.pack()

# 그리퍼 활성화 버튼
activate_button = tk.Button(root, text="Activate Gripper", command=activate_gripper)
activate_button.pack()

# 그리퍼 동작 시작 버튼
move_button = tk.Button(root, text="Move Gripper", command=move_gripper)
move_button.pack()

# 상태 표시 라벨
status_label = tk.Label(root, text="Status: Waiting for action")
status_label.pack()

# GUI 실행
root.mainloop()
