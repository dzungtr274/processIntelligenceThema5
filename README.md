
# Solve4X Dataset

[Link to project website](https://x2log.pages.fraunhofer.de/solve4x/)

## **The Solve4X Dataset**: Business Processes in IT Asset Management Multimedia Event Log

### Introduction

The Business Processes in IT Asset Management Multimedia Event Log (Solve4X) dataset is a multimedia dataset for object-centric business process mining in IT asset management (ITAM). It contains 121 instances of IT asset management processes and their ground-truth annotations in 36 scripted video scenes. Each scene includes video recording from two angles, an process event log from an IT asset management system, human movement tracking data (including pose, location in the room, walking speed and handling height), task mining log from the web browser and various additional sensor data (e.g. door and shelf openings, distance sensor). We provide ground truth annotations for business process activity segments captured in the video data including segment time and length, involved humans, IT assets, location and the corresponding business process instance type and ID.

### License

The dataset and labelings provided on this page are published under the [Creative Commons Attribution-NonCommercial 4.0 International License](https://creativecommons.org/licenses/by-nc/4.0/).
This means you can use it for research and educational purposes but you must give appropriate credit, provide a link to the license, and indicate if changes were made.
You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.
You may not use the material for commercial purposes, for commercial licensing please [contact us](https://x2log.pages.fraunhofer.de/solve4x/)

### Lokal einstellung:
Bitte lade den Folder dataProcessing runter mit so eingestellter Darstellung im Projekt

``` git pull master ```

![image](https://github.com/user-attachments/assets/4c4064c3-aab3-4639-82d6-db3d2ad29213)

Installieren geforderte Packages wie Jupyter, Pandas, Numpy oder PM4PY zu installieren

``` pip install jupyter
    pip install pandas
    pip install Numpy
    pip install PM4py
    pip install graphviz
```
### Install graphviz
- install OS specific version https://graphviz.org/download/
- add installation path/bin to system variable path


Der objekt_type in der Datei "convert_data_type" ist noch fragwürdig, noch nicht festgelegt ob er als "admin_user" oder "item_asset" gesetzt werden soll. Hab an Andy gemeldet. Kannst freiwillig lokal ausprobieren bei den beiden Fällen

### Notizen:
- Ich habe verstanden dass du die Prozesses von 36 zu 15 reduziert hast. Aber falls es dir nicht absichtig wars, da kannst du anpassen.
- Welche Python Version hast du auf deine Rechner?