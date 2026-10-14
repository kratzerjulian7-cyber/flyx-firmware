# Vaultoria – UI-Vorgabe 2.2 (verbindlich, nachbaufähig ohne Bilder)

Stand 14.10.2026, 08:00 (2.2: Julians Überarbeitungsliste nach Prüfung von 25 Screenshots, Spielkonzept Teil G: Teil 0b, neue Tab-Leiste, Bottom-Sheets, 16 pt, Tutorial in 7 Schritten, Rebirth-Zusammenfassung). 2.1 vom 14.10. 07:20 ( Euro statt Spielgeld, Kamera von weit oben, Erklärkarten K5, Julian 14.10 07:09). 2.0 vom 13.10.2026, 20:45 ersetzt die erste Fassung. Grund: Julian zu Build 1.0 (18:33): „noch sehr unübersichtlich … so wie ich es dir geschickt habe, so möchte ich das haben und nicht anders. Sondern genau so. Wie auf den Bildern … Genau diese Logik.“

**Diese Datei beschreibt jede Ansicht aus Julians Konzeptbildern so, dass sie ohne Bild nachgebaut werden kann.** Spielregeln und Zahlen stehen in `Spielkonzept.md`. Bei Widerspruch gilt für Aussehen und Bedienung diese Datei, für Regeln und Zahlen das Spielkonzept.

Quelle: fünf Bilder von Julian (13.10.2026, 12:40 bis 12:50), im selben Ordner:
- `ui-vorgabe-ansichten.png` → Ansichten A1 bis A4
- `icons-und-start.png` → Startbildschirm S0 und App-Icon
- `ui-vorgabe-shop.png` → Menüs M1 bis M4
- `ui-vorgabe-raubzug.png` → Raubzug R1 bis R6
- `ui-vorgabe-betrieb.png` → Betrieb B1 bis B6

---

# Teil 0 – Grundregeln (warum 1.0 unübersichtlich war, und wie es richtig ist)

Jede der 20 Ansichten auf Julians Bildern folgt demselben Bauplan. Wer diesen Bauplan einhält, bekommt automatisch Julians Look:

1. **Die 3D-Szene füllt immer den ganzen Bildschirm.** Sie ist das Spiel. Die Oberfläche liegt nur als wenige Inseln darüber. Kein Vollbild-Menü mit Listen, keine Formulare, keine Tabellen über die ganze Breite.
2. **Pro Ansicht höchstens fünf Bedienelemente:** Kopfleiste oben, Bereichstitel darunter, **eine oder zwei Karten**, **genau ein Hauptknopf** (grün im Betrieb, gold im Raubzug), unten gegebenenfalls die Tab-Leiste oder eine Kachelreihe. Mehr nicht.
3. **Wenig Text, große Zahlen.** Jede Zahl hat ein Symbol davor (Münze, Stern, Uhr, Pfote). Erklärungen höchstens zwei kurze Zeilen. Beträge immer groß und fett.
4. **Ein Hauptknopf, volle Breite der Karte, mindestens 50 pt hoch, mit Symbol links vom Text.** Ablehnen und Zurück sind kleiner oder dunkler.
5. **Figuren bewegen sich immer** (Kunden laufen, warten, zeigen Gegenstände, Mitarbeiter tragen Waren, Hunde spielen und ruhen). Auch hinter Menü-Karten läuft die Szene weiter.
6. **Die Kamera ist fest und schaut von weit oben** (Julian 14.10: „von viel weiter oben, nicht so komisch schräg“). Hauptansichten B1 und A3: Neigung ≈ 70° (fast Draufsicht), **keine seitliche Drehung** (Gebäude steht gerade, Kanten parallel zum Bildschirmrand), weit herausgezoomt, sodass der ganze Laden samt Gehweg bzw. das ganze Gebäude ins Bild passt. Schräge Blicke nur in Nahansichten (A1, B2: Blick über die Theke) und im Raubzug R4. Kamerafahrt in eine Nahansicht und zurück: 0,6 s, weich ein- und auslaufend.
9. **Jedes System erklärt sich selbst** (Julian 14.10: „den Kredit und alles besser erklären“). Siehe K5: Erklärkarte beim ersten Mal und „?“-Knopf auf jeder Karte.
7. **Alles wird schrittweise freigeschaltet.** Am Anfang gibt es nur den Laden mit einer Theke. Neue Bereiche, Tabs und Knöpfe erscheinen erst, wenn sie gebraucht werden (siehe Teil 8, Kernablauf). Ausnahme Tab-Leiste: Sie hat immer dieselben fünf Plätze, gesperrte Tabs tragen ein Schloss (K3).
8. **Keine Fremdmarken.** Erfundene Namen wie „LUMEN S-100“.

## Bildschirmmaß und Positionsangaben

- Referenz: iPhone im Hochformat, 393 × 852 pt (iPhone 15/16). Alle Positionen sind in **Prozent der Bildschirmhöhe (y) und -breite (x)** angegeben, von oben links gemessen, damit sie auf allen Größen gleich wirken. Safe Area oben (Dynamic Island) und unten (Home-Leiste) kommt zusätzlich.
- Außenrand der Karten zum Bildschirmrand: 3 % der Breite (≈ 12 pt). Abstand zwischen Karten: 1 % der Höhe (≈ 8 pt).
- Ecken: Karten 14 pt, Knöpfe 12 pt, Kacheln 10 pt.

## Farben (aus den Bildern gemessen)

| Rolle | Wert | Wo |
|---|---|---|
| Panel dunkel | `#171E20` bis `#1D2427`, 90 % deckend | Kopfleiste, dunkle Karten, Kachelreihen |
| Panel-Rand | `#2E3438`, 1 pt | dunkle Karten |
| Raubzug-Panel | `#141D19` mit Goldrand `#C9A45C` 1 pt | alle Raubzug-Karten |
| Creme-Karte | `#F7F1E8` (Menüs `#F2E6D2`), Goldrand 1 pt in Menüs | Verhandlung, Voraussetzungen, Shop-Karten |
| Creme dunkler | `#EBDBC5` | Belohnungs-Kachel |
| Grüner Hauptknopf | Verlauf `#3D7545` → `#235E35`, Rand `#4E8A55`, Text weiß | Betrieb |
| Goldener Hauptknopf | Verlauf `#F0CB62` → `#C99A2E`, Text und Symbol `#1C1C1E` | Raubzug |
| Roter Knopf | Verlauf `#8A4032` → `#6E2F25` | Ablehnen |
| Fortschritt grün | `#78C56F` | Stufenbalken, XP, „Gut“ |
| Gold | `#C9A45C`, Münze `#BD8337`, Stern `#CE913A` | Münze, Stern, Rahmen, Auswahl |
| Auswahl-Leuchten | Gold `#F2C94C`, 2 pt, äußeres Leuchten 8 pt | ausgewählte Etage, ausgewählte Kachel |
| Violett | Münze und Banner `#5B2D86`, Text `#B98BE6` | nur Rebirth-Coins |
| Engpass rot | `#9C2518` mit weißem Text | „Personal fehlt“, Sanduhr |
| Wache-Sichtkegel | `#E0453A`, 35 % deckend | Raubzug |
| Fluchtweg | `#3BD16F` | Raubzug |
| Tab-Leiste | `#1A1F1C`, aktiv gold `#E9BE4A` | Betrieb |
| Menü-Holz | `#3A2A1C` bis `#5A4230` | Hintergrund zwischen Menü-Karten |
| Text hell | `#FFFFFF` / `#D7D7DB` | auf Dunkel |
| Text dunkel | `#1C1C1E` / `#3A3A40` | auf Creme |

## Schrift

- Spielansichten: SF Pro. Bereichstitel 28 pt fett in Versalien („HANDEL“), Untertitel 15 pt normal.
- Menüs (Shop, Ausbau, Rebirth-Shop, Bonus): Titel in **Gold-Serifen-Versalien** (z. B. New York Bold oder eigenes Bild-Asset) mit Symbol davor. Kartentitel SF Pro Semibold 17 pt, zentriert (Serife nur für Überschriften und Logo, N6).
- Beträge fett, Tausenderpunkt, **immer mit „€“** und realistischen Preisen (Julian 14.10, Spielkonzept F2): „12.460 €“, „150 €“. Kein Wort „Spielgeld“ und keine Goldmünzen als Währung im Laden. Geldsymbol = kleiner grüner Geldschein. Rebirth-Coins bleiben violette Münzen (eigene Währung). Echtgeld-Preise im Shop kommen aus StoreKit und stehen nur dort. Überall, wo in dieser Datei „Münzen fliegen“ steht, fliegen im Laden **Geldscheine** zur Kopfleiste. Der Kontostand ist Geld im Spiel, er kann nie ausgezahlt oder gegen echtes Geld getauscht werden (steht einmal in den Einstellungen).

---

# Teil 0b – Neu in 2.2 (geht bei Widerspruch allem anderen in dieser Datei vor)

Arbeitsreihenfolge laut Julian: 1. Oberfläche entschlacken · 2. Tutorial · 3. Navigation · 4. Verkauf und Verhandlung animieren · 5. Räume optisch unterscheiden · 6. Raubzüge · 7. Wirtschaft und Preise · 8. neue Inhalte. **Keine neuen Funktionen vor Punkt 8.**

**N1. Spielwelt sichtbar (Julian: 60–70 %).** Ohne offenes Fenster sind mindestens **65 % der Bildschirmfläche freie Spielwelt** (Kopfleiste, Tab-Leiste, Aufgaben-Kapsel und Besitz-Leiste zusammen höchstens 35 %). Prüfen per Screenshot: alle Oberflächen-Flächen addieren.

**N2. Bottom-Sheets.** Jedes größere Fenster (Handel, Pfand, Personal, Werkstatt, Wertlager, Shop, Rebirth, Mehr, Bank) kommt als **Bottom-Sheet** von unten. Zwei Höhen: **halb (45 %)**, Laden bleibt darüber sichtbar, und **groß (85 %)** nur für Shop, Rebirth-Shop und Listen. Handel und Pfand nutzen immer die halbe Höhe. Schließen: nach unten wischen oder „✕“ oben rechts.

**N3. Eine Fensterform für alles.** Alle Sheets: oben 22 pt abgerundet, unten bündig mit dem Bildschirmrand, Hintergrund `#1E2A23` (dunkelgrün), 1,5 pt Goldrand oben, grauer Griff (36 × 5 pt) mittig oben. Karten in Sheets: 14 pt Radius. **Keine anders gerundeten Shop-Fenster mehr**, keine schwebenden Vollbild-Panels.

**N4. Aufgaben-Kapsel einklappbar.** Aufgaben und Ziele stehen nicht mehr als Leiste, sondern als **eine Kapsel** oben links unter der Kopfleiste (y 6–10 %, max. 60 % breit): Häkchen-Symbol + aktuelles Ziel in einer Zeile („Verkaufe 3 Gegenstände 1/3“). Antippen klappt die Liste auf (max. 3 Ziele), erneut antippen klappt sie zu. Eingeklappt ist Standard.

**N5. Besitz-Leiste klein.** Eingeklappt: schmale Leiste über der Tab-Leiste (y 85–90 %, 44 pt hoch): Kisten-Symbol, „Besitz 7“, Gesamtwert „1.840 €“, drei Mini-Bilder, Pfeil ▲. Antippen öffnet das Besitz-Sheet (halbe Höhe) mit Kachelraster. Die Leiste erscheint erst nach dem ersten Kauf.

**N6. Schrift größer und ruhiger.** Wichtige Texte und Werte **mindestens 16 pt**, Nebentexte mindestens 14 pt in `#C9C3B8` (nicht dunkler auf Dunkelgrün). **Serifenschrift nur für Überschriften und das Vaultoria-Logo**, alles andere SF Pro (Kartentitel SF Pro Semibold 17 pt). **Pro Karte genau eine große Zahl** (28–34 pt fett, z. B. der Preis), alle anderen Zahlen normal. Erklärtexte höchstens eine Zeile. **Höchstens ein grüner Hauptknopf pro Fenster**, weitere Aktionen als dunkle Umrissknöpfe. Besonders prüfen: Shop, Rebirth-Shop, Bank, Gebäudeübersicht.

**N7. Kein Hinweis-Gewitter.** Nie mehr als ein Hinweis gleichzeitig (Zeigehand, Pfeil, Erklärkarte oder Schwebetext). Titel wie „DEIN ERSTER LADEN“ blenden nach 2 s aus, bevor die Zeigehand erscheint.

**N8. Verkaufs-Effekte (Julian: „befriedigend“).** Bei jedem Verkauf in dieser Reihenfolge (zusammen ≈ 1,6 s): Gegenstand gleitet über den Tresen zum Kunden (0,4 s) → Kunde reagiert (Freuen-Geste + Sprechblase mit Herz oder Daumen) → **Kontostand zählt sichtbar hoch** (0,8 s, Ziffern rollen) mit Geldschein-Flug → **Ruf-Stern** des Bereichs pulsiert, „+3 Ruf“ steigt auf → leichte Haptik (Erfolg). Beim Ankauf dasselbe rückwärts. Großer Gewinn (über 50 %): zusätzlich kurzer Goldglanz und kräftigere Haptik.

**N9. Räume optisch unterscheiden.** Jeder Bereich bekommt eigene Farbe, eigenes Licht und eigene Ausstattung:

| Bereich | Wände und Boden | Licht | Typische Ausstattung |
|---|---|---|---|
| Laden | warmes Holz, roter Teppich | warm, Lampenlicht 2.700 K | Theke, Vitrinen, Uhren, Gitarren |
| Werkstatt | heller Beton, Holzwerkbank | neutral helles Arbeitslicht 4.500 K, Lampen über der Werkbank | Werkzeugwand, Schraubstock, Farbdosen, Späne am Boden |
| Wertlager | dunkler Stahl, Steinboden | dunkel mit goldenen Spots auf den Fächern | Schließfächer, Rundtresor, Gitterschiebetür |
| Tierpension | helles Holz, grüne Wände | Tageslicht, freundlich | Körbchen, Kratzbaum, Futternäpfe, Rasenauslauf |

**N10. Figuren.** Kunden mit weichem Schatten am Boden, größeren klar lesbaren Gesichtern (Augen und Mund sichtbar auch von oben), mindestens 12 Kleidungs-Varianten (Jacken, Hüte, Taschen, Farben), keine zwei gleich gekleideten Kunden gleichzeitig im Laden.

**N11. Shop ohne Lücken.** Keine leeren Flächen. Nicht verfügbare Käufe ausblenden oder als graue Karte mit Band „Demnächst“ (höchstens eine solche Karte pro Seite).

---

# Teil 1 – Feste Elemente

## K1. Kopfleiste (in allen Spielansichten gleich)

Lage: y 0–5 % (unter der Safe Area), x 3–97 %. Dunkles Panel, Ecken 12 pt, Höhe ≈ 44 pt. Von links nach rechts:

| Position x | Element |
|---|---|
| 4–24 % | Logo: kleines goldenes „V“ mit Schlüsselloch (App-Icon-Motiv, 22 pt) und daneben „VAULTORIA“ in Gold-Serifen-Versalien 17 pt |
| 27–46 % | „Lv. 28“ (11 pt, grau) über einem XP-Balken (grün auf dunkel, 6 pt hoch) |
| 53–74 % | Kapsel dunkel: grüner Geldschein 22 pt + Kontostand fett 17 pt („12.460 €“) |
| 75–88 % | Kapsel dunkel: Goldstern 20 pt + Gesamtansehen („420“) |
| 89–96 % | quadratischer Knopf, Zahnrad → Einstellungen (Musik, Sound, Vibration getrennt; Käufe wiederherstellen; Datenschutz) |

Ab dem ersten Neustart erscheint zwischen Stern und Zahnrad zusätzlich eine Kapsel mit **violetter Münze + Rebirth-Coins**. Keine Edelstein-Premiumwährung. Der violette Edelstein auf den Raubzug-Bildern bedeutet Rebirth-Coins.

Animation: Kommt Geld dazu, fliegen kleine Münzen von der Stelle in der Szene zur Geld-Kapsel (0,5 s), die Zahl zählt hoch, die Kapsel pulsiert kurz (Skalierung 1,0 → 1,1 → 1,0).

## K2. Bereichskopf (Spielansichten Teil 2 und Raubzug)

Lage: y 6–14 %, links, Breite nach Inhalt (max. 70 %). Halbtransparentes dunkles Panel. Links eine dunkle quadratische Kachel 56 × 56 pt mit cremeweißem Symbol, rechts daneben Titel (28 pt, fett, Versalien) und Untertitel (15 pt). Die Szene ist darunter sichtbar.

In den Betriebsansichten (Teil 6) steht der Titel **ohne Kachel und ohne Panel** direkt auf der Szene, weiß mit weichem Schatten.

## K3. Tab-Leiste (Betrieb)

Lage: y 91–100 % (über der Home-Leiste), volle Breite, Panel `#1A1F1C`. Fünf gleich breite Tabs, Symbol 24 pt über Text 12 pt:

| Tab | Symbol | Inhalt |
|---|---|---|
| Laden | Haus | Hauptansicht Laden (B1), Handel und Pfand als Sheet (A1, B2) |
| Besitz | Kiste | Besitz-Sheet: eigene Ware, sortierbar nach Wert, Zustand, Seltenheit. Antippen eines Gegenstands: Verkaufen, Restaurieren, Ausstellen |
| Personal | zwei Personen | B4 |
| Werkstatt | Hammer + Schraubenschlüssel | B5 |
| Mehr | drei Punkte | Sheet mit großen Zeilen (je 56 pt, Symbol + Text 17 pt): Kunden (B6) · Album · Aufträge · Statistik · Einstellungen. Noch nicht gebaut: ausgeblendet oder „Demnächst“ |

**Die Tab-Leiste ist in allen Betriebsansichten identisch** (gleiche 5 Tabs, gleiche Reihenfolge, nie andere Tabs, Julian 14.10). Wertlager und Tierpension haben keinen Tab, sie öffnen sich über ihre Etage in der Gebäudeübersicht A3 oder durch Antippen des Raums. Im Raubzug und in Sheets der großen Höhe ist die Tab-Leiste ausgeblendet.

Aktiver Tab: Symbol und Text gold `#E9BE4A`, goldene Linie 2 pt am oberen Rand des Tabs, Hintergrund etwas heller. Inaktiv: hellgrau. Die Tab-Leiste erscheint nach Tutorial-Schritt 6 sofort mit allen fünf Tabs. Noch gesperrte Tabs (Personal, Werkstatt) zeigen ein kleines Schloss und bleiben an ihrem Platz, damit sich nichts verschiebt. Antippen eines gesperrten Tabs: Schwebetext „Ab Laden Stufe 5“.

## K4. Gebäude-Knopf, Raubzug-Knopf, Shop-Knopf

Nicht auf den Bildern, aber nötig, um zwischen den Ansichten zu wechseln (Festlegung für den Umbau):
- **Gebäude-Knopf:** runder dunkler Knopf 48 pt mit Haus-Schnitt-Symbol, oben rechts unter der Kopfleiste (x 85–96 %, y 6–11 %), in allen Betriebsansichten → Gebäudeübersicht (A3). Wischen von links nach rechts tut dasselbe.
- **Raubzug-Knopf und Shop-Knopf:** zwei runde goldene Knöpfe 56 pt am rechten Rand der Gebäudeübersicht (x 84–96 %, y 50 % und 59 %), Symbole Maske bzw. Wappen mit Pfote. Raubzug erst ab Freischaltung sichtbar (Teil 8).

---

## K5. Erklärungen (neu, Julian 14.10)

Jedes System erklärt sich beim ersten Mal selbst, in Euro-Beispielen und ohne Fachwörter. Kein Textblock, sondern eine **Erklärkarte**:

- Creme-Karte mittig (x 6–94 %, y 30–72 %), Szene dahinter abgedunkelt, läuft weiter. Oben Symbol des Systems und Titel (z. B. „So funktioniert ein Pfandkredit“).
- **Drei nummerierte Schritte**, je ein kleines Bild links und höchstens eine Zeile Text, immer mit echten Beträgen aus der aktuellen Situation.
- Unten eine grüne Zeile **„Dein Gewinn: …“** oder **„Dein Risiko: …“** und ein grüner Knopf „Verstanden“.
- Danach auf jeder Karte dieses Systems oben rechts ein runder **„?“-Knopf** (28 pt, Gold auf Dunkelgrün), der dieselbe Erklärkarte wieder öffnet.

Pflicht-Erklärkarten (Texte als Vorlage, Zahlen kommen aus dem Spiel):

| System | Schritt 1 | Schritt 2 | Schritt 3 | Grüne Zeile |
|---|---|---|---|---|
| **Pfandkredit** | „Du leihst dem Kunden 150 € sofort bar.“ | „Er lässt seine Kamera als Sicherheit bei dir.“ | „Holt er sie in 2 Spieltagen ab, zahlt er 150 € + 15 € Gebühr zurück. Sonst gehört die Kamera dir (Wert ca. 220 €).“ | „Dein Gewinn: 15 € oder die Kamera.“ |
| **Ankauf & Verkauf** | „Du kaufst günstig an.“ | „Du verkaufst zum Marktwert.“ | „Die Differenz ist dein Gewinn.“ | „Beispiel: 200 € gezahlt, 330 € verkauft = 130 € Gewinn.“ |
| **Wertlager** | „Kunden lagern Wertsachen bei dir ein.“ | „Pro Spieltag zahlen sie Lagergebühr.“ | „Die Sachen gehören weiter dem Kunden, du darfst sie nie verkaufen.“ | „Dein Gewinn: 12 € pro Spieltag und Fach.“ |
| **Werkstatt** | „Abgenutzte Ware restaurieren lassen.“ | „Kostet Material und Zeit.“ | „Danach ist sie mehr wert.“ | „Beispiel: 80 € Material, Wert steigt von 300 € auf 520 €.“ |
| **Personal** | „Einmal einstellen, arbeitet für immer.“ | „Jede Stufe macht ihn schneller.“ | „Er bedient Kunden, auch wenn du nicht spielst.“ | „Mehr Kunden pro Minute = mehr Umsatz.“ |
| **Bank-Kredit** (eigener Kredit) | „Du leihst dir Geld von der Bank für einen Ausbau.“ | „Höchstens so viel, wie du selbst schon besitzt.“ | „Jeden Spieltag geht ein fester Teil plus Zinsen automatisch zurück.“ | „Dein Risiko: Offene Kredite blockieren den Neustart.“ |
| **Tierpension** | „Besitzer bringen ihre Tiere.“ | „Du betreust sie gut.“ | „Bei Abholung zahlen sie pro Tag.“ | „Tiere sind nie Beute und werden nie verletzt.“ |
| **Raubzug** | „Plane die Route.“ | „Wähle deine Crew.“ | „Nimm die wertvollste Beute, die du tragen kannst.“ | „Training kostet nichts und nimmt niemandem etwas weg.“ |
| **Neustart** | „Du ziehst an einen besseren Standort.“ | „Betrieb und Kontostand beginnen neu.“ | „Rebirth-Coins und Boni bleiben für immer.“ | „Dafür: dauerhaft mehr Einnahmen.“ |

# Teil 2 – Spielansichten (Bild `ui-vorgabe-ansichten.png`)

## A1. HANDEL (Nahansicht An- und Verkauf, Tab Laden während eines Kundengesprächs)

> **2.2 (geht vor):** Gegenstandskarte und Verhandlungskarte liegen zusammen in **einem Bottom-Sheet halber Höhe** (y 55–91 %, N2), darüber bleibt der Laden mit Kunde und Theke sichtbar (y 6–55 %). Im Sheet von oben: Gegenstand (Bild 64 pt links, Name 17 pt, Zustand und Seltenheit als Chips) · **eine große Zahl: „Dein Angebot 200 €“** (34 pt) mit Regler · eine Vergleichszeile 16 pt „Marktwert 320 € · Reparatur ca. 60 € · erwarteter Gewinn 60–220 €“ · grüner Hauptknopf „Kaufen“ und dunkler Umrissknopf „Ablehnen“. Forderung und Kundensatz stehen als Sprechblase über dem Kopf des Kunden in der Szene, nicht im Sheet. Die Besitz-Leiste ist während des Handels eingeklappt (N5). **„Prüfen“:** Lupe am Gegenstandsbild, Antippen dreht das Bild in 3D und deckt versteckte Merkmale auf (Kratzer, Signatur, Fälschungs-Hinweis), 1 s.

**Szene (ganzer Bildschirm):** Ladeninneres aus Sicht hinter der Theke. Im Vordergrund links unten (x 0–45 %, y 45–85 %) der **Betreiber von hinten** angeschnitten (dunkle Weste, weißes Hemd, Brille), die Theke aus dunklem Holz läuft quer durch das untere Drittel (y 52–80 %), darauf Kasse und kleiner Bildschirm. Hinter der Theke der **Kunde** (x 15–50 %, y 18–55 %): junger Mann, grüne Jacke, graue Kapuze, Rucksack, er hält die Kamera mit beiden Händen nach vorne. Hintergrund: Holzregale mit Uhren, Gitarren, Bildern, Lampen, Pflanzen; Wandschild „GUTE DINGE NEUE GESCHICHTEN“ mit kleiner Goldkrone (x 80–98 %, y 8–17 %). Warmes Lampenlicht, Teppich.

**Overlays von oben nach unten:**

| y | x | Element |
|---|---|---|
| 0–5 % | voll | Kopfleiste K1 |
| 6–14 % | 2–65 % | Bereichskopf: Kachel mit Handschlag · „HANDEL“ · „Kaufen · Verkaufen · Verhandeln“ |
| 20–47 % | 63–96 % | **Gegenstandskarte** (dunkel): „Gebrauchte Kamera“ (17 pt fett), darunter „LUMEN S-100“ (13 pt grau). Produktbild (≈ 40 % der Kartenhöhe). Drei Zeilen mit dünnen Trennlinien: „Zustand“ … **„Gut“** (grün), „Marktwert“ … „320 €“, „Unser Wert“ … „ca. 220 €“ |
| 48–81 % | 55–96 % | **Verhandlungskarte** (Creme): Zeile „Forderung:“ links, **„240“** rechts sehr groß (34 pt fett). Darunter Kundenporträt 44 pt (abgerundetes Quadrat) mit grauer Sprechblase „Mein letzter Preis.“ Dann „Dein Angebot:“ mit Trennlinie, darunter **„180“** zentriert (28 pt fett). Schieberegler: links dunkler Quadrat-Knopf „–“, grüne Füllung bis zum Regler-Knopf, rechts „+“. Grüner Hauptknopf volle Breite mit Handschlag-Symbol **„Angebot machen“**. Darunter roter Knopf mit X **„Ablehnen“** |
| 82–96 % | 2–96 % | **Besitz-Leiste** (dunkel): Kopf „Dein Besitz (Ladenbestand)“ mit kleinem Geldschein. Fünf quadratische Kacheln nebeneinander (je ≈ 18 % breit), Bild oben, Preis unten: Armbanduhr 450 €, Goldring 320 €, Kamera 220 €, Spielkonsole 180 €, Gitarre 650 €. Mehr als fünf: waagerecht wischen |

**Ablauf:** Kunde kommt zur Theke → Kamera fährt in A1 → Kunde hält Gegenstand hoch → Spieler stellt mit Regler oder +/– ein Angebot ein → „Angebot machen“.
- Kunde nimmt an: nickt, gibt den Gegenstand ab, Gegenstand fliegt in die Besitz-Leiste (0,5 s), Münzen fliegen vom Geldstand zum Kunden.
- Gegenangebot: Kopfschütteln, Sprechblase zeigt neuen Preis („260 sind fair.“), „Forderung“ ändert sich.
- Abbruch: Kunde winkt ab und geht durch die Tür. „Ablehnen“ beendet das Gespräch sofort.
- Verkauf an einen kaufenden Kunden: Kunde zeigt auf eine Kachel der Besitz-Leiste, dieselbe Karte erscheint mit „Gebot“ statt „Forderung“.
- Danach Kamera zurück in den Laden (B1) oder zur Gebäudeübersicht.

## A2. TIERPENSION (Nahansicht)

**Szene:** Heller Raum, beiger Fliesenboden. Links Holzregal mit Decken und Körben (x 0–18 %, y 15–45 %), Hundebild, Schild „Hier sind Freunde zuhause ♡“ (x 37–48 %, y 19–30 %). Pflegerin in grünem Polo kniet links (x 9–30 %, y 30–55 %) und füttert einen **Golden Retriever** aus einem schwarzen Napf. Jack Russell steht in der Mitte (x 50–64 %, y 42–55 %), Berner Sennenhund liegt rechts auf einem grünen Hundebett mit Knochen-Aufdruck (x 66–97 %, y 37–55 %). Grüne Hundebetten verteilt, Tennisbälle. Rechts oben eine große Öffnung zum umzäunten Außenauslauf mit Rasen, Holzrampe, zwei Besitzern, die einen Hund bringen bzw. abholen (x 60–100 %, y 14–37 %).

**Overlays:**

| y | x | Element |
|---|---|---|
| 0–5 % | voll | Kopfleiste |
| 6–14 % | 4–66 % | Bereichskopf: Pfote · „TIERPENSION“ · „Liebevolle Betreuung für glückliche Tiere“ |
| 7–12 % | 70–97 % | Creme-Kapsel: Pfote + **„3 / 4 Plätze“** |
| 60–77 % | 4–53 % | **Tierkarte** (dunkel): Pfeile ‹ › links und rechts zum Blättern, Porträt (quadratisch, ≈ 45 % der Kartenbreite), **„Bello“** (20 pt fett), „Golden Retriever“, zwei grüne Chips untereinander: Stern „Zufrieden“, Herz „Frisst gut“ |
| 57–80 % | 54–97 % | **Upgrade-Karte** (dunkel): „Betreuung · Stufe 12 / 100“, grüner Balken. Drei Zeilen mit kleinen Gold-Symbolen: „+1 Platz“, „Schnellere Betreuung“, „Höhere Zufriedenheit“. Grüner Hauptknopf mit Pfeil nach oben **„Upgrade: 1.200“** |
| 81–96 % | 3–97 % | **Platz-Leiste** (dunkel): vier Kacheln. Bello „Groß“ (ausgewählt, Goldrand), Luna „Mittel“, Max „Klein“, gesperrter Platz mit Schloss: „Platz frei ab Stufe 20“ |

Ablauf: Kachel antippen = Tier auswählen, Kamera schwenkt leicht zu diesem Hund. Besitzer bringen und holen Tiere im Auslauf ab, die Abrechnung fliegt als Münzen zur Kopfleiste. Tiere sind nie Beute und werden nie verletzt.

## A3. AUSBAU – Gebäudeübersicht (Hauptansicht des Spiels)

**Szene:** Das ganze Gebäude als **Schnittmodell**, **gerade von vorne und deutlich von oben** (≈ 30° Blick von oben, keine seitliche Drehung, weit herausgezoomt, ganzes Gebäude mit Gehweg im Bild), alle Etagen offen einsehbar wie ein Puppenhaus. Nicht mehr schräg gedreht (Julian 14.10). Abendstimmung, warmes Licht in den Räumen, Bäume links und rechts, Straße und Gehweg vorne. Von oben nach unten:

| y | Etage | Inhalt und Bewegung |
|---|---|---|
| 9–25 % (x 72–95 %) | Nächste Etage | gestrichelter weißer Umriss mit „+“-Kachel: „Nächste Etage“ / „(noch nicht verfügbar)“. Verfügbar: Umriss gold, „+“ pulsiert |
| 14–27 % | Tierpension | Hunde auf Betten, Pflegerin geht hin und her, Golden Retriever steht |
| 27–45 % | Wertlager | Regale mit goldenen Kisten, großer Rundtresor rechts, Mitarbeiter an einem Tisch. **Ausgewählt:** leuchtender Goldrahmen um die ganze Etage |
| 45–60 % | Laden (Erdgeschoss) | Zwei Theken, Mitarbeiter in Grün, Kunden stehen in einer **Schlange bis auf den Gehweg**. Rotes Engpass-Schild **„Personal fehlt“** (Personen-Symbol) über der Schlange (x 75–96 %, y 50–53 %) |
| 60–75 % | Parkplatz | Vier Stellplätze, zwei mit Autos (grüner SUV, weißer Kleinwagen), zwei leer mit gestricheltem Kreis und „×“. Text „2 / 4 Parkplätze belegt“ rechts unten (y 71–73 %) |

Autos fahren ein und aus, Kunden steigen aus und laufen zur Tür, stellen sich an, gehen mit Tüten wieder.

**Overlays:**

| y | x | Element |
|---|---|---|
| 0–5 % | voll | Kopfleiste |
| 6–14 % | 2–60 % | Bereichskopf: Hammer · „AUSBAU“ · „Dein Geschäft. Schritt für Schritt.“ |
| je Etage | 3–28 % | **Etagen-Schild** (dunkel, Ecken 10 pt): Symbol (Pfote, Kiste, Ladenfront) + Name + „Stufe 12“. Ausgewähltes Schild mit Goldrand und Leuchten |
| 76–97 % | 2–96 % | **Detailkarte** (dunkel): links Vorschaubild der Etage (≈ 25 % breit), rechts „Wertlager · Stufe 24 / 100“ + grüner Balken, drei Zeilen mit Gold-Symbolen („Mehr Kapazität für wertvolle Gegenstände“, „Höhere Sicherheit“, „Schnellere Einlagerung“), grüner Hauptknopf rechts unten mit Pfeil nach oben **„Ausbauen: 2.400“** |

Bedienung:
- Etage oder Schild einmal antippen = auswählen (Goldrahmen, Detailkarte wechselt).
- Ausgewählte Etage noch einmal antippen = **Kamerafahrt in die Nahansicht** (Laden → B1/A1, Wertlager → B3, Tierpension → A2).
- „Ausbauen“ = sofort eine Stufe höher. Bei Meilensteinstufen (10, 25, 50, 75, 100) ändert sich das Modell sichtbar (mehr Regale, zweite Theke, größerer Tresor), mit kurzem Funken- und Staubeffekt.
- Reicht das Geld: der Knopf pulsiert langsam. Reicht es nicht: grau, „Zu wenig Geld“.
- Engpass-Schilder (rot) schweben direkt über der betroffenen Etage. Antippen springt zum passenden Tab (z. B. „Personal fehlt“ → B4).

## A4. UMZIEHEN & NEU STARTEN (Rebirth)

> **2.2 (geht vor, Julian 14.10): erst Zusammenfassung, dann Bestätigung.** Ablauf in drei Schritten, jeder als Bottom-Sheet (N2):
>
> **Schritt 1 – Zusammenfassung** (Sheet groß, Titel „Umziehen“ in Gold-Serife). Vier große Blöcke untereinander, je Symbol 32 pt links + eine Zeile 17 pt:
> - rot `#AB4539`, Kreispfeil: **„Du verlierst:** Geld, Ladenstufen und normale Gegenstände“
> - grün, Schloss: **„Du behältst:** gekaufte Designs, Werbefreiheit und dauerhafte Boni“
> - violett, Coin: **„Du erhältst: 20 Rebirth-Coins“** (die Zahl als einzige große Zahl, 34 pt)
> - gold, Gebäude: **„Neuer Standort:** mehr Etagen, Kunden und Funktionen“
> Darunter grüner Knopf „Weiter“. Sind Voraussetzungen offen, steht statt „Weiter“ eine Zeile „Noch offen: …“ mit dem ersten fehlenden Punkt und der Knopf ist grau.
>
> **Schritt 2 – Alter Laden:** Sheet halb: „Verkaufen“ oder „Geschäftsführer einsetzen“ (D3, E2.4), je eine Karte, eine Zahl pro Karte.
>
> **Schritt 3 – Bestätigung:** mittiges Fenster (gleiche Form N3, 80 % breit), Szene stark abgedunkelt: „Wirklich umziehen?“ (22 pt), eine Zeile „Das kann nicht rückgängig gemacht werden.“, grüner Knopf „Umziehen“, darunter Textknopf „Abbrechen“.
>
> Die Tabelle unten (Standortkarten, Voraussetzungen, Wird zurückgesetzt, Bleibt) entfällt als Einzelbildschirm. Die Voraussetzungen sind über „Noch offen“ und R6 erreichbar.

Über der abgedunkelten Gebäudeübersicht (60 % Schwarz), dichtes Layout:

| y | x | Element |
|---|---|---|
| 0–5 % | voll | Kopfleiste |
| 6–14 % | 4–96 % | Kopf: Ortsmarke · „Umziehen & neu starten“ · „Größerer Standort. Mehr Möglichkeiten.“ |
| 15–55 % | 2–47 % und 53–98 % | **Zwei Standortkarten**, oben Creme mit Titel, Mitte gerendertes Gebäude, unten dunkel transparent mit drei Werte-Zeilen. Links: „Aktueller Standort“ · „Kleiner Laden“ · „Vorstadt“, kleines Eckhaus mit grünen Markisen und Goldkrone, Parkplatz. Werte: Gebäude-Symbol „3 Etagen“, Auto „4 Parkplätze“, Haus „Kleines Einzugsgebiet“. Rechts: „Neuer Standort (Vorschau)“ · „Geschäftshaus“ · „Stadtzentrum“, großes vierstöckiges Altbau-Eckhaus mit Mansarddach, Passanten, Autos. Werte: „4 Etagen“, „8 Parkplätze“, Hochhaus-Symbol „Großes Einzugsgebiet“. Dazwischen ein weißer Pfeil → |
| 56–71 % | 4–97 % | **Voraussetzungen** (Creme): Titel „Voraussetzungen für den Neustart“. Fünf Zeilen mit grünem Haken-Kreis: „Etagen vollständig (3 / 3)“, „Upgrades vollständig“, „Ansehen erreicht (500 / 500)“, „Geldziel erreicht (250.000 € / 250.000 €)“, „Keine offenen Kredite“. Dazu (Spielkonzept B5): „Kundenverträge abgewickelt“, „Tiere abgeholt“. Nicht erfüllt: leerer grauer Kreis. Rechts Kachel (Creme dunkler): „Belohnung:“ große Goldmünze mit Stern, **„+12“** (30 pt fett), „Rebirth-Coins“ |
| 72–85 % | 4–49 % | **„Wird zurückgesetzt:“** (hellrot `#E9B9A9`, Titel `#AB4539`, Kreispfeil-Symbol): Betrieb & Kontostand · Gebäude und Upgrades · Laufende Aufträge · Mitarbeiter |
| 72–85 % | 52–97 % | **„Bleibt:“** (hellgrün `#B7CAAD`, grüner Stern): Dauerhafte Boni · Freigeschaltete Designs · Erfolge · Rebirth-Coins |
| 87–95 % | 5–27 % | dunkler Rahmen-Knopf „‹ Zurück“ |
| 86–96 % | 39–97 % | großer grüner Knopf mit Rakete **„Neustart bestätigen“**, nur aktiv, wenn alles erfüllt ist |

Dazu (Spielkonzept D3, E2.4): Vor „Neustart bestätigen“ fragt ein Creme-Sheet „Was passiert mit deinem alten Laden?“ mit zwei großen Karten: **„Verkaufen“** (+15 % Rebirth-Coins) und **„Geschäftsführer einsetzen“** (drei Typen zum Antippen: Gewinn, Ruf, Sicherheit, je mit Prozentwert). Danach Kamerafahrt: alter Standort zoomt heraus, Fahrt über die Stadt, neuer Standort zoomt herein, Startbildschirm-Logo blendet kurz ein.

---

# Teil 3 – Startbildschirm und Icon (Bild `icons-und-start.png`)

## S0. Startbildschirm

- **Szene ganzer Bildschirm:** das Gebäude des aktuellen Standorts als 3D-Schnittmodell in Abendsonne, leicht schräg von vorne, leise animiert (Hund atmet, Lichter flackern leicht, Kunde und Betreiber an der Theke bewegen sich). Oben die Tierpension (Hund im Körbchen, Katzenbaum), Mitte das Wertlager (Regale mit Kisten, goldener Rundtresor rechts), unten der Laden (Betreiber mit Schürze, Kunde, Gitarre an der Wand). Rechts eine Hundehütte mit grünem Dach und Hund im umzäunten Garten, links ein dunkler SUV auf dem Parkplatz, Laternen, im Hintergrund Altstadt mit Kirchturm und Bäumen.
- **Logo** oben mittig (y 6–16 %): „VAULTORIA“ in großen Gold-Serifen-Versalien mit dunkler Kontur und Prägung, darüber ein kleines Dachgiebel-Element mit Pfote.
- **Claim** direkt darunter (y 17–20 %): „Dein Geschäft. Dein Imperium.“ (Serife, weiß, 15 pt).
- **Unten** (y 88–95 %): großer dunkelgrüner Knopf mit dünnem Goldrand und Serifen-Text **„Spielen“** (x 12–78 %), rechts daneben quadratischer Knopf gleicher Art mit Zahnrad (x 82–94 %).
- „Spielen“ → Kamera fährt in das Gebäude hinein: beim allerersten Start direkt in B1, sonst in die Gebäudeübersicht A3 mit Offline-Abrechnung.

## App-Icon: „Goldenes V“ (gewählt, Julian 13.10. 12:41)

Großes genietetes Gold-„V“ (sechs Nieten, gebürstetes Gold) mit rundem Schlüsselloch-Beschlag in der Mitte, auf dunkelgrünem, leicht strukturiertem Grund `#1E3A2E`. Datei `icon-goldenes-v.png` (aus dem Konzeptbild hochskaliert, für den Store in voller Auflösung neu zeichnen, Motiv gleich).

---

# Teil 4 – Menüs (Bild `ui-vorgabe-shop.png`)

Gemeinsamer Bauplan aller vier Menüs:
- Vollbild-Sheet von unten über der abgedunkelten Szene, nach unten wischen schließt.
- **Kopfbild** oben (y 0–28 %): warme Ladenszene mit einer **Gastgeber-Figur** im stilisierten 3D-Look (große Augen, weiche Formen) und einem Kreidetafel-Schild mit Spruch. Im Spiel als echte 3D-Szene oder als gerendertes Standbild aus eigenem 3D-Material, kein KI-Bild.
- **Titel** oben links in Gold-Serifen-Versalien mit Symbol davor (y 1–7 %). **Währungs-Kapsel** oben rechts (dunkel, halbtransparent): Münze + Betrag groß, darunter der Name klein.
- **Karten** Creme mit Goldrand, Titel in dunkler Serife zentriert, Bild, zwei Nutzen-Zeilen mit grünen Haken, unten Knopf über volle Kartenbreite.
- **Kaufknopf Euro oder Coins** zweiteilig: obere Hälfte grün mit Geldschein + Preis groß (bzw. violette Münze bei Coins), untere Hälfte grün mit „Kaufen“. **Kaufknopf Echtgeld** einteilig, nur Preis aus StoreKit.
- **Zustände:** kaufbar (grün) · zu wenig (beide Hälften grau `#C9C4BC`, Text `#6E6A63`, „Zu wenig Geld“ bzw. „Zu wenig Rebirth-Coins“) · gekauft oder maximal (grau mit Haken, „Gekauft“ bzw. „Maximal“).
- Zwischen den Karten: warmes dunkles Holzbraun.

## M1. VAULTORIA · SHOP

- Titel: Wappen mit Pfote + **„VAULTORIA · SHOP“**. Gastgeberin: junge Verkäuferin mit braunem Dutt, grüner Latzschürze, Arme verschränkt auf der Theke, links neben ihr ein Golden Retriever. Schild rechts: „ANKAUF · VERKAUF · PFOTE MIT HERZ“ + Pfote.
- **Drei Reiter** (y 29–34 %, volle Breite): **Shop** (aktiv: grün mit Goldrand) · **Ausbau** · **Rebirth-Coins** (inaktiv: fast schwarz-grün `#1A1F1C`, Text weiß). Ausbau → M2, Rebirth-Coins → M3.
- **Drei hohe Karten** nebeneinander (y 35–83 %):
  1. **Werbefrei**: großes rotes Verbotsschild über „AD“. Text „Keine Pflichtanzeigen. Belohnungsvideos bleiben freiwillig.“ Gold-brauner Chip „Einmalkauf“. Knopf **„6,99 €“** (Bild zeigt noch 4,99 €).
  2. **Starterpaket**: Bild eines Ladenschilds mit Pfote und „VAULTORIA“ über Goldmünzen. Punkte „Exklusives Shopschild (kosmetisch)“, **„5.000 € Startkapital“** (fett). Knopf **„2,99 €“**.
  3. **Gebäude-Design**: Bild einer eleganten Altbau-Ladenfront mit Schild „VAULTORIA“. Text „Elegantes Design für dein Pfandhaus (kosmetisch).“ Knopf **„3,99 €“**.
- Darunter (y 85–91 %) dunkler Knopf volle Breite mit Kreispfeil: **„Käufe wiederherstellen“**.
- Unter dem Knopf ein kleiner Text-Knopf „Bonus & Schutz ›“ → M4.
- Produkt-IDs: `com.julian.vaultoria.adfree`, `.starterpack`, `.design.classicfacade`.

## M2. AUSBAU (Reiter Ausbau)

- Titel: gekreuzte Hämmer + **„AUSBAU“**. Kapsel: Geldschein **„18.320 €“** / „Kontostand“. Gastgeber: kräftiger bärtiger Handwerker mit grüner Kappe, grüner Latzhose und Klemmbrett. Rechts ein grüner Pickup mit Pfote auf der Tür und zwei Hunden. Schild: „GRÖSSER · BESSER · MEHR TIERE · GLÜCKLICHER“.
- **2 × 2 Karten** (y 28–59 % und 61–94 %):
  1. **Verkäufer einstellen**: Bild Verkäuferin mit Daumen hoch an der Theke. „Bedient mehr Kunden“, „Schnellerer Verkauf“. **2.000** · Kaufen.
  2. **Parkplatz erweitern**: Bild Parkplatz mit P-Schild. „+2 Parkplätze“, „Mehr Kunden gleichzeitig“. **3.500** · Kaufen.
  3. **Tresor verbessern**: Bild Tresortür mit Pfote. „Mehr Lagerplatz“, „Wertvollere Gegenstände“. **4.000 €** · „Zu wenig Geld“ (Beispiel für den grauen Zustand).
  4. **Tierplätze erweitern**: Bild Hund und Katze im Körbchen. „+2 Tierplätze“, „Mehr Betreuung möglich“. **2.500** · Kaufen.
- Das ist die Schnellkauf-Liste: Sie zeigt immer die vier nächsten sinnvollen Käufe aus denselben Upgrade-Daten wie A3. Katzen erst, wenn Modelle da sind.

## M3. REBIRTH-SHOP (Reiter Rebirth-Coins)

- Titel: violette Münze mit Kreispfeilen + **„REBIRTH-SHOP“**. Kapsel: violette Münze **„24“** / „Rebirth-Coins“ (violetter Text). Gastgeber: älterer Herr mit weißem Haar, Schnurrbart, runder Brille, Weste, goldener Fliege und Taschenuhrkette, neben ihm eine graue Katze auf Büchern, Globus links. Schild: „NEUER ANFANG · STÄRKER · FÜR IMMER ∞“.
- Violettes Banner mit Goldrand und Krone (y 30–35 %): **„Diese Verbesserungen bleiben beim Neustart.“**
- **2 × 2 Karten** (Titel, Symbol links, Wert groß rechts mit Erklärung, Level-Zeile mit Punkten, zweiteiliger Knopf mit violetter Münze):
  1. **Mehr Startkapital**: Münzstapel mit grünem Pfeil, **„+10 %“** „Mehr Startkapital beim Neustart.“ Level 1/5. **5** · Kaufen.
  2. **Höhere Einnahmen**: Geldsack mit Pfote und Pfeil, **„+5 %“** „Mehr Einnahmen aus allen Quellen.“ Level 2/10. **8** · Kaufen.
  3. **Offline-Zeit**: Sanduhr, **„4 → 6 Stunden“** „Längere Offline-Einnahmen.“ Level 1/5. **10** · Kaufen.
  4. **Verhandlungsgeschick**: Handschlag, **„+2 %“** „Bessere Preise beim Verhandeln.“ Level 0/5. **6** · Kaufen.
- Level-Punkte: fünf Kreise, gefüllt violett, leer grau. Der Wert zeigt immer die Wirkung der nächsten Stufe.
- Vor dem ersten Neustart: Reiter sichtbar, Karten grau mit „Nach dem ersten Umzug“.

## M4. BONUS & SCHUTZ

- Titel: Wappen mit Pfote + **„BONUS & SCHUTZ“**. Kopfbild: Golden Retriever und grau-weiße Katze liegen auf der Theke. Schild: „GUTE GESCHÄFTE · GLÜCKLICHE TIERE“ + Pfote.
- **Große Creme-Karte „Freiwillige Belohnung“** (y 23–58 %), grünes Video-Symbol, Untertitel „Schau dir ein Video an und erhalte einen zeitlich begrenzten Bonus.“ Darin zwei Unterkarten:
  - **„Offline-Einnahmen verdoppeln“**: Goldmünzen mit zwei grünen Pfeilen, „4 Stunden“, grüner Knopf mit Play-Symbol **„Video ansehen“**.
  - **„Kurzer Schutz“**: Schild mit Pfote, „30 Minuten“, „Schützt vor Angriffen anderer Spieler.“, „Video ansehen“. **Erst mit echten Angriffen anderer Spieler, im ersten Build ausblenden.** An dieser Stelle steht dann „Kleiner Geldbonus“ (Münze, „+15 Minuten Einnahmen“, „Video ansehen“).
- Unten links Creme-Karte **„Echtgeld“** (€-Symbol): „Schutzpaket · 4 Stunden“, Schild mit Pfote und Uhr, „Schützt vor Angriffen anderer Spieler.“, „Eigener Angriff beendet den Schutz.“, Knopf „0,99 €“. **Später, im ersten Build nicht anlegen.** Bis dahin steht hier die Starterpaket-Karte aus M1.
- Unten rechts dunkle Karte **„Gewähltes Design“** (Goldwappen): Creme-Unterkarte „Klassische Fassade“ mit Bild der Ladenfront, dunkler Knopf **„Fassade ansehen“** → Kamera fährt zur Gebäudefront.

---

# Teil 5 – Raubzug (Bild `ui-vorgabe-raubzug.png`)

**Look:** nächtlich, dunkler als der Betrieb. Panels `#141D19` mit Goldrand. **Hauptknöpfe gold** mit dunklem Text. Grün nur für Haken und Fluchtweg. Wachen mit roten Sichtkegeln, Kameras mit roten Kegeln, Notausgang grün leuchtend.

Kopfleiste im Raubzug: V-Logo + „VAULTORIA“ · Geldschein „12.480 €“ · violette Münze „12“ (Rebirth-Coins) · Zahnrad.

Erster Build: nur lokale **Trainingsanlagen** („Rivalen-Lagerhaus – Ebene 1“ usw.), klar als Training benannt, keine Spielernamen.

## R1. RAUBZUG PLANEN

- Kopf (y 6–13 %): Fernglas-Maske · **„RAUBZUG PLANEN“** · „Rivalen-Lagerhaus – Ebene 1“.
- Szene (y 13–75 %): Lagerhaus als Grundriss von weit oben (≈ 75°, gerade ausgerichtet), Räume mit Kisten und Regalen, Tresorraum oben mit großem Rundtresor, zwei Wachen mit roten Sichtkegeln (eine oben links, eine Mitte links), zwei weitere Wachen in einem Raum rechts, Kamera-Symbol an einer Wand. **Weiß gestrichelte Route** mit runden weißen Wegpunkten vom Startmarker (Kopf-Symbol links) zum Tresor, **grün gestrichelter Fluchtweg** vom Tresor zum grünen Notausgang-Schild (Laufmann) unten rechts.
- Unten (y 76–81 %): Segment-Schalter volle Breite **„Manuell“** (aktiv, grün) | **„Automatisch“**.
- Darunter (y 83–89 %): goldener Knopf mit Play-Dreieck **„Starten“**.
- Bedienung: Wegpunkte antippen oder ziehen, die Route zeichnet sich live. Wachen laufen ihre Runden in Echtzeit, damit man Lücken sieht. „Starten“ → R2.

## R2. DEINE CREW

- Kopf: Personen-Symbol · **„DEINE CREW“** · „Spezialisten für diesen Auftrag“. Szene: Hinterzimmer mit Weltkarte an der Wand, Lampe.
- **Drei hohe Karten** (y 24–69 %, je ≈ 30 % breit, grüner Rahmen, dunkel). Oben Porträt (halbe Kartenhöhe), dann Name fett, Beschreibung, dann Zeile mit grünem Haken-Kästchen und Prozent in Gold, unten Werkzeug-Bilder:
  - **Die Schlosserin** (rote Haare, Dietriche in der Hand): „Öffnet selbst komplexe Schlösser.“ **15 %**. Werkzeug: Dietriche, Werkzeugrolle.
  - **Der Techniker** (Kappe, Kopfhörer, Brille, Tablet): „Deaktiviert Sicherheitssysteme.“ **10 %**. Werkzeug: Störsender, Gerätebox.
  - **Der Fahrer** (Kappe, braune Jacke): „Sorgt für eine saubere Flucht.“ **8 %**. Werkzeug: Autoschlüssel, Lieferwagen.
- Kapsel (y 72–77 %): **„Crew-Anteil: 33%“** (Zahl gold).
- Goldener Knopf (y 80–87 %): **„Crew bestätigen“** → R3 (manuell) oder direkt R4 (automatisch, mit 5 s Zeitraffer der Szene).
- Haken antippen = Mitglied an/aus. Jedes Mitglied senkt ein Risiko (Schlosszeit, Kameras/Alarm, Fluchtzeit, Tragfähigkeit +10 kg beim Fahrer, Spielkonzept E2.3).

## R3. EINBRUCH (manuell)

> **2.2 (Julian, Punkt 6 der Reihenfolge):** Sichtkegel **35 % Deckkraft** mit klarem Rand (2 pt) und Ausrufezeichen, wenn man hineinläuft. **Ziel** = pulsierender goldener Ring mit Raute-Symbol, **Ausgang** = grün leuchtender Rahmen mit Laufmann, beide auch am Bildschirmrand als Pfeil, wenn außer Sicht. Neue Hindernisse: Wachhund (Geruchskegel), Bewegungsmelder (pulsierender roter Kreis am Boden), verschlossene Räume (Schloss-Symbol, Schlosserin nötig). Beute-Wahl: kleine sichere Beute nahe am Weg, wertvolle Beute tiefer im Gebäude. **Gegenstände sind sichtbar** im Rucksack bzw. unter dem Arm, Figur wird mit Gewicht langsamer. Knappes Entkommen (Wache unter 1,5 m): **0,6 s Zeitlupe + starke Haptik**. Automatik bringt 70 % der möglichen Beute (Spielkonzept G2.3). Folgen bei Erwischen: Teilbeute, Crew-Mitglied 1 Spieltag „verletzt“ (Pflaster-Symbol, nicht verfügbar), nächster Raubzug 1 Spieltag „Alarmstufe erhöht“.

- Kopf links: Laufmann · **„EINBRUCH“** · „Finde das Ziel und entkomme unbemerkt.“
- Rechts oben (x 69–96 %, y 7–12 %): Kapsel mit Goldrand, Uhr + **„01:24“** (läuft rückwärts). Darunter (y 15–20 %): Kapsel Geldschein + **„1.200 €“** (Beute, zählt hoch, Tausenderpunkt).
- Szene: Nahansicht im Lager, schräg von oben **hinter der Spielfigur** (Dieb mit Kappe und großem Rucksack, geduckt). Wache mit Taschenlampe und rotem Sichtkegel in der Mitte, Kamera an der Wand mit rotem Kegel, offener Rundtresor mit Goldbarren rechts oben, grüner Notausgang rechts.
- Steuerung: **virtueller Joystick** unten links (x 5–35 %, y 74–88 %, dunkler Ring mit vier Pfeilen, heller Knauf). **Schleich-Knopf** unten rechts (x 71–95 %, y 77–87 %, runder dunkelgrüner Knopf mit weißem Ring, Symbol geduckte Figur).
- Gegenstände antippen = einsammeln (Fortschrittsring zeigt die Entwendungszeit). Gewicht macht langsamer (E2.3). Sicherheitskette Hund → Kamera → Wache und Gegenmaßnahmen wie E2.2 (Knöpfe für Leckerli, Störsender, Lärmquelle erscheinen als kleine runde Knöpfe über dem Schleich-Knopf, sobald nötig).
- Ausgang erreicht → R4. Zeit 0 oder von der Wache erreicht → R4 mit Teilbeute.

## R4. RAUBZUG BEENDET

- Kopf: grüner Haken im Kreis · **„RAUBZUG BEENDET“** · „Sauberer Abgang! Dein Team ist entkommen.“
- Szene (y 0–57 %): Nacht, die Crew sitzt jubelnd auf Kisten vor einem offenen dunklen Lieferwagen mit Goldkisten, dahinter Lagerhalle mit Schild „LAGER“, Lampen.
- **Abrechnungskarte** (y 58–80 %, dunkel, Goldrand): Münzstapel links. „Beute:“ **3.000** · „Crew:“ **−990** · Trennlinie · „Dein Anteil:“ **2.010** (groß, gold).
- Goldener Knopf (y 83–91 %): Haus · **„Zurück zum Betrieb“** → A3.
- Rechnung: Crew = Beute × Crew-Anteil, Dein Anteil = Beute − Crew, genau einmal verbucht.

## R5. SCHUTZ & BERICHT (simulierter Einbruch in den eigenen Betrieb)

- Kopf: Schild · **„SCHUTZ & BERICHT“** · „Ein Einbruch hat dein Lager getroffen.“
- Szene (y 0–53 %): aufgebrochene Tresortür mit Loch, Trümmer am Boden, Sicherheitsmann mit „SECURITY“-Weste kniet mit Tablet und Taschenlampe, Fußspuren, gelber Beweismarker „1“, Regale mit Kartons.
- Creme-Karte (y 54–66 %): kleines Bild der Tresortür, **„Verlust:“** **400 €**.
- Grüne Karte (y 67–76 %): grünes Schild-Symbol, **„Kostenloser Schutz aktiv“**, Uhr „Noch 2 Stunden“.
- Dunkler Knopf (y 78–85 %): Dokument · **„Bericht ansehen“** (Wegeskizze des Diebs, was erkannt wurde).
- Goldener Knopf (y 86–93 %): Schild · **„Sicherheit verbessern“** → A3 mit ausgewählter Sicherheits-Einrichtung.
- Verlust nur eigenes Geld, höchstens 10 %, nie Kundeneigentum, Pfänder, Tiere oder Gebäude.

## R6. DEIN NÄCHSTER AUFSTIEG

- Kopf: Diagramm mit Pfeil · **„DEIN NÄCHSTER AUFSTIEG“** · „Wachse in eine neue Stadt und übernimm ein größeres Lagerhaus.“
- Szene (y 0–45 %): Stadt am Fluss mit Bogenbrücke und Hochhäusern, großes Lagerhaus mit Schild „FLUSSLAGER“, Parkplatz mit dunklen SUVs, umzäunter Hundeauslauf mit Schäferhund.
- Dunkle Karte (y 46–84 %): Ortsmarke **„Flusslager – Stufe 2“**. Fünf Zeilen, Symbol links, Wert rechts, grüner Haken: Etagen 2 / 2 · Upgrades 6 / 6 · Ansehen 300 / 300 · Kapital 500.000 € / 500.000 € · Kredite zurückgezahlt 3 / 3. Darunter violetter Knopf mit Goldrand: Goldmünze **„+12 Rebirth-Coins“**. Darunter Haus-Symbol „Dauerhafte Boni bleiben.“
- Goldener Knopf (y 86–92 %): Karte · **„Vorschau öffnen“** → A4.
- R6 ist der Einstieg zum Rebirth: Die Ansicht wird erreichbar, sobald 80 % der Voraussetzungen erfüllt sind (Hinweis-Punkt am Gebäude-Knopf).

---

# Teil 6 – Betrieb mit Tab-Leiste (Bild `ui-vorgabe-betrieb.png`)

Kopfleiste in diesen Bildern: „VAULTORIA“ in Gold-Serife · Betrag (in den Bildern mit „Spielgeld“ darunter, im Umbau nur „12.460 €“) · Stern · Zahnrad. Für den Umbau gilt einheitlich K1. Bereichstitel groß weiß ohne Kachel direkt auf der Szene (y 7–14 %), Untertitel darunter. Unten die Tab-Leiste K3.

## B1. DEIN ERSTER LADEN (Tutorial, Tab Laden)

- Titel: **„DEIN ERSTER LADEN“** · „Bediene deinen ersten Kunden.“
- Szene: kleiner Laden **von weit oben ohne Dach** (≈ 70° fast Draufsicht, gerade ausgerichtet, nicht schräg; ganzer Laden, Gehweg und Parkplatz im Bild, Figuren klein, aber gut erkennbar), davor Gehweg und Parkplatz. Holztheke mit Glasvitrine in der Mitte (y 22–36 %), dahinter der Betreiber (Weste, Hemd), an der Rückwand Vitrinenschränke mit Uhren und Bildern, Gitarre und Stehlampe rechts. Links eine Kasse. Vorne links Kreidetafel-Aufsteller „VAULTORIA · ANKAUF · PFAND · SERVICE“ mit Waage (x 10–33 %, y 32–46 %). Blumenkästen, Laterne rechts. Teppich vor der Theke. Parkplatz (y 47–78 %) mit grünem Kleinwagen und beigem Oldtimer.
- **Tutorial-Hinweis:** dicker **grüner Pfeil** vom Kunden zur Theke, **Zeigehand** (cremefarben, dunkle Kontur) pulsiert auf dem Kunden. Der Kunde (junger Mann, Rucksack, Jeans) läuft vom Parkplatz zur Tür.
- Grüner Knopf (x 15–83 %, y 80–86 %): Person-Symbol **„Kunde bedienen“** → Kamerafahrt in A1.
- Nach dem Tutorial verschwinden Pfeil und Hand. Der Knopf erscheint dann nur, wenn ein Kunde an der Theke wartet, den kein Mitarbeiter übernimmt. Besondere Kunden tragen ein Ausrufezeichen in einer Sprechblase über dem Kopf. Antippen öffnet das Gespräch.

## B2. PFANDGESCHÄFT (Tab Laden)

- Titel: **„PFANDGESCHÄFT“** · „Biete einen fairen Kredit an.“
- Szene wie A1: junger Mann mit Locken und grüner Jacke hält eine Kamera über die Theke, rechts der Betreiber von hinten (Brille, Weste). Hinten Gitarre, Lampe, Fenster mit Schild „VAULTORIA“.
- Dunkle Karte (y 57–88 %): links Bild der Kamera (Kachel 32 % breit), rechts **„Verpfändet“** (fett) und darunter eine innere dunkle Box: „Kredit:“ **150 €** und Kalender „Frist:“ **2 Spieltage**. Unten zwei Knöpfe nebeneinander: grün mit Haken **„Kredit vergeben“**, rot mit X **„Ablehnen“**.
- Unter den Zahlen eine graue Zeile: **„Rückzahlung: 165 € (150 € + 15 € Gebühr)“** und ein „?“-Knopf oben rechts (öffnet die Erklärkarte Pfandkredit aus K5, beim allerersten Pfand automatisch).
- Spieltag vorerst 10 Minuten Echtzeit. Kredit wird sofort vom Kontostand abgezogen, Pfand bekommt Schloss-Chip „Verpfändet“ mit Restzeit. Auslösung = Kunde kommt zurück, zahlt Kredit + Gebühr (Münzen fliegen), nimmt das Stück mit. Sonst wird es nach Fristende „Dein Besitz“ und landet in der Besitz-Leiste.

## B3. WERTLAGER (über die Etage in A3, Sheet halbe Höhe)

- Titel: **„WERTLAGER“** · „Sichere Kundeneigentum ein.“
- Szene: Wand mit großen Schließfächern 01 bis 06 (Messingschilder), Fach in der Mitte offen (Gemälde, goldene Uhr, Vase). Mitarbeiterin in Weste und weißen Handschuhen zeigt einem älteren Kunden (Brille, Tweedjacke, von hinten links) das Fach.
- Dunkle Karte (y 57–88 %): „Kundeneigentum“, Reihe aus fünf Kacheln (Taschenuhr, Vase, Gemälde, Geige, Perlenkette). Darunter Fach-Symbol + **„Lagerplätze: 6 / 10“** und grüner Balken. Zwei Knöpfe: grün mit Kiste **„Einlagern“**, dunkel mit Goldrand und Handschlag **„Kaufangebot“** (Angebot an den Besitzer).
- Kundeneigentum: Schloss-Symbol, nie verkaufbar, nie ausstellbar, nie Raubzug-Verlust.

## B4. PERSONAL (Tab Personal)

- Titel: **„PERSONAL“** · „Stelle die richtigen Mitarbeiter ein.“
- Szene: voller Laden, lange Kundenschlange, roter Sanduhr-Kreis über der Schlange (Engpass „Kunden warten“). Ein Mitarbeiter von hinten an der Theke, Hund im Körbchen rechts.
- Dunkle Karte (y 45–90 %): oben drei Porträtkarten nebeneinander mit Namensschild darunter: **„Verkäufer“** (ausgewählt, Goldrand), **„Gutachter“** (Mann mit Bart und Lupe), **„Tierbetreuer“** (Frau mit Hund). Darunter Creme-Karte: Person-Symbol **„Verkäufer · Stufe 8“**, „Bedient Kunden schneller.“, graue Zeile „Einmalig einstellen“ **2.000 €**, grüner Knopf mit Person-Plus **„Einstellen“** (danach heißt er „Verbessern: …“).
- Eingestellte Mitarbeiter erscheinen sofort als Figur in der Szene und arbeiten sichtbar.

## B5. WERKSTATT (Tab Werkstatt)

- Titel: **„WERKSTATT“** · „Restauriere und erhöhe den Wert.“
- Szene: Werkstatt mit Werkzeugwand und Wanduhr, Restaurator (Dutt, Bart, Lederschürze) pinselt einen alten Holzstuhl auf der Werkbank, Messinglampe.
- Dunkle Karte (y 55–90 %): „Restaurieren“. Zwei Bilder nebeneinander „Vorher“ (abgenutzter Stuhl) → „Nachher“ (glänzender Stuhl), rechts daneben Box: **350 €** und grüner Pfeil „Wertsteigerung möglich“. Grüner Knopf mit Hammer **„Auftrag starten“**.
- Nur eigene Ware. Dauer mit Fortschrittsbalken über der Werkbank. Ergebnis: Zustand eine Stufe besser, Wert steigt.

## B6. KUNDEN & ANSEHEN (Tab Mehr → Kunden)

- Titel: **„KUNDEN & ANSEHEN“** · „Zufriedene Kunden kommen wieder.“
- Szene: ältere Dame mit Sonnenbrille im Haar und buntem Tuch im Vordergrund, dunkle Sprechblase mit Krone **„Stammkunde“**. Dahinter weitere Kunden und ein Golden Retriever.
- Dunkle Karte (y 35–90 %):
  - oben: Bild Armband, daneben Box „Letzte Transaktion“ · „Armband verpfändet“ · **320 €** · „vor 1 Spieltag“ · grüner Haken-Kreis.
  - Mitte: Box „Ansehen“ mit **5 Sternen** (4 gold, 1 grau) und goldenem Fortschrittsbalken. **Neu nach Spielkonzept E3:** darunter vier schmale Balken mit Symbol für die Bereiche Handel, Wertlager, Pfand, Tierpension (je 0–1.000). Der Stern-Wert ist der Durchschnitt.
  - darunter: Reihe aus vier Kundenporträts, das erste mit Krone und Goldrand (Stammkunde).
  - unten: grüner Knopf mit Sprechblasen **„Verhandeln“**, dunkler Knopf mit Goldrand und Lupe **„Angebot prüfen“**.

---

# Teil 7 – Navigation und Ablauf zwischen den Ansichten

```
S0 Start ──Spielen──► (erster Start) B1 Tutorial ──► A1 Handel
                      (später)      A3 Gebäudeübersicht

A3 Gebäudeübersicht (Hauptansicht)
 ├─ Etage antippen 2× ─► Laden: B1/A1/B2 · Wertlager: B3 · Tierpension: A2
 ├─ „Ausbauen“ ─► Stufe +1 (bleibt in A3)
 ├─ „+ Nächste Etage“ ─► Kauf-Bestätigung (Creme-Karte) ─► Bauanimation
 ├─ Engpass-Schild ─► passender Tab
 ├─ goldener Knopf Raubzug ─► R1 ─► R2 ─► R3 (manuell) ─► R4 ─► A3
 │                                    └─► (automatisch) R4
 ├─ goldener Knopf Shop ─► M1 ◄─Reiter─► M2 / M3 ; M4 über „Bonus & Schutz ›“ in M1
 └─ Rebirth-Hinweis ─► R6 ─► A4 ─► neuer Standort

Tab-Leiste (überall gleich): Laden · Besitz · Personal · Werkstatt · Mehr (Mehr → Kunden, Album, Aufträge, Statistik, Einstellungen)
Wertlager und Tierpension: nur über ihre Etage in A3
Gebäude-Knopf oben rechts oder Wischen nach rechts ─► A3 (immer möglich)
Simulierter Einbruch (Ereignis) ─► R5 als Karte über A3
```

Regeln:
- Jeder Wechsel in eine Nahansicht ist eine Kamerafahrt in derselben 3D-Welt, kein Bildschirmwechsel mit Schnitt.
- Menüs (M1–M4, A4) kommen als Sheet von unten. Zurück immer per Wischen nach unten oder „‹ Zurück“.
- Pflichtwerbung nie in Gespräch, Raubzug, Kauf oder Tutorial, nur beim Zurückkehren zu A3.

---

# Teil 8 – Kernablauf in Schritten (die ersten 10 Minuten)

Ziel: Im Zentrum steht Julians Kernablauf **Gegenstand entdecken → Wert einschätzen → verhandeln → verbessern → verkaufen oder sammeln → Laden ausbauen**. Das Tutorial folgt seinen 7 Schritten, ein Hinweis nach dem anderen (N7). Personal, Pfand, Wertlager, Tiere, Bank und Raubzug sind Erweiterungen und kommen erst danach. Der Spieler versteht das, mit je einer kurzen Erklärkarte pro neuem System (K5). Alle Zahlen sind Startwerte (Entwurf) für die Balancing-Datei.

| Zeit | Was der Spieler sieht | Was er tut | Was passiert |
|---|---|---|---|
| 0:00 | S0 Startbildschirm | „Spielen“ | Kamera fährt von weit oben auf den Laden (Draufsicht B1). Nur Kopfleiste mit **5.000 €**. Keine Tab-Leiste, keine Besitz-Leiste, keine Aufgaben-Kapsel |
| 0:03 | Titel „DEIN ERSTER LADEN“ blendet ein und nach 2 s wieder aus | nichts | Ruhige Szene, Betreiber hinter der Theke |
| 0:06 | **Schritt 1 – Kunde kommt herein:** Tür bimmelt, Kunde läuft vom Gehweg zur Theke | nichts | Kamera bleibt oben |
| 0:10 | **Schritt 2 – Kunde antippen:** erst jetzt Zeigehand über dem Kunden (einziger Hinweis) | Kunde antippen | Kamerafahrt in A1, Handel-Sheet halbe Höhe. Erklärkarte „Ankauf & Verkauf“ (K5, eine Zeile pro Schritt) |
| 0:20 | **Schritt 3 – Gegenstand prüfen:** Armbanduhr, Zustand „Gebraucht“, Zeigehand auf die Lupe | Lupe antippen | Uhr dreht sich, Kratzer am Glas wird sichtbar: „Glas zerkratzt, Werk läuft“. Marktwert 320 € erscheint |
| 0:35 | **Schritt 4 – Preis einstellen:** Sprechblase „240 € hätte ich gern.“, Zeigehand auf den Regler | Regler auf 200 € | Vergleichszeile zeigt „erwarteter Gewinn 60–220 €“ |
| 0:50 | **Schritt 5 – Gegenstand kaufen** | „Kaufen“ | Kunde nickt, Uhr gleitet über den Tresen zu dir, Kontostand zählt herunter auf 4.800 €. **Besitz-Leiste erscheint** (N5) mit der Uhr |
| 1:10 | **Schritt 6 – Restaurieren oder direkt verkaufen:** Sheet „Was machst du mit der Uhr?“, zwei Karten mit je einer großen Zahl: „Direkt verkaufen · **290 €**“ und „Restaurieren · 60 € → **420 €**“ | eine Karte wählen (Zeigehand auf Restaurieren, beide gehen) | Restaurieren: Werkbank-Animation 10 s, Glas glänzt. Danach kommt ein Käufer, Verkauf mit vollem Effekt N8: Kontostand zählt hoch auf 5.160 € (bzw. 5.090 €), „+3 Ruf“ |
| 2:00 | **Tab-Leiste erscheint** mit allen fünf Tabs (Personal und Werkstatt mit Schloss bzw. Werkstatt offen, falls restauriert). Aufgaben-Kapsel erscheint eingeklappt: „Verkaufe 3 Gegenstände 1/3“ | weiterspielen | Kunden kommen jetzt von selbst |
| 2:00–3:30 | Normale Kunden handelt der Betreiber automatisch zum fairen Preis ab, nur Kunden mit „!“ brauchen den Spieler | 2–3 „!“-Kunden selbst bedienen | Kontostand ≈ 6.000 € |
| 3:30 | **Schritt 7 – Ausbau:** Gebäude-Knopf pulsiert, Kamera fährt zu A3, „Theke ausbauen: 250 €“ | zweimal ausbauen | Theke Stufe 3, Kunden schneller |
| 4:30 | **Schritt 7 – Personal:** Schlange wird lang, Schild „Personal fehlt“, Schloss am Tab Personal fällt ab | Tab Personal → „Verkäufer einstellen: 1.500 €“ | Verkäuferin erscheint, Schlange baut sich ab. **Tutorial endet hier** |
| 5:30 | Kunde „Ich brauche schnell Geld.“ | „Pfand“ im Handel-Sheet → Erklärkarte Pfandkredit → 150 € | Erstes Pfand, Chip „Verpfändet“ |
| 6:30 | In A3 wird „+ Nächste Etage“ gold: „Wertlager freischalten: 4.500 €“ | kaufen | Etage Wertlager, öffnet sich über die Etage (kein Tab). Erklärkarte „Wertlager“ |
| 8:00 | Hinweis-Punkt auf „Mehr“ | Mehr → Kunden | Vier Bereichsbalken |
| 9:00 | Pfand-Kunde kommt zurück | nichts | 165 € fliegen ein, „+15 € Gebühr“ |
| 9:30 | Goldener Knopf „Raubzug-Training“ in A3 | optional | Erklärkarte Raubzug → R1 |
| 10:00 | Nächstes Ziel in der Aufgaben-Kapsel: „Tierpension freischalten: 18.000 €“ | weiterspielen | Kreislauf läuft. Pflichtwerbung frühestens nach 15 aktiven Minuten, nie im Tutorial |

Danach (Orientierung, kein Tutorial mehr): Tierpension nach ≈ 12–15 Min, Shop-Knopf ab ≈ 10 Min, Spezialisierungswahl ab Etage 2 (E2.8), Warenpakete ab Handels-Ruf 300 (E2.6), Schaufenster ab Laden Stufe 10 (E2.7), Rebirth-Hinweis R6 nach ≈ 2–3 Stunden Spielzeit.

## Prüfliste für den Umbau (vor TestFlight)

0. Teil 0b N1–N11 einzeln abhaken (65 % Spielwelt, Bottom-Sheets, eine Fensterform, 16 pt, ein grüner Knopf, gleiche Tab-Leiste).
1. Jede Ansicht gegen diese Datei prüfen: Lage der Karten (y-Prozent), Texte wörtlich, Zahlen mit Symbol, genau ein Hauptknopf.
2. Szene füllt immer den ganzen Bildschirm und bewegt sich, auch hinter Karten.
3. Hauptansichten von weit oben und gerade (Regel 6), alle Beträge in € (Spielkonzept F2), jede Erklärkarte aus K5 vorhanden.
4. Erster Start folgt Teil 8 Schritt für Schritt, ohne dass andere Tabs oder Knöpfe vorher sichtbar sind.
5. Kamerafahrten zwischen A3 und den Nahansichten statt harter Schnitte.
6. Screenshots aller 20 Ansichten (6,9" und 6,5") für Julian, neben seine Konzeptbilder gelegt.
