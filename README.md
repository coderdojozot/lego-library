# CoderDojo Zottemgem: Lego League Challenge Code

> PyBricks libraries and source code for entry in the [Lego League robotics Competition](https://www.firstlegoleague.org/season).

Herbruikbare stukken code (libraries) voor het [Lego league team](https://www.firstlegoleague.org/season) van de [Zottegemse CoderDojo](https://zottegem.coderdojobelgium.be).

## Repository Structuur

```
lego-library/
├── 2025/                          # Huidige seizoen code
│   ├── hoofd_programma.py         # Hoofdprogramma met kleur detectie
│   ├── functies.py                # Alle herbruikbare robot functies
│   ├── missie_roodA.py            # Missies voor rood opzetstuk
│   ├── missie_geelA.py            # Missies voor geel opzetstuk
│   ├── missie_blauwA.py           # Missies voor blauw opzetstuk
│   ├── missie_groenA.py           # Missies voor groen opzetstuk
│   ├── batterij_meter.py          # Controle batterijstatus robot
│   ├── reflectie_meter.py         # Reflectie sensor tools
│   ├── start_code.py              # Basis startcode
│   ├── zender.py                  # Innovatieproject communicatie
│   └── ontvanger.py               # Innovatieproject communicatie
├── code_vuilbak/                  # Oude code en experimentele code
└── venv_linux/                    # Python virtual environment (Linux)
```

## Hoe werkt het systeem?

### Kleur-gebaseerde Missie Selectie

Onze robot gebruikt een **kleurensensor** om te detecteren welk opzetstuk er op de robot gemonteerd is. We hebben **4 verschillende opzetstukken**, elk met een unieke kleur:

- 🔴 **Rood** → voert `missie_roodA.py` uit
- 🟡 **Geel** → voert `missie_geelA.py` uit
- 🔵 **Blauw** → voert `missie_blauwA.py` uit
- 🟢 **Groen** → voert `missie_groenA.py` uit

Het **hoofd_programma.py** detecteert de kleur en roept automatisch de juiste missie aan. Dit betekent dat je geen code hoeft aan te passen wanneer je van opzetstuk wisselt!

### Functies Bibliotheek

Alle herbruikbare robot functies staan in **functies.py**. Deze bevat:
- Vooruit/achteruit rijden (met afstand en snelheid)
- Links/rechts draaien (met graden nauwkeurigheid)
- Extensiemotor aansturing
- Gyro-sensor functies
- En meer...

In je missie bestanden importeer je alleen de functies die je nodig hebt uit `functies.py`.

### Batterij Monitoring

**batterij_meter.py** laat je de huidige status van de robot batterij checken. Dit is handig om te voorkomen dat de robot midden in een run stopt door een lege batterij.

### Zender en Ontvanger

De bestanden **zender.py** en **ontvanger.py** zijn voorbereidingen voor ons innovatieproject en maken gebruik van draadloze communicatie tussen robots/hubs. Deze horen niet bij de standaard missie code.

## Hoe gebruik je deze repository?

### Pybricks VS Code Extensie

We gebruiken de **Pybricks extensie voor VS Code** zodat we rechtstreeks vanuit de code editor naar de robot kunnen programmeren, zonder naar de Pybricks webomgeving te hoeven gaan.

**Setup:**
1. Installeer de Pybricks extensie in VS Code
2. Verbind je LEGO hub via Bluetooth
3. Open een `.py` bestand
4. Druk op de **Run** knop (▶️) om de code naar de robot te pushen

**Voordelen:**
- Sneller ontwikkelen en testen
- Volledige VS Code functionaliteit (IntelliSense, debugging, etc.)
- Geen browser nodig
- Betere samenwerking met version control (Git)

## Nieuwe Missies Toevoegen

Volg deze stappen om een nieuwe missie toe te voegen:

### Stap 1: Bepaal de kleur
Beslis welk opzetstuk/kleur je gaat gebruiken voor deze missie.

### Stap 2: Maak of update het missie bestand
Open het juiste bestand (bijv. `missie_roodA.py` voor een rood opzetstuk) en voeg je missie functie toe:

```python
from functies import gyro_rechtdoor, draai_links, draai_rechts, extensiemotor1

def missie_nieuwe_functie():
    """
    Beschrijving van wat deze missie doet
    """
    gyro_rechtdoor(500, 200)  # 500mm vooruit, snelheid 200
    draai_rechts(90)           # 90 graden rechts draaien
    extensiemotor1(360)        # Motor 360 graden draaien
    # ... etc
```

### Stap 3: Voeg de missie toe aan het menu
In hetzelfde missie bestand, voeg je nieuwe functie toe aan de menu opties:

```python
async def main():
    # Bestaande menu items...
    selected = await hub_menu(
        "1", "2", "3", "4"  # Voeg een nieuw nummer toe indien nodig
    )
    
    if selected == "1":
        await bestaande_missie_1()
    elif selected == "2":
        await bestaande_missie_2()
    elif selected == "3":
        await missie_nieuwe_functie()  # Jouw nieuwe missie
```

### Stap 4: Test je missie
1. Plaats het juiste kleur opzetstuk op de robot
2. Upload `hoofd_programma.py` naar de robot
3. De robot detecteert de kleur en laadt jouw missie bestand
4. Selecteer je missie nummer op de hub

### Stap 5: Documenteer je code
Voeg een commentaar blok toe bovenaan je functie met uitleg en update datum:

```python
####################################################################################
# Missie naam: [Naam]
# Beschrijving: [Wat doet deze missie]
# Opzetstuk: [Welke kleur/opzetstuk]
#
# Laatste update: 24/01/2026
####################################################################################
```


## Afspraken en Tips

### Code Conventies
- Gebruik duidelijke functie namen die beschrijven wat ze doen
- Voeg commentaar toe bij complexe logica
- Test je code grondig voordat je commit
- Update de laatste wijzigingsdatum in je commentaar blok

### Basis Imports
Deze imports zijn standaard nodig voor de meeste programma's:

```python
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, run_task, hub_menu
```

### Functies Importeren
Importeer alleen de functies die je nodig hebt uit `functies.py`:

```python
from functies import gyro_rechtdoor, draai_links, draai_rechts
```

### Best Practices
- ✅ Test elke missie apart voordat je ze combineert
- ✅ Check regelmatig de batterij status
- ✅ Gebruik duidelijke variabele namen
- ✅ Commit regelmatig naar Git
- ✅ Documenteer wat je code doet
- ❌ Vermijd hard-coded waardes waar mogelijk (gebruik constanten)
- ❌ Plaats geen experimentele code in de `2025/` map

## Troubleshooting

### Robot reageert niet
- Check of de batterij voldoende is geladen
- Controleer of de Bluetooth verbinding actief is
- Herstart de hub indien nodig

### Verkeerde missie wordt uitgevoerd
- Controleer of het juiste kleur opzetstuk gemonteerd is
- Test de kleurensensor met `reflectie_meter.py`
- Zorg dat de sensor goed gepositioneerd is

### Code upload lukt niet
- Controleer of de Pybricks extensie actief is
- Verbreek en maak opnieuw verbinding met de hub
- Check of een ander programma de Bluetooth verbinding gebruikt

## Requirements

Zie [requirements.txt](requirements.txt) voor de benodigde Python packages.

## Licentie

Zie [LICENSE](LICENSE) voor meer informatie.

---

**Veel succes met jullie missies! 🚀🤖**

---

**Veel succes met jullie missies! 🚀🤖**
