# Vaultoria – Erweiterungsplan Pannenhilfe (Planung, noch nicht bauen)

Stand 14.10.2026, 13:30. Grundlage: `Spielkonzept-Pannenhilfe.md`, `UI-Vorgabe-Pannenhilfe.md` (1.4). Das Kernspiel mit Draufsicht bleibt, nichts wird ersetzt. Gebaut wird Update für Update nach Teil 5. Die frühere „Später“-Liste (UI-Vorgabe Teil 13) geht in diesem Plan auf.

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

## 0. Leitplanken

- **Die Karte bleibt die Mitte.** Jedes neue System zeigt sich zuerst auf der Karte (Marker, Fahrzeug, Gebäudeteil, Straßenabschnitt) und nur unterstützend in den vier vorhandenen Tabs **Karte · Flotte · Zentrale · Personal** oder im Einsatz-Panel (UI-Vorgabe 00b). **Kein fünfter Tab, keine neuen Hauptmenüs.**
- **Eine neue Funktion pro Freischaltstufe.** Was noch nicht freigeschaltet ist, ist unsichtbar (keine grauen Platzhalter, kein „Demnächst“).
- **Zahlen sind Startwerte** zum Ausbalancieren im Test. Der Mac gleicht Namen und Felder mit dem echten Swift-Code ab; bei Abweichung gilt der Code, dieser Plan wird angepasst.
- **Spielzeit:** 1 Spieltag ≈ 6 Minuten echte Zeit (bei normaler Geschwindigkeit). 50–100 Stunden ≈ 500–1.000 Spieltage. Fristen aus dem echten Recht werden im Spiel gestaucht (1 echter Monat = 7 Spieltage), die Reihenfolge der Schritte bleibt echt.

---

## 1. Architektur und Datenmodelle

### 1.1 Aufbau

```
GameState (ein Spielstand, Codable)
├── meta: SaveMeta            Version, Spieltag, Uhrzeit, Spielzeit gesamt
├── company: Company          Geld, Ruf, Ziele, freigeschaltete Stufen
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
  var gameDay: Int; var minuteOfDay: Int
  var totalPlaySeconds: Int
  var unlockedStage: Int      // 0…18, siehe Teil 2
}
```

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

**(2) Mehrere Ausgänge pro Einsatz**

```swift
enum Outcome: String, Codable { case fixedOnSite, towedToDepot, towedToPartner, needsSecondVehicle, customerLeft, aborted, partial }
struct MissionResult: Codable { var outcome: Outcome; var income: Int; var costs: Int; var stars: Int; var minutes: Int; var xp: [EmployeeID: Int] }
```
Ausgang wird bei Ankunft gewürfelt: Chance aus Mitarbeiterwert vs. Schwierigkeit, Ausrüstung, Wetter. Spieler sieht vorher nur ein Wort („gute Chance“ / „riskant“). Beispiel Batterie: vor Ort behoben 80 % · Batterie defekt → Abschleppen 15 % · Kunde weg 5 %.

**(3) Dringende Autobahn-Einsätze**

`Mission.priority: .normal | .urgent | .highway`. Autobahn = eigenes Gebiet (Teil 2, Stufe 8), kurzer Countdown, hohe Bezahlung, Bonus bei Ankunft unter Zielzeit, Sicherungsaufwand (Absicherung durch zweites Fahrzeug oder Polizei bringt mehr Sterne).

**(4) Mitarbeiterwerte und Erfahrung**

```swift
struct Employee: Codable {
  var id: EmployeeID; var name: String; var portrait: String
  var repair, towing, speed, reliability: Int  // 1…5, wie bisher
  var level: Int; var xp: Int                  // Stufe 1…10
  var licenses: Set<License>                   // .b, .c (Lkw), .ce, .crane
  var shiftMinutesLeft: Int; var wage: Int
  var trait: Trait?                            // höchstens eine: nachtfit, ruhig bei Stress, schnell aber grob …
}
```
Erfahrung pro Einsatz in der genutzten Fähigkeit; alle 3 Stufen +1 auf einen Wert nach Wahl des Spielers (eine Karte, ein Tipp). Führerscheine schalten Fahrzeuge frei (Lkw-Führerschein = Schulung im Tab Personal, kostet Geld und eine Schicht).

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
enum SizeClass: String, Codable { case car, van, truck, bus }   // Platzbedarf: car 1, van 2, truck 4, bus 4 Einheiten
struct Depot: Codable { var capacityUnits: Int; var level: Int; var stored: [StoredVehicle] }
struct StoredVehicle: Codable {
  var id: UUID; var size: SizeClass; var model: GenericModel; var plate: String?  // fiktive Kennzeichen
  var reason: StorageReason   // .breakdown, .accident, .policeSeizure, .privateTow, .unpaidRepair, .abandoned, .purchased
  var arrivedDay: Int; var expectedPickupDay: Int?
  var ownerStatus: OwnerStatus   // .unknown, .identified, .notified, .pickupRequested, .noResponse
  var feePerDay: Int; var feesAccrued: Int; var feesStopDay: Int?
  var legalCase: LegalCase?      // Teil 4
}
```
Betriebshof ist ein eigenes Gebäudeteil an der Zentrale (sichtbar wachsend, UI-Vorgabe Teil 12). Stufen: 6 → 12 → 20 → 32 → 48 Einheiten. Ist er voll, kann kein weiteres Fahrzeug eingelagert werden; Abschleppaufträge gehen dann nur noch zu Partnern.

**(11) Tägliche Standgebühren**

Startwerte pro Tag: Pkw 15 € · Transporter 20 € · Lkw/Bus 40 €. Gebühren laufen **bis zum Herausgabeverlangen des Halters** (siehe Teil 4, BGH V ZR 192/22). Danach laufen keine Gebühren mehr, auch wenn er das Fahrzeug erst später holt; der Platz bleibt aber belegt. Das macht volle Höfe zu einer echten Entscheidung.

**(12) Standzeiten und Platzbedarf**

| Grund | Pkw | Transporter | Lkw/Bus | Standzeit (Spieltage) |
|---|---|---|---|---|
| Panne, wartet auf Werkstatt | 1 | 2 | 4 | 1–3 |
| Unfall, wartet auf Gutachter/Versicherung | 1 | 2 | 4 | 3–10 |
| Polizeiliche Sicherstellung | 1 | 2 | 4 | 1–14, ca. 5 % nie abgeholt |
| Privat abgeschleppter Falschparker | 1 | 2 | — | 0–2 |
| Reparatur nicht bezahlt | 1 | 2 | 4 | bis Rechtsweg (Teil 4) |
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

## 2. Freischaltreihenfolge (erste Welt, ca. 50–100 Stunden)

Genau **eine neue Funktion pro Stufe**. Freischaltung zeigt eine einzige Karte: was neu ist, ein Satz, „Los geht’s“. Auslöser sind Geld, Ruf, erledigte Einsätze oder Spieltag; alle Bedingungen einer Stufe müssen erfüllt sein. Kosten werden erst beim Bestätigen abgezogen.

| Stufe | ca. Stunde | Auslöser | Neue Funktion | Punkt |
|---|---|---|---|---|
| 0 | 0 | Spielstart | Kernspiel (Version 1 mit den 8 Pflichtpunkten) | – |
| 1 | 1 | 15 Einsätze | **Wetter** auf der Karte, beeinflusst Fahrt und Arbeit | 1 |
| 2 | 2,5 | 30 Einsätze | **Erfahrung und Stufen** für Mitarbeiter | 4 |
| 3 | 4 | Ruf 20 | **Mehrere Ausgänge** (Abschleppen statt Reparatur, Kunde weg …) | 2 |
| 4 | 6 | Spieltag 50 | **Unternehmensziele** (immer 3 aktiv) | 9 |
| 5 | 8 | 60 Einsätze, 8.000 € | **Betriebshof** mit 6 Einheiten und **Standgebühren** | 10, 11 |
| 6 | 11 | Ruf 30 | **Standzeiten und Platzbedarf** (Pkw/Transporter unterscheiden) | 12 |
| 7 | 14 | 15.000 € | **Gebiet Wohnviertel + Bahnhof** | 7 |
| 8 | 17 | Ruf 35, 120 Einsätze | **Vertrag Werkstatt** | 8 |
| 9 | 21 | 25.000 € | **Bergefahrzeug** + Bergungseinsätze | 5 |
| 10 | 25 | Ruf 45 | **Gebiet Autobahn** + dringende Autobahn-Einsätze | 3, 7 |
| 11 | 30 | Betriebshof Stufe 2 | **Kaufangebote** von Haltern für abgestellte Fahrzeuge + **Sammlung** (Behalten/Verkaufen) | 13, 14 |
| 12 | 35 | Ruf 50 | **Vertrag Polizei** (Sicherstellung, Verwahrung, Absicherung) | 8 |
| 13 | 41 | Werkstatt Stufe 2 | **Restaurieren** in der Sammlung | 14 |
| 14 | 48 | 60.000 €, Lkw-Führerschein bei einem Mitarbeiter | **Schwerlastabschlepper** + **Lkw-Einsätze**, Gebiet Gewerbegebiet | 5, 6, 7 |
| 15 | 55 | Ruf 60 | **Vertrag Automobilclub** | 8 |
| 16 | 63 | 300 Einsätze | **Öffentliche Versteigerungen** (Pfandverkauf eigener Forderungen, Behördenauktionen) | 13 |
| 17 | 72 | 120.000 € | **Kranwagen** + **Bus-Einsätze**, Gebiet Industriehafen | 5, 6, 7 |
| 18 | 82 | Ruf 75, alle Verträge Stufe 2 | **Großunfälle** (mehrere Teilaufträge) + Gebiet Land/Vororte | 6, 7 |
| Ziel | 90–100 | Ruf 90, alle Gebiete | Endziel der ersten Welt: „Größte Pannenhilfe der Region“ mit großer Autobahnbergung als Abschluss-Einsatz | – |

**Ausführliche Statistik** (Punkt 9) kommt ohne eigene Stufe mit Stufe 4 als Knopf „Verlauf“ in der Tagesabrechnung, weil sie nichts Neues zu bedienen verlangt.

Bremse für den Einstieg: In den ersten 2 Stunden gibt es nie mehr als 4 gleichzeitige Einsätze und kein Wetter schlimmer als Regen.

---

## 3. UI-Ablauf (keine neue Menüstruktur)

| System | Auf der Karte | Im Panel / Tab |
|---|---|---|
| Einsatzdauer | Route, Ankunftszeit an der Plakette | Panel 00b: „Ankunft 3:10 · Arbeit ca. 6 Min“ |
| Wetter | Regen-/Schnee-/Nebel-Effekt über der ganzen Karte, Glatteis-Straßen glänzen | kleines Wettersymbol in der Kopfleiste neben Geld |
| Ausgänge | Ergebnis-Symbol am Marker (Haken, Haken + Haken-Symbol für Abschleppen, X) | Einsatzbericht nennt den Ausgang in einem Satz |
| Autobahn-Einsätze | rote Marker mit blinkendem Rand auf der Autobahn, Sirene-Ton | Panel 00b mit „Dringend“-Kapsel und Zielzeit |
| Mitarbeiter-Erfahrung | Stufen-Zahl auf der Fahrzeugplakette | Tab **Personal**: Karte pro Person mit 4 Werten, Stufe, Erfahrungsleiste, Führerscheine; „Stufe erreicht“-Karte |
| Fahrzeugklassen | eigene 3D-Modelle, gelb-schwarz | Tab **Flotte**: Karten nach Klasse, Kauf bei freiem Stellplatz |
| Lkw/Bus/Großunfall | großer Marker mit Zähler „0/4“, mehrere Routen gleichzeitig | Panel 00b zeigt Teilaufträge als Reihe kleiner Karten, je ein Fahrzeug zuteilen |
| Gebiete | gesperrt = abgedunkelt mit Schild; Freischalten = Kamera fährt hin, Lichter gehen an | Antippen des Schilds: Kosten, Ruf, Knopf „Freischalten“ |
| Verträge | Partnergebäude auf der Karte (Werkstatt, Polizeiwache, Club-Station) mit Logo-Schild in Gold; Vertragsaufträge mit kleinem Partnersymbol am Marker | Antippen des Partnergebäudes: Vertrag, Pünktlichkeit, Verlängern |
| Ruf | — | Stern-Kapsel in der Kopfleiste zeigt Ø Sterne; Antippen: Ruf 0–100 als Leiste + was der nächste Ruf freischaltet |
| Ziele | — | 3 kleine Zielkarten, einklappbar am rechten Kartenrand |
| Statistik | — | Tagesabrechnung → „Verlauf“ |
| Betriebshof | eigenes Gebäudeteil, abgestellte Fahrzeuge stehen sichtbar auf dem Hof | Tab **Zentrale**: Karte „Betriebshof“ (wie Garage/Werkstatt/Leitstelle) mit Belegung „14/20“, Liste der Fahrzeuge mit Grund, Tagen, Gebühren, Status |
| Standgebühren | Münz-Symbol über lange stehenden Fahrzeugen | Tagesabrechnung: Zeile „Standgebühren“ |
| Kaufangebote/Auktionen | Hammer-Symbol über dem betroffenen Fahrzeug im Hof | Antippen: Angebot mit Preis, Zustand, Rechtsgrund in einem Satz, „Kaufen“ bzw. „Bieten“ |
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

| Fall | Schritte im Spiel (Fristen gestaucht: 1 Monat = 7 Spieltage) | Was der Spieler tun kann |
|---|---|---|
| **A Panne/Unfall, Halter bekannt** | Gebühren laufen → Halter meldet sich (Herausgabeverlangen, Gebühren stoppen) → Abholung | Warten. Manchmal **Kaufangebot**: Halter bietet das Fahrzeug an (Reparatur lohnt sich nicht) → Kaufen oder Ablehnen |
| **B Reparatur nicht bezahlt** | Forderung offen → 1) Halter ermitteln (§ 39 StVG, kleine Gebühr, 1 Tag) → 2) Mahnung, 3 Tage → 3) **Verkauf androhen** mit Betrag → 4) **7 Spieltage Wartefrist** → 5) **öffentliche Versteigerung** durch Versteigerer (Gebühr) → Erlös: Forderung an Spieler, Rest „an den Eigentümer“ (im Bericht ausgewiesen) | Jeden Schritt per Knopf anstoßen; bei der Versteigerung **mitbieten** wie jeder andere Bieter; Halter kann bis zur Versteigerung zahlen und abholen |
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

Plan-Nummern E1–E19. Die echte Versionsnummer und Build-Nummer vergibt der Mac. Jedes Update: kompiliert, alte Spielstände laden (Migrationstest), TestFlight-Build, Screenshots als ZIP.

| Update | Inhalt | Abnahme | Screenshots |
|---|---|---|---|
| **E1 Fundament** | `schemaVersion`, Migration, Simulationstakt, Freischaltstufen-System (Stufe 0), Seed-Tests; nichts Neues sichtbar | Alter Spielstand lädt, neuer Stand speichert v2; defekter Stand → sauberer Neustart; Spiel sieht aus wie vorher | Karte unverändert, Freischalt-Testkarte |
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
| **E19 Großunfälle + Land** (Stufe 18) | SubTasks, Großunfall-Marker, Gebiet Land/Vororte, Endziel | 4 Teilaufträge parallel, Bezahlung am Ende; Endziel-Einsatz | Großunfall mit 4 Routen, Endziel-Karte |

Reihenfolge ist verbindlich, Inhalte eines Updates werden nicht vorgezogen. Nach jedem Update: TestFlight, Screenshots, Julian testet, dann das nächste.

---

## 6. Offen bei Julian

- Ob die Spielzeit-Stauchung (1 Monat = 7 Spieltage) so passt.
- Startwerte für Gebühren und Freischaltkosten nach dem ersten Test.
