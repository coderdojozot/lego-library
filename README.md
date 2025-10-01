# CoderDojo Zottemgem: Lego League Challenge Code

> PyBricks libraries and source code for entry in the [Lego League robotics Competition](https://www.firstlegoleague.org/season).

Herbruikbare stukken code (libraries) voor het [Lego league team](https://www.firstlegoleague.org/season) van de [Zottegemse CoderDojo](https://zottegem.coderdojobelgium.be).


## Hoe gebruik je deze repository?


## Afspraken, en tips



## Opmerkingen/To Do

- eerst .py files voor alle basis functies
- de .py files met functies die in andere files kunnen worden opgeroepen:
    - vooruit rijden (afstand/snelheid)
    - achteruit rijden (afstand/snelheid)
    - naar rechts draaien (hoeveel graden)
    - naar links draaien (hoeveel graden)
    - extensiemotor1 beweging
    - extensiemotor2 beweging

- eens bovenstaande helemaal goed zit kan iedereen deze functies gebruiken
- wat zijn de basis imports? waar zetten we die? (niet nodig om die in elke file te doen)

```python
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, run_task,hub_menu
```

- je eigen functies gebruiken doe je zo:
```python
from rijden_met_gyro_versie_lukas import gyro_rechtdoor
```

- zet in je eigen missiefile een commentaar blok bovenaan met wat info voor anderen en eventueel een laatste update datum
```
####################################################################################
# Dit is een eerste versie van xxx om de de missies te laten starten door herkenning
# van een kleur door de kleurensensor
#
# Laatste update: 24/09/2025 - eerste versie
####################################################################################
```
