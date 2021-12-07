# This program was made to test randomisation, math and variables.

# Imports

import time
import random

# Variables

htime = 0
mtime = 0
weather = "Sunny"

# Loop

while True:
   time.sleep(1)
   chance = random.randint(1,4)
   if chance == 4:
      wchance = random.randint(1,4)
      if wchance == 1:
         weather = "Sunny"
      else:
         if wchance == 2:
            weather = "Cloudy"
         else:
            if wchance == 3:
               weather = "Windy"
            else:
               weather = "Rainy"
   mtime += 1
   if mtime >= 6:
      htime += 1
      mtime = 0
   if htime >= 24:
      htime = 0
   print(f"The time is {htime}:{mtime}0 and the weather is {weather}.")