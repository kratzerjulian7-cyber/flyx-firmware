# Vaultoria – UI-Vorgabe Pannenhilfe 2.2 (verbindlich)

Stand 14.10.2026, 14:00 (**2.2: Julians Bewertung des 5.0-Zwischenstands (8/10), Teil 000a Lesbarkeit. Grundoptik bleibt, Realismus-Block abgeschwächt, Orange wieder Funktionsfarbe.** 2.1 13:45: **2.1: realistische Autos, Häuser und Menschen, CC0 von Poly Haven und ambientCG freigegeben, Julian 13:40.** 2.0 13:20: **2.0: KEIN GOLD. Julian zu 1.4: „nicht gold mache es besser das sieht scheiße billig aus und wie für ein 2 jährigen“. Teil 000 Stil geht allem vor; Layout und Aufbau der Konzeptbilder bleiben, Farbe und Stil daraus gelten nicht mehr.** 1.4 11:30: **1.4: Teil 13 erste Version mit 8 Pflichtpunkten, Später-Liste, offene Konzeptbilder, Julian 11:21.** 1.3 11:20: **1.3: Teil 00b Einsatz-Zuteilung und 00c Zentrale nach Julians Konzeptbildern 11:16.** 1.2 11:10: **1.2: Teil 12 Große Welt + sichtbare Ausbauten, Julian 11:06.** 1.1 11:00: **1.1: Julians Konzeptbild und App-Icon sind verbindlich, Teil 00 geht bei Widerspruch vor**). 1.0 vom 14.10.2026, 10:40. Grundlage: `Spielkonzept-Pannenhilfe.md` (Julian 14.10 10:34). Ersetzt alle früheren UI-Vorgaben (Archiv in `archiv-pfandhaus/`). Zahlen sind Startwerte zum Testen, im Spiel anpassen.

**Versionen:** Die nächste App-Version ist **Vaultoria 5.0**, danach 5.1, 5.2 … (Julian 14.10.2026). Stil 2.0 dieser Datei gilt ab 5.0; „1.4“ meint den bisherigen Gold-Build 202610141306.

**Prüffrage für jeden Bildschirm:** Sieht man in zwei Sekunden, welches Fahrzeug wohin fährt und was als Nächstes zu tun ist? Wenn nicht, ist der Bildschirm zu voll.

## 000. Stil 2.0: erwachsen und realistisch, KEIN GOLD (geht allem in dieser Datei vor)

Julian 14.10 13:12 zu Build 1.4: „nicht gold mache es besser das sieht scheiße billig aus und wie für ein 2 jährigen“.

**Bleibt aus den Konzeptbildern:** Aufbau und Anordnung (Kopfleiste mit Geld- und Bewertungs-Kapsel, Karte als Hauptbildschirm, Einsatz-Panel von unten mit Bild, Titel, km, €-Spanne, zwei vorausgewählten Karten und einem Hauptknopf, Tab Zentrale mit Nahansicht und drei Ausbaukarten, vier Tabs unten), isometrische Stadt bei Abend, Abläufe und Zahlen.
**Gilt nicht mehr aus den Konzeptbildern:** Gold, Goldränder, goldene Schrift, Glow und Leuchtlinien, glänzende Knöpfe, Verläufe, verspielte Symbole. Überall wo in dieser Datei „gold“ steht, gilt die Tabelle unten.

**Farben**

| Rolle | Farbe |
|---|---|
| Hintergrund, Leisten | Graphit #1C1C1E |
| Flächen, Panels, Karten | Anthrazit #2A2A2E, Rand 0,5–1 pt #3A3A3F |
| Text | #FFFFFF, zweitrangig #D7D7DB, leise #8A8A91 |
| Akzent (aktiver Tab, Auswahlrahmen, Hauptknopf, eigene Routen, eigene Fahrzeuge auf der Karte) | Silber #C7C7CC, gedrückt #AEAEB2; Hauptknopf: Silber-Fläche mit dunkler Schrift #1C1C1E |
| Status dringend | #D9473A (rot, gedeckt) |
| Status normal / wartet | #D99A2B (bernstein, gedeckt) |
| **Funktionsfarbe Orange (2.2)** | #F08A24 für Einsatzmarker, Warnungen, Rundumlichter |
| Status erledigt / Gewinn | #3FA35B (grün, gedeckt) |
| Verlust | #D9473A |

Farbe nur für Status. Kein Blau/Cyan in der Oberfläche (Wasser auf der Karte darf nachtdunkel bleiben).

**Form und Schrift**
- **SF Pro** (System) überall: Titel SF Pro Display Semibold, Text SF Pro Text Regular, Zahlen mit Tabellenziffern (`monospacedDigit`). Keine Versal-Zierschrift, kein „VAULTORIA“ in Großbuchstaben-Gold.
- Dünne Linien (0,5–1 pt), Ecken 12 pt bei Karten, 10 pt bei Knöpfen, 20 pt beim Panel oben. Keine Schatten-Glows, höchstens ein weicher dunkler Schatten unter dem Panel.
- Symbole: SF Symbols in Linienstärke Regular, einfarbig (Silber oder Textgrau, Statusfarbe nur bei Status). Keine Geldbündel-Bilder, kein Stern-Emoji-Look: Geld als „12.480 €“ mit `eurosign`-Symbol, Bewertung als „4,8“ mit `star.fill` in #D7D7DB.
- Knöpfe flach, kein Glanz, kein Doppelpfeil-Deko. „Losschicken“ = silberner Hauptknopf mit dunkler Schrift, volle Breite, 52 pt hoch (das Grün aus 00b entfällt).
- Animationen ruhig: Ein- und Ausblenden 0,2–0,3 s, Federung gering. Belohnung als kurzer Zähler „+180 €“ in Grün, keine fliegenden Münzen, kein Konfetti.

**Logo**
- Im Spiel nur klein und dezent: V-Symbol einfarbig Silber, ca. 22 pt, links in der Kopfleiste, daneben „Vaultoria“ in SF Pro Semibold 17 pt #FFFFFF (normale Schreibweise). Auf dem Dach der Zentrale als unaufdringliches, unbeleuchtetes Schild.
- App-Icon: bis Julian entscheidet, bleibt das bisherige Icon (Frage offen).

**3D und Karte**
- Entsättigte, realistische Materialien: Asphalt matt, Häuser in gedeckten Putz- und Ziegeltönen, Dächer dunkelgrau/rotbraun, Bäume dunkelgrün. Abendlicht warm, aber zurückhaltend; Straßenlaternen kleine Lichtpunkte ohne Bloom.
- **Eigene Fahrzeuge:** realistisch weiß/graphit lackiert mit rot-weißer Warnmarkierung am Heck und orangefarbenem Rundumlicht (wie echte Abschleppwagen), kleines silbernes V an der Tür. Kein Gelb-Schwarz, kein Gold. Keine echten Marken.
- **Routen:** ~~dünne silberne Linie (2 pt)~~ ab 2.2 siehe Teil 000a.
- **Einsatzmarker:** ab 2.2 Orange, siehe Teil 000a.
- **Zentrale:** moderner Flachbau in Anthrazit und Glas, Rolltore, sachlich beleuchtet, keine Goldfassade.
- Personen (Mitarbeiterporträts): realistische Arbeitskleidung in Grau/Anthrazit mit Warnstreifen, kleines V-Logo.

**Realismus (2.1, ab 2.2 abgeschwächt, siehe Teil 000a: einheitlicher Stil geht vor; kein großer Asset-Tausch jetzt) — ursprünglich Julian 14.10 13:40: „ich gebe es dir frei weil ich wil ldas das realisitische autos häuser und menschen sind man“)**
- **Autos, Häuser und Menschen realistisch**: echte Proportionen, realistische Fahrzeugformen (Kleinwagen, Kombi, Transporter, Lkw, Bus), Häuser mit echten Fassaden, Fenstern, Dächern, Gehwegen; Menschen mit natürlichen Körperproportionen und Kleidung.
- **Keine Spielzeug- oder Low-Poly-Optik, auch nicht bei Figuren**: keine Kastenköpfe, keine Knubbelfiguren, keine übergroßen Köpfe, keine flachen Einfarb-Polygone, keine Comic-Konturen.
- **Freigegebene Quellen (CC0):** Poly Haven (Modelle, PBR-Texturen, HDRIs) und ambientCG (PBR-Materialien: Asphalt, Putz, Ziegel, Dachziegel, Metall, Glas). Bisherige Kenney-/Quaternius-Low-Poly-Teile werden schrittweise ersetzt, wo sie sichtbar sind.
- Materialien als PBR (Albedo, Normal, Roughness), entsättigt nach der Farbtabelle oben; Beleuchtung über ein Abend-HDRI. Lizenz und Quelle jedes Assets in einer Liste im Projekt festhalten (CC0, keine Namensnennung nötig, aber nachvollziehbar).
- Keine echten Automarken oder Logos an Modellen; Kennzeichen fiktiv.
- Leistung beachten: LOD-Stufen, beim Herauszoomen einfachere Modelle; 60 fps auf kleinen iPhones bleibt Pflicht.

**Prüffrage zum Stil:** Sieht der Bildschirm aus wie eine ernsthafte Disponenten-Software in einem hochwertigen Spiel, nicht wie ein Kinderspiel? Wenn irgendwo Gold, Glow oder Spielzeug-Optik auftaucht, ist es falsch.

## 000a. Lesbarkeit nach dem 5.0-Zwischenstand (2.2, geht Teil 000 bei Widerspruch vor)

Julian 14.10 13:50 (wörtlich):

> Das sieht deutlich professioneller aus. Die neue Richtung passt viel besser zu Vaultoria: seriös, hochwertig und wie ein richtiger Management-Tycoon. Die alte gelb-goldene Spielzeugoptik ist größtenteils weg.
> Was noch geändert werden sollte:
>
> * Route etwas kräftiger machen. Die dünne silberne Linie geht zwischen Straßen und Gebäuden teilweise unter. Etwas dicker plus dunkler Rand.
> * Orange als Funktionsfarbe behalten: Einsatzmarker, Warnungen und Rundumlichter dürfen orange sein. Sonst wird alles zu grau und unübersichtlich.
> * Zeitknöpfe größer antippbar machen. Optisch dürfen sie klein bleiben, aber die unsichtbare Touchfläche sollte mindestens 44 × 44 Punkte haben.
> * Eigene Fahrzeuge stärker kennzeichnen, damit man sofort erkennt, welcher Wagen gerade unterwegs oder verfügbar ist.
> * Einsatzarten benötigen verschiedene Symbole: Batterie, Reifen, Unfall und Abschleppen dürfen nicht alle gleich aussehen.
> * Bewertung am Spielstart nicht direkt 5,0: besser zunächst „Neu“ und die Sterne erst durch echte Einsätze aufbauen.
> * Bei „Ausbauen“ zusätzlich Preis und Nutzen anzeigen, beispielsweise „2.500 € · +1 Stellplatz“. Nur „Ausbauen“ ist zu unklar.
> * Die neu gerenderten Kartenbilder müssen stilistisch zur Stadt passen. Keine fotorealistischen Fahrzeuge in einer deutlich stilisierten Low-Poly-Stadt.
>
> Der große freie Hof hinter der Zentrale ist sehr gut – dort können später Stellplätze, Sammlung, Werkstatt und schwere Abschlepper sichtbar dazukommen.
> Mein Urteil für diesen Zwischenstand: 8/10. Die Grundoptik würde ich jetzt nicht erneut verändern. Claude soll die Kartenbilder fertigstellen, die genannten Lesbarkeitsprobleme korrigieren und anschließend lieber das eigentliche Gameplay testen.

**Grundoptik bleibt** wie im 5.0-Zwischenstand (Graphit/Anthrazit/Silber, SF Pro, dünne Linien, kein Gold). Nicht erneut umbauen. Danach Gameplay testen.

1. **Einheitlicher Stil statt Fotorealismus:** Karte, Fahrzeuge, Häuser und Figuren im selben Stil wie die Stadt. Keine fotorealistischen Einzelteile in der stilisierten Stadt. Neu gerenderte Kartenbilder werden an Stil, Licht und Detailgrad der Stadt angepasst. Poly Haven/ambientCG nur für Materialien und Licht, wo es zur Stadt passt; **kein großer Asset-Tausch jetzt**. Keine Kinder-/Knubbel-Optik bleibt verboten.
2. **Orange als Funktionsfarbe (#F08A24):** Einsatzmarker, Warnungen und Rundumlichter sind orange. Dringend bleibt rot (#D9473A) mit orangem Rundumlicht-Puls. Sonst bleibt alles Graphit/Silber.
3. **Route kräftiger:** 4 pt Silber #C7C7CC mit 1,5 pt dunklem Rand #1C1C1E (insgesamt ca. 7 pt), auf Straßenniveau, nicht von Gebäuden verdeckt (über der Geometrie gezeichnet). Rückfahrt gestrichelt in gleicher Stärke. Kein Leuchten.
4. **Touchflächen:** Alle Bedienelemente mindestens **44 × 44 pt** Trefferfläche, auch wenn sie optisch kleiner sind (Zeitknöpfe ⏸ 1× 2× 4× bleiben optisch klein, `contentShape` auf 44 × 44).
5. **Eigene Fahrzeuge klar kennzeichnen:** Über jedem eigenen Fahrzeug eine Plakette (Anthrazit, Silberrand) mit Kürzel und Statuspunkt: **grün = frei** (in der Zentrale), **orange = unterwegs zum Einsatz**, **silber = Arbeit vor Ort**, **grau = Rückfahrt**, **rot = Problem** (Tank/Zustand). Unter dem Fahrzeug ein dezenter silberner Ring, den fremde Autos nicht haben. Antippen wählt das Fahrzeug aus.
6. **Eigene Symbole je Einsatzart** (SF Symbols, im orangen bzw. roten Marker weiß):

| Einsatzart | Symbol |
|---|---|
| Batterie leer | `minus.plus.batteryblock` |
| Reifenpanne | `circle.circle` (Reifen) bzw. eigenes Reifen-Symbol |
| Fahrzeug abgeschlossen | `key.fill` |
| Falscher Kraftstoff | `fuelpump.fill` |
| Technischer Defekt | `wrench.and.screwdriver.fill` |
| Abschleppen | eigenes Abschlepphaken-Symbol |
| Unfall | `car.side.rear.and.collision.and.car.side.front` |

Keine zwei Einsatzarten mit gleichem Symbol.
7. **Bewertung startet als „Neu“:** Die Bewertungskapsel zeigt „Neu“ statt Sternen, bis 5 Einsätze bewertet sind; danach Ø Sterne mit einer Nachkommastelle.
8. **„Ausbauen“ mit Preis und Nutzen:** Knopf zweizeilig oder mit Unterzeile, z. B. **„Ausbauen“ / „2.500 € · +1 Stellplatz“**. Reicht das Geld nicht, Knopf ausgegraut mit „Fehlen 800 €“. Beispiele: Garage „+1 Stellplatz“, Werkstatt „Reparatur 20 % schneller“, Leitstelle „+1 gleichzeitiger Einsatz“.
9. **Hof hinter der Zentrale reserviert:** Die große freie Fläche hinter der Zentrale bleibt frei für spätere, sichtbar wachsende Teile: Betriebshof-Stellplätze (E6), Sammlung/Schauhalle (E12), Werkstatt-Erweiterung, Stellplätze für schwere Abschlepper (E15/E18). Nichts anderes dort bauen.

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

## 00b. Einsatz-Zuteilung (Konzeptbild `Konzept-Einsatz-Zuteilung.png`, 1.3, verbindlich)

Ersetzt den Ablauf aus Teil 2 und 3 (zwei Seiten) durch **ein** Panel. Antippen eines Einsatzmarkers lässt das Panel von unten über die Karte hochfahren (etwa 45 % Höhe, Griffleiste oben, nach unten wischen schließt). Karte, Kopfleiste und Tab-Leiste bleiben sichtbar.

- **Oben links** ein Bild des Kundenautos am Einsatzort (Motorhaube offen, Warndreiecke), Rahmen mit Goldrand.
- **Rechts daneben** der Einsatztitel in goldener Versalschrift, z. B. **„BATTERIE LEER“**, darunter zwei Kapseln: Ortsnadel + **„4,2 km“** und Geldbündel + **„180–240 €“** (Belohnung als Spanne).
- **Darunter zwei gleich große Karten nebeneinander**, beide schon vorausgewählt (goldener Haken oben rechts):
  - **Mitarbeiter**: Porträt in gelb-schwarzer Arbeitsjacke mit V-Logo und Kappe, Name (z. B. „Jonas“) mit Personensymbol, darunter eine 3-Segment-Leiste (Erfahrung/Eignung).
  - **Fahrzeug**: Bild des Wagens, Name (z. B. „Servicewagen 01“) mit Fahrzeugsymbol, darunter eine 4-Segment-Leiste (Zustand).
  - Antippen einer Karte öffnet die Auswahl der anderen freien Mitarbeiter bzw. Fahrzeuge als waagerechte Reihe gleicher Karten; Werte wie in Teil 3 (vier Balken, Hinweis wenn ungeeignet).
- **Unten ein breiter grüner Knopf** mit Goldrand: V-Logo links, **„Losschicken“** in Gold, Doppelpfeil rechts. Das ist der einzige Hauptknopf (Ausnahme zur Goldregel, Grün nur hier für „Los“). Ablehnen = Panel nach unten wischen.
- Dringlichkeit, benötigte Ausrüstung und Dauer erscheinen nur, wenn sie wichtig sind: rote Kapsel „Dringend“ neben dem Titel, bernsteinfarbene Zeile über dem Knopf, wenn das Fahrzeug nicht passt.
- Fahrzeugbilder ohne echte Herstellerlogos oder Marken (im Konzeptbild ist ein Stern zu sehen, der entfällt), nur das V-Logo.

## 00c. Tab Zentrale (Konzeptbild `Konzept-Zentrale.png`, 1.3, verbindlich)

- **Obere Hälfte**: isometrische Nahansicht der eigenen Zentrale bei Nacht: schwarzes Gebäude mit goldenem V-Logo, offene beleuchtete Tore mit gelb-schwarzen Fahrzeugen, gelb markierte Stellplätze, Tankstelle mit Dach, Reifenlager, Werkbänke, Mitarbeiter laufen herum, V-Schild an der Einfahrt, Kundenautos auf dem Hof. Alles, was ausgebaut ist, ist hier sichtbar (Teil 12).
- **Untere Hälfte**: Panel mit Gebäudesymbol und **„ZENTRALE“** in goldener Versalschrift, darunter **drei Ausbaukarten nebeneinander**:
  - **Garage** (Torsymbol): Bild mit Wagen auf Hebebühne, Symbol Auto+, Wirkung: mehr Stellplätze / Fahrzeuge.
  - **Werkstatt** (Werkzeugsymbol): Bild mit Werkbank und Reifen, Symbol Zahnrad, Wirkung: Reparaturen in der Zentrale, schnellere Arbeit.
  - **Leitstelle** (Bildschirmsymbol): Bild mit Arbeitsplatz und Stadtkarte auf Monitoren, Symbol Personen, Wirkung: mehr gleichzeitige Einsätze, mehr Personal, neue Viertel.
  - Jede Karte: Kapsel **„Stufe 1“** oben rechts, Bild, Symbol, **3-Segment-Stufenleiste** (gold = erreicht), goldener Knopf **„Ausbauen“**. Antippen von „Ausbauen“ zeigt kurz Preis und einen Satz Auswirkung, dann bestätigen, Kamera schwenkt auf das wachsende Gebäudeteil (Bau-Animation, Teil 12).
- Die sechs Ausbauten aus Teil 7 werden diesen drei Karten als Stufen zugeordnet: Garage = Stellplätze; Werkstatt = Werkstatt, Ersatzteillager, Tankstelle/Ladepunkt; Leitstelle = verbesserte Leitstelle. Mehr als drei Karten nur, wenn neue Gebäude dazukommen (dann seitlich wischen).
- Aktiver Tab „Zentrale“ unten in Gold.

## 0. Grundregeln

- **Kein Selbstfahren.** Kein Lenkrad, kein Steuerkreuz, kein Antippen zum Fahren. Fahrzeuge fahren nur automatisch.
- **Eine Hauptentscheidung pro Fenster**, ein goldener Hauptknopf, höchstens ein zweiter grauer Knopf.
- Fenster sind Bottom-Sheets (höchstens 50 % Höhe), die Karte bleibt immer sichtbar.
- Schrift mindestens 16 pt, Zahlen mindestens 20 pt, Knöpfe mindestens 52 pt hoch, volle Breite.
- Keine Prozentwerte, keine Sternleisten mit Zahlen, keine Textwände (höchstens zwei Zeilen Text pro Fenster).
- Keine Platzhalter-Menüs, kein „Demnächst“.
- Euro, deutsche Zahlen (1.250 €).

### Farben (bis 1.4, ÜBERHOLT durch Teil 000, nur noch Archiv)

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

- Draufsicht, leicht schräg von oben wie ein Tycoon-Spiel. Ab 1.2 ist die Welt sehr groß (Teil 12); der Start-Ausschnitt zeigt das erste Viertel mit der Zentrale. Zoomen mit zwei Fingern, verschieben mit einem.
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

## 12. Große Welt + sichtbare Ausbauten (1.2, Julian 14.10 11:06)

**Große Welt**
- Eine zusammenhängende, sehr große Stadtkarte aus mehreren Vierteln, z. B. Altstadt mit Kirche und Fluss (Start), Wohnviertel, Bahnhof, Gewerbegebiet, Autobahnzubringer, Hafen, Vororte. Jedes Viertel hat einen eigenen Look und eigene typische Einsätze.
- Frei wischen und mit zwei Fingern zoomen, flüssig mit Schwung und weichem Abbremsen. Weit herausgezoomt sieht man die ganze Stadt mit allen Fahrzeugen und Markern, nah dran Einzelheiten wie Warndreiecke und Werkzeug.
- Viertel sind von Anfang an sichtbar. Einsätze kommen zuerst nur aus dem Startviertel, weitere Viertel kommen mit dem Ausbau „Bessere Leitstelle“ und weiteren Stellplätzen hinzu (kein eigenes Freischalt-Menü).
- Einsatz außerhalb des Bildes: kleiner Pfeil am Bildrand in Markerfarbe, Antippen springt hin.
- Knopf unten rechts über der Tab-Leiste: „Zur Zentrale“ (V-Symbol), zentriert die Kamera.
- Leistung: nur sichtbare Bereiche voll zeichnen, ruckelfrei bei 60 fps auch auf kleinen iPhones.

**Sichtbare Ausbauten**
- Jeder Ausbau ist ein eigenes Gebäudeteil an der Zentrale und bleibt dauerhaft auf der Karte: Stellplatz = neue markierte Parkbucht, kleine Werkstatt = Anbau mit Rolltor und Hebebühne, Ersatzteillager = Hallenteil mit Regalen, Tankstelle = Zapfsäule mit Dach, Ladepunkt = Ladesäulen, bessere Leitstelle = Turm mit Antenne und Bildschirmen.
- Ausbauten haben Stufen (mindestens 3), jede Stufe sieht man: größere Werkstatt mit mehr Toren und Bühnen, mehr Stellplätze, größere Halle. Die Werkstatt wächst sichtbar mit.
- Beim Kauf: Kamera fährt zur Zentrale, kurze Bau-Animation (Gerüst, Kran, Staubwolke, Teil wächst hoch, Funken), dann goldenes Aufleuchten und Ton. Etwa 2–3 Sekunden, antippen überspringt.
- Im Tab Zentrale zeigt jeder Eintrag ein Vorschaubild, wie das Teil an der Zentrale aussehen wird.

## 13. Erste Version: 8 Pflichtpunkte (1.4, Julian 14.10 11:21, Spielkonzept Teil 3)

**Priorität:** bewegte Karte, echte Routen, mehrere gleichzeitige Einsätze. Spielspaß entsteht auf der Karte, nicht in Menüs. Jeder Punkt unten wird auf der Karte oder im vorhandenen Panel gezeigt, kein neues Menü.

1. **Einsatzwarteschlange:** Es liegen meist 2–4 Einsätze gleichzeitig auf der Karte. Der Tab „Karte“ zeigt die Zahl offener Einsätze. Antippen der Zahl öffnet eine schmale Liste (nach Countdown sortiert), Antippen eines Eintrags springt zum Marker und öffnet das Panel 00b.
2. **Countdown:** Jeder Marker hat einen Ring, der abläuft (grün → bernstein → rot). Im Panel steht die Restzeit („wartet noch 2:40“). Ist er abgelaufen, fährt der Kunde weg, der Marker verblasst und die Bewertung sinkt etwas.
3. **Live-Status:** An der Fahrzeugplakette und im Marker steht eine von vier Phasen mit Symbol: **Anfahrt → vor Ort → Reparatur → Rückfahrt**. Antippen eines Fahrzeugs zeigt eine kleine Leiste mit diesen vier Schritten, der aktuelle in Gold.
4. **Verkehr und Routen:** Staus sind als rot eingefärbte Straßenabschnitte auf der Karte sichtbar und wandern langsam. Die Route weicht automatisch aus, wenn das schneller ist. Im Panel 00b steht die Ankunftszeit mit Stau. Kein Selbstlenken; der Spieler wählt nur das Fahrzeug.
5. **Fahrzeugzustand:** Tank (bzw. Akku) und Zustand als zwei kleine Balken an jeder Fahrzeugkarte. Tanken, laden, reparieren und warten passiert in der Zentrale (Tab Flotte, Teil 6). Ist der Tank fast leer, schlägt das Spiel die Rückfahrt vor.
6. **Mitarbeiterschichten:** Jeder Mitarbeiter hat eine Schichtleiste (z. B. 8 Spielstunden). Ist sie leer, geht er nach dem laufenden Einsatz nach Hause und ist für die nächste Schicht wieder da. Müde Mitarbeiter (wenig Restschicht) arbeiten langsamer. Sichtbar im Tab Personal und auf der Mitarbeiterkarte im Panel 00b.
7. **Bewertungen:** Nach jedem Einsatz 1–5 Sterne, abhängig von Wartezeit und Ergebnis. Der Durchschnitt oben in der Kopfleiste. Höhere Bewertung bringt mehr und besser bezahlte Einsätze (in einem Satz erklärt, keine Prozentwerte).
8. **Einsatzbericht:** Nach jedem Auftrag kurz eine kleine Karte über der Karte (blockiert nicht, verschwindet nach 4 s oder per Wisch): **Einnahmen, Kosten (Kraftstoff, Teile, Lohnanteil), Dauer, Gewinn** groß in Grün oder Rot und die Sterne. Antippen zeigt die Zeilen genauer.

**Später, nicht jetzt (nichts davon einbauen, auch keine Platzhalter; Reihenfolge und Umsetzung jetzt in `Erweiterungsplan-Pannenhilfe.md`, Update für Update):** Verträge (Polizei, Versicherungen, Autohäuser, Werkstätten, Automobilclubs, Gemeinden), große Ereignisse (Massenkarambolage, Unwetter, Glatteis, Festival, Autobahnsperrung, Hochwasser, Wintereinbruch), Regionen (Innenstadt, Autobahn, Land, Berge, Industriegebiet), Spezialfahrzeuge (mobiler Batteriedienst, Plattform-Abschlepper, schwerer Berge-LKW, Kranwagen, mobile Ladestation, Ersatzteiltransporter), mehrere Zentralen mit Geschäftsführer, zusätzliche zufällige Entscheidungen (Öl verloren, Kunde kann nicht zahlen). Die eine seltene Sonderentscheidung aus Teil 5 bleibt.

**Offene Konzeptbilder:** Julian hat diese Ansichten als nächste Bilder vorgeschlagen. Sobald er eins schickt, wird es wie 00–00c verbindlich und kommt als eigener Teil hierher:
1. Flottenübersicht mit Fahrzeugzustand und Wartung
2. Personalansicht mit verfügbaren Fahrern
3. Einsatzbericht nach erfolgreicher Pannenhilfe
4. Nacht-/Regenkarte mit mehreren Notfällen
5. Große Autobahnbergung (späteres Spielziel)

Bis dahin gelten für Flotte, Personal und Einsatzbericht die Texte in Teil 6, Teil 00 (Tab Personal) und Punkt 8 oben.

## 11. Screenshots für die Abnahme

Hauptkarte leer · Einsatz erscheint · Einsatzfenster · Zuteilung · Fahrzeug unterwegs mit Route · Arbeit vor Ort · Belohnung · Rückfahrt · Fahrzeuge mit Warten · Zentrale mit Ausbau · Einsatz-Zuteilung-Panel (00b) · Tab Zentrale (00c) · Sonderentscheidung · Tagesabrechnung · mehrere Einsätze gleichzeitig mit Countdown-Ringen · Stau mit Umweg · Einsatzbericht · Personal mit Schichten · ganze Stadt herausgezoomt · Zentrale vor und nach einem Ausbau · Bau-Animation.
