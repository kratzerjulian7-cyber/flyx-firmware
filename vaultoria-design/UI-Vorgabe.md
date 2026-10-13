# Vaultoria – UI-Vorgabe 2.0 (verbindlich, nachbaufähig ohne Bilder)

Stand 13.10.2026, 20:45. Ersetzt die erste Fassung. Grund: Julian zu Build 1.0 (18:33): „noch sehr unübersichtlich … so wie ich es dir geschickt habe, so möchte ich das haben und nicht anders. Sondern genau so. Wie auf den Bildern … Genau diese Logik.“

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
6. **Die Kamera ist fest** (leicht erhöht, schräg von oben), außer bei der Kamerafahrt in eine Nahansicht (0,6 s, weich ein- und auslaufend) und zurück.
7. **Alles wird schrittweise freigeschaltet.** Am Anfang gibt es nur den Laden mit einer Theke. Neue Bereiche, Tabs und Knöpfe erscheinen erst, wenn sie gebraucht werden (siehe Teil 8, Kernablauf). Gesperrte Tabs sind ausgeblendet, nicht grau.
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
- Menüs (Shop, Ausbau-Spielgeld, Rebirth-Shop, Bonus): Titel in **Gold-Serifen-Versalien** (z. B. New York Bold oder eigenes Bild-Asset) mit Symbol davor. Kartentitel in dunkler Serife, zentriert.
- Beträge fett, Tausenderpunkt (12.460). Spielgeld **ohne „€“** (Festlegung B9 im Spielkonzept), „€“ nur bei Echtgeld-Preisen im Shop.

---

# Teil 1 – Feste Elemente

## K1. Kopfleiste (in allen Spielansichten gleich)

Lage: y 0–5 % (unter der Safe Area), x 3–97 %. Dunkles Panel, Ecken 12 pt, Höhe ≈ 44 pt. Von links nach rechts:

| Position x | Element |
|---|---|
| 4–24 % | Logo: kleines goldenes „V“ mit Schlüsselloch (App-Icon-Motiv, 22 pt) und daneben „VAULTORIA“ in Gold-Serifen-Versalien 17 pt |
| 27–46 % | „Lv. 28“ (11 pt, grau) über einem XP-Balken (grün auf dunkel, 6 pt hoch) |
| 53–74 % | Kapsel dunkel: Goldmünze 22 pt + Spielgeld fett 17 pt („12.460“) |
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
| Laden | Haus | Handel und Pfand (B1, B2, A1) |
| Wertlager | Tresor-Quadrat | B3 |
| Personal | zwei Personen | B4 |
| Werkstatt | Hammer + Schraubenschlüssel | B5 |
| Kunden | Stern | B6 |

Aktiver Tab: Symbol und Text gold `#E9BE4A`, goldene Linie 2 pt am oberen Rand des Tabs, Hintergrund etwas heller. Inaktiv: hellgrau. Tabs erscheinen erst, wenn der Bereich freigeschaltet ist (Teil 8).

## K4. Gebäude-Knopf, Raubzug-Knopf, Shop-Knopf

Nicht auf den Bildern, aber nötig, um zwischen den Ansichten zu wechseln (Festlegung für den Umbau):
- **Gebäude-Knopf:** runder dunkler Knopf 48 pt mit Haus-Schnitt-Symbol, oben rechts unter der Kopfleiste (x 85–96 %, y 6–11 %), in allen Betriebsansichten → Gebäudeübersicht (A3). Wischen von links nach rechts tut dasselbe.
- **Raubzug-Knopf und Shop-Knopf:** zwei runde goldene Knöpfe 56 pt am rechten Rand der Gebäudeübersicht (x 84–96 %, y 50 % und 59 %), Symbole Maske bzw. Wappen mit Pfote. Raubzug erst ab Freischaltung sichtbar (Teil 8).

---

# Teil 2 – Spielansichten (Bild `ui-vorgabe-ansichten.png`)

## A1. HANDEL (Nahansicht An- und Verkauf, Tab Laden während eines Kundengesprächs)

**Szene (ganzer Bildschirm):** Ladeninneres aus Sicht hinter der Theke. Im Vordergrund links unten (x 0–45 %, y 45–85 %) der **Betreiber von hinten** angeschnitten (dunkle Weste, weißes Hemd, Brille), die Theke aus dunklem Holz läuft quer durch das untere Drittel (y 52–80 %), darauf Kasse und kleiner Bildschirm. Hinter der Theke der **Kunde** (x 15–50 %, y 18–55 %): junger Mann, grüne Jacke, graue Kapuze, Rucksack, er hält die Kamera mit beiden Händen nach vorne. Hintergrund: Holzregale mit Uhren, Gitarren, Bildern, Lampen, Pflanzen; Wandschild „GUTE DINGE NEUE GESCHICHTEN“ mit kleiner Goldkrone (x 80–98 %, y 8–17 %). Warmes Lampenlicht, Teppich.

**Overlays von oben nach unten:**

| y | x | Element |
|---|---|---|
| 0–5 % | voll | Kopfleiste K1 |
| 6–14 % | 2–65 % | Bereichskopf: Kachel mit Handschlag · „HANDEL“ · „Kaufen · Verkaufen · Verhandeln“ |
| 20–47 % | 63–96 % | **Gegenstandskarte** (dunkel): „Gebrauchte Kamera“ (17 pt fett), darunter „LUMEN S-100“ (13 pt grau). Produktbild (≈ 40 % der Kartenhöhe). Drei Zeilen mit dünnen Trennlinien: „Zustand“ … **„Gut“** (grün), „Marktwert“ … „320“, „Unser Wert“ … „ca. 220“ |
| 48–81 % | 55–96 % | **Verhandlungskarte** (Creme): Zeile „Forderung:“ links, **„240“** rechts sehr groß (34 pt fett). Darunter Kundenporträt 44 pt (abgerundetes Quadrat) mit grauer Sprechblase „Mein letzter Preis.“ Dann „Dein Angebot:“ mit Trennlinie, darunter **„180“** zentriert (28 pt fett). Schieberegler: links dunkler Quadrat-Knopf „–“, grüne Füllung bis zum Regler-Knopf, rechts „+“. Grüner Hauptknopf volle Breite mit Handschlag-Symbol **„Angebot machen“**. Darunter roter Knopf mit X **„Ablehnen“** |
| 82–96 % | 2–96 % | **Besitz-Leiste** (dunkel): Kopf „Dein Besitz (Ladenbestand)“ mit kleiner Goldmünze. Fünf quadratische Kacheln nebeneinander (je ≈ 18 % breit), Bild oben, Preis unten: Armbanduhr 450, Goldring 320, Kamera 220, Spielkonsole 180, Gitarre 650. Mehr als fünf: waagerecht wischen |

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

**Szene:** Das ganze Gebäude als **Schnittmodell**, schräg von oben (≈ 35° Neigung, 20° seitlich gedreht), alle Etagen offen einsehbar wie ein Puppenhaus. Abendstimmung, warmes Licht in den Räumen, Bäume links und rechts, Straße und Gehweg vorne. Von oben nach unten:

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
- Reicht das Geld: der Knopf pulsiert langsam. Reicht es nicht: grau, „Zu wenig Spielgeld“.
- Engpass-Schilder (rot) schweben direkt über der betroffenen Etage. Antippen springt zum passenden Tab (z. B. „Personal fehlt“ → B4).

## A4. UMZIEHEN & NEU STARTEN (Rebirth)

Über der abgedunkelten Gebäudeübersicht (60 % Schwarz), dichtes Layout:

| y | x | Element |
|---|---|---|
| 0–5 % | voll | Kopfleiste |
| 6–14 % | 4–96 % | Kopf: Ortsmarke · „Umziehen & neu starten“ · „Größerer Standort. Mehr Möglichkeiten.“ |
| 15–55 % | 2–47 % und 53–98 % | **Zwei Standortkarten**, oben Creme mit Titel, Mitte gerendertes Gebäude, unten dunkel transparent mit drei Werte-Zeilen. Links: „Aktueller Standort“ · „Kleiner Laden“ · „Vorstadt“, kleines Eckhaus mit grünen Markisen und Goldkrone, Parkplatz. Werte: Gebäude-Symbol „3 Etagen“, Auto „4 Parkplätze“, Haus „Kleines Einzugsgebiet“. Rechts: „Neuer Standort (Vorschau)“ · „Geschäftshaus“ · „Stadtzentrum“, großes vierstöckiges Altbau-Eckhaus mit Mansarddach, Passanten, Autos. Werte: „4 Etagen“, „8 Parkplätze“, Hochhaus-Symbol „Großes Einzugsgebiet“. Dazwischen ein weißer Pfeil → |
| 56–71 % | 4–97 % | **Voraussetzungen** (Creme): Titel „Voraussetzungen für den Neustart“. Fünf Zeilen mit grünem Haken-Kreis: „Etagen vollständig (3 / 3)“, „Upgrades vollständig“, „Ansehen erreicht (500 / 500)“, „Geldziel erreicht (25.000 / 25.000)“, „Keine offenen Kredite“. Dazu (Spielkonzept B5): „Kundenverträge abgewickelt“, „Tiere abgeholt“. Nicht erfüllt: leerer grauer Kreis. Rechts Kachel (Creme dunkler): „Belohnung:“ große Goldmünze mit Stern, **„+12“** (30 pt fett), „Rebirth-Coins“ |
| 72–85 % | 4–49 % | **„Wird zurückgesetzt:“** (hellrot `#E9B9A9`, Titel `#AB4539`, Kreispfeil-Symbol): Betrieb & Spielgeld · Gebäude und Upgrades · Laufende Aufträge · Mitarbeiter |
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
- **Kaufknopf Spielgeld oder Coins** zweiteilig: obere Hälfte grün mit Münze + Preis groß, untere Hälfte grün mit „Kaufen“. **Kaufknopf Echtgeld** einteilig, nur Preis aus StoreKit.
- **Zustände:** kaufbar (grün) · zu wenig (beide Hälften grau `#C9C4BC`, Text `#6E6A63`, „Zu wenig Spielgeld“ bzw. „Zu wenig Rebirth-Coins“) · gekauft oder maximal (grau mit Haken, „Gekauft“ bzw. „Maximal“).
- Zwischen den Karten: warmes dunkles Holzbraun.

## M1. VAULTORIA · SHOP

- Titel: Wappen mit Pfote + **„VAULTORIA · SHOP“**. Gastgeberin: junge Verkäuferin mit braunem Dutt, grüner Latzschürze, Arme verschränkt auf der Theke, links neben ihr ein Golden Retriever. Schild rechts: „ANKAUF · VERKAUF · PFOTE MIT HERZ“ + Pfote.
- **Drei Reiter** (y 29–34 %, volle Breite): **Echtgeld** (aktiv: grün mit Goldrand) · **Spielgeld** · **Rebirth-Coins** (inaktiv: fast schwarz-grün `#1A1F1C`, Text weiß). Spielgeld → M2, Rebirth-Coins → M3.
- **Drei hohe Karten** nebeneinander (y 35–83 %):
  1. **Werbefrei**: großes rotes Verbotsschild über „AD“. Text „Keine Pflichtanzeigen. Belohnungsvideos bleiben freiwillig.“ Gold-brauner Chip „Einmalkauf“. Knopf **„6,99 €“** (Bild zeigt noch 4,99 €).
  2. **Starterpaket**: Bild eines Ladenschilds mit Pfote und „VAULTORIA“ über Goldmünzen. Punkte „Exklusives Shopschild (kosmetisch)“, **„5.000 Spielgeld“** (fett). Knopf **„2,99 €“**.
  3. **Gebäude-Design**: Bild einer eleganten Altbau-Ladenfront mit Schild „VAULTORIA“. Text „Elegantes Design für dein Pfandhaus (kosmetisch).“ Knopf **„3,99 €“**.
- Darunter (y 85–91 %) dunkler Knopf volle Breite mit Kreispfeil: **„Käufe wiederherstellen“**.
- Unter dem Knopf ein kleiner Text-Knopf „Bonus & Schutz ›“ → M4.
- Produkt-IDs: `com.julian.vaultoria.adfree`, `.starterpack`, `.design.classicfacade`.

## M2. AUSBAU · SPIELGELD (Reiter Spielgeld)

- Titel: gekreuzte Hämmer + **„AUSBAU · SPIELGELD“**. Kapsel: Münze **„18.320“** / „Spielgeld“. Gastgeber: kräftiger bärtiger Handwerker mit grüner Kappe, grüner Latzhose und Klemmbrett. Rechts ein grüner Pickup mit Pfote auf der Tür und zwei Hunden. Schild: „GRÖSSER · BESSER · MEHR TIERE · GLÜCKLICHER“.
- **2 × 2 Karten** (y 28–59 % und 61–94 %):
  1. **Verkäufer einstellen**: Bild Verkäuferin mit Daumen hoch an der Theke. „Bedient mehr Kunden“, „Schnellerer Verkauf“. **2.000** · Kaufen.
  2. **Parkplatz erweitern**: Bild Parkplatz mit P-Schild. „+2 Parkplätze“, „Mehr Kunden gleichzeitig“. **3.500** · Kaufen.
  3. **Tresor verbessern**: Bild Tresortür mit Pfote. „Mehr Lagerplatz“, „Wertvollere Gegenstände“. **4.000** · „Zu wenig Spielgeld“ (Beispiel für den grauen Zustand).
  4. **Tierplätze erweitern**: Bild Hund und Katze im Körbchen. „+2 Tierplätze“, „Mehr Betreuung möglich“. **2.500** · Kaufen.
- Das ist die Schnellkauf-Liste: Sie zeigt immer die vier nächsten sinnvollen Käufe aus denselben Upgrade-Daten wie A3. Katzen erst, wenn Modelle da sind.

## M3. REBIRTH-SHOP (Reiter Rebirth-Coins)

- Titel: violette Münze mit Kreispfeilen + **„REBIRTH-SHOP“**. Kapsel: violette Münze **„24“** / „Rebirth-Coins“ (violetter Text). Gastgeber: älterer Herr mit weißem Haar, Schnurrbart, runder Brille, Weste, goldener Fliege und Taschenuhrkette, neben ihm eine graue Katze auf Büchern, Globus links. Schild: „NEUER ANFANG · STÄRKER · FÜR IMMER ∞“.
- Violettes Banner mit Goldrand und Krone (y 30–35 %): **„Diese Verbesserungen bleiben beim Neustart.“**
- **2 × 2 Karten** (Titel, Symbol links, Wert groß rechts mit Erklärung, Level-Zeile mit Punkten, zweiteiliger Knopf mit violetter Münze):
  1. **Mehr Startkapital**: Münzstapel mit grünem Pfeil, **„+10 %“** „Mehr Spielgeld beim Neustart.“ Level 1/5. **5** · Kaufen.
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

Kopfleiste im Raubzug: V-Logo + „VAULTORIA“ · Münze „12.480“ · violette Münze „12“ (Rebirth-Coins) · Zahnrad.

Erster Build: nur lokale **Trainingsanlagen** („Rivalen-Lagerhaus – Ebene 1“ usw.), klar als Training benannt, keine Spielernamen.

## R1. RAUBZUG PLANEN

- Kopf (y 6–13 %): Fernglas-Maske · **„RAUBZUG PLANEN“** · „Rivalen-Lagerhaus – Ebene 1“.
- Szene (y 13–75 %): Lagerhaus als Schnitt von schräg oben wie A3, Räume mit Kisten und Regalen, Tresorraum oben mit großem Rundtresor, zwei Wachen mit roten Sichtkegeln (eine oben links, eine Mitte links), zwei weitere Wachen in einem Raum rechts, Kamera-Symbol an einer Wand. **Weiß gestrichelte Route** mit runden weißen Wegpunkten vom Startmarker (Kopf-Symbol links) zum Tresor, **grün gestrichelter Fluchtweg** vom Tresor zum grünen Notausgang-Schild (Laufmann) unten rechts.
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

- Kopf links: Laufmann · **„EINBRUCH“** · „Finde das Ziel und entkomme unbemerkt.“
- Rechts oben (x 69–96 %, y 7–12 %): Kapsel mit Goldrand, Uhr + **„01:24“** (läuft rückwärts). Darunter (y 15–20 %): Kapsel Münze + **„1.200“** (Beute, zählt hoch, Tausenderpunkt).
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
- Creme-Karte (y 54–66 %): kleines Bild der Tresortür, **„Verlust:“** Münze **400** „Spielgeld“.
- Grüne Karte (y 67–76 %): grünes Schild-Symbol, **„Kostenloser Schutz aktiv“**, Uhr „Noch 2 Stunden“.
- Dunkler Knopf (y 78–85 %): Dokument · **„Bericht ansehen“** (Wegeskizze des Diebs, was erkannt wurde).
- Goldener Knopf (y 86–93 %): Schild · **„Sicherheit verbessern“** → A3 mit ausgewählter Sicherheits-Einrichtung.
- Verlust nur eigenes Spielgeld, höchstens 10 %, nie Kundeneigentum, Pfänder, Tiere oder Gebäude.

## R6. DEIN NÄCHSTER AUFSTIEG

- Kopf: Diagramm mit Pfeil · **„DEIN NÄCHSTER AUFSTIEG“** · „Wachse in eine neue Stadt und übernimm ein größeres Lagerhaus.“
- Szene (y 0–45 %): Stadt am Fluss mit Bogenbrücke und Hochhäusern, großes Lagerhaus mit Schild „FLUSSLAGER“, Parkplatz mit dunklen SUVs, umzäunter Hundeauslauf mit Schäferhund.
- Dunkle Karte (y 46–84 %): Ortsmarke **„Flusslager – Stufe 2“**. Fünf Zeilen, Symbol links, Wert rechts, grüner Haken: Etagen 2 / 2 · Upgrades 6 / 6 · Ansehen 300 / 300 · Spielgeld 50.000 / 50.000 · Kredite zurückgezahlt 3 / 3. Darunter violetter Knopf mit Goldrand: Goldmünze **„+12 Rebirth-Coins“**. Darunter Haus-Symbol „Dauerhafte Boni bleiben.“
- Goldener Knopf (y 86–92 %): Karte · **„Vorschau öffnen“** → A4.
- R6 ist der Einstieg zum Rebirth: Die Ansicht wird erreichbar, sobald 80 % der Voraussetzungen erfüllt sind (Hinweis-Punkt am Gebäude-Knopf).

---

# Teil 6 – Betrieb mit Tab-Leiste (Bild `ui-vorgabe-betrieb.png`)

Kopfleiste in diesen Bildern: „VAULTORIA“ in Gold-Serife · Münze + Betrag mit „Spielgeld“ klein darunter · Stern · Zahnrad. Für den Umbau gilt einheitlich K1. Bereichstitel groß weiß ohne Kachel direkt auf der Szene (y 7–14 %), Untertitel darunter. Unten die Tab-Leiste K3.

## B1. DEIN ERSTER LADEN (Tutorial, Tab Laden)

- Titel: **„DEIN ERSTER LADEN“** · „Bediene deinen ersten Kunden.“
- Szene: kleiner Laden **von schräg oben ohne Dach**, davor Gehweg und Parkplatz. Holztheke mit Glasvitrine in der Mitte (y 22–36 %), dahinter der Betreiber (Weste, Hemd), an der Rückwand Vitrinenschränke mit Uhren und Bildern, Gitarre und Stehlampe rechts. Links eine Kasse. Vorne links Kreidetafel-Aufsteller „VAULTORIA · ANKAUF · PFAND · SERVICE“ mit Waage (x 10–33 %, y 32–46 %). Blumenkästen, Laterne rechts. Teppich vor der Theke. Parkplatz (y 47–78 %) mit grünem Kleinwagen und beigem Oldtimer.
- **Tutorial-Hinweis:** dicker **grüner Pfeil** vom Kunden zur Theke, **Zeigehand** (cremefarben, dunkle Kontur) pulsiert auf dem Kunden. Der Kunde (junger Mann, Rucksack, Jeans) läuft vom Parkplatz zur Tür.
- Grüner Knopf (x 15–83 %, y 80–86 %): Person-Symbol **„Kunde bedienen“** → Kamerafahrt in A1.
- Nach dem Tutorial verschwinden Pfeil und Hand. Der Knopf erscheint dann nur, wenn ein Kunde an der Theke wartet, den kein Mitarbeiter übernimmt. Besondere Kunden tragen ein Ausrufezeichen in einer Sprechblase über dem Kopf. Antippen öffnet das Gespräch.

## B2. PFANDGESCHÄFT (Tab Laden)

- Titel: **„PFANDGESCHÄFT“** · „Biete einen fairen Kredit an.“
- Szene wie A1: junger Mann mit Locken und grüner Jacke hält eine Kamera über die Theke, rechts der Betreiber von hinten (Brille, Weste). Hinten Gitarre, Lampe, Fenster mit Schild „VAULTORIA“.
- Dunkle Karte (y 57–88 %): links Bild der Kamera (Kachel 32 % breit), rechts **„Verpfändet“** (fett) und darunter eine innere dunkle Box: „Kredit:“ Münze **150** „Spielgeld“ und Kalender „Frist:“ **2 Spieltage**. Unten zwei Knöpfe nebeneinander: grün mit Haken **„Kredit vergeben“**, rot mit X **„Ablehnen“**.
- Spieltag vorerst 10 Minuten Echtzeit. Kredit wird sofort vom Spielgeld abgezogen, Pfand bekommt Schloss-Chip „Verpfändet“ mit Restzeit. Auslösung = Kunde kommt zurück, zahlt Kredit + Gebühr (Münzen fliegen), nimmt das Stück mit. Sonst wird es nach Fristende „Dein Besitz“ und landet in der Besitz-Leiste.

## B3. WERTLAGER (Tab Wertlager)

- Titel: **„WERTLAGER“** · „Sichere Kundeneigentum ein.“
- Szene: Wand mit großen Schließfächern 01 bis 06 (Messingschilder), Fach in der Mitte offen (Gemälde, goldene Uhr, Vase). Mitarbeiterin in Weste und weißen Handschuhen zeigt einem älteren Kunden (Brille, Tweedjacke, von hinten links) das Fach.
- Dunkle Karte (y 57–88 %): „Kundeneigentum“, Reihe aus fünf Kacheln (Taschenuhr, Vase, Gemälde, Geige, Perlenkette). Darunter Fach-Symbol + **„Lagerplätze: 6 / 10“** und grüner Balken. Zwei Knöpfe: grün mit Kiste **„Einlagern“**, dunkel mit Goldrand und Handschlag **„Kaufangebot“** (Angebot an den Besitzer).
- Kundeneigentum: Schloss-Symbol, nie verkaufbar, nie ausstellbar, nie Raubzug-Verlust.

## B4. PERSONAL (Tab Personal)

- Titel: **„PERSONAL“** · „Stelle die richtigen Mitarbeiter ein.“
- Szene: voller Laden, lange Kundenschlange, roter Sanduhr-Kreis über der Schlange (Engpass „Kunden warten“). Ein Mitarbeiter von hinten an der Theke, Hund im Körbchen rechts.
- Dunkle Karte (y 45–90 %): oben drei Porträtkarten nebeneinander mit Namensschild darunter: **„Verkäufer“** (ausgewählt, Goldrand), **„Gutachter“** (Mann mit Bart und Lupe), **„Tierbetreuer“** (Frau mit Hund). Darunter Creme-Karte: Person-Symbol **„Verkäufer · Stufe 8“**, „Bedient Kunden schneller.“, graue Zeile „Einmalig einstellen“ Münze **2.000** „Spielgeld“, grüner Knopf mit Person-Plus **„Einstellen“** (danach heißt er „Verbessern: …“).
- Eingestellte Mitarbeiter erscheinen sofort als Figur in der Szene und arbeiten sichtbar.

## B5. WERKSTATT (Tab Werkstatt)

- Titel: **„WERKSTATT“** · „Restauriere und erhöhe den Wert.“
- Szene: Werkstatt mit Werkzeugwand und Wanduhr, Restaurator (Dutt, Bart, Lederschürze) pinselt einen alten Holzstuhl auf der Werkbank, Messinglampe.
- Dunkle Karte (y 55–90 %): „Restaurieren“. Zwei Bilder nebeneinander „Vorher“ (abgenutzter Stuhl) → „Nachher“ (glänzender Stuhl), rechts daneben Box: Münze **350** „Spielgeld“ und grüner Pfeil „Wertsteigerung möglich“. Grüner Knopf mit Hammer **„Auftrag starten“**.
- Nur eigene Ware. Dauer mit Fortschrittsbalken über der Werkbank. Ergebnis: Zustand eine Stufe besser, Wert steigt.

## B6. KUNDEN & ANSEHEN (Tab Kunden)

- Titel: **„KUNDEN & ANSEHEN“** · „Zufriedene Kunden kommen wieder.“
- Szene: ältere Dame mit Sonnenbrille im Haar und buntem Tuch im Vordergrund, dunkle Sprechblase mit Krone **„Stammkunde“**. Dahinter weitere Kunden und ein Golden Retriever.
- Dunkle Karte (y 35–90 %):
  - oben: Bild Armband, daneben Box „Letzte Transaktion“ · „Armband verpfändet“ · Münze **320** „Spielgeld“ · „vor 1 Spieltag“ · grüner Haken-Kreis.
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

Tab-Leiste (in B1–B6, A1, A2): Laden · Wertlager · Personal · Werkstatt · Kunden
Gebäude-Knopf oben rechts oder Wischen nach rechts ─► A3 (immer möglich)
Simulierter Einbruch (Ereignis) ─► R5 als Karte über A3
```

Regeln:
- Jeder Wechsel in eine Nahansicht ist eine Kamerafahrt in derselben 3D-Welt, kein Bildschirmwechsel mit Schnitt.
- Menüs (M1–M4, A4) kommen als Sheet von unten. Zurück immer per Wischen nach unten oder „‹ Zurück“.
- Pflichtwerbung nie in Gespräch, Raubzug, Kauf oder Tutorial, nur beim Zurückkehren zu A3.

---

# Teil 8 – Kernablauf in Schritten (die ersten 10 Minuten)

Ziel: Der Spieler versteht in 10 Minuten den Eatventure-Kreislauf **Kunden bedienen → Geld → ausbauen → Personal → Engpass lösen → neuer Bereich**, ohne einen einzigen Erklärtext zu lesen. Alle Zahlen sind Startwerte (Entwurf) für die Balancing-Datei.

| Zeit | Was der Spieler sieht | Was er tut | Was passiert |
|---|---|---|---|
| 0:00 | S0 Startbildschirm, Logo, Claim, Szene animiert | „Spielen“ | Kamera fährt ins Erdgeschoss. Nur der Laden existiert, die oberen Etagen sind dunkle Umrisse. Spielgeld **1.000**, Ansehen 0. Keine Tab-Leiste, keine anderen Knöpfe |
| 0:10 | B1 „DEIN ERSTER LADEN“, Kunde läuft vom Parkplatz zur Theke, grüner Pfeil, Zeigehand | „Kunde bedienen“ | Kamerafahrt in A1 |
| 0:20 | A1 Handel: Kunde bietet **Armbanduhr** an, Forderung 240, Marktwert 320, unser Wert ca. 220 | Regler bewegen (Zeigehand zeigt auf den Regler), „Angebot machen“ | Kunde nimmt bei 200 an (im Tutorial immer Annahme). Uhr fliegt in „Dein Besitz“. Spielgeld 800 |
| 0:50 | Zweiter Kunde will kaufen, zeigt auf die Uhr | Angebot annehmen | Verkauf für 330. Münzen fliegen zur Kopfleiste. Spielgeld 1.130. Schwebetext „+130 Gewinn“ |
| 1:20 | Dritter Kunde mit Kamera, Sprechblase **„Ich brauche schnell Geld.“** (Kundenwunsch E2.1) | Zeigehand auf neuen Knopf „Pfand“ in der Karte → B2 „Kredit vergeben“ 150, Frist 2 Spieltage (20 Min) | Erstes Pfand. Kamera bekommt Chip „Verpfändet 19:59“. **Tab-Leiste erscheint mit „Laden“** |
| 2:00 | Kamera fährt zurück zur Gebäudeübersicht A3 (erste Fahrt nach außen). Nur Erdgeschoss „Laden · Stufe 1“, Detailkarte „Theke · Stufe 1 / 100“, Knopf „Ausbauen: 100“ pulsiert | „Ausbauen“ zweimal | Theke Stufe 3: Kunden werden schneller bedient. Der Unterschied ist sofort sichtbar |
| 2:30 | Kunden kommen jetzt von selbst in kurzer Folge. Normale Kunden handelt der Betreiber automatisch zum fairen Preis ab, nur Kunden mit „!“ brauchen den Spieler | 2–3 besondere Kunden selbst verhandeln | Geld steigt auf ≈ 1.800 |
| 4:00 | Schlange wird lang, rotes Schild **„Personal fehlt“** über dem Laden | Schild antippen → **Tab „Personal“ erscheint**, B4, „Verkäufer einstellen: 600“ | Verkäuferin erscheint als Figur an der zweiten Theke. Schlange baut sich sichtbar ab |
| 5:00 | Umriss „+ Nächste Etage“ wird gold und pulsiert: **„Wertlager freischalten: 1.500“** | antippen, Kauf bestätigen | Bauanimation (Gerüst, Staub, 3 s). Etage 2 Wertlager. **Tab „Wertlager“ erscheint** |
| 5:30 | Kunde mit Gemälde, Sprechblase „Kann ich das sicher bei Ihnen lassen?“ | „Einlagern“ in B3 | Fach 01 öffnet sich, Gemälde mit Schloss „Kundeneigentum“. Gebühr kommt pro Spieltag |
| 6:30 | Ein gekaufter abgenutzter Stuhl liegt in „Dein Besitz“, Hinweis-Punkt am neuen **Tab „Werkstatt“** | „Auftrag starten“ (350) | Restaurator arbeitet 30 s sichtbar, Stuhl wird „Sehr gut“, Wert steigt von 300 auf 520 |
| 8:00 | Ansehen-Stern zeigt erste Fortschritte, **Tab „Kunden“ erscheint**, erste Stammkundin mit Krone | Tab ansehen | Spieler sieht die vier Bereichsbalken (Handel schon gefüllt, Wertlager und Pfand wenig) |
| 9:00 | Pfand-Kunde von 1:20 kommt zurück | nichts | Er löst aus: 150 + 30 Gebühr fliegen als Münzen. Erklärt das Pfandprinzip ohne Text |
| 9:30 | Gebäudeübersicht: Wertlager Stufe 1, Laden Stufe 5, neuer goldener Knopf rechts **„Raubzug-Training“** mit Hinweis-Punkt | (optional) antippen → R1 Trainingsanlage Ebene 1 | Kurzer Trainings-Raubzug: Route, Crew (nur Schlosserin frei), Einbruch 60 s, Abrechnung |
| 10:00 | Nächstes Ziel sichtbar: Umriss **„+ Tierpension freischalten: 6.000“** | weiterspielen | Ab hier läuft der Kreislauf: Geld sammeln, Etagen und Stufen kaufen, Engpässe lösen. Pflichtwerbung frühestens nach 15 aktiven Minuten und nie im Tutorial |

Danach (Orientierung, kein Tutorial mehr): Tierpension nach ≈ 12–15 Min, Shop-Knopf ab ≈ 10 Min, Spezialisierungswahl ab Etage 2 (E2.8), Warenpakete ab Handels-Ruf 300 (E2.6), Schaufenster ab Laden Stufe 10 (E2.7), Rebirth-Hinweis R6 nach ≈ 2–3 Stunden Spielzeit.

## Prüfliste für den Umbau (vor TestFlight)

1. Jede Ansicht gegen diese Datei prüfen: Lage der Karten (y-Prozent), Texte wörtlich, Zahlen mit Symbol, genau ein Hauptknopf.
2. Szene füllt immer den ganzen Bildschirm und bewegt sich, auch hinter Karten.
3. Erster Start folgt Teil 8 Schritt für Schritt, ohne dass andere Tabs oder Knöpfe vorher sichtbar sind.
4. Kamerafahrten zwischen A3 und den Nahansichten statt harter Schnitte.
5. Screenshots aller 20 Ansichten (6,9" und 6,5") für Julian, neben seine Konzeptbilder gelegt.
