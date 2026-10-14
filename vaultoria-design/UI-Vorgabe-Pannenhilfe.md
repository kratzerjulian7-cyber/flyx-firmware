# Vaultoria – UI-Vorgabe Pannenhilfe 1.1 (verbindlich)

Stand 14.10.2026, 11:00 (**1.1: Julians Konzeptbild und App-Icon sind verbindlich, Teil 00 geht bei Widerspruch vor**). 1.0 vom 14.10.2026, 10:40. Grundlage: `Spielkonzept-Pannenhilfe.md` (Julian 14.10 10:34). Ersetzt alle früheren UI-Vorgaben (Archiv in `archiv-pfandhaus/`). Zahlen sind Startwerte zum Testen, im Spiel anpassen.

**Prüffrage für jeden Bildschirm:** Sieht man in zwei Sekunden, welches Fahrzeug wohin fährt und was als Nächstes zu tun ist? Wenn nicht, ist der Bildschirm zu voll.

## 00. Julians Konzeptbild und App-Icon (14.10 10:55, verbindlich, genau so umsetzen)

Bilder im selben Ordner: `Konzept-Hauptbildschirm-Karte.png` (Hauptbildschirm, „so soll das aussehen“) und `App-Icon-Pannenhilfe.png` (neues App-Icon, sofort als Icon setzen). Das Konzeptbild ist eine Vorgabe für den Look, kein Screenshot.

**App-Icon:** goldenes, gebürstetes V auf schwarzem Grund, oben ein goldener Kranhaken an Seilen, unten durch das V eine schwarze Straße mit goldenen Mittelstreifen. Ersetzt das alte „Goldene V“. In alle Icon-Größen exportieren, Hintergrund ohne Transparenz. App-Name bleibt **Vaultoria**.

**Hauptbildschirm (von oben nach unten):**
1. **Kopfleiste** auf schwarzem Grund mit feinem Goldrand unten: links das Icon-Logo (V mit Haken), daneben „VAULTORIA“ in goldener Versal-Schrift. Rechts zwei Kapseln mit Goldrand: **Geld** (Geldbündel-Symbol, „12.480 €“) und **Bewertung** (goldener Stern, „4,8“). Uhrzeit/Tag nicht in der Kopfleiste (steht in der Tagesabrechnung).
2. **Karte** füllt den ganzen Rest: isometrische Abendstadt, warmes Laternenlicht, europäische Häuser mit roten und grauen Dächern, Kirche, Fluss mit Brücke, Kreisverkehr mit Denkmal, Bahnstrecke mit Bahnsteig, Bäume, Zebrastreifen. Keine echten Ortsnamen oder Marken.
3. **Zentrale** in der Mitte: schwarzes, flaches Gebäude mit großem goldenen V-Haken-Logo auf dem Dach, beleuchtete Rolltore, Parkplatz mit Stellplätzen davor.
4. **Eigene Fahrzeuge**: gelb-schwarz mit goldenem V auf dem Dach, orangefarbenes Rundumlicht. Servicewagen als Transporter, Abschleppwagen als Plateau-Abschlepper.
5. **Routen**: leuchtende goldene Linien, die auf den Straßen von der Zentrale zum Fahrzeug und weiter zum Einsatz führen.
6. **Einsatzmarker**: runde Nadel mit Symbol über dem Kundenauto, Kundenauto mit Warndreiecken. **Rot** = dringend (z. B. Batterie, Unfall/Abschleppen), **goldorange** = normal (z. B. Reifen). Leichtes Pulsieren.
7. **Untere Leiste**, vier Tabs auf schwarzem Grund mit Goldrand oben: **Karte · Flotte · Zentrale · Personal**. Aktiver Tab gold mit goldenem Strich darunter, andere grau.

**Farben ab 1.1:** Schwarz und Graphit mit Gold sind jetzt der Grundlook (Julians Bild, geht der alten Flyx-Regel „kein Schwarz“ hier vor). Kein Blau in der Oberfläche; Wasser auf der Karte darf nachtdunkel sein, wie im Bild.

Was weiter unten anders steht (3 Tabs, Kopfleiste mit Uhrzeit, Farbe der Fahrzeuge), gilt nicht mehr; der Rest (Fenster, Abläufe, Zahlen) gilt unverändert.

## 0. Grundregeln

- **Kein Selbstfahren.** Kein Lenkrad, kein Steuerkreuz, kein Antippen zum Fahren. Fahrzeuge fahren nur automatisch.
- **Eine Hauptentscheidung pro Fenster**, ein goldener Hauptknopf, höchstens ein zweiter grauer Knopf.
- Fenster sind Bottom-Sheets (höchstens 50 % Höhe), die Karte bleibt immer sichtbar.
- Schrift mindestens 16 pt, Zahlen mindestens 20 pt, Knöpfe mindestens 52 pt hoch, volle Breite.
- Keine Prozentwerte, keine Sternleisten mit Zahlen, keine Textwände (höchstens zwei Zeilen Text pro Fenster).
- Keine Platzhalter-Menüs, kein „Demnächst“.
- Euro, deutsche Zahlen (1.250 €).

### Farben (dunkles Tycoon-Design, Gold als Akzent)

| Rolle | Farbe |
|---|---|
| Hintergrund | #1C1C1E |
| Flächen, Fenster | #2A2A2E, Rand 1 pt #3A3A3F |
| Text | #FFFFFF, zweitrangig #D7D7DB, leise #8A8A91 |
| Gold (Akzent, Hauptknopf, eigene Fahrzeuge, Zentrale, Routen) | #C9A24A, gedrückt #A8862F |
| Dringend | #E0533D (rot) |
| Normal | #E3A83A (bernstein) |
| Erledigt, Gewinn | #4CB86A (grün) |

Ab 1.1: Hintergrund und Leisten schwarz/graphit wie im Konzeptbild (Teil 00). Kein Blau, kein Cyan in der Oberfläche.

## 1. Hauptbildschirm: Stadtkarte (immer sichtbar)

- Draufsicht, leicht schräg von oben wie ein Tycoon-Spiel, Stadt klein genug, dass sie ohne Zoomen fast ganz zu sehen ist. Zoomen mit zwei Fingern, verschieben mit einem.
- **Straßen** dunkelgrau, Häuserblöcke etwas heller, ein paar Bäume. Keine echten Ortsnamen oder Marken.
- **Zentrale**: goldenes Gebäude mit Vaultoria-V auf dem Dach, Stellplätze davor sichtbar.
- **Eigene Fahrzeuge**: goldene Fahrzeugsymbole (Servicewagen klein, Abschleppwagen länger mit Haken). Darüber eine kleine Plakette mit Fahrerinitial und Restzeit („2:10“).
- **Einsätze**: pulsierende Nadel auf der Straße, Farbe nach Dringlichkeit (rot/bernstein), daneben das Kundenauto mit Warnblinker und ein Symbol der Panne.
- **Routen**: gestrichelte goldene Linie vom Fahrzeug zum Ziel, bewegt sich mit. Bei Rückfahrt dünner und grau-gold.
- **Ankunftszeit** an der Fahrzeugplakette; Status des Einsatzes an der Nadel: wartet · unterwegs · in Arbeit · fertig (Haken).
- Fahrzeuge folgen den Straßen flüssig (60 fps), biegen sichtbar ab, kein Springen.

### Obere Leiste (schmal, eine Zeile)

Links Geld (z. B. **2.000 €**), Mitte Uhrzeit des Spieltags (**Tag 1 · 09:40**), rechts Bewertung als Zahl mit einem Stern (**4,6 ★**). Zahnrad ganz rechts für Einstellungen.

### Untere Leiste (ab 1.1: vier Tabs)

**Karte** (mit Zähler offener Einsätze) · **Flotte** (Teil 6) · **Zentrale** (Teil 7) · **Personal** (Mitarbeiter mit ihren vier Werten, Gehalt, aktueller Einsatz; Einstellen erst, wenn ein Ausbau Platz schafft).

## 2. Einsatzfenster (Antippen einer Einsatznadel)

Kompakte Karte, oben ein großes Symbol der Panne:

1. **Batterie leer** (Batterie), 2. **Reifenpanne** (Reifen), 3. **Fahrzeug abgeschlossen** (Schlüssel), 4. **Falscher Kraftstoff** (Zapfsäule), 5. **Technischer Defekt** (Zahnrad), 6. **Abschleppen** (Haken).

Darunter in einem Raster, je Zeile Symbol und kurzer Wert:
- Kundenfahrzeug (Kleinwagen, Kombi, Transporter, E-Auto)
- Entfernung **2,4 km**
- Dringlichkeit **Dringend** (rotes Schild) oder **Normal**
- Belohnung **ca. 120 €** (groß, gold)
- Benötigt: Symbole der Ausrüstung (z. B. Starthilfe, Abschlepphaken)
- Dauer **ca. 6 Min** (Spielzeit)

Knöpfe: **Weiter zur Zuteilung** (gold) · **Ablehnen** (grau, Text). Ablehnen kostet nichts, der Einsatz verschwindet nach kurzer Zeit auch von selbst.

## 3. Zuteilung: Mitarbeiter und Fahrzeug

Zweite Seite im selben Fenster, keine neue Ansicht.

- **Fahrzeug wählen**: zwei große Karten nebeneinander (Servicewagen, Abschleppwagen). Jede zeigt Zustand als Balken (grün/bernstein/rot), Tank als Balken, Ausrüstungssymbole. Passt das Fahrzeug, grüner Haken „passt“. Passt es nicht, bernsteinfarbener Hinweis in einer Zeile, z. B. „Kann nicht abschleppen, zweiter Wagen nötig“ oder „Dauert länger, weniger Geld“. Belegte Fahrzeuge sind grau mit „unterwegs, frei in 3:20“.
- **Mitarbeiter wählen**: Liste mit Gesicht, Name und vier Werten als kleine Balken mit Symbol: Reparatur (Schraubenschlüssel), Abschleppen (Haken), Geschwindigkeit (Pfeil), Zuverlässigkeit (Schild). Keine Zahlen außer Stufe 1–5. Der für diesen Einsatz wichtigste Wert ist gold umrandet.
- Unten die Vorschau in einer Zeile: **Ankunft in 1:40 · ca. 120 €**.
- Hauptknopf: **Losschicken** (gold). Danach schließt das Fenster sofort und die Kamera schwenkt kurz zum losfahrenden Fahrzeug.

Voreinstellung: das passendste freie Fahrzeug und der beste freie Mitarbeiter sind schon ausgewählt, damit ein Tipp reicht.

## 4. Einsatz läuft (auf der Karte)

- Fahrzeug fährt, Route und Restzeit sichtbar.
- Vor Ort: kleiner Fortschrittsring über dem Kundenauto, Arbeitssymbol dreht sich, Funken/Werkzeug-Animation.
- Fertig: Münzen fliegen zur Geldanzeige, **+120 €** grün, darunter Sterne der Kundenbewertung (1–5) kurz eingeblendet. Haptik und Ton.
- Abschleppen: Kundenauto hängt sichtbar am Haken und fährt mit zur Zentrale (Werkstatt) oder zum Ziel.
- Danach fährt das Fahrzeug automatisch zurück. Liegt ein passender Einsatz auf dem Weg, kleiner Knopf an der Plakette **„Direkt weiter“**.

## 5. Sonderentscheidung (selten, höchstens jeder fünfte Einsatz)

Bottom-Sheet, Spiel pausiert dabei:
- Eine Zeile: **„Der Schaden ist größer als gemeldet.“**
- Drei Knöpfe untereinander, jeder mit einer Zeile Folge:
  - **Zweiten Wagen anfordern** – sicher, kostet Zeit
  - **Reparatur versuchen** – Chance hängt vom Reparaturwert ab, als Wort: „gute Chance“ / „riskant“
  - **Abbrechen** – kein Geld, Bewertung sinkt
- Kein Prozentwert, nur die Worte.

## 6. Flotte (Tab)

Je Fahrzeug eine Karte: Bild, Name, Zustand, Tank, Geschwindigkeit, Verbrauch, Wartungskosten, Ausrüstung, aktueller Einsatz mit Restzeit, zugeteilter Mitarbeiter.

- Knopf **Warten – 80 €** (nur wenn in der Zentrale), danach Zustand voll. Unter 30 % Zustand fährt das Fahrzeug langsamer und kann ausfallen; die Karte zeigt das als Satz, nicht als Prozent.
- Knopf **Tanken – 25 €** (bzw. Laden am Ladepunkt).
- Ganz unten **Neues Fahrzeug kaufen** nur, wenn ein freier Stellplatz da ist.

## 7. Zentrale und Ausbauten (Reiter)

Kamera fährt zur Zentrale. Liste der sechs Ausbauten; jeder Eintrag: Bild, Name, Preis und **ein Satz Auswirkung** in Worten, z. B.:

| Ausbau | Auswirkung (so im Spiel formuliert) |
|---|---|
| Zusätzlicher Stellplatz | Platz für ein drittes Fahrzeug |
| Kleine Werkstatt | Abgeschleppte Autos bringen Reparaturgeld |
| Ersatzteillager | Defekte werden vor Ort öfter gleich repariert |
| Tankstelle | Tanken in der Zentrale kostet weniger |
| Ladepunkt | Elektro-Einsätze möglich, E-Fahrzeuge laden hier |
| Bessere Leitstelle | Einsätze werden früher angezeigt, ein Einsatz mehr gleichzeitig |

Gekaufter Ausbau erscheint sofort sichtbar am Gebäude auf der Karte (kurze Bau-Animation). Keine schwebenden Preisschilder auf der Karte.

## 8. Tagesabrechnung (Ende jedes Spieltags)

Ein Fenster, drei Blöcke:
- **Einnahmen**: Einsätze, Reparaturen, Abschleppen, Bonus für gute Bewertungen
- **Kosten**: Gehälter, Kraftstoff, Wartung, Ersatzteile, Käufe
- **Reingewinn** groß (grün oder rot), darunter Bewertung des Tages
Knopf: **Nächster Tag**.

## 9. Start und Speichern

- Erster Start: kurze Karte „Willkommen in deiner Pannenhilfe“, ein Satz, Knopf **Los geht’s**. Der erste Einsatz (Batterie leer, nah, Normal) erscheint sofort, ein Finger zeigt auf die Nadel, dann auf „Weiter zur Zuteilung“, dann „Losschicken“. Danach keine Hilfen mehr.
- Startwerte: 2.000 €, Servicewagen, Abschleppwagen, zwei Mitarbeiter (einer stärker in Reparatur, einer im Abschleppen).
- Automatisch speichern nach jedem Einsatz, jedem Kauf und am Tagesende. Alter Pfandhaus-Spielstand wird erkannt und ohne Absturz durch ein neues Spiel ersetzt.

## 10. Entfällt komplett (nichts davon sichtbar)

Pfandhaus, Gegenstandshandel, Käufer und Sammler, Marktpreise, Museum, Auktionen, Rufgruppen, Konkurrenten, Versicherungsbüro, Rebirth, altes Imperium, Tierpension, Raubzüge, alter Baumodus, alte Handelswährungen, Shop und Werbung (bis Julian etwas anderes sagt).

## 11. Screenshots für die Abnahme

Hauptkarte leer · Einsatz erscheint · Einsatzfenster · Zuteilung · Fahrzeug unterwegs mit Route · Arbeit vor Ort · Belohnung · Rückfahrt · Fahrzeuge mit Warten · Zentrale mit Ausbau · Sonderentscheidung · Tagesabrechnung.
