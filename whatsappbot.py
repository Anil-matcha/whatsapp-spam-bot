import pyautogui

while True:
	pyautogui.click(1356, 792)#position of chatbox
	pyautogui.typewrite("spam", interval=0.1)
	pyautogui.click(1568, 789)#position of end button