# Vaultoria – Erweiterungsplan Pannenhilfe 1.2 (freigegeben, Umsetzung ab E1)

Stand 14.10.2026, 14:15 (**1.2: Teil 7 Abgleich mit dem Code vom Mac übernommen; wo der Code abweicht, gilt Teil 7. Spielstand der App: Vaultoria 1.4, Build 202610141306, auf TestFlight, mit Optik-Angleichung und Kenney-Stadt.** 1.1 13:45: **1.1: Julians 8 Änderungen eingearbeitet, betroffene Stellen mit [R1]–[R8] markiert. Freigegeben, zuerst nur E1.**). 1.0 vom 14.10.2026, 13:30. Grundlage: `Spielkonzept-Pannenhilfe.md`, `UI-Vorgabe-Pannenhilfe.md` (1.4). Das Kernspiel mit Draufsicht bleibt, nichts wird ersetzt. Gebaut wird Update für Update nach Teil 5. Die frühere „Später“-Liste (UI-Vorgabe Teil 13) geht in diesem Plan auf.

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
| **E1 Fundament** (siehe 5a) | Profil + Weltstand mit `worldId`, `schemaVersion` + Migration, Spieltag 18 Min, Simulation in festen Spielminuten, **Zeitsteuerung ⏸/1×/2×/4× mit Auto-Pause**, Freischaltsystem (nur Stufe 0), Seed-Tests | siehe 5a | siehe 5a |
| **E2 Wetter + Dauer** (Stufe 1) | Wetter, Verkehrsfaktoren, Dauerformel, A*-Route über Stau | Regen verlängert sichtbar Fahrt; Route weicht Stau aus; Anzeige stimmt mit tatsächlicher Dauer ±10 % | Karte bei Regen, Panel mit Ankunft/Arbeit, Umweg um Stau |
| **E3 Erfahrung** (Stufe 2) | XP, Stufen, Wertwahl alle 3 Stufen | Nach Einsätzen steigt XP in der genutzten Fähigkeit; Stufenkarte erscheint; Wert wirkt auf Dauer | Personal-Tab, Stufe-erreicht-Karte |
| **E4 Ausgänge** (Stufe 3) | Outcome-Würfel, „gute Chance/riskant“, Berichte | Alle 7 Ausgänge mit festem Seed auslösbar, Geld/Sterne korrekt | Panel mit Chance-Wort, 3 Berichte mit unterschiedlichem Ausgang |
| **E5 Ziele + Verlauf** (Stufe 4) | 3 aktive Ziele, Belohnungen, Verlauf in der Tagesabrechnung | Ziel erfüllen → Belohnung, neues Ziel; Verlauf zeigt 30 Tage | Zielkarten am Rand, Verlauf-Diagramme |
| **E6 Betriebshof** (Stufe 5) | Depot, Einlagern, Gebühren bis Herausgabeverlangen | Voller Hof blockiert Einlagern; Gebühren stoppen bei Herausgabeverlangen; Tagesabrechnung zeigt Gebühren | Hof auf der Karte, Zentrale-Karte Betriebshof, Liste |
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

### 5a. E1 genau (als Nächstes umsetzen, sonst nichts)

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
