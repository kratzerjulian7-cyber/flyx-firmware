# Vaultoria – Erweiterungsplan Pannenhilfe 2.0 (freigegeben, E1 erledigt, als Nächstes Komplettüberarbeitung 5.3; Rückgrat = Firmenentwicklung, Teil 2b)

**Vorrang ab 14.10.2026 14:30: `Komplettueberarbeitung-5.3.md`** (Julians Komplettüberarbeitung, wörtlich). 5.3 ist ein polierter vertikaler Ausschnitt mit Starttempo, Premium-UI/Modelltausch, E1.6 und E1.5 komplett, ohne Zwischenversion auf TestFlight; erst danach E2 ff. Wo jene Datei Neueres festlegt, gilt sie.

Stand 14.10.2026, 16:55 (**2.0: Julian 16:46: „Werbung entfernen“ 6,99 €, Werbung (Google AdMob + Einwilligung) schon in 5.4, Teil 2c und 5d Punkt 9.** 1.9 16:10: **1.9: Julians Test von 5.3 → Update 5.4, Teil 5d: alle Käufe, Gebiete mit Spielgeld, Premium-Gebiet, Weltprodukte, Fahrzeugbefehle, abgelegener Betriebshof.** 1.8 15:00: **1.8: Julians Preismodell 14:48 → Teil 2c; ersetzt die Regel „Echtgeld nur Designs“; Premium-Gebiet als Update P1 nach 5.3.** 1.7 14:50: **1.7: Firmenentwicklung in 5 Stufen + Bausystem als Rückgrat (Teil 2b), Garage/Werkstatt/Leitstelle ×3 entfallen; Monetarisierungsregel in Teil 0.** 1.6 14:35: **1.6: Verweis auf Komplettueberarbeitung-5.3.md; Build-Reihenfolge in 5c ersetzt.** 1.5 14:20: **1.5: Julian 14:15 bestellt vor allen großen Erweiterungen ein Transparenz- und Detail-Update → E1.6, Teil 5c. Build-Reihenfolge: 5.2 Tempo + Premium-UI, 5.3 E1.6 + Zielort/Lager aus E1.5, 5.4 Rest E1.5, danach E2.** 1.4 14:10: **1.4: Julian 14:03 bestellt E1.5 „Zielorte und Betriebsmittel“ vor E2 und ein ruhigeres Starttempo (8–12 Einsätze pro Spieltag), siehe Teil 5b. Tempo kommt in 5.2, E1.5 als 5.3.** 1.3 14:00: **1.3: E1 erledigt in Vaultoria 5.1, Build 202610141353, auf TestFlight; 17 Tests grün; Testbericht `/mnt/project-files/Testbericht.md`. Urteil Mac: Start mit 2 Wagen zu hektisch, Viertel öffnen zu schnell → Balancing in den nächsten Updates.** 1.2 14:15: **1.2: Teil 7 Abgleich mit dem Code vom Mac übernommen; wo der Code abweicht, gilt Teil 7. Spielstand der App: Vaultoria 1.4, Build 202610141306, auf TestFlight, mit Optik-Angleichung und Kenney-Stadt.** 1.1 13:45: **1.1: Julians 8 Änderungen eingearbeitet, betroffene Stellen mit [R1]–[R8] markiert. Freigegeben, zuerst nur E1.**). 1.0 vom 14.10.2026, 13:30. Grundlage: `Spielkonzept-Pannenhilfe.md`, `UI-Vorgabe-Pannenhilfe.md` (1.4). Das Kernspiel mit Draufsicht bleibt, nichts wird ersetzt. Gebaut wird Update für Update nach Teil 5. Die frühere „Später“-Liste (UI-Vorgabe Teil 13) geht in diesem Plan auf.

## Julians Auftrag (wörtlich, 14.10.2026 12:57)

> Erweitere Vaultoria auf Grundlage der bestehenden Pannenhilfe-Version. Das aktuelle Kernspiel und die Draufsicht bleiben erhalten. Baue keine komplizierte Menüstruktur und ersetze das Spiel nicht erneut.
> Plane die erste Spielwelt für ungefähr 50–100 Stunden Fortschritt. Neue Systeme müssen schrittweise freigeschaltet werden, damit der Einstieg weiterhin einfach bleibt.
> Ergänze:
>
> * unterschiedliche Einsatzdauer anhand von Strecke, Verkehr, Wetter, Fahrzeug und Mitarbeiter
> * mehrere mögliche Ausgänge pro Einsatz
> * dringende Autobahn-Einsätze
> * individuelle Mitarbeiterwerte und Erfahrung
> * Servicewagen, Abschlepper, Bergefahrzeuge, Schwerlastabschlepper und Kranwagen
> * Lkw-, Bus- und Großunfall-Einsätze
> * neue freischaltbare Stadtgebiete
> * Partnerverträge mit Werkstätten, Polizei und Automobilclubs
> * Rufsystem, Unternehmensziele und ausführliche Statistiken
> * einen ausbaubaren Betriebshof mit begrenzten Stellplätzen
> * tägliche Standgebühren für abgestellte Fahrzeuge
> * unterschiedliche Standzeiten und Platzbedarfe für Pkw, Transporter und Lkw
> * rechtlich nachvollziehbare Auktionen oder Kaufangebote für einzelne Fahrzeuge
> * eine Fahrzeug-Sammlung mit Verkaufen, Restaurieren und Behalten
>
> Zunächst nur Architektur, Datenmodelle, Freischaltreihenfolge und UI-Ablauf planen. Noch nicht sämtliche Inhalte gleichzeitig implementieren. Danach die Umsetzung in kleine, einzeln testbare Updates aufteilen. Die Karte bleibt das zentrale Spielelement; Menüs sollen nur unterstützend eingesetzt werden.

## Julians Freigabe mit Änderungen (wörtlich, 14.10.2026 13:05)

> Der Plan ist insgesamt sehr gut und trifft deine Idee. Claude sollte aber vor dem Bauen noch ein paar Dinge ändern, sonst werden aus 100 Stunden schnell 100 Stunden Wiederholung.
> Wichtigste Änderungen
>
> 1. Ein Spieltag darf nicht nur 6 Minuten dauern.
> Bei 100 Stunden wären das ungefähr 1.000 Tagesabrechnungen – extrem nervig. Besser:
>    * ein Spieltag etwa 15–20 Minuten
>    * ungefähr 250–350 Spieltage für die erste Welt
>    * Zeitsteuerung: Pause, 1×, 2× und 4×
>    * automatische Pause bei neuen dringenden Einsätzen und wichtigen Entscheidungen
> 2. Einsatzausgänge nicht einfach auswürfeln.
> Fahrzeug, Ausrüstung und Mitarbeiter müssen den Ausgang sichtbar beeinflussen. Zufall darf nur einen kleinen Anteil haben. Sonst fühlt es sich unfair an.
> 3. Betriebshof darf keine automatische Gelddruckmaschine werden.
>    * Einnahmen durch Standgebühren
>    * gleichzeitig Kosten für Platz, Verwaltung und Sicherheit
>    * nicht abgeholte Fahrzeuge blockieren wertvolle Stellplätze
>    * große Fahrzeuge benötigen deutlich mehr Platz
> 4. Rechtssystem spielerisch vereinfachen.
> Die Recherche ist gut, aber der Spieler sollte nicht sieben juristische Schritte einzeln anklicken müssen. Besser nur:
>    * Halter kontaktieren
>    * Frist läuft
>    * Abholung, Verkauf oder offizielle Auktion
> Im Hintergrund kann die Simulation trotzdem korrekt arbeiten.
> 5. Mitarbeiter brauchen echte Persönlichkeiten.
> Nicht nur Zahlen, sondern beispielsweise:
>    * schnell, aber unsauber
>    * zuverlässig, aber langsam
>    * besonders gut nachts
>    * Spezialist für Lkw
>    * stark bei schwierigen Bergungen
>    * wird bei zu vielen Schichten müde
> 6. Die Welt muss von Anfang an für Erweiterungen vorbereitet sein.
> Nach dem Abschluss erscheint zunächst keine sofort spielbare zweite Welt, sondern ein sichtbarer Ausblick: „Neue Region folgt mit einem späteren Update“. Spielstand, Fahrzeuge und bestimmte Mitarbeiter sollten später übernommen werden können.
>
> Nachricht an Claude
> Der Erweiterungsplan ist grundsätzlich freigegeben. Vor der Umsetzung bitte folgende Punkte einarbeiten:
>
> * Ein Spieltag dauert ungefähr 15–20 Minuten statt 6 Minuten. Ziel sind etwa 250–350 Spieltage beziehungsweise 50–100 Stunden für die erste Welt.
> * Zeitsteuerung mit Pause, 1×, 2× und 4× ergänzen. Bei dringenden Einsätzen und wichtigen Entscheidungen automatisch pausieren.
> * Einsatzausgänge dürfen nicht hauptsächlich zufällig sein. Mitarbeiterwerte, Fahrzeugklasse, Ausrüstung, Wetter und getroffene Entscheidungen müssen ausschlaggebend sein. Zufall bleibt nur als kleiner Unsicherheitsfaktor.
> * Der Betriebshof erzeugt Standgebühren, verursacht gleichzeitig aber Verwaltungs-, Sicherheits- und Platzkosten. Dadurch entsteht keine passive Gelddruckmaschine.
> * Rechtliche Abläufe intern korrekt simulieren, für Spieler aber auf drei verständliche Schritte reduzieren: Kontaktaufnahme, Frist, Abholung/Verkauf/Auktion.
> * Mitarbeitern erkennbare Stärken, Schwächen und höchstens eine besondere Eigenschaft geben.
> * Die Architektur bereits auf weitere Welten vorbereiten. Eine zweite Welt wird aber erst in einem späteren Update veröffentlicht.
> * Die 50–100 Stunden dürfen nicht durch bloßes Wiederholen gleicher Einsätze entstehen. Neue Einsatzvarianten, größere Verantwortung, Fahrzeuge, Verträge und Gebiete müssen regelmäßig dazukommen.
>
> Danach zuerst ausschließlich E1 umsetzen und testen. Keine späteren Systeme vorziehen.

**Eingearbeitet als:**
- **[R1]** Spieltag 18 Minuten bei 1×, erste Welt ca. 300 Spieltage → Teil 0, Teil 2 neu gerechnet.
- **[R2]** Zeitsteuerung Pause/1×/2×/4× mit Auto-Pause → Teil 1.2a, Teil 3, E1.
- **[R3]** Ausgänge überwiegend aus Werten, Zufall höchstens ±8 % → Teil 1.3 (2) mit Formel.
- **[R4]** Betriebshof mit Platz-, Verwaltungs- und Sicherheitskosten, Rechnung → Teil 1.3 (10)–(12).
- **[R5]** Recht für Spieler in 3 Schritten → Teil 4.2.
- **[R6]** Mitarbeiter mit Stärke, Schwäche, höchstens einer Besonderheit → Teil 1.3 (4).
- **[R7]** Mehrere Welten in der Architektur, Ausblick nach Welt 1 → Teil 1.1, 1.2, E1, E19.
- **[R8]** Taktplan gegen Wiederholung → Teil 2a.

## 0. Leitplanken

- **Die Karte bleibt die Mitte.** Jedes neue System zeigt sich zuerst auf der Karte (Marker, Fahrzeug, Gebäudeteil, Straßenabschnitt) und nur unterstützend in den vier vorhandenen Tabs **Karte · Flotte · Zentrale · Personal** oder im Einsatz-Panel (UI-Vorgabe 00b). **Kein fünfter Tab, keine neuen Hauptmenüs.**
- **Eine neue Funktion pro Freischaltstufe.** Was noch nicht freigeschaltet ist, ist unsichtbar (keine grauen Platzhalter, kein „Demnächst“).
- **Zahlen sind Startwerte** zum Ausbalancieren im Test. Der Mac gleicht Namen und Felder mit dem echten Swift-Code ab; bei Abweichung gilt der Code, dieser Plan wird angepasst.
- **Monetarisierung (Julian 14.10.2026 14:48, ersetzt die Regel „nur Designs“ von 14:43):** Vaultoria ist kostenlos mit Werbung. Die komplette Hauptwelt inkl. normalem Firmenwachstum bleibt **ohne Kauf vollständig spielbar**; der normale Ausbau wird **nie** blockiert. Käufe: Werbung entfernen, Premium-Fahrzeuge, Premium-Zentrale, Premium-Gebiet „Flughafen- und Eventbezirk“, Pakete, später Zusatzregionen/Welten/Designs (Preise und Regeln: Erweiterungsplan Teil 2c). Nicht im Preismodell: Spielgeld gegen Echtgeld, „Sofort fertig“, Zufallskäufe.
- **[R1] Spielzeit:** 1 Spieltag = **18 Minuten** echte Zeit bei 1× (Spieluhr 06:00–22:00, Nacht wird übersprungen, außer Nachtdienst ist freigeschaltet). Erste Welt ≈ **300 Spieltage** (250–350) ≈ 75 Stunden bei 1×; wer oft 2× oder 4× nutzt, kommt eher auf 50, wer gründlich spielt eher auf 100 Stunden. Fristen aus dem echten Recht werden gestaucht (**1 echter Monat = 5 Spieltage**), die Reihenfolge der Schritte bleibt echt.

---

## 1. Architektur und Datenmodelle

### 1.1 Aufbau

**[R7]** Zwei Ebenen: ein **Profil** (weltübergreifend) und je Welt ein **Weltstand**. Welt 1 ist die einzige spielbare Welt.

```
Profile (profile.json, weltübergreifend)
├── schemaVersion, activeWorldId, completedWorldIds
├── company: Company          Firmenname, Ruf gesamt, Erfolge
├── carryOver: CarryOver      übertragbare Fahrzeuge, ausgewählte Mitarbeiter, Sammlung
└── settings: Settings        Zeitsteuerung, Auto-Pause an/aus je Ereignis, Ton

WorldState (world-<id>.json, eine Datei pro Welt)
├── meta: SaveMeta            Version, worldId, Spieltag, Uhrzeit, Spielzeit, Geschwindigkeit
├── economy: Economy          Geld, Ruf in dieser Welt, Ziele, freigeschaltete Stufen
├── world: World              Gebiete, Wetter, Verkehr
├── fleet: [Vehicle]          eigene Einsatzfahrzeuge
├── staff: [Employee]
├── missions: [Mission]       offene + laufende Einsätze
├── depot: Depot              Betriebshof mit Stellplätzen und abgestellten Fahrzeugen
├── contracts: [Contract]     Partnerverträge
├── collection: [CollectionCar]
├── market: [Offer]           Auktionen und Kaufangebote
└── stats: Stats              Tages- und Gesamtstatistik
```

Getrennte Schichten: **Simulation** (reine Logik, Takt pro Spielminute, ohne UI, testbar mit festem Zufalls-Seed) → **Spielstand** (Codable) → **Darstellung** (Karte, Panels). Neue Systeme sind eigene Module, die sich am Takt anmelden (`tick(minute)`), damit jedes Update einzeln an- und abschaltbar bleibt.

### 1.2 Spielstand-Versionierung

```swift
struct SaveMeta: Codable {
  var schemaVersion: Int      // steigt mit jedem Update, das Felder ergänzt
  var worldId: String         // [R7] "welt1-heimatstadt"
  var gameDay: Int; var minuteOfDay: Int
  var speed: GameSpeed        // [R2] .paused, .x1, .x2, .x4
  var totalPlaySeconds: Int
  var unlockedStage: Int      // 0…18, siehe Teil 2
}
struct WorldDefinition {      // [R7] statische Daten, im App-Paket, nicht im Spielstand
  let id: String; let name: String
  let districts: [DistrictDefinition]; let roadGraph: String   // Datei
  let stages: [StageDefinition]; let finale: FinaleDefinition
  let isPlayable: Bool        // Welt 2 später: false → nur Ausblick
}
struct CarryOver: Codable {   // [R7] was in eine spätere Welt mitkommt
  var vehicleIds: [VehicleID]           // alle eigenen Fahrzeuge
  var employeeIds: [EmployeeID]         // höchstens 3, vom Spieler gewählt
  var collection: [CollectionCar]
  var startMoneyBonus: Int              // fester Bonus statt Restgeld
}
```

- **[R7]** Alle Inhalte (Gebiete, Einsatzarten, Stufen) hängen an `worldId`. Neue Welt = neue `WorldDefinition` + neue Datei `world-<id>.json`, ohne Codeänderung am Kern.
- **[R7]** Nach dem Endziel von Welt 1: Am Kartenrand erscheint eine abgedunkelte Region mit Schild **„Neue Region folgt mit einem späteren Update“**. Antippen zeigt, was mitkommt (Fahrzeuge, bis zu 3 Mitarbeiter, Sammlung). Welt 1 bleibt weiter spielbar (freies Spiel).

### 1.2a Zeitsteuerung **[R2]**

```swift
enum GameSpeed: Int, Codable { case paused = 0, x1 = 1, x2 = 2, x4 = 4 }
enum AutoPauseReason: String, Codable { case urgentMission, specialDecision, unlock, dayEnd, legalStepDone }
struct GameClock { var speed: GameSpeed; var pauseQueue: [AutoPauseReason]
  mutating func tick(realSeconds: Double) -> Int   // liefert vergangene Spielminuten (1 Spielminute = 1,125 s bei 1×)
}
```
- Auto-Pause bei: neuem dringenden Einsatz (`urgent`; Countdown unter 2 Spielminuten erst ab E11, Teil 7), Sonderentscheidung, Freischaltung, Tagesende. Nicht bei normalen Einsätzen.
- Nach Auto-Pause geht es mit der vorherigen Geschwindigkeit weiter, sobald der Spieler das Fenster schließt oder „Weiter“ tippt.
- Einstellungen: Auto-Pause je Grund an/aus (Standard: alle an).
- Die Simulation läuft in festen Schritten von **1/10 Spielminute** (Teil 7); 4× rechnet 4 Schritte pro Takt, damit Ergebnisse bei jeder Geschwindigkeit gleich sind.
- App im Hintergrund: Spiel pausiert, keine Simulation offline.

- Neue Felder sind immer **optional oder mit Standardwert** (`decodeIfPresent ?? Standard`), damit alte Stände laden.
- `migrate(from: Int)` läuft Schritt für Schritt (v1→v2→v3 …). Jeder Schritt füllt neue Felder sinnvoll (z. B. Mitarbeiter ohne Erfahrung bekommen Stufe 1).
- Schlägt das Laden fehl: Spielstand nach `save-defekt-<datum>.json` sichern und **sauberer Neustart** (Regel aus dem Neuauftrag). Pfandhaus-Stände bleiben wie bisher ausgeschlossen.
- Automatisch speichern nach jedem Einsatz, Kauf, Freischaltung und am Tagesende.

### 1.3 Modelle zu den 14 Punkten

**(1) Einsatzdauer aus Strecke, Verkehr, Wetter, Fahrzeug, Mitarbeiter**

```swift
struct Weather: Codable { var kind: WeatherKind; var until: GameTime }  // klar, regen, nebel, glatteis, schnee, sturm
struct TrafficSegment: Codable { var roadId: Int; var factor: Double }   // 1.0 frei … 3.0 Stau
```
Dauer = **Anfahrt** + **Arbeit**
- Anfahrt = Σ (Straßenlänge ÷ Fahrzeugtempo × Verkehrsfaktor × Wetterfaktor), Route über A* auf dem Straßengraph mit diesen Kosten (weicht Stau aus).
- Arbeit = Grunddauer(Einsatzart) × Eignung(Fahrzeug, Einsatzart) × Mitarbeiterfaktor × Wetterfaktor.
- Mitarbeiterfaktor = 1,3 − 0,06 × passender Wert (1–5) + Müdigkeitszuschlag.
- Wetter: Regen 1,15 · Nebel 1,2 · Schnee 1,35 · Glatteis 1,5 (Glatteis auch mehr Unfälle).
- Angezeigt wird nur das Ergebnis: „Ankunft 3:10 · Arbeit ca. 6 Min“.

**(2) Mehrere Ausgänge pro Einsatz [R3]**

```swift
enum Outcome: String, Codable { case fixedOnSite, fixedLate, towedToDepot, towedToPartner, needsSecondVehicle, aborted, customerLeft }
struct OutcomeFactors: Codable { var staff, vehicle, equipment, conditions, decisions, luck: Double }  // je −1…+1 bzw. luck klein
struct MissionResult: Codable { var outcome: Outcome; var factors: OutcomeFactors; var income: Int; var costs: Int; var stars: Int; var minutes: Int; var xp: [EmployeeID: Int] }
```

**Formel.** Jeder Einsatz hat eine Schwierigkeit `D` (0,30 leicht … 0,90 Großunfall). Der Einsatzwert `E` (0…1):

| Anteil | Faktor | Berechnung (0…1) |
|---|---|---|
| **35 %** | Mitarbeiter | passender Wert (1–5) ÷ 5, ± Stärke/Schwäche/Besonderheit, × Müdigkeit (1,0 frisch … 0,8 erschöpft) |
| **25 %** | Fahrzeugklasse | 1,0 passend · 0,6 geht notdürftig · 0 ungeeignet; × Zustand (unter 50 % linear schlechter) |
| **15 %** | Ausrüstung | Anteil der benötigten Ausrüstung, die an Bord ist |
| **10 %** | Bedingungen | Wetter und Tageszeit: klar 1,0 · Regen 0,85 · Nebel 0,8 · Schnee 0,7 · Glatteis 0,6 · Nacht 0,85 (Nachteule 1,0) |
| **15 %** | Entscheidungen | Sonderentscheidung gut gewählt, Absicherung angefordert, zweites Fahrzeug, Ersatzteil mitgenommen: 0,5 neutral, bis 1,0 |

`Ergebnis = E − D + Glück`, **Glück** gleichverteilt zwischen **−0,08 und +0,08** (also höchstens eine Stufe Verschiebung).

| Ergebnis | Ausgang |
|---|---|
| ≥ +0,15 | vor Ort behoben, schnell (Bonus-Stern) |
| 0 … +0,15 | behoben, etwas länger |
| −0,15 … 0 | Teilerfolg: abschleppen statt reparieren oder zweiter Wagen nötig |
| < −0,15 | Abbruch (Kosten, Bewertung sinkt) |

„Kunde weg“ entsteht **nur** durch den abgelaufenen Countdown, nie durch Zufall.

**Sichtbar machen:**
- Vor dem Losschicken (Panel 00b): Wort aus `E − D` **ohne** Glück: „sehr gute Chance“ (≥ 0,15), „gute Chance“ (0…0,15), „knapp“ (−0,15…0), „riskant“ (darunter). Darunter bis zu zwei Hinweise, was hilft: „Abschlepper würde passen“, „Starthilfe fehlt an Bord“.
- Im Einsatzbericht: fünf kleine Zeilen mit Symbol und grünem Plus bzw. rotem Minus (Mitarbeiter, Fahrzeug, Ausrüstung, Wetter, Entscheidung), Glück nur als „etwas Glück“ / „etwas Pech“, wenn es den Ausgang verschoben hat.

**(3) Dringende Autobahn-Einsätze**

`Mission.priority: .normal | .urgent | .highway`. Autobahn = eigenes Gebiet (Teil 2, Stufe 8), kurzer Countdown, hohe Bezahlung, Bonus bei Ankunft unter Zielzeit, Sicherungsaufwand (Absicherung durch zweites Fahrzeug oder Polizei bringt mehr Sterne).

**(4) Mitarbeiterwerte, Persönlichkeit und Erfahrung [R6]**

```swift
enum Skill: String, Codable { case repair, towing, speed, reliability }
enum Trait: String, Codable { case fastButSloppy, reliableButSlow, nightOwl, truckSpecialist, recoveryPro, tiresQuickly, calmUnderPressure, customerCharmer }
struct Employee: Codable {
  var id: EmployeeID; var name: String; var portrait: String
  var repair, towing, speed, reliability: Int  // 1…5
  var strength: Skill; var weakness: Skill     // genau eine Stärke (+1 wirksam) und eine Schwäche (−1 wirksam)
  var trait: Trait?                            // höchstens eine Besonderheit
  var level: Int; var xp: Int                  // Stufe 1…10
  var licenses: Set<License>                   // .b, .c1, .c, .ce, .crane
  var shiftMinutesLeft: Int; var fatigue: Double; var wage: Int
  var transferable: Bool                       // [R7] darf in spätere Welt mit
}
```

| Besonderheit | Wirkung (im Spiel in einem Satz erklärt) |
|---|---|
| schnell, aber unsauber | Arbeit 20 % schneller, Ausgang −0,05 (öfter Nacharbeit) |
| zuverlässig, aber langsam | Arbeit 20 % langsamer, Ausgang +0,07 |
| Nachteule | nachts kein Abzug, tagsüber normal |
| Lkw-Spezialist | +0,10 bei Lkw/Bus, Lkw-Führerschein günstiger |
| Bergungsprofi | +0,10 bei Bergungen und Großunfällen |
| wird schnell müde | Müdigkeit steigt 50 % schneller, dafür niedrigeres Gehalt |
| ruhig unter Druck | kein Abzug bei dringenden Einsätzen |
| Kundenliebling | +1 Stern bei gelungenem Einsatz |

Darstellung: Mitarbeiterkarte zeigt Stärke (grünes Symbol), Schwäche (rotes Symbol) und die Besonderheit als goldene Kapsel mit Kurztext. Keine Talentbäume. Erfahrung pro Einsatz in der genutzten Fähigkeit; alle 3 Stufen +1 auf einen Wert nach Wahl (eine Karte, ein Tipp). Führerscheine per Schulung im Tab Personal (Geld + eine Schicht). Neue Bewerber kommen alle paar Tage mit zufälliger, aber sichtbarer Kombination.

**(5) Fahrzeugklassen**

```swift
enum VehicleClass: String, Codable { case service, tow, recovery, heavyTow, crane }
struct Vehicle: Codable {
  var id: VehicleID; var cls: VehicleClass; var name: String
  var speed: Double; var condition: Double; var fuel: Double; var isElectric: Bool
  var equipment: Set<Equipment>   // starthilfe, reifen, öffnung, absaugung, diagnose, plateau, seilwinde, unterhebe, kran
  var capacity: SizeClass?        // was transportiert werden kann
  var task: Task?; var homeSlot: Int
}
```
| Klasse | Kann | Transportiert | Führerschein |
|---|---|---|---|
| Servicewagen | Batterie, Reifen, Öffnung, kleine Defekte, Kraftstoff | nichts | B |
| Abschlepper (Plateau) | Abschleppen, einfache Hilfe | Pkw, kleine Transporter | C1 |
| Bergefahrzeug (Seilwinde) | Bergung aus Graben/Böschung | Pkw, Transporter | C |
| Schwerlastabschlepper | Lkw/Bus abschleppen | Lkw, Bus | CE |
| Kranwagen | Heben, umgestürzte Fahrzeuge, Großunfall | — (hebt, transportiert nicht) | CE + Kran |

**(6) Lkw-, Bus- und Großunfall-Einsätze**

`Mission.size: SizeClass (.car, .van, .truck, .bus)`, `Mission.requiredClasses: [VehicleClass]`. Großunfall = **ein Einsatz mit mehreren Teilaufträgen** (`subTasks: [SubTask]`), jeder braucht ein eigenes Fahrzeug; Bezahlung erst, wenn alle Teilaufträge erledigt oder abgebrochen sind. Auf der Karte ein großer Marker mit Zähler „0/4“.

**(7) Freischaltbare Stadtgebiete**

```swift
struct District: Codable { var id: String; var name: String; var unlocked: Bool; var unlockCost: Int; var minReputation: Int
  var missionMix: [MissionKind: Double]; var trafficLevel: Double; var bounds: MapRect }
```
Gebiete (erste Welt): Altstadt (Start) · Wohnviertel · Bahnhof · Gewerbegebiet · Autobahn · Industriehafen · Land/Vororte. Gesperrte Gebiete sind auf der Karte sichtbar, aber abgedunkelt mit einem Schild „Freischalten: 12.000 € · Ruf 40“.

**(8) Partnerverträge**

```swift
enum PartnerKind: String, Codable { case workshop, police, autoClub }
struct Contract: Codable {
  var partner: PartnerKind; var level: Int              // 1…3
  var missionsPerDay: ClosedRange<Int>; var maxResponseMinutes: Int
  var payFactor: Double; var penaltyPerLate: Int
  var signedDay: Int; var durationDays: Int; var performance: Double  // 0…1, Anteil pünktlich
}
```
- **Werkstatt:** liefert Abschleppaufträge zur Partnerwerkstatt, zahlt pro Fahrzeug Provision; Kunden mit Defekt können statt in den Betriebshof dorthin.
- **Polizei:** Sicherstellungen, Unfälle, Autobahn-Absicherung. Kurze Reaktionszeit. Polizei-Fahrzeuge kommen in den Betriebshof (Verwahrung, Teil 4).
- **Automobilclub:** viele kleine Pannen mit festem Satz pro Einsatz, sehr kurze Reaktionszeit, verbessert Ruf bei Kunden.
Verträge laufen 30 Spieltage; Verlängerung nur bei Pünktlichkeit ≥ 80 %. Zu oft zu spät → Vertrag endet, Ruf sinkt.

**(9) Ruf, Unternehmensziele, Statistiken**

```swift
struct Reputation: Codable { var score: Int /* 0…100 */; var rating: Double /* Ø Sterne */ }
struct Goal: Codable { var id: String; var text: String; var metric: Metric; var target: Int; var reward: Reward; var done: Bool }
struct Stats: Codable { var days: [DayStats]; var totals: Totals }   // pro Tag: Einsätze, Ø Ankunft, Umsatz, Kosten, Gewinn, Sterne, Ausgänge, km
```
Ruf 0–100 aus Ø Sternen, Pünktlichkeit und Vertragserfüllung. Ruf öffnet Gebiete, Verträge und besser bezahlte Einsätze. **Ziele:** immer genau 3 aktive Ziele (z. B. „10 Einsätze heute pünktlich“, „Ersten Lkw bergen“), Belohnung Geld oder Ruf. **Statistik:** keine eigene Seite; Tagesabrechnung bekommt einen Knopf „Verlauf“ mit 3 einfachen Diagrammen (Gewinn, Einsätze, Ø Ankunft, letzte 30 Tage).

**(10) Betriebshof mit begrenzten Stellplätzen**

```swift
enum SizeClass: String, Codable { case car, van, truck, bus }   // [R4] Platzbedarf: car 1, van 2, truck 5, bus 6 Einheiten
struct Depot: Codable { var capacityUnits: Int; var level: Int; var stored: [StoredVehicle]
  var dailyCosts: DepotCosts }   // [R4] Platz, Verwaltung, Sicherheit
struct StoredVehicle: Codable {
  var id: UUID; var size: SizeClass; var model: GenericModel; var plate: String?  // fiktive Kennzeichen
  var reason: StorageReason   // .breakdown, .accident, .policeSeizure, .privateTow, .unpaidRepair, .abandoned, .purchased
  var arrivedDay: Int; var expectedPickupDay: Int?
  var ownerStatus: OwnerStatus   // .unknown, .identified, .notified, .pickupRequested, .noResponse
  var feePerDay: Int; var feesAccrued: Int; var feesStopDay: Int?
  var legalCase: LegalCase?      // Teil 4
}
```
Betriebshof ist ein eigenes Gebäudeteil an der Zentrale (sichtbar wachsend, UI-Vorgabe Teil 12). Stufen: 6 → 12 → 20 → 32 → 48 Einheiten. Ist er voll, kann kein weiteres Fahrzeug eingelagert werden; Abschleppaufträge gehen dann nur noch zu Partnern (bringt 40 % weniger).

**[R4] Kosten, damit der Hof keine Gelddruckmaschine wird** (Startwerte pro Spieltag):

| Kostenart | Wert | läuft |
|---|---|---|
| Platz (Pacht, Unterhalt) | 4 € je **gebauter** Einheit | immer, auch wenn leer |
| Sicherheit (Zaun, Licht, Kamera, Versicherung) | 20 / 40 / 70 / 110 / 160 € je Hofstufe | immer |
| Verwaltung | 3 € je eingelagertem Fahrzeug | solange es steht |

Einnahmen: Standgebühr pro Fahrzeug (Teil 11) nur bis zum Herausgabeverlangen; Polizei-Verwahrung 20 €/Tag von der Behörde (nur mit Vertrag, begrenzt auf 6 Fahrzeuge gleichzeitig).

**Nachgerechnet (Hofstufe 2, 12 Einheiten, Ø 8 Pkw, Gebühr läuft im Schnitt 2 von 4 Standtagen):**
Einnahmen 8 × 15 € × ½ = 60 € · Kosten 12 × 4 € + 40 € + 8 × 3 € = 112 € · **Saldo −52 €/Tag.**
Gut geführt mit Polizeivertrag (Stufe 3, 20 Einheiten, 6 Polizei- + 8 Privat-Pkw): 120 € + 60 € − (80 € + 70 € + 42 €) = **−12 €/Tag.**
Ein Lkw (5 Einheiten, 40 €/Tag Gebühr) bringt 8 € je Einheit statt 15 €, ein nicht abgeholtes Auto belegt Platz ohne Einnahme und kostet 7 € am Tag.
Der Hof verdient also **nicht von allein**. Er lohnt sich nur, weil er Abschleppaufträge mit voller Bezahlung (120–400 €) und später Verträge, Kaufangebote und Auktionen möglich macht. Ein voller Hof mit Dauerstehern ist ein spürbares Problem, das der Spieler über Halterkontakt und Frist lösen muss.

**(11) Tägliche Standgebühren**

Startwerte pro Tag: Pkw 15 € · Transporter 20 € · Lkw/Bus 40 € (pro Einheit weniger als beim Pkw, **[R4]**). Gebühren laufen **bis zum Herausgabeverlangen des Halters** (siehe Teil 4, BGH V ZR 192/22). Danach laufen keine Gebühren mehr, auch wenn er das Fahrzeug erst später holt; der Platz bleibt aber belegt. Das macht volle Höfe zu einer echten Entscheidung.

**(12) Standzeiten und Platzbedarf**

| Grund | Pkw | Transporter | Lkw/Bus **[R4]** | Standzeit (Spieltage) |
|---|---|---|---|---|
| Panne, wartet auf Werkstatt | 1 | 2 | 5 / 6 | 1–3 |
| Unfall, wartet auf Gutachter/Versicherung | 1 | 2 | 5 / 6 | 3–10 |
| Polizeiliche Sicherstellung | 1 | 2 | 5 / 6 | 1–14, ca. 5 % nie abgeholt |
| Privat abgeschleppter Falschparker | 1 | 2 | — | 0–2 |
| Reparatur nicht bezahlt | 1 | 2 | 5 / 6 | bis Rechtsweg (Teil 4) |
| Schrottfahrzeug ohne Kennzeichen | 1 | 2 | — | bis Entsorgung |

**(13) Auktionen und Kaufangebote (rechtlich nachvollziehbar)**

```swift
enum OfferKind: String, Codable { case ownerSale, publicAuction, authorityAuction }
struct Offer: Codable {
  var id: UUID; var kind: OfferKind; var car: GenericModel; var condition: Double
  var startPrice: Int; var currentBid: Int; var endsDay: Int; var endsMinute: Int
  var seller: String          // „Halter“, „Öffentlich bestellter Versteigerer“, „Stadt (Verwertungsstelle)“
  var legalNote: String       // ein Satz, warum der Verkauf erlaubt ist
}
```
Der Spieler **kann ein Fahrzeug nie einfach behalten**, weil es lange steht. Ablauf und Regeln in Teil 4.

**(14) Fahrzeug-Sammlung**

```swift
struct CollectionCar: Codable {
  var id: UUID; var model: GenericModel; var rarity: Rarity   // alltag, selten, klassiker, legende
  var condition: Double; var restoreStage: Int                // 0…3
  var boughtFor: Int; var marketValue: Int; var acquiredVia: OfferKind
  var displayed: Bool
}
```
- Fahrzeuge kommen **nur** über Kaufangebot oder ersteigerte Auktion in die Sammlung.
- **Restaurieren** in der eigenen Werkstatt (Zentrale-Ausbau), 3 Stufen, kostet Teile und Mitarbeiter-Schichten, erhöht den Wert sichtbar.
- **Verkaufen** an fiktive Käufer (Angebot nach Zustand und Seltenheit) oder **Behalten**: Ausstellung auf dem Hof der Zentrale (Gebäudeteil „Schauhalle“), jedes ausgestellte Fahrzeug ist auf der Karte sichtbar und hebt den Ruf leicht.
- Nur fiktive Modelle ohne echte Marken (`GenericModel`: Bauart, Epoche, Farbe, Name wie „Kombi 90er“ oder „Roadster 60er“).

---

## 2. Freischaltreihenfolge (erste Welt, ca. 300 Spieltage) **[R1]**

Genau **eine neue Funktion pro Stufe**. Freischaltung zeigt eine einzige Karte (Auto-Pause): was neu ist, ein Satz, „Los geht’s“. Auslöser sind Geld, Ruf, erledigte Einsätze oder Spieltag; alle Bedingungen einer Stufe müssen erfüllt sein. Kosten werden erst beim Bestätigen abgezogen. Spieltag und Stunde sind **Zielwerte fürs Ausbalancieren** (Stunden bei 1×, 18 Min pro Tag).

| Stufe | Spieltag | ca. Stunde | Auslöser | Neue Funktion | Punkt |
|---|---|---|---|---|---|
| 0 | 1 | 0 | Spielstart | Kernspiel (Version 1 mit den 8 Pflichtpunkten) | – |
| 1 | 4 | 1 | 15 Einsätze | **Wetter** auf der Karte, beeinflusst Fahrt und Arbeit | 1 |
| 2 | 8 | 2,5 | 35 Einsätze | **Erfahrung und Stufen** für Mitarbeiter | 4 |
| 3 | 14 | 4 | Ruf 20 | **Sichtbare Ausgänge** mit Faktoren (Teil 1.3 (2)) | 2 |
| 4 | 22 | 6,5 | Spieltag 22 | **Unternehmensziele** (immer 3 aktiv) + Verlauf | 9 |
| 5 | 32 | 9,5 | 100 Einsätze, 8.000 € | **Betriebshof** mit Kosten und **Standgebühren** | 10, 11 |
| 6 | 44 | 13 | Ruf 30 | **Standzeiten und Platzbedarf** (Pkw/Transporter) | 12 |
| 7 | 58 | 17 | 15.000 € | **Gebiet Wohnviertel + Bahnhof** | 7 |
| 8 | 72 | 21,5 | Ruf 35, 220 Einsätze | **Vertrag Werkstatt** | 8 |
| 9 | 88 | 26 | 25.000 € | **Bergefahrzeug** + Bergungseinsätze | 5 |
| 10 | 104 | 31 | Ruf 45 | **Gebiet Autobahn** + dringende Autobahn-Einsätze | 3, 7 |
| 11 | 122 | 36,5 | Betriebshof Stufe 2 | **Kaufangebote** + **Sammlung** (Behalten/Verkaufen) | 13, 14 |
| 12 | 140 | 42 | Ruf 50 | **Vertrag Polizei** (Sicherstellung, Verwahrung, Absicherung) | 8 |
| 13 | 158 | 47,5 | Werkstatt Stufe 2 | **Restaurieren** in der Sammlung | 14 |
| 14 | 178 | 53 | 60.000 €, Lkw-Führerschein bei einem Mitarbeiter | **Schwerlastabschlepper** + **Lkw-Einsätze**, Gebiet Gewerbegebiet | 5, 6, 7 |
| 15 | 198 | 59,5 | Ruf 60 | **Vertrag Automobilclub** | 8 |
| 16 | 218 | 65,5 | 550 Einsätze | **Offizielle Auktionen** (Pfandverkauf, Behördenauktion) | 13 |
| 17 | 240 | 72 | 120.000 € | **Kranwagen** + **Bus-Einsätze**, Gebiet Industriehafen | 5, 6, 7 |
| 18 | 262 | 78,5 | Ruf 75, alle Verträge Stufe 2 | **Großunfälle** (Teilaufträge) + Gebiet Land/Vororte | 6, 7 |
| Ziel | 290–330 | 87–99 | Ruf 90, alle Gebiete | Endziel „Größte Pannenhilfe der Region“ mit großer Autobahnbergung; danach Ausblick „Neue Region folgt mit einem späteren Update“ **[R7]** | – |

Bremse für den Einstieg: In den ersten 10 Spieltagen nie mehr als 4 gleichzeitige Einsätze und kein Wetter schlimmer als Regen.

## 2b. Firmenentwicklung: das Rückgrat (1.7, Julian 14.10.2026 14:43)

Julians Text steht wörtlich in `Komplettueberarbeitung-5.3.md` (Nachtrag 2). Die Abschleppfirma wächst **sichtbar auf der Karte** in 5 Firmenstufen. Die 18 Freischaltstufen aus Teil 2 hängen jetzt an diesen Firmenstufen. **Garage, Werkstatt und Leitstelle mit je 3 Stufen entfallen**; an ihre Stelle tritt das Bausystem unten. **Monetarisierung (Julian 14.10.2026 14:48, ersetzt die Regel „nur Designs“ von 14:43):** Vaultoria ist kostenlos mit Werbung. Die komplette Hauptwelt inkl. normalem Firmenwachstum bleibt **ohne Kauf vollständig spielbar**; der normale Ausbau wird **nie** blockiert. Käufe: Werbung entfernen, Premium-Fahrzeuge, Premium-Zentrale, Premium-Gebiet „Flughafen- und Eventbezirk“, Pakete, später Zusatzregionen/Welten/Designs (Preise und Regeln: Erweiterungsplan Teil 2c). Nicht im Preismodell: Spielgeld gegen Echtgeld, „Sofort fertig“, Zufallskäufe.

### Firmenstufen und Freischaltstufen

| Firmenstufe | Spieltag (Ziel) | Freischaltstufen (Teil 2) | Sichtbar auf der Karte | Fahrzeuge | Aufstieg zur nächsten Firmenstufe |
|---|---|---|---|---|---|
| **1 Kleiner Familienbetrieb** | 1–31 | 0–4 (Kernspiel, Wetter, Erfahrung, Ausgänge, Ziele) | gemietete kleine Halle, einfaches Büro, 4 Stellplätze, kleiner Teilebestand, 3 kleine Bauflächen | 1 Servicewagen + 1 Abschlepper, 2 Mitarbeiter (bis 3 Fahrzeuge) | 100 Einsätze, Ruf 25, 8.000 € Anzahlung (Rest als Kredit möglich) → **Grundstück kaufen** |
| **2 Eigener Betriebshof** | 32–71 | 5–7 (Betriebshof mit Standgebühren, Standzeiten/Platz, Gebiet Wohnviertel + Bahnhof) | Umzug auf eigenes Grundstück: größere Werkstatt, Stellplatzflächen, Reifen-/Teilelager, Altteillager, Waschplatz, Aufenthaltsraum, kleine Leitstelle, 8 Bauflächen | 4–6 | Ruf 35, 220 Einsätze, Werkstattplatz + kleine Leitstelle gebaut → **Grundstückserweiterung** |
| **3 Professioneller Abschleppdienst** | 72–197 | 8–15 (Verträge Werkstatt/Polizei/Automobilclub, Bergefahrzeug, Autobahn, Kaufangebote + Sammlung, Restaurieren, Schwerlast + Lkw) | mehrere Werkstattplätze, großer Verwahrhof, Schwerlastbereich, eigene Tankstelle/Ladesäulen, moderne Leitstelle, Schulungsraum, +6 Bauflächen | 8–12 | alle 3 Verträge, Ruf 60, Schwerlastgarage gebaut → **zweite Niederlassung** |
| **4 Regionalunternehmen** | 198–261 | 16–17 (offizielle Auktionen, Kranwagen + Bus, Industriehafen) | zweite Niederlassung im Gewerbegebiet mit eigenem Niederlassungsleiter; Fahrzeuge starten vom näheren Standort; zentrale Lagerverwaltung | 15–25 | Ruf 75, beide Standorte voll ausgebaut → **Leitstelle rund um die Uhr** |
| **5 Marktführer der Region** | 262–330 | 18 + Ziel (Großunfälle, Land/Vororte, Endziel) | mehrere Niederlassungen, 24-h-Leitstelle (Nachtdienst), Verwaltungs- und Werkstattkomplex als Wahrzeichen, Kran- und Spezialfahrzeuge, Autobahn- und Großschadensverträge | 25+ | Endziel und Ausblick „Neue Region folgt“ [R7] |

Hinweis zur Reihenfolge: Teil 2 bleibt gültig, mit einer Anpassung: Schwerlast + Lkw (Stufe 14) gehört zum Schwerlastbereich der Firmenstufe 3, große Lkw- und Busbergungen kommen in Firmenstufe 4 (Bus mit Stufe 17). Ein **Firmenaufstieg** ist ein eigener Moment (Auto-Pause, eine Karte, Kamerafahrt über das neue Gelände), nie automatisch: Der Spieler bestätigt Kauf bzw. Umzug selbst.

### Bausystem auf freien Hofflächen

```swift
struct BuildPlot: Codable { let id: String; let siteId: String; let size: PlotSize; var building: BuildingInstance? }   // PlotSize: .small, .medium, .large
struct BuildingType: Codable { let id: String; let plotSize: PlotSize; let cost: Int; let buildDays: Double; let dailyCost: Int;
                               let minCompanyStage: Int; let minReputation: Int?; let permit: String?; let effect: String }
struct BuildingInstance: Codable { let typeId: String; var state: BuildState; var progress: Double }   // .construction, .ready
struct CompanyState: Codable { var stage: Int = 1; var sites: [Site]; var loans: [Loan] }
struct Loan: Codable { let principal: Int; var remaining: Int; let dailyRate: Int }   // Startwert: bis 60 % der Baukosten, 20 Spieltage, +8 % gesamt
```
- **Freie Bauflächen** sind auf der Karte als dezent silbern umrandete Flächen sichtbar (keine Platzhalter-Gebäude). Antippen → Sheet mit den passenden Gebäuden für diese Flächengröße.
- **Bau dauert Spielzeit:** Absperrung, Bauzaun, Baufahrzeuge (Bagger/Kran/Lieferwagen fahren an), Fortschrittsring; danach steht das Gebäude dort, und Fahrzeuge/Mitarbeiter **benutzen es sichtbar** (Wagen fährt in die Werkstatt, Mitarbeiter geht in den Aufenthaltsraum).
- **Jeder Ausbau zeigt vorher:** Kaufpreis (oder Kredit), laufende Kosten pro Tag, Bauzeit, Flächenbedarf, Voraussetzung (Firmenstufe, Ruf, Genehmigung) und **einen konkreten Nutzen** in einem Satz.
- Laufende Kosten gehen in die täglichen Fixkosten (Teil 5c Punkt 4) und ins Kassenbuch.

**Gebäudekatalog (Startwerte zum Ausbalancieren, Julians Beispiel „Zweite Werkstatthalle“ als Anker):**

| Gebäude | Fläche | Ab Firmenstufe | Baukosten | Bauzeit | Laufend/Tag | Nutzen |
|---|---|---|---|---|---|---|
| Stellplatzfläche | klein | 1 | 4.000 € | 1 Tag | 15 € | +4 Einheiten Hof |
| Reifencontainer | klein | 1 | 2.500 € | 1 Tag | 5 € | Altreifen-Kapazität +10 |
| Entsorgungsbereich | klein | 1 | 4.000 € | 2 Tage | 15 € | Altbatterien/Altöl/Schrott-Kapazität ×2 |
| Lagerhalle (Teile) | mittel | 1 | 9.000 € | 3 Tage | 40 € | Lager +20 Einheiten, Lieferung 30 % schneller |
| Zusätzliche Garage | mittel | 1 | 12.000 € | 3 Tage | 50 € | +1 Einsatzfahrzeug möglich, Fahrzeuge altern draußen nicht schneller |
| Werkstattplatz | mittel | 2 | 18.000 € | 4 Tage | 90 € | 1 Fahrzeug gleichzeitig warten/reparieren |
| Waschplatz | klein | 2 | 5.000 € | 2 Tage | 20 € | +2 % Bewertung je Einsatz (sauberes Fahrzeug) |
| Mitarbeitergebäude (Aufenthaltsraum) | mittel | 2 | 10.000 € | 3 Tage | 40 € | Müdigkeit erholt sich 25 % schneller |
| Leitstelle (klein) | mittel | 2 | 15.000 € | 4 Tage | 60 € | +1 gleichzeitiger Auftrag, Einsätze 5 Spielminuten früher sichtbar |
| Zweite Werkstatthalle | groß | 3 | 35.000 € | 5 Tage | 180 € | 2 Fahrzeuge gleichzeitig warten |
| Tankstelle / Ladesäulen | mittel | 3 | 20.000 € | 4 Tage | 50 € | Tanken auf dem Hof, Kraftstoff 15 % günstiger |
| Leitstelle (modern) | groß | 3 | 40.000 € | 6 Tage | 150 € | +2 gleichzeitige Aufträge, Routenvorschlag |
| Schulungsraum | mittel | 3 | 25.000 € | 4 Tage | 80 € | Führerscheine/Erfahrung schneller |
| Schwerlastgarage | groß | 3 | 60.000 € | 7 Tage | 220 € | Voraussetzung Schwerlastabschlepper |
| Sammlungshalle | groß | 3 | 45.000 € | 6 Tage | 120 € | Sammlung + Restaurieren (E12/E14) |
| Niederlassung | eigenes Gelände | 4 | 150.000 € | 10 Tage | 600 € | zweiter Startpunkt, eigener Leiter |

### Was in 5.3 gebaut wird

**Firmenstufe 1 komplett** (gemietete Halle, Büro, 4 Stellplätze, 1 Servicewagen + 1 Abschlepper, 2 Mitarbeiter, kleiner Teilebestand) **plus das Bausystem** mit den ersten Ausbauten Richtung Stufe 2: Stellplatzfläche, Reifencontainer, Entsorgungsbereich, Lagerhalle, Zusätzliche Garage (ersetzen die Ausbaustufen aus Teil 5b Punkt 5–6). Bausystem inkl. Baustelle, Bauzeit, laufender Kosten, Kredit und Anzeige „Firmenstufe 1 · Kleiner Familienbetrieb“ mit Fortschritt zum Aufstieg. **Der Aufstieg zu Stufe 2 selbst** kommt mit E6 (Betriebshof); Stufen 3–5 in den späteren Updates nach Teil 5.

## 2c. Preismodell und Premium-Inhalte (1.8, Julian 14.10.2026 14:48)

Julians Text steht wörtlich in `Komplettueberarbeitung-5.3.md` (Nachtrag 3). Product-IDs (Präfix `com.julian.vaultoria.`) vom Mac festgelegt, 14.10.2026 15:05. Klick-Anleitung für App Store Connect: `/mnt/project-files/vaultoria/AppStoreConnect-InApp-Kaeufe.md`.

| Produkt | Typ | Preis | Kommt mit | Wirkung im Spiel |
|---|---|---:|---|---|
| Werbung entfernen (= Werbefrei-Paket) `noads` | Nicht-Verbrauchsartikel | **6,99 €** (⚠ Neuer gilt, Julian 16:46; vorher 5,99 €) | **5.4** mit Werbung (Teil 5d Punkt 9) | automatische Werbung dauerhaft aus |
| Premium-Servicewagen `premium.service` | Nicht-Verbrauchsartikel | 2,49 € | **5.3** | eigenes Modell, +15 % Tempo |
| Premium-Abschlepper `premium.tow` | Nicht-Verbrauchsartikel | 3,99 € | **5.3** | eigenes Modell, eigene Lade-Animation, 15 % schneller auf- und abladen |
| Premium-Zentrale `premium.hq` | Nicht-Verbrauchsartikel | 3,49 € | **5.3** | exklusive Gebäudevarianten, Hof-Gestaltung, Beleuchtung |
| Premium-Schwerlastfahrzeug `premium.heavy` | Nicht-Verbrauchsartikel | 4,99 € | **5.4** (Teil 5d Punkt 8) | besonderes Schwerlastfahrzeug |
| Premium-Fuhrpark `premium.fleet` | Nicht-Verbrauchsartikel | 8,99 € | **5.4** | alle drei Premium-Fahrzeuge |
| Premium-Unternehmen `bundle.company` | Nicht-Verbrauchsartikel | 12,99 € | **5.4** | werbefrei + Fuhrpark + Zentrale |
| Flughafen- und Eventbezirk `area.event` | Nicht-Verbrauchsartikel | 8,99 € | **5.4** (P1 vorgezogen) | Premium-Gebiet, siehe unten |
| Vaultoria Ultimate `bundle.ultimate` | Nicht-Verbrauchsartikel | 17,99 € | **5.4** | werbefrei + alle Premium-Fahrzeuge + Zentrale + Gebiet |
| Seeufer `region.extra` / Umland Ost `world.large` / Bergland mit Bergekran `world.special` / Designs `design.carbon` 1,49 €, `design.night` 2,49 € | Nicht-Verbrauchsartikel | 5,99 € / 8,99 € / 11,99 € / 1,49–2,49 € | **5.4** (Teil 5d Punkt 7) | Zusatzregion, zweite Welt, Welt + Spezialfahrzeug, Optik |

**Regeln für die Umsetzung (Docs-Thread, aus Julians Text abgeleitet):**
- Ein Produkt wird erst in App Store Connect angelegt und im Shop angeboten, wenn sein Inhalt im Build wirklich spielbar ist (Pakete erst, wenn alle Teile da sind). „Werbefrei-Paket“ und „Werbung entfernen“ sind dasselbe Produkt.
- Premium-Fahrzeuge sind spürbar besser in **einem** Wert (höchstens ca. +15 %) und optisch eigenständig; jeder Auftrag der Hauptwelt bleibt mit normalen Fahrzeugen lösbar. Premium-Fahrzeuge kosten im Spiel normale laufende Kosten.
- Premium-Zentrale ist Optik und Gestaltung (Gebäudevarianten, Beleuchtung), kein schnellerer Ausbau, keine zusätzlichen Bauflächen in der Hauptwelt.
- **Werbung:** nur „automatische“ Werbung (Vollbild) an ruhigen Stellen, Startwert höchstens 1 pro Spieltag bei der Tagesabrechnung, nie während einer Entscheidung, eines Einsatzes oder in den ersten 30 Minuten. Datenschutz/ATT nach Store-Texten Teil Datenschutz. **Anbieter (Julian 16:46, Vorschlag Koordinator): Google AdMob** mit Googles Einwilligungsdialog (UMP, für EU/DSGVO) und danach Apples ATT-Abfrage; ohne Zustimmung nur nicht personalisierte Werbung. Werbeformat: **Interstitial** (Vollbild) bei der Tagesabrechnung, keine Banner, kein Rewarded (Julian hat keine Belohnungswerbung bestellt). Während der Entwicklung nur Googles Test-IDs. Wer `noads`, `bundle.company` oder `bundle.ultimate` besitzt, sieht keine Werbung und keine Abfrage.
- **Käufe wiederherstellen** in den Einstellungen; Kaufstatus über StoreKit 2 (`Transaction.currentEntitlements`), offline gültig.
- Shop-Ort ohne neuen Tab: Karte **„Premium“** im Tab Zentrale (UI-Vorgabe 000e).

### Update P1: Premium-Gebiet „Flughafen- und Eventbezirk“ (8,99 €, eigenes Update nach 5.3)

- Eigener großer Kartenbereich, über eine Brücke/Zufahrt mit der Hauptwelt verbunden, ohne Kauf sichtbar aber gesperrt (dezent, mit Infokarte statt Werbung im Spielfluss).
- Bezirke: Flughafen, Messegelände, Rennstrecke, Luxusviertel; eigene Partnerverträge (Flughafen-Betreiber, Messe, Rennveranstalter; fiktiv, keine Marken).
- Auftragsarten: VIP-Pannen, Sportwagen- und Oldtimertransporte (geschlossener Transporter), Pannen bei Großveranstaltungen (mehrere gleichzeitig), Transport von Rennfahrzeugen, Sicherheits- und Begleitaufträge; seltene Fahrzeuge für die Sammlung (sobald Sammlung E12 freigeschaltet ist, vorher normale Transporte).
- Besondere Mitarbeiter und Lackierungen nur dort.
- Wirtschaft: Erlöse ca. ×1,6, Kosten ca. ×1,3, strengere Zeitfenster und Bewertung; nach Kauf sofort nutzbar, aber auf Firmenstufe 1 mit kleiner Flotte bewusst fordernd.
- Hauptwelt bleibt vollständig ohne P1 spielbar; Endziel der Hauptwelt hängt nie an P1.
- Datenmodell: eigener `District` mit `requiresEntitlement: "area.event"`, eigene `JobType`-Varianten; Spielstand speichert Fortschritt im Gebiet getrennt, damit ein Wiederherstellen nach Neuinstallation funktioniert.

## 2a. Taktplan gegen Wiederholung **[R8]**

Regel: **Spätestens alle 8 Spieltage (ca. 2½ Stunden) kommt etwas Neues**: eine Stufe aus Teil 2 oder eine neue Einsatzvariante. Keine Einsatzart läuft länger als 20 Spieltage ohne neue Variante. Varianten sind neue Inhalte innerhalb bekannter Abläufe, kein neues System.

| Spieltage | Neues System (Teil 2) | Neue Einsatzvarianten | Mehr Verantwortung |
|---|---|---|---|
| 1–20 | Wetter, Erfahrung, sichtbare Ausgänge | Kind/Hund im abgeschlossenen Auto (dringend) · E-Auto ohne Akku · Wohnmobil-Panne · Motorrad | 2 → 3 Mitarbeiter, erster Bewerber |
| 21–50 | Ziele, Betriebshof | Unfall mit Gutachter-Wartezeit · Anhänger-Panne · Falschparker im Privatauftrag | Hof verwalten, Standgebühren |
| 51–90 | Standzeiten, Wohnviertel+Bahnhof, Werkstatt-Vertrag, Bergefahrzeug | Taxi am Bahnhof (schnell, gute Sterne) · Lieferwagen mit Ware (Zeitdruck) · Fahrzeug im Graben · Tiefgarage (enge Zufahrt) | erster Vertrag mit Pünktlichkeitsquote, 4–5 Fahrzeuge |
| 91–140 | Autobahn, Kaufangebote+Sammlung, Polizei | Pannenstreifen nachts · Unfall mit Absicherung · Sicherstellung nach Kontrolle · Oldtimer-Panne (Sammler-Kontakt) | Nachtdienst, Schichtplan für 6–8 Mitarbeiter, Polizei-Zeitlimits |
| 141–200 | Restaurieren, Schwerlast+Lkw, Automobilclub | Lkw mit Reifenschaden · Sattelzug blockiert Kreuzung · Club-Serienpannen bei Hitze/Kälte · Baustellenfahrzeug | zwei Standorte im Hof, 10+ Mitarbeiter, Club-Reaktionszeiten |
| 201–260 | Offizielle Auktionen, Kranwagen+Bus | Linienbus liegengeblieben (Fahrgäste warten) · Reisebus auf Autobahn · umgestürzter Transporter · Hafen-Container-Lkw | Großaufträge mit 2–3 Fahrzeugen, Auktionen bewerten |
| 261–330 | Großunfälle, Land/Vororte, Endziel | Massenkarambolage bei Nebel · Glatteis-Welle (viele kleine Einsätze) · Landstraße weit draußen · große Autobahnbergung (Finale) | 4 Fahrzeuge gleichzeitig koordinieren, ganze Region |

Zusätzlich wechselnde Wetterwochen (Herbstregen, Wintereinbruch) ab Spieltag 60, je 5–7 Tage, mit eigener Einsatzmischung.

## 3. UI-Ablauf (keine neue Menüstruktur)

| System | Auf der Karte | Im Panel / Tab |
|---|---|---|
| **Zeitsteuerung [R2]** | kleine Leiste oben links unter der Kopfleiste: ⏸ · 1× · 2× · 4× (aktive Stufe gold); bei Auto-Pause ein Banner „Pausiert: dringender Einsatz“ mit Knopf „Weiter“ | Einstellungen (Zahnrad): Auto-Pause je Grund |
| Einsatzdauer | Route, Ankunftszeit an der Plakette | Panel 00b: „Ankunft 3:10 · Arbeit ca. 6 Min“ |
| Wetter | Regen-/Schnee-/Nebel-Effekt über der ganzen Karte, Glatteis-Straßen glänzen | kleines Wettersymbol in der Kopfleiste neben Geld |
| Ausgänge **[R3]** | Ergebnis-Symbol am Marker (Haken, Haken + Haken-Symbol für Abschleppen, X) | Panel 00b: Chance-Wort + bis zu 2 Hinweise; Einsatzbericht: 5 Faktor-Zeilen mit Plus/Minus |
| Autobahn-Einsätze | rote Marker mit blinkendem Rand auf der Autobahn, Sirene-Ton | Panel 00b mit „Dringend“-Kapsel und Zielzeit |
| Mitarbeiter **[R6]** | Stufen-Zahl auf der Fahrzeugplakette, Mond-Symbol bei Nachteulen nachts | Tab **Personal**: Karte pro Person mit 4 Werten, Stärke (grün), Schwäche (rot), Besonderheit (goldene Kapsel), Stufe, Müdigkeit, Führerscheine |
| Fahrzeugklassen | eigene 3D-Modelle, gelb-schwarz | Tab **Flotte**: Karten nach Klasse, Kauf bei freiem Stellplatz |
| Lkw/Bus/Großunfall | großer Marker mit Zähler „0/4“, mehrere Routen gleichzeitig | Panel 00b zeigt Teilaufträge als Reihe kleiner Karten, je ein Fahrzeug zuteilen |
| Gebiete | gesperrt = abgedunkelt mit Schild; Freischalten = Kamera fährt hin, Lichter gehen an | Antippen des Schilds: Kosten, Ruf, Knopf „Freischalten“ |
| Verträge | Partnergebäude auf der Karte (Werkstatt, Polizeiwache, Club-Station) mit Logo-Schild in Gold; Vertragsaufträge mit kleinem Partnersymbol am Marker | Antippen des Partnergebäudes: Vertrag, Pünktlichkeit, Verlängern |
| Ruf | — | Stern-Kapsel in der Kopfleiste zeigt Ø Sterne; Antippen: Ruf 0–100 als Leiste + was der nächste Ruf freischaltet |
| Ziele | — | 3 kleine Zielkarten, einklappbar am rechten Kartenrand |
| Statistik | — | Tagesabrechnung → „Verlauf“ |
| Betriebshof **[R4]** | eigenes Gebäudeteil, abgestellte Fahrzeuge stehen sichtbar auf dem Hof, Dauersteher grau markiert | Tab **Zentrale**: Karte „Betriebshof“ mit Belegung „14/20 Einheiten“ und **Tagessaldo** (Gebühren − Kosten, grün/rot), Liste der Fahrzeuge |
| Standgebühren | Münz-Symbol über lange stehenden Fahrzeugen | Tagesabrechnung: Zeile „Standgebühren“ |
| Halter/Frist/Auktion **[R5]** | Countdown-Ring über dem Fahrzeug im Hof, Hammer-Symbol bei Auktion | Antippen: 3 Schritte als Leiste (Kontakt · Frist · Ergebnis), Knopf „Halter kontaktieren“, später „Kaufen“ bzw. „Bieten“; „i“ für den Zeitstrahl |
| Welt-Ausblick **[R7]** | abgedunkelte Region am Kartenrand mit Schild „Neue Region folgt mit einem späteren Update“ | Antippen: was mitkommt |
| Sammlung | Schauhalle an der Zentrale, Fahrzeuge sichtbar ausgestellt | Tab **Zentrale** → Karte „Sammlung“: Behalten / Restaurieren / Verkaufen |

Neue Zentrale-Karten (Betriebshof, Sammlung) erscheinen erst mit ihrer Stufe und reihen sich hinter Garage, Werkstatt, Leitstelle ein (seitlich wischen, UI-Vorgabe 00c).

---

## 4. Abgestellte Fahrzeuge, Auktionen und Kaufangebote: echter Ablauf in Deutschland und Umsetzung im Spiel

> Vereinfachte Spielumsetzung nach geltendem Recht, keine Rechtsberatung. Im Spiel gibt es nur fiktive Personen, Firmen, Kennzeichen und Fahrzeuge.

### 4.1 Der echte Ablauf (Stand der Recherche 14.10.2026)

1. **Halter ermitteln.** Wer ein rechtliches Interesse hat (z. B. Forderung gegen den Halter), bekommt bei der Zulassungsbehörde eine einfache Registerauskunft über den Halter (§ 39 StVG). Die Polizei ermittelt den Halter selbst.
2. **Verwahrkosten (Standgebühren) bei privat abgeschleppten Fahrzeugen.** Der Bundesgerichtshof hat entschieden: Verwahrkosten sind nur **bis zu dem Zeitpunkt** erstattungsfähig, **zu dem der Halter die Herausgabe verlangt**. Im entschiedenen Fall verlangte der Abschlepper 15 € pro Tag für rund elf Monate (4.935 €), zu zahlen waren nur 75 € für fünf Tage (BGH, Urteil vom 17.11.2023, V ZR 192/22).
3. **Polizeilich sichergestellte Fahrzeuge** (z. B. Abschleppen im Auftrag der Polizei). Die Behörde darf verwerten, wenn die Sache z. B. trotz Mitteilung einer Frist nicht abgeholt wird, wobei die Mitteilung auf die Verwertung hinweisen muss, oder wenn die Verwahrung unverhältnismäßig teuer ist. Betroffene sollen vorher gehört werden, Zeit und Ort werden mitgeteilt. Regelform ist die **öffentliche Versteigerung**, freihändiger Verkauf nur, wenn die Versteigerung scheitert oder aussichtslos ist. **Der Erlös tritt an die Stelle der Sache**, gehört also dem Berechtigten (Beispiel NRW: § 45 PolG NRW; andere Länder ähnlich). Der Abschlepper verwertet dabei nicht selbst, sondern die Behörde.
4. **Nicht bezahlte Reparatur.** Wer eine Sache repariert, hat ein Pfandrecht daran (Werkunternehmerpfandrecht, § 647 BGB). Verkauf nur nach den Regeln des Pfandverkaufs: Verkauf vorher **androhen** mit Angabe des Geldbetrags, dann **ein Monat Wartefrist** (§ 1234 BGB), dann **öffentliche Versteigerung** (§ 1235 BGB) durch einen öffentlich bestellten Versteigerer oder Gerichtsvollzieher. Aus dem Erlös wird die Forderung bezahlt; der Rest steht dem Eigentümer zu (§ 1247 BGB).
5. **Schrottfahrzeuge ohne gültige Kennzeichen.** Die Behörde bringt einen gut sichtbaren Hinweis an (z. B. in Bayern einen roten Punkt, mindestens 12 cm). Wird das Fahrzeug nicht **innerhalb eines Monats** entfernt, gilt es als **Abfall** (§ 20 Abs. 3 KrWG) und wird auf Kosten des Verantwortlichen beseitigt und verwertet (Altfahrzeug-Verordnung). Ein Abschlepper darf es dann nur im Auftrag zur Entsorgung bringen, nicht behalten.
6. **Freiwilliger Kauf.** Der Halter bzw. Eigentümer kann sein Fahrzeug jederzeit freiwillig verkaufen, z. B. weil sich die Reparatur nicht lohnt. Das ist ein normaler Kaufvertrag.

### 4.2 Umsetzung im Spiel

**[R5] Für den Spieler gibt es nur drei Schritte:**

1. **Halter kontaktieren**: ein Knopf am Fahrzeug im Hof. Die Simulation erledigt im Hintergrund Halterauskunft und Anschreiben.
2. **Frist läuft**: ein Countdown-Ring am Fahrzeug (z. B. „noch 5 Tage“). Im Hintergrund laufen Mahnung, Androhung und Wartefrist automatisch nacheinander.
3. **Abholung, Verkauf oder offizielle Auktion**: Das Ergebnis erscheint von selbst: Halter holt ab und zahlt, Halter bietet das Fahrzeug zum Kauf an, oder es kommt zur offiziellen Auktion (Versteigerer bzw. Behörde), bei der der Spieler mitbieten kann.

Wer mehr wissen will, tippt auf ein kleines „i“: Dann zeigt ein Zeitstrahl die echten Schritte aus der Tabelle unten. Bedienen muss man dort nichts.

Intern:

Jedes Fahrzeug im Betriebshof hat einen `LegalCase`:

```swift
struct LegalCase: Codable {
  var track: LegalTrack          // .ownerSale, .pledgeSale, .authorityRelease, .waste
  var step: Int                  // aktueller Schritt im Ablauf unten
  var stepStartedDay: Int
  var claim: Int                 // offene Forderung (Abschleppen, Reparatur, Gebühren bis Herausgabeverlangen)
  var log: [String]              // Verlauf, im Panel als Zeitstrahl
}
```

| Fall | Schritte intern (Fristen gestaucht: 1 Monat = 5 Spieltage) | Was der Spieler tun kann |
|---|---|---|
| **A Panne/Unfall, Halter bekannt** | Gebühren laufen → Halter meldet sich (Herausgabeverlangen, Gebühren stoppen) → Abholung | Warten. Manchmal **Kaufangebot**: Halter bietet das Fahrzeug an (Reparatur lohnt sich nicht) → Kaufen oder Ablehnen |
| **B Reparatur nicht bezahlt** | Forderung offen → 1) Halter ermitteln (§ 39 StVG, kleine Gebühr, 1 Tag) → 2) Mahnung, 2 Tage → 3) **Verkauf androhen** mit Betrag → 4) **5 Spieltage Wartefrist** (= 1 Monat) → 5) **öffentliche Versteigerung** durch Versteigerer (Gebühr) → Erlös: Forderung an Spieler, Rest „an den Eigentümer“ (im Bericht ausgewiesen) | Nur „Halter kontaktieren“ **[R5]**; der Rest läuft automatisch; bei der Versteigerung **mitbieten** wie jeder andere Bieter; Halter kann bis zur Versteigerung zahlen und abholen |
| **C Polizeiliche Sicherstellung** (Vertrag Polizei) | Spieler verwahrt im Auftrag, Behörde zahlt Verwahrung → Abholung durch Halter oder, wenn nicht abgeholt, **Behörde verwertet**: Behördenauktion | Gebühren werden von der Behörde bezahlt. Bei der **Behördenauktion** mitbieten; der Spieler verkauft nie selbst |
| **D Privat abgeschleppter Falschparker** | Gebühren laufen nur bis Herausgabeverlangen (BGH) → Halter zahlt Abschleppen + Gebühren bis dahin → Abholung | Nichts verkaufen. Wer zahlt nicht, wird über Fall B geführt, wenn eine Werkleistung offen ist; sonst bleibt nur die Forderung |
| **E Schrottfahrzeug ohne Kennzeichen** (Auftrag Stadt) | Abholung im Auftrag → Entsorgung beim Verwerter | Auftrag ausführen, Bezahlung von der Stadt. Kein Behalten, keine Sammlung |

Regeln im Code:
- `Offer` vom Typ `publicAuction` darf nur entstehen, wenn `LegalCase.track == .pledgeSale` **und** Schritte 1–4 abgeschlossen sind.
- `authorityAuction` nur bei `track == .authorityRelease` nach Ablauf der Abholfrist.
- `ownerSale` nur als Angebot des Halters, nie vom Spieler erzwungen.
- Erlösverteilung immer im Einsatzbericht sichtbar: „Erlös 3.200 € · deine Forderung 1.150 € · an den Eigentümer 2.050 €“.
- Jede Auktion zeigt in einem Satz den Rechtsgrund, z. B. „Öffentliche Versteigerung nach Androhung und Wartefrist (Pfandverkauf).“

### 4.3 Quellen

- § 39 StVG, Fahrzeugregisterauskunft: [gesetze-im-internet.de/stvg/__39.html](https://www.gesetze-im-internet.de/stvg/__39.html)
- BGH V ZR 192/22 vom 17.11.2023, Verwahrkosten nur bis Herausgabeverlangen: [bussgeldkatalog.org](https://www.bussgeldkatalog.org/news/bgh-begrenzt-verwahrkosten-fuer-abgeschlepptes-auto-8567160), [LTO](https://www.lto.de/recht/nachrichten/n/bgh-vzr19222-auto-abschleppen-verwahrung-kosten-aufwendungsersatz-goa/print.html), [jura-online.de](https://jura-online.de/blog/2023/11/30/bgh-zu-ersatzfaehigen-kosten-beim-abschleppen-eines-pkw/)
- § 45 PolG NRW, Verwertung sichergestellter Sachen: [lexmea.de/de/gesetz/polg-nrw/45](https://lexmea.de/de/gesetz/polg-nrw/45); vergleichbar Bundespolizei § 49 BPolG: [lxgesetze.de/bpolg/49](https://lxgesetze.de/bpolg/49), Bayern Art. 27 PAG: [lxgesetze.de/pag/27](https://lxgesetze.de/pag/27)
- § 1234 BGB Verkaufsandrohung und Wartefrist, Verweis § 1235 öffentliche Versteigerung: [bgb.kommentar.de](https://bgb.kommentar.de/verkaufsandrohung-wartefrist); Durchführung durch Gerichtsvollzieher: [GVGA § 181](https://www.gesetze-bayern.de/Content/Document/GVGA-181)
- § 20 Abs. 3 KrWG und Ablauf mit rotem Punkt: [Leitfaden Bayerisches Staatsministerium](https://www.bauministerium.bayern.de/assets/stmi/vum/strasse/strassenundverkehrsrecht/iib3_leitfaden_beseitigung_verbotswidrig_abgestellter_kraftfahrzeuge_20130912.pdf)
- § 647 BGB (Werkunternehmerpfandrecht) und § 1247 BGB (Erlös) aus dem Gesetzestext übernommen, nicht gesondert verlinkt.

---

## 5. Updates (klein, einzeln testbar)

Plan-Nummern E1–E19. **App-Versionen ab 14.10.2026: nächster Build = Vaultoria 5.0, danach 5.1, 5.2 … (Julians Wahl, weil 1.x unter der installierten 4.1 keine automatischen TestFlight-Updates bekam).** E1 kommt also als 5.0 oder später; die genaue Zuordnung vergibt der Mac. Jedes Update: kompiliert, alte Spielstände laden (Migrationstest), TestFlight-Build, Screenshots als ZIP.

| Update | Inhalt | Abnahme | Screenshots |
|---|---|---|---|
| **E1 Fundament** (siehe 5a) **✓ erledigt in 5.1** | Profil + Weltstand mit `worldId`, `schemaVersion` + Migration, Spieltag 18 Min, Simulation in festen Spielminuten, **Zeitsteuerung ⏸/1×/2×/4× mit Auto-Pause**, Freischaltsystem (nur Stufe 0), Seed-Tests | siehe 5a | siehe 5a |
| **E1.5 Zielorte + Betriebsmittel** (Stufe 0, siehe 5b) | Zielwahl nach dem Abschleppen, Ladung sichtbar, Hof-Grundumfang, 5 Bestände, 4 Entsorgungscontainer, Ausbau Lager/Reifencontainer/Recycling, Starttempo | siehe 5b | siehe 5b |
| **E1.6 Transparenz + Details** (Stufe 0, siehe 5c) | Kalkulation vor Zuteilung, Status während, Abrechnung danach, Kassenbuch, Fixkosten, Verlauf, eindeutige Status, Gründe, Kaufbestätigung, Geld-Rückmeldung, Ersthinweise | siehe 5c | siehe 5c |
| **P1 Premium-Gebiet** (Kauf 8,99 €, nach 5.3, siehe 2c) | Flughafen- und Eventbezirk, VIP- und Event-Aufträge, eigene Verträge | Hauptwelt ohne Kauf vollständig; Kauf/Wiederherstellen schaltet frei | Gebiet gesperrt, gekauft, VIP-Auftrag |
| **E2 Wetter + Dauer** (Stufe 1) | Wetter, Verkehrsfaktoren, Dauerformel, A*-Route über Stau | Regen verlängert sichtbar Fahrt; Route weicht Stau aus; Anzeige stimmt mit tatsächlicher Dauer ±10 % | Karte bei Regen, Panel mit Ankunft/Arbeit, Umweg um Stau |
| **E3 Erfahrung** (Stufe 2) | XP, Stufen, Wertwahl alle 3 Stufen | Nach Einsätzen steigt XP in der genutzten Fähigkeit; Stufenkarte erscheint; Wert wirkt auf Dauer | Personal-Tab, Stufe-erreicht-Karte |
| **E4 Ausgänge** (Stufe 3) | Outcome-Würfel, „gute Chance/riskant“, Berichte | Alle 7 Ausgänge mit festem Seed auslösbar, Geld/Sterne korrekt | Panel mit Chance-Wort, 3 Berichte mit unterschiedlichem Ausgang |
| **E5 Ziele + Verlauf** (Stufe 4) | 3 aktive Ziele, Belohnungen, Verlauf in der Tagesabrechnung | Ziel erfüllen → Belohnung, neues Ziel; Verlauf zeigt 30 Tage | Zielkarten am Rand, Verlauf-Diagramme |
| **E6 Betriebshof + Firmenstufe 2** (Stufe 5) | Aufstieg zu Firmenstufe 2 (Grundstück, Umzug, Teil 2b); baut auf dem Hof-Grundumfang aus E1.5 auf: Depot, Einlagern, Gebühren bis Herausgabeverlangen | Voller Hof blockiert Einlagern; Gebühren stoppen bei Herausgabeverlangen; Tagesabrechnung zeigt Gebühren | Hof auf der Karte, Zentrale-Karte Betriebshof, Liste |
| **E7 Standzeiten/Platz** (Stufe 6) | Größenklassen, Gründe, Standzeiten | Transporter belegt 2 Einheiten; Standzeiten im Bereich der Tabelle | Hof mit gemischten Fahrzeugen |
| **E8 Gebiete 1** (Stufe 7) | District-System, Wohnviertel + Bahnhof | Gesperrt sichtbar, Freischalten mit Kosten/Ruf; neue Einsatzmischung | Gesperrtes Gebiet, Freischalt-Kamerafahrt |
| **E9 Vertrag Werkstatt** (Stufe 8) | Contract-System, Partnergebäude | Vertragsaufträge mit Zeitlimit; Pünktlichkeit zählt; Verlängerung/Ende | Partnergebäude, Vertragskarte |
| **E10 Bergefahrzeug** (Stufe 9) | Klasse `recovery`, Bergungseinsätze | Bergung nur mit Bergefahrzeug sinnvoll; falsches Fahrzeug → zweiter Wagen | Flotte, Bergung auf der Karte |
| **E11 Autobahn** (Stufe 10) | Gebiet Autobahn, dringende Einsätze, Absicherung | Dringend-Marker, Zielzeit-Bonus, Absicherung bringt Sterne | Autobahn mit Einsatz |
| **E12 Kaufangebote + Sammlung** (Stufe 11) | `ownerSale`, Sammlung Behalten/Verkaufen, Schauhalle | Angebot nur vom Halter; gekauftes Fahrzeug in der Sammlung und auf dem Hof sichtbar | Angebot, Sammlung, Schauhalle |
| **E13 Vertrag Polizei** (Stufe 12) | Sicherstellung, Verwahrung durch Behörde bezahlt, Behördenauktion vorbereitet | Fall C komplett bis Abholung | Polizeiwache, verwahrtes Fahrzeug mit Status |
| **E14 Restaurieren** (Stufe 13) | 3 Restaurierungsstufen | Wert steigt, Kosten/Schichten korrekt | Fahrzeug vor/nach |
| **E15 Schwerlast + Lkw** (Stufe 14) | Klasse `heavyTow`, Führerschein-Schulung, Gewerbegebiet | Lkw-Einsatz nur mit CE-Mitarbeiter und Schwerlast | Lkw-Bergung, Schulung |
| **E16 Automobilclub** (Stufe 15) | dritter Vertrag | Viele kurze Einsätze, fester Satz | Club-Station |
| **E17 Versteigerungen** (Stufe 16) | LegalCase Fall B komplett, Behördenauktion Fall C, Bieten | Auktion entsteht nur nach allen Schritten; Erlösverteilung korrekt; Halter kann vorher zahlen | Zeitstrahl LegalCase, Auktion, Erlösbericht |
| **E18 Kranwagen + Bus** (Stufe 17) | Klasse `crane`, Bus-Einsätze, Industriehafen | Umgestürztes Fahrzeug nur mit Kran | Kraneinsatz, Hafen |
| **E19 Großunfälle + Land** (Stufe 18) | SubTasks, Großunfall-Marker, Gebiet Land/Vororte, Endziel, Ausblick „Neue Region folgt“ **[R7]** | 4 Teilaufträge parallel, Bezahlung am Ende; Endziel-Einsatz | Großunfall mit 4 Routen, Endziel-Karte |

Reihenfolge ist verbindlich, Inhalte eines Updates werden nicht vorgezogen. Jedes Update bringt neben seiner Funktion die Einsatzvarianten seines Spieltag-Bereichs aus Teil 2a mit **[R8]**.

### 5a. E1 genau (**erledigt**)

**Status 14.10.2026:** E1 komplett in Vaultoria 5.1 (Build 202610141353, TestFlight): Profil- und Weltstand, 18-Minuten-Tag, Zeitsteuerung mit Auto-Pause, 17 Tests grün. 5.1 enthält außerdem die Lesbarkeitspunkte aus UI-Vorgabe 000a. Testbericht: `/mnt/project-files/Testbericht.md`. Erkenntnis aus dem Test: Start mit 2 Wagen zu hektisch, Viertel öffnen zu schnell (die alte Viertel-Freischaltung läuft bis E8 weiter, Teil 7). Balancing folgt in den nächsten Updates; danach E2.

**Inhalt**
1. **Spielstand neu aufteilen [R7]:** `profile.json` (Profil, Einstellungen, CarryOver leer) und `world-welt1-heimatstadt.json` (Weltstand). Bestehenden Spielstand automatisch in diese Form migrieren (**Schema 2 → 3**, Teil 7; alte Datei bleibt als `…-v2-backup.json`). `WorldDefinition` für Welt 1 als statische Daten; der bisherige Kartenaufbau wird daraus geladen.
2. **Versionierung:** `schemaVersion`, schrittweise `migrate(from:)`, neue Felder mit Standardwerten. Defekter oder unbekannter Stand → Kopie als `save-defekt-<datum>.json`, dann sauberer Neustart mit kurzem Hinweis.
3. **Spieltag 18 Minuten [R1]:** Spieluhr 06:00–22:00, Tagesabrechnung am Tagesende wie bisher.
4. **Simulationstakt:** feste Schritte von 1/10 Spielminute (Teil 7), getrennt von der Darstellung; 2× und 4× rechnen mehrere Schritte pro Takt.
5. **Zeitsteuerung [R2]:** Leiste ⏸ · 1× · 2× · 4× oben links unter der Kopfleiste. Auto-Pause bei dringendem Einsatz, Sonderentscheidung, Tagesende (Freischaltung folgt ab E2). Banner „Pausiert: …“ mit „Weiter“, danach alte Geschwindigkeit. App im Hintergrund = Pause. Einstellung Auto-Pause je Grund.
6. **Freischaltsystem:** `unlockedStage`, `StageDefinition` mit Auslösern; in E1 nur Stufe 0 aktiv, Stufe 1 als Testeintrag im Debug-Menü. Die bisherige Viertel-Freischaltung bleibt bis E8 unverändert (Teil 7).
8. **Löhne ×3,6** zum 18-Minuten-Tag (Teil 7), Feinjustierung per Bot-Test über 3 Spieltage.
7. **Tests:** Simulation mit festem Seed: gleicher Seed + gleiche Eingaben = gleicher Spielstand nach 3 Spieltagen, bei 1× und bei 4× identisch. Migrationstest mit einem echten Spielstand der aktuellen Version.

**Nicht in E1:** Wetter, Ausgangsformel, Persönlichkeiten, Betriebshof, Gebiete, alles ab E2.

**Abnahme**
- Bestehender Spielstand lädt ohne Verlust (Geld, Fahrzeuge, Mitarbeiter, Ausbauten, Einsätze) und liegt danach als Profil + Weltstand Schema 3 vor.
- Absichtlich kaputter Spielstand → kein Absturz, sauberer Neustart, Kopie vorhanden.
- Ein Spieltag dauert bei 1× 18 Minuten (±10 s), bei 2× 9, bei 4× 4½ Minuten.
- ⏸/1×/2×/4× funktionieren jederzeit; Fahrzeuge bewegen sich bei 4× flüssig auf der Route, ohne Springen.
- Dringender Einsatz und Sonderentscheidung pausieren automatisch; „Weiter“ setzt die vorige Geschwindigkeit fort.
- Seed-Test grün, Projekt ohne Warnungen, sonst sieht das Spiel aus wie vorher.

**Screenshots:** Karte mit Zeitsteuerung (1× aktiv) · Karte bei 4× mit fahrenden Fahrzeugen · Auto-Pause-Banner bei dringendem Einsatz · Einstellungen Auto-Pause · Hinweis nach Neustart wegen defektem Stand. Nach jedem Update: TestFlight, Screenshots, Julian testet, dann das nächste.

---

### 5b. E1.5 Zielorte und Betriebsmittel (vor E2; Tempo in 5.2, E1.5 als 5.3)

**Julians Auftrag (wörtlich, 14.10.2026 14:03):**

> Genau, du hast einen wichtigen fehlenden Teil entdeckt: Nach einem Einsatz verschwindet momentan alles einfach. Das wirkt unfertig. Es fehlt ein richtiges Abschlepp- und Lagersystem.
> Nach dem Abschleppen
> Der Spieler wählt ein Ziel:
>
> * eigener Betriebshof
> * Partnerwerkstatt
> * Polizeiverwahrung
> * Schrottplatz
> * vom Kunden gewünschte Werkstatt
>
> Der Abschlepper fährt mit dem Auto sichtbar dorthin, lädt es ab und ist erst danach wieder verfügbar. Auf dem eigenen Hof bleibt das Fahrzeug sichtbar stehen und belegt Platz.
> Ersatzteile und Abfälle
> Die Zentrale braucht zusätzlich ein kleines Lager:
> Verbrauchsmaterial
>
> * Batterien
> * Pkw-, Transporter- und später Lkw-Reifen
> * Kraftstoffkanister
> * Ersatzteile
> * Ölbindemittel
>
> Altteile und Abfälle
>
> * alte Reifen
> * defekte Batterien
> * Altöl
> * beschädigte Ersatzteile
> * Unfallschrott
>
> Neue Teile werden bei Einsätzen verbraucht. Alte Teile kommen danach in begrenzte Container am Betriebshof:
>
> * Altreifenentsorgung kostet Geld.
> * Altöl muss kostenpflichtig abgeholt werden.
> * Batterien und Metallschrott können etwas Geld bringen.
> * Ist der Lagerplatz voll, können bestimmte Einsätze nicht mehr angenommen werden.
> * Lager, Reifencontainer und Recyclingbereich lassen sich ausbauen.
>
> Es sollte aber keine Kleinteile-Mikroverwaltung geben. Lieber fünf verständliche Bestände statt jede einzelne Schraube.
> Änderung für Claude
> Vor E2 ein zusätzliches Update E1.5 – Zielorte und Betriebsmittel einfügen.
>
> * Abgeschleppte Fahrzeuge dürfen nicht verschwinden.
> * Nach der Bergung muss ein Ziel gewählt werden: eigener Hof, Partnerwerkstatt, Polizei, Schrottplatz oder Kundenwerkstatt.
> * Das abgeschleppte Fahrzeug bleibt während der Fahrt sichtbar auf dem Abschlepper.
> * Der Abschlepper bleibt bis Abladen und Rückfahrt belegt.
> * Fahrzeuge auf dem eigenen Hof stehen sichtbar dort und belegen Stellfläche.
> * Einfaches Lager für Batterien, Reifen, Kraftstoff, Ersatzteile und Ölbindemittel ergänzen.
> * Einsätze verbrauchen passende Materialien.
> * Alte Reifen, Batterien, Altöl und Schrott landen in begrenzten Entsorgungsbereichen.
> * Abholung beziehungsweise Entsorgung kostet Geld; Batterien und Metallschrott können einen kleinen Erlös bringen.
> * Keine Verwaltung einzelner Schrauben oder unnötige Menüs. Lagerbestand direkt in der Zentrale und bei der Einsatzwahl anzeigen.
> * Der große Betriebshof mit Standgebühren, Auktionen und Sammlung bleibt später in E6. E1.5 baut nur den notwendigen Grundablauf.
>
> Außerdem das Starttempo reduzieren: 43–49 erledigte Einsätze pro Spieltag sind viel zu hektisch. Anfangs ungefähr 8–12 Einsätze pro Tag, später mit größerer Flotte entsprechend mehr.
> Das gehört tatsächlich früh rein. Erst dadurch wird aus „Einsatz erledigt und Auto weg“ ein nachvollziehbarer Abschleppbetrieb.

**Umsetzung (Startwerte zum Testen):**

**1. Starttempo (zuerst, in 5.2).** Einsätze kommen über ein Tagesbudget statt über ein festes Intervall:
`tagesbudget = clamp(4,5 × einsatzfähige eigene Fahrzeuge + 1 × Leitstellen-Stufe, 8, 40)` → mit 2 Wagen ca. 9–10, Spanne durch Zufall ±2, also **8–12 am Anfang**. Die Einsätze verteilen sich über den Tag mit Spitzen morgens und am späten Nachmittag; nachts weniger. Mehr Fahrzeuge bedeuten mehr Einsätze, nie mehr als die Flotte schaffen kann (Ziel: jedes Fahrzeug 4–6 Einsätze pro Tag). Die alte Viertel-Freischaltung bleibt bis E8 (Teil 7), darf aber das Tagesbudget nicht erhöhen.

**2. Zielorte nach dem Abschleppen.**
```swift
enum TowDestination: String, Codable { case ownYard, partnerWorkshop, policeImpound, scrapyard, customerWorkshop }
struct DestinationSite: Codable { let id: String; let kind: TowDestination; let position: GridPos; let name: String }
```
- Jeder Zielort steht als Gebäude auf der Karte (fiktive Namen, keine Marken). In Welt 1: eigener Hof an der Zentrale, 2 Partnerwerkstätten, 1 Polizeiverwahrung, 1 Schrottplatz, Kundenwerkstätten als 3–4 normale Werkstätten in den Vierteln.
- Nach der Bergung erscheint **ein** kleines Panel „Wohin?“ mit nur den passenden Zielen (2–4 Knöpfe, Empfehlung markiert, Fahrzeit und Erlös je Ziel). Passend heißt: Kundenwerkstatt nur, wenn der Kunde eine nennt; Polizei nur bei Unfall mit Polizei vor Ort; Schrottplatz nur bei Totalschaden oder Kundenwunsch; Partnerwerkstatt und eigener Hof immer (Hof nur mit freiem Platz).
- Erlös je Ziel (zusätzlich zum Einsatzlohn): Partnerwerkstatt +40 € Vermittlung, Kundenwerkstatt +0 € aber +Ruf, Polizei +60 € Pauschale, Schrottplatz +Schrotterlös nach Fahrzeug (80–200 €), eigener Hof +0 € (Abholung durch Halter nach 1–3 Spieltagen, dann +50 € Abstellpauschale; **keine Tagesgebühren vor E6**).
- Auto-Pause-Grund „Ziel wählen“; ohne Wahl nach 30 Spielminuten wird die Empfehlung genommen.

**3. Ladung auf dem Abschlepper.**
```swift
struct Load: Codable { let jobId: UUID; let size: VehicleSize; let visual: CarVisualId }   // VehicleSize: .car, .van (.truck ab E15)
// FleetVehicle bekommt: var load: Load?   und Phasen:
enum TowPhase: String, Codable { case toScene, working, loading, toDestination, unloading, returning }
```
- Das Fahrzeug steht sichtbar auf der Ladefläche (gleiches Modell wie am Einsatzort). Aufladen 10 Spielminuten, Abladen 10 Spielminuten, beides als kurze Animation.
- Der Abschlepper ist bis zur Rückkehr in die Zentrale belegt. Plakette: Statuspunkt orange während `toDestination`, zusätzlich kleines Auto-Symbol solange `load != nil`; grau bei `returning`.
- Servicewagen ohne Plattform können nicht abschleppen; Einsätze, die Abschleppen brauchen, verlangen einen Abschlepper.

**4. Eigener Hof, Grundumfang.**
```swift
struct YardBasic: Codable { var capacityUnits: Int = 4; var parked: [ParkedVehicle] }
struct ParkedVehicle: Codable { let id: UUID; let size: VehicleSize; let slot: Int; let since: GameTime; let pickupAt: GameTime; let visual: CarVisualId }
```
- 4 Einheiten am Start, Pkw 1, Transporter 2. Abgestellte Fahrzeuge stehen sichtbar auf festen Stellplätzen im Hof hinter der Zentrale (UI 000a Punkt 9).
- Hof voll → Ziel „eigener Hof“ ausgegraut mit „Hof voll“.
- Abholung: Der Halter holt nach 1–3 Spieltagen ab (kleines Kundenauto fährt vor und wieder weg).
- E6 baut darauf auf (mehr Platz, Standgebühren bis Herausgabeverlangen, Kosten, Auktionen, Sammlung). Nichts davon in E1.5.

**5. Fünf Bestände (Verbrauchsmaterial).**
```swift
enum Supply: String, Codable, CaseIterable { case battery, tire, fuelCan, spareParts, oilBinder }
struct Storage: Codable { var stock: [Supply: Int]; var level: Int = 1 }   // Kapazität je Stufe gesamt
```
| Bestand | Einkauf | Verbrauch |
|---|---|---|
| Batterien | 90 € | Batterie-Einsatz: 1 (nur wenn Starthilfe nicht reicht, ca. 40 %) |
| Reifen (Pkw/Transporter; Lkw ab E15 als eigene Größe) | 60 € | Reifenpanne: 1 |
| Kraftstoffkanister | 15 € | Kraftstoff-Einsatz: 1 |
| Ersatzteile (ein Sammelbestand) | 40 € | Technischer Defekt: 1 |
| Ölbindemittel (Sack) | 12 € | Unfall: 1–2 |

- Lager Stufe 1/2/3: 20/40/70 Einheiten gesamt; Ausbau 1.500 € / 4.000 €, sichtbar größeres Regal-Gebäude neben der Zentrale.
- Nachkaufen mit einem Knopf je Bestand in der Zentrale („+5 · 300 €“), Lieferung nach 1 Spielstunde (Lieferwagen fährt sichtbar vor). Optional „Automatisch nachbestellen unter 3“ (Standard an).
- Fehlt das passende Material, ist der Einsatz in der Zuteilung ausgegraut mit Grund („Keine Reifen“). Bestände stehen als 5 kleine Zähler in der Zentrale und in der Einsatzwahl.

**6. Vier Entsorgungscontainer (Altteile und Abfälle).**
```swift
enum WasteBin: String, Codable, CaseIterable { case oldTires, oldBatteries, usedOil, scrapMetal }   // scrapMetal = beschädigte Ersatzteile + Unfallschrott
struct WasteArea: Codable { var fill: [WasteBin: Int]; var tireLevel: Int = 1; var recyclingLevel: Int = 1 }
```
| Container | Füllung pro Einsatz | Größe Stufe 1/2/3 | Abholung |
|---|---|---|---|
| Altreifen | Reifenpanne +1 | 10/20/35 (Reifencontainer) | **kostet** 4 € je Reifen |
| Altbatterien | Batterietausch +1 | 8/15/25 (Recycling) | **bringt** 6 € je Batterie |
| Altöl | Unfall/Defekt +1 Kanister | 6/12/20 (Recycling) | **kostet** 45 € pauschal je Abholung |
| Metallschrott | Defekt +1, Unfall +2 | 12/25/40 (Recycling) | **bringt** 3 € je Einheit |

- Ausbau Reifencontainer 800 € / 2.000 €; Recyclingbereich 1.200 € / 3.000 €; beides sichtbar am Hof.
- Abholung per Knopf „Abholen lassen“ in der Zentrale; der Entsorger-Lkw kommt sichtbar innerhalb 1 Spielstunde. Bei 80 % Füllung ein orangefarbener Hinweis.
- Container voll → Einsätze, die genau diesen Abfall erzeugen, sind ausgegraut („Altreifen-Container voll“). Nie ein Absturz und kein Totlauf: Abholen ist immer möglich, notfalls mit Kredit-Hinweis im Minus.
- Tagesabrechnung bekommt die Zeilen „Material“, „Entsorgung“ und „Recycling-Erlös“.

**7. UI (keine neuen Menüs).** Zielwahl als einzelnes Panel nach dem Einsatz. Bestände und Container als eine kompakte Karte „Lager“ im Tab Zentrale (5 Zähler, 4 Füllbalken, Knöpfe Nachkaufen und Abholen). In der Einsatzwahl eine Zeile mit dem benötigten Material. Stil nach UI-Vorgabe 000/000a/000b.

**8. Spielstand.** Schema 3 → 4: `yardBasic`, `storage`, `wasteArea`, `load` und `towPhase` an Fahrzeugen, mit Standardwerten (Lager mit 3 von jedem Bestand, leere Container). Laufende Einsätze aus Schema 3 schließen wie bisher ab. Migrationstest mit einem echten 5.1/5.2-Stand.

**Tests:** gleicher Seed = gleiches Ergebnis; mit 2 Wagen 8–12 Einsätze am Tag 1–3; abgeschlepptes Auto ist bis zum Abladen sichtbar und steht danach am Ziel bzw. auf dem Hof; voller Hof blockiert nur das Ziel Hof; fehlendes Material und voller Container sperren nur passende Einsätze; Abholung rechnet Kosten und Erlöse richtig.

**Screenshots:** Panel „Wohin?“ · Abschlepper mit Auto auf der Ladefläche unterwegs · Abladen auf dem Hof · Hof mit 3 abgestellten Autos · Lager-Karte in der Zentrale · ausgegrauter Einsatz wegen fehlender Reifen · Entsorger-Lkw am Hof · Tagesabrechnung mit Material/Entsorgung.

**Nicht in E1.5:** Standgebühren, Auktionen, Kaufangebote, Sammlung, Hofkosten (alles E6/E12), Lkw-Reifen (E15), Wetter (E2).

### 5c. E1.6 Transparenz und Details (vor E2; App 5.3 zusammen mit Zielort + Lager aus E1.5)

**Julians Auftrag (wörtlich, 14.10.2026 14:15):**

> Vaultoria 5.1 wirkt optisch deutlich besser, aber es fehlen viele kleine Informationen und nachvollziehbare Abläufe. Dadurch fühlt sich das Spiel noch wie eine technische Demo an. Ergänze vor weiteren großen Erweiterungen ein Transparenz- und Detailupdate.
> Jeder Einsatz zeigt vor der Zuteilung erwartete Einnahmen, Kraftstoff, Material, anteilige Mitarbeiterkosten, Verschleiß, mögliche Zusatzkosten und den erwarteten Gewinn. Kennzeichne Schätzwerte klar.
> Während des Einsatzes müssen Status, Restdauer, Mehrkosten, Probleme, Zielort und Verfügbarkeit sichtbar sein.
> Nach jedem Einsatz folgt eine vollständige Abrechnung mit Einnahmen, sämtlichen Kosten, tatsächlichem Gewinn, Bewertung, Erfahrung, Verbrauch, Fahrzeugzustand und Zielort.
> Ergänze außerdem Lagerbestände, Gründe für ungeeignete Fahrzeuge, eindeutige Fahrzeugstatus, Kaufbestätigungen, ein einfaches Kassenbuch, tägliche Fixkosten, Auftragshistorie, verständliche Ersthinweise sowie sichtbare Rückmeldungen bei Geldbewegungen.
> Die Informationen dürfen die Karte nicht überladen. Im normalen Zustand wird nur der erwartete Gewinn gezeigt; über „Details“ öffnet sich die vollständige Aufschlüsselung. Keine neue Hauptnavigation und kein fünfter Tab.
> Erst diesen vollständigen Spielablauf sauber machen, bevor Wetter, weitere Gebiete oder neue Fahrzeugklassen gebaut werden.

**Reihenfolge der Builds:** ~~(1.5) 5.2 / 5.3 / 5.4 einzeln~~ **ab 1.6: alles zusammen als 5.3 (Komplettüberarbeitung), keine Zwischenversion auf TestFlight, danach E2.** Ursprüngliche Aufteilung zur Nachvollziehbarkeit:
- **5.2:** Starttempo (5b Punkt 1) + Premium-UI und Modelltausch (UI-Vorgabe 000b).
- **5.3:** E1.6 komplett + aus E1.5 **Zielorte, Ladung auf dem Abschlepper, Hof-Grundumfang und die 5 Bestände** (5b Punkte 2–5), weil die Abrechnung Zielort und Verbrauch braucht.
- **5.4:** Rest von E1.5: 4 Entsorgungscontainer, Ausbau Lager/Reifencontainer/Recycling (5b Punkt 6 und Ausbaustufen aus Punkt 5).
- Danach erst E2. Wetter, neue Gebiete und neue Fahrzeugklassen warten, bis dieser Ablauf sauber ist.

**Umsetzung (Startwerte zum Testen):**

**1. Kalkulation vor der Zuteilung.**
```swift
struct JobEstimate: Codable {   // alle Werte in €, isEstimate = true
  var revenue: ClosedRange<Int>          // Einsatzlohn + Zielort-Erlös
  var fuel: Int                          // km hin + zum Ziel + zurück × Verbrauch × Literpreis
  var material: Int                      // Bestände × Einkaufspreis (Teil 5b)
  var staffShare: Int                    // Tageslohn / Schichtminuten × erwartete Minuten
  var wear: Int                          // km × Verschleißsatz der Fahrzeugklasse
  var possibleExtra: ClosedRange<Int>    // z. B. Wartezeit, zweites Material, Stau
  var expectedProfit: ClosedRange<Int>   // Spanne, nicht ein Punktwert
}
```
- Startsätze: Diesel 1,75 €/l; Servicewagen 9 l/100 km, Abschlepper 16 l/100 km; Verschleiß 0,08 €/km (Service) bzw. 0,15 €/km (Abschlepper).
- Im Panel 00b steht standardmäßig **nur** „Erwarteter Gewinn ca. 120–160 €“. „Details“ klappt die Aufschlüsselung aus. Alle Schätzwerte tragen „ca.“ und eine Spanne.
- Wechselt der Spieler Mitarbeiter oder Fahrzeug, rechnet die Schätzung sofort neu (Zahl animiert).

**2. Während des Einsatzes.** Antippen des Fahrzeugs oder des Einsatzes zeigt eine kompakte Karte: Status (eindeutig, Punkt 6), Restdauer („noch ca. 12 Min“), Zielort, Mehrkosten bisher (nur wenn > 0, orange), Probleme (z. B. „Kunde nicht vor Ort, +10 Min“), Verfügbarkeit („frei ab ca. 15:40“). Auf der Karte selbst bleibt nur die Plakette (UI 000a Punkt 5).

**3. Abrechnung nach jedem Einsatz.**
```swift
struct JobReport: Codable {
  let jobId: UUID; let finishedAt: GameTime; let destination: TowDestination?
  let revenue: [Line]; let costs: [Line]      // Line = (Bezeichnung, Betrag)
  let profit: Int; let stars: Int; let xp: Int
  let consumed: [Supply: Int]; let vehicleCondition: (before: Int, after: Int); let fuelUsed: Double
}
```
- Kosten-Zeilen: Kraftstoff, Material, Lohnanteil, Verschleiß, Zusatzkosten (mit Grund). Gewinn = Einnahmen − Kosten, **tatsächlich** (keine Spanne mehr).
- Standard: kleines Banner „Einsatz erledigt · +142 € Gewinn · ★★★★“ (3 s, antippbar). Antippen öffnet den vollständigen Bericht. Auto-Pause nicht nötig.
- Schätzung vs. Ergebnis: Im Bericht steht die Abweichung („2 € besser als geschätzt“), damit die Schätzung nachvollziehbar wird.

**4. Kassenbuch und Fixkosten.**
```swift
struct LedgerEntry: Codable { let time: GameTime; let text: String; let amount: Int; let category: LedgerCategory; let jobId: UUID? }
enum LedgerCategory: String, Codable { case job, destination, material, fuel, wages, fixed, purchase, upgrade, disposal, recycling, other }
```
- Jede Geldbewegung erzeugt einen Eintrag. Gespeichert werden die letzten 7 Spieltage voll, ältere als Tagessumme.
- **Tägliche Fixkosten** (abends gebucht, vorher in der Zentrale sichtbar): Löhne (Teil 7, ×3,6), Fahrzeugversicherung/Steuer 12 € je Fahrzeug, Gebäude 30 € (Zentrale Stufe 1, +20 € je Ausbaustufe). Die Tagesabrechnung zeigt Fixkosten als eigenen Block.
- Ort: Zentrale → Karte „Kasse“ (Saldo heute, Fixkosten heute, Einträge als Liste). Kein eigener Tab.

**5. Auftragshistorie.** Liste der erledigten Einsätze (neueste oben, letzte 7 Spieltage) mit Art-Symbol, Ort, Gewinn, Sternen; Antippen öffnet den gespeicherten `JobReport`. Ort: Zentrale → „Verlauf“ (oder über die Warteschlangen-Liste, Teil 13 Punkt 1, als zweiter Reiter „Erledigt“).

**6. Eindeutige Fahrzeugstatus.** Ein Status je Fahrzeug, immer genau einer, gleich benannt in Plakette, Flotte und Zuteilung:
`Frei · Zum Einsatz · Vor Ort · Aufladen · Zum Ziel · Abladen · Rückfahrt · Tanken · Wartung · Defekt · Außer Dienst (keine Schicht)`. Farben nach UI 000a Punkt 5 (Zum Ziel = orange mit Auto-Symbol, Tanken/Wartung = grau, Defekt = rot).

**7. Gründe für ungeeignete Fahrzeuge.** In der Zuteilung bleiben ungeeignete Fahrzeuge sichtbar, aber ausgegraut, mit einem Grund in einer Zeile: „Kein Abschlepper“, „Tank zu leer (8 %)“, „Zustand zu schlecht“, „Im Einsatz bis ca. 15:40“, „Keine Reifen im Lager“, „Fahrer hat keine Schicht“. Ungeeignete Mitarbeiter ebenso.

**8. Kaufbestätigungen.** Jeder Kauf und Ausbau über 0 € zeigt vorher eine kleine Bestätigung: Was, Preis, Nutzen, Kontostand danach („Kontostand danach: 1.240 €“). Ausnahme: automatische Nachbestellung (einmal in den Einstellungen bestätigt, erscheint im Kassenbuch).

**9. Rückmeldung bei Geldbewegungen.** Die Geldkapsel oben zählt animiert hoch/runter (`numericText`), dazu ein kurzes „+142 €“ (grün) bzw. „−300 €“ (Silber, nicht rot, außer der Kontostand geht ins Minus) neben der Kapsel. Haptik nach UI 000b Punkt 5. Mehrere Bewegungen in 1 s werden zusammengefasst.

**10. Ersthinweise.** Höchstens ein Hinweis gleichzeitig, als schmale Sprechblase am betroffenen Element, je Hinweis nur einmal: erster Einsatz („Tippe auf den Marker“), erste Zuteilung („Erwarteter Gewinn: Details zeigen die Kosten“), erster Einsatz unterwegs, erster Bericht, erste Zielwahl, erstes leeres Material, erste Fixkostenabrechnung. „Hinweise zurücksetzen“ in den Einstellungen. Keine Textwände, kein Tutorial-Zwang.

**11. Lagerbestände sichtbar.** Die Lager-Karte aus 5b Punkt 7 erscheint in 5.3; in der Zuteilung zeigt die Material-Zeile „Reifen: 1 von 6 im Lager“.

**12. Spielstand.** Schema 4 bekommt zusätzlich `ledger`, `jobHistory` (Reports), `hintsSeen`, `autoReorder`. Alles mit Standardwerten; alte Stände starten mit leerem Kassenbuch.

**Tests:** Schätzung liegt bei Einsätzen ohne Zwischenfall innerhalb der angezeigten Spanne; Summe des Kassenbuchs = Kontostandänderung (auf den Euro genau, über 3 Spieltage); jeder Kauf hat einen Eintrag; jedes Fahrzeug hat zu jedem Zeitpunkt genau einen Status; jeder ausgegraute Eintrag hat einen Grund.

**Screenshots:** Panel mit „Erwarteter Gewinn“ zu und mit „Details“ offen · Fahrzeugkarte während des Einsatzes · Banner nach dem Einsatz · vollständiger Bericht · Kasse mit Fixkosten · Verlauf · Zuteilung mit ausgegrautem Fahrzeug und Grund · Kaufbestätigung · Geldkapsel mit „+142 €“ · ein Ersthinweis.

**Nicht in E1.6:** neue Tabs oder Hauptnavigation, Statistiken mit Diagrammen (E10), Wetter (E2), neue Gebiete oder Fahrzeugklassen.

### 5d. Update 5.4 nach Julians Test von 5.3 (Julian 14.10.2026 15:57)

Julians Text steht wörtlich in `Komplettueberarbeitung-5.3.md` (Nachtrag 4). Der neuere Auftrag gilt und zieht vor: Gebiete mit Spielgeld (eigentlich E8), Premium-Gebiet (P1), Premium-Schwerlastfahrzeug, alle Pakete und die Weltprodukte. Regel bleibt: **Jedes Produkt im Shop braucht spielbaren Inhalt im Build**, und die kostenlose Hauptwelt bleibt ohne Kauf vollständig.

**1. Optik dunkler und abwechslungsreicher.** Standard-Licht Spätnachmittag/Abend statt Mittag; Boden und Dächer dunkler (Asphalt #2B2B2E bis #3A3A3F, Fassaden entsättigt in mehreren Tönen: Sandstein, Backstein, Putz grau/beige, Glas). Jedes Viertel mit eigenem Charakter (Altbau, Wohnsiedlung, Gewerbe, Hafen). Mehr Details: Bäume, Zäune, Laternen, Schilder (fiktiv). Weiterhin kein Gold, Farbe nur gedämpft.

**2. Geparkte Autos ordentlich.** Nur auf Parkbuchten, Stellplätzen und am Straßenrand, ausgerichtet an Fahrbahn bzw. Markierung, keine Überschneidung mit Gebäuden, Bäumen oder anderen Autos; Kollisionstest beim Platzieren.

**3. Jedes Fenster schließbar.** Jede Ansicht/jedes Sheet (auch Flotte, Personal, Zentrale-Karten) hat oben rechts ein ✕ (44 × 44 pt) und lässt sich nach unten wegwischen; Tippen auf den Tab „Karte“ schließt alles. Nie muss man „über einen anderen Tab raus“.

**4. Fahrzeugbefehle.** Fahrzeug antippen (Karte oder Flotte) → Befehlsleiste mit großen Knöpfen: **Tanken** (fährt zur Zapfstelle, Kosten vorher), **Warten/Reparieren** (fährt in die Halle, Dauer + Kosten vorher), **Zur Zentrale**, **Folgen** (Kamera), **Einsatz zuweisen** (nächster passender offener Auftrag). Nicht verfügbare Befehle ausgegraut mit Grund. Automatik als Einstellung: „Bei unter 20 % Tank automatisch tanken“ (Standard an).

**5. Betriebshof abgelegen und anklickbar.** Die Zentrale liegt **am Stadtrand** (nicht mittig) mit freier Fläche ringsum. Jedes Objekt auf dem Hof ist antippbar und zeigt sein eigenes kleines Panel: Halle (Wartung), Zapfstelle (Tanken, Preis), Lager (Bestände, Nachbestellen), Container (Füllstand, Abholen), Stellplätze (abgestellte Autos), Büro (Kasse/Verlauf), freie Bauflächen (Bauen). **Grundstück erweitern:** angrenzende Flächen sind sichtbar (Bauzaun-Markierung) und mit Spielgeld kaufbar, Startwerte 6.000 € / 12.000 € / 20.000 € je Erweiterung, jeweils +2 Bauflächen.

**6. Größere Welt mit Gebieten.** Karte deutlich größer, alle Gebiete von Anfang an sichtbar:
| Gebiet | Freischalten | Charakter |
|---|---|---|
| Innenstadt (Start) | frei | Verkehr, Falschparker, kurze Wege |
| Wohnviertel + Bahnhof | 15.000 € Spielgeld, Ruf 20 | Taxis, Pendler, Morgen-/Abendspitzen |
| Gewerbegebiet | 30.000 € Spielgeld, Ruf 35 | Lieferwagen, Transporter |
| Autobahnabschnitt | 45.000 € Spielgeld, Ruf 45 | lange Wege, dringende Einsätze |
| Industriehafen | 70.000 € Spielgeld, Ruf 55 | große Fahrzeuge |
| Land/Vororte | 90.000 € Spielgeld, Ruf 65 | wenige, weite Einsätze |
| **Flughafen- und Eventbezirk** | **Kauf 8,99 €** (`area.event`) | Premium-Gebiet nach Teil 2c (P1) |
| **Seeufer** | **Kauf 5,99 €** (`region.extra`) | Zusatzregion am See: Uferstraßen, Bootsanhänger, Ausflugsverkehr |
Gesperrte Gebiete leicht entsättigt mit Grenze; Antippen → Karte mit Preis, Voraussetzung, was es bringt, Knopf „Freischalten“ (Spielgeld) bzw. „Im Shop ansehen“ (Kauf). Spielgeld-Gebiete ersetzen die alte Viertel-Freischaltung (vorgezogen aus E8).

**7. Weltprodukte.**
- **Umland Ost** (`world.large`, 8,99 €): große neue Spielwelt mit eigener Firma ab Firmenstufe 1. Profil teilt sich Erfolge, Welten haben eigene Spielstände (Architektur R7, `world-<id>.json`). Weltwechsel über Zentrale → „Welten“.
- **Bergland mit Bergekran** (`world.special`, 11,99 €): eigene Welt Bergland (Passstraßen, Serpentinen, schwierige Bergungen) mit exklusivem Bergekran.
- **Designs:** Design Carbon 1,49 € (`design.carbon`), Design Nachtlicht 2,49 € (`design.night`). Nur Optik.
- Mindestumfang, damit der Kauf echten Inhalt liefert: Seeufer 1 Gebiet mit 3 eigenen Einsatzvarianten; jede Welt mindestens 4 Viertel, alle 7 Einsatzarten, eigener Betriebshof.
- Alle IDs vom Mac endgültig festgelegt (14.10.2026 16:15); Präfix `com.julian.vaultoria.`.

**8. Premium-Schwerlastfahrzeug in 5.4.** Mit dem Fahrzeug kommen Lkw-/Transporter-Bergungen, die nur ein Schwerlastfahrzeug annehmen kann; in der Hauptwelt sind sie ohne Kauf ab E15 mit dem normalen Schwerlastabschlepper erreichbar.

**9. Werbung und Werbung entfernen.** ⚠ Neuer gilt (Julian 14.10.2026 16:46): „Werbung entfernen“ kostet **6,99 €** statt 5,99 €, und die Werbung kommt **schon in 5.4** (Anbieter Google AdMob mit Einwilligungsdialog, Klick-Anleitung `AdMob-Anleitung.md`). Ersetzt „`noads` gesperrt bis ein Werbeanbieter eingebaut ist“ (Mac, 16:15). 5.4 enthält Google AdMob (SDK über Swift Package Manager) mit Einwilligungsdialog, ATT-Hinweis, SKAdNetwork-Einträgen und Interstitial bei der Tagesabrechnung nach den Regeln aus Teil 2c. `noads` ist in 5.4 kaufbar, Preis aus StoreKit. Die echten App- und Werbeeinheit-IDs trägt Julian nach `AdMob-Anleitung.md` ein; bis dahin Test-IDs.

**10. Abnahme:** Block „5.4“ in `Abnahme-Checkliste-5.3.md`.

## 6. Offen bei Julian

- Startwerte (Gebühren, Hofkosten, Freischaltkosten, 18 Minuten) nach den ersten Tests feinjustieren.

---

## 7. Abgleich mit dem echten Code (Mac, 14.10.2026, Stand Vaultoria 1.4)

Wo der Code abweicht, gilt der Code. So setze ich den Plan um:

| Plan | Code heute (Vaultoria/Tow/) | Umsetzung |
|---|---|---|
| `Mission`, `fleet`, `staff`, `economy.money` | `Job`, `vehicles`, `employees`, `TowState.money` | Die Code-Namen bleiben. Das Planmodell wird als Felder in `TowState` ergänzt, nicht umbenannt. Umbenennen würde jeden Spielstand brechen und bringt keinen sichtbaren Vorteil. |
| `schemaVersion` 1 → 2 | `TowState.version` ist schon **2** (große Stadt) | E1 führt **Schema 3** ein (Profil + Weltstand). Die Migration v2 → v3 übernimmt Geld, Fahrzeuge, Mitarbeiter, Ausbauten und Einsätze. |
| Datei `world-<id>.json` + `profile.json` | eine Datei `vaultoria-pannenhilfe.json` | E1: `profile.json` + `world-welt1-heimatstadt.json` in Application Support. Die alte Datei wird nach der Migration als `…-v2-backup.json` aufbewahrt. |
| Simulation in festen Spielminuten | `Tow.tick(dt:)` in 0,1-s-Schritten, Uhr in Sekunden | Fester Schritt = **1/10 Spielminute** (0,1125 s bei 1×). Ganze Spielminuten würden Fahrzeuge springen lassen. 2× und 4× rechnen 2 bzw. 4 Schritte pro Takt. Der Seed-Test vergleicht 1× und 4×. |
| Spieltag 18 Min, 06:00–22:00 | `dayLength = 300` s, 08:00–20:00 | `dayLength = 1080` s, Anzeige 06:00–22:00. Fahrzeug- und Arbeitszeiten bleiben in Echtzeit-Sekunden, die Fahrten fühlen sich also gleich an. |
| Wirtschaft pro Tag | Löhne 110–120 €/Tag bei 5-Min-Tag | Ein Tag ist jetzt 3,6× so lang, darum steigen auch die Tageslöhne um den Faktor 3,6 (rund 400 €). Sonst würde Geld zu schnell wachsen. Feinjustierung über den Bot-Test (3 Spieltage). |
| `unlockedStage` 0…18 | Viertel schalten heute über Ausbaustufen und 4 erledigte Einsätze frei | E1: `unlockedStage` = 0, `StageDefinition` angelegt, Verhalten unverändert. Die bisherige Viertel-Freischaltung wird in E8 in das Stufensystem überführt. Bis dahin bleibt sie, damit E1 „aussieht wie vorher“. |
| `WorldDefinition` | `enum City` (16 × 20, Viertel, Fluss, Bahn, Autobahn) als statische Konstanten | `WorldDefinition.welt1` verweist auf `City`. Eine zweite Welt bekommt später eine eigene Definition. |
| Auto-Pause bei dringendem Einsatz | Einsätze haben `urgent` | Auto-Pause, sobald ein neuer Einsatz mit `urgent` erscheint. Ein Countdown unter 2 Spielminuten pausiert erst ab E11. |
| Sonderentscheidung pausiert | `decision != nil` hält die Simulation an | bleibt; zusätzlich zeigt das Banner den Grund |
| Bestehende Entscheidung „Schaden größer als gemeldet“ | vorhanden | bleibt unverändert |
| Ausgänge [R3] | heute: Reparaturchance = Fähigkeit + Werkstatt-Stufe | E4 baut darauf auf: Wert-Anteil ≥ 80 %, Zufall ≤ 20 %. |

**Speicherorte:** Application Support/Vaultoria/profile.json und world-welt1-heimatstadt.json. Ein defekter Stand wird als `save-defekt-<Datum>.json` daneben gelegt.

**Hinweis zu Ausgängen:** Die Formel in Teil 1.3 (2) (Werte 100 %, Glück höchstens ±0,08) liegt innerhalb der Grenze aus Teil 7 (Zufall ≤ 20 %) und gilt für E4.
