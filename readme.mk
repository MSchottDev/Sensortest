# Dies ist die Originalversion

Abschlussarbeit meiner Ausbildung zum Fachinformatiker für Anwendungsentwicklung.

„Anwendersoftware zur automatisierten Ausgangskontrolle mit standardisierten Testverfahren für Sensoren“

---

## Projektbeschreibung

Diese Anwendung ist eine PyQt5-basierte Desktopsoftware zur Durchführung von Test- und Messverfahren für industrielle Sensoren. Die Software dient der automatisierten Ausgangskontrolle und ermöglicht standardisierte Prüfabläufe für Distanz- und Amplitudenmessungen.

Die Benutzeroberfläche ist darauf ausgelegt, mehrere Sensoren parallel zu verwalten, deren Status anzuzeigen und definierte Testsequenzen auszuführen.

---

## Funktionsumfang (Originalversion)

- Erkennung und Verwaltung mehrerer Sensoren über COM-Ports  
- Anzeige von Sensordaten (Typ, Comport, Seriennummer, Messwerte)  
- Durchführung von Distanztests  
- Durchführung von Amplitudentests  
- Auswertung der Testergebnisse (PASS / FAIL)  
- Protokollierung der Testergebnisse in Log-Dateien  
- PyQt5-basierte grafische Benutzeroberfläche  

---

## Technische Abhängigkeiten

Diese Originalversion setzt folgende externe Komponenten voraus:

- Python 3.x  
- PyQt5  
- pyserial  
- OndoSense Sensor SDK (`ondoconnect`)  
- interfaces_python (Sensor-Interface Definitionen)  

Ohne diese Abhängigkeiten ist die Anwendung in der aktuellen Form nicht ausführbar.

---

## Hinweis zur Weiterentwicklung

Diese Version stellt den ursprünglichen Entwicklungsstand der Abschlussarbeit dar.  
In einer späteren Erweiterung wird eine Simulationsschicht ergänzt, um die Anwendung auch ohne Sensorhardware demonstrieren zu können.

---

## Status

✔ Originalversion (Baseline)  
✖ Keine Simulation integriert  
✖ Keine Hardware-Abstraktion vorhanden