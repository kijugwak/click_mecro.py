import pyautogui
import keyboard

while True:


  position = pyautogui.position()
  
  
  print(pyautogui.size())
  
  
  print(position.x)
  print(position.y)
  
  
  
  pyautogui.click()
  
  
  pyautogui.click(clicks = 1, interval = 0.1)
  
  
  pyautogui.doubleClick()
