# Dies ist die DEMO-Version von Sensortest

Abschlussarbeit meiner Ausbildung zum Fachinformatiker für Anwendungsentwicklung.

„Anwendersoftware zur automatisierten Ausgangskontrolle mit standardisierten Testverfahren für Sensoren“

---

## Projektbeschreibung

Diese Anwendung ist eine PyQt5-basierte Desktopsoftware zur Durchführung von Test- und Messverfahren für 
industrielle Sensoren. Die Software dient der automatisierten Ausgangskontrolle und ermöglicht standardisierte 
Prüfabläufe für Distanz- und Amplitudenmessungen.

Die Benutzeroberfläche ist darauf ausgelegt, mehrere Sensoren parallel zu verwalten, deren Status anzuzeigen 
und definierte Testsequenzen auszuführen.

---

## Funktionsumfang (DEMO Version)

- Erkennung und Verwaltung mehrerer simulierter Sensoren aus einem ergänzten Skript sensor_simulation.py  
- Anzeige von Sensordaten (Typ, Comport, Seriennummer, Messwerte)  
- Durchführung von Distanztests  
- Durchführung von Amplitudentests  
- Auswertung der Testergebnisse (PASS / FAIL)  
- Protokollierung der Testergebnisse in Log-Dateien  
- PyQt5-basierte grafische Benutzeroberfläche
- Anpassungen, um den original Workflow darszustellen  

---

## Technische Abhängigkeiten

Diese Demoversion setzt folgende externe Komponenten voraus:

- Python 3.x  
- PyQt5 
- PyTest 
 

Ohne diese Abhängigkeiten ist die Anwendung in der aktuellen Form nicht ausführbar.
Die Packages können installiert werden über:
 pip --install pyqt 
 und 
 pip --install pytest

---

## Hinweis zur Weiterentwicklung

Diese Version stellt den erweitertet Demozustand der Abschlussarbeit dar. Sie dient zur Demonstration der
Facharbeit, da die originalen Sensoren sowie die dazugehörige Pythonbibliothek nicht mehr zur Verfügung stehen. 
Die Demoversion kann über GitHub bezogen und demonstriert werden.

---

## Status

X Originalversion (Baseline)  
✔ Demoversion
✔ Simulation integriert  
✔ Hardware-Abstraktion vorhanden