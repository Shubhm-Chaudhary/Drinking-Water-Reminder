import random

from plyer import notification
from time import sleep

quotes = ["“Drinking water is like washing out your insides.”",
          "“Water is life’s matter and matrix, mother and medium.”",
          "“In time and with water, everything changes.”",
          "“Water is the only drink for a wise man.”",
          "“If there is magic on this planet, it is contained in water.”",
          "“Thousands have lived without love, not one without water.”",
          "“Water is the soul of the Earth.”",
          "“We never know the worth of water till the well is dry.”",
          "“Water is the best of all things.”",
          "“We forget that the water cycle and the life cycle are one.”",
          "“Anyone who can solve the problems of water will be worthy of two Nobel prizes – one for peace and one for "
          "science.”",
          "“Whiskey is for drinking; water is for fighting over.”",
          "“Thirst drove me down to the water\nwhere I drank the moon’s reflection.”",
          "“What makes the desert beautiful is that somewhere it hides a well.”",
          "“A river is more than an amenity, it is a treasure.” ",
          "“And all the air is filled with pleasant noise of waters”",
          "“If you gave me several million years, there would be nothing that did not grow in beauty if it were "
          "surrounded by water.”",
          "“I never drink water; that is the stuff that rusts pipes.”",
          "“There’s over a billion people on this planet that don’t have access to clean drinking water.”",
          "“Irrigation of the land with seawater desalinated by fusion power is ancient. It’s called rain.”",
          "“Plans to protect air and water, wilderness and wildlife are in fact plans to protect man.”",
          "“By polluting clear water with slime you will never find good drinking water.”",
          "“Be praised, My Lord, through Sister Water; she is very useful, and humble, and precious, and pure.”",
          "“Let the rain sing you a lullaby.”"
          ]


title = "Drink Water"
appname = "Alice"
sleep(600)
while True:
    Message = f"{random.choice(quotes)} \nTime To Drink Some Water"
    notification.notify(title=title, message=Message, app_name=appname)
    sleep(1200)

