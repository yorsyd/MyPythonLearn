import pyautogui, time

pesan = "Hai Abang!\n"
time.sleep(3)

for x in range(3):
    pyautogui.write(pesan)
    time.sleep(2)
