# Vaultoria – UI-Vorgabe (verbindlich)

> Spielregeln und Systeme stehen in `Spielkonzept.md` (Stand Julian 13.10. 13:06). Bei Widerspruch gilt der neuere Stand.

Quelle: Julian, 13.10.2026 12:40, 12:48 und 12:50, fünf Bilder in diesem Ordner (20 Ansichten + Icons/Start):
- `ui-vorgabe-ansichten.png` (4 Spielansichten im Hochformat, 2×2)
- `icons-und-start.png` (3 Icon-Entwürfe + Startbildschirm)
- `ui-vorgabe-shop.png` (Shop, Ausbau mit Spielgeld, Rebirth-Shop, Bonus & Schutz – siehe Teil 2)
- `ui-vorgabe-raubzug.png` (Raubzug-Ablauf, 6 Ansichten – Teil 3)
- `ui-vorgabe-betrieb.png` (Betrieb mit Tab-Leiste, 6 Ansichten – Teil 4)

Offene Entscheidungen stehen ganz am Ende.

Die Bilder sind KI-Konzeptbilder. Sie legen Aufbau, Stimmung, Farben, Texte und Anordnung fest. Die Spielwelt selbst wird echt in 3D gebaut und animiert, die Bilder sind keine Assets und kommen nicht ins Spiel oder in den Store.

## Julians Text zum Ablauf (wörtlich)

> die ui soll genau so aussehen. Genau, so halten wir es fest:
> - 2,5D-Gebäudeübersicht: Du siehst deinen gesamten Betrieb.
> - Bereich antippen: Die Kamera wechselt in eine nähere Ansicht – etwa Handel, Tierpension oder Tresorraum.
> - Lebendiger Betrieb: Kunden laufen hinein, warten und gehen zur Theke. Mitarbeiter transportieren Waren und betreuen Tiere; Hunde spielen und ruhen.
> - Auch in der Detailansicht bewegen sich die Figuren: Kunden zeigen Gegenstände, reagieren auf Angebote und verlassen nach dem Geschäft den Laden.
>
> Die Ansichten sind echte animierte Spielszenen. Die Oberfläche liegt darüber; zurück geht es jederzeit zur Gebäudeübersicht.

Daraus folgt:
- Hauptansicht = **Ausbau-/Gebäudeübersicht** (Gebäude im Schnitt, alle Etagen sichtbar, schräg von oben, 2,5D-Wirkung, Kamera fest).
- Antippen einer Etage/eines Bereichs → **Kamerafahrt** (weich, ca. 0,5–0,8 s) in die Nahansicht dieses Bereichs. Die 3D-Szene läuft dabei weiter.
- In jeder Nahansicht oben links ein Weg **zurück zur Gebäudeübersicht** (Zurück-Knopf oder Wischgeste; immer möglich).
- UI-Elemente sind **Overlays über der laufenden 3D-Szene**, nie ein Vollbild-Menü, das die Szene ersetzt (Ausnahme: „Umziehen & neu starten“, siehe unten, liegt als dichte Karte über abgedunkelter Szene).

---

## Stil allgemein

**Look:** warm, hochwertig, „Antiquitätenladen trifft Bank“. Holz, warmes Lampenlicht, Pflanzen, Dunkelgrün mit Gold. Warme Abendstimmung. Figurenstil: siehe „Offener Punkt: Figurenstil“ am Ende.

**Farben (aus den Bildern gemessen, gerundet):**

| Rolle | Hex | Verwendung |
|---|---|---|
| Leiste/Panel dunkel | `#171E20` – `#1D2427` | Obere Leiste, dunkle Karten (Gegenstand, Hund, Upgrade, Besitz), leicht transparent (ca. 90 %) |
| Panel-Rand | `#2E3438` | 1 px Rand an dunklen Karten |
| Creme-Karte | `#F7F1E8` | Verhandlungskarte, Voraussetzungen, Standortkarten |
| Creme dunkler | `#EBDBC5` | Belohnungs-Kachel in Creme-Karte |
| Hauptknopf Grün | Verlauf `#3D7545` → `#235E35`, Rand `#4E8A55` | „Angebot machen“, „Upgrade“, „Ausbauen“, „Neustart bestätigen“, „Spielen“ |
| Abbrechen Rot | Verlauf `#8A4032` → `#6E2F25` | „Ablehnen“ |
| Fortschritt Grün | `#78C56F` | XP-Balken, Stufenbalken, Zustand „Gut“ |
| Gold | `#C9A45C` (Münze `#BD8337`, Stern `#CE913A`, Icon-Gold `#E9BE4A`) | Münze, Stern, Rahmen/Hervorhebung, Logo |
| Grün Icon-Hintergrund | `#1E3A2E` – `#162C26` | App-Icon, Startbildschirm-Knöpfe |
| Warnung Rot | `#9C2518` | Engpass-Schild „Personal fehlt“ |
| Rot hell (Karte) | `#E9B9A9`, Titel `#AB4539` | „Wird zurückgesetzt“ |
| Grün hell (Karte) | `#B7CAAD`, Stern `#2F6B3A` | „Bleibt“ |
| Text hell | `#FFFFFF` / `#D7D7DB` | auf dunklen Panels |
| Text dunkel | `#1C1C1E` / `#3A3A40` | auf Creme |

**Schrift:** SF Pro (System). Titel Bereich: groß, fett, Versalien bei „HANDEL / TIERPENSION / AUSBAU“ (ca. 28 pt), Untertitel normal ca. 15 pt. Leiste ca. 17 pt halbfett. Beträge fett, mit Tausenderpunkt und „ €“ (12.460 €). Startbildschirm-Logo: Serifen-Versalien in Goldprägung (eigenes Schriftbild, z. B. als Bild-Asset).

**Formen:** Ecken 12–16 pt bei Karten, 10–12 pt bei Knöpfen. Knöpfe mindestens 50 pt hoch, volle Kartenbreite. Icons: SF Symbols in Creme/Weiß, in Bereichs-Titeln in einer dunklen Kachel (ca. 56×56 pt).

**Abstände:** Außenrand 12 pt zum Bildschirmrand, Karten 8–12 pt auseinander.

---

## Feste obere Leiste (in allen Spielansichten gleich)

Eine durchgehende dunkle Leiste (Panel dunkel), volle Breite, ca. 52 pt hoch, unter der Dynamic Island:

1. Links **„VAULTORIA“** (Versalien, halbfett, weiß).
2. Daneben **„Lv. 28“** klein über einem **XP-Balken** (grün auf dunklem Grund, ca. 120 pt breit).
3. Rechts in eigener dunkler Kapsel: **Goldmünze + Geldstand** („12.460 €“).
4. Eigene Kapsel: **Goldstern + Ansehen** („420“).
5. Ganz rechts quadratischer Knopf mit **Zahnrad** (Einstellungen).

Darunter links der **Bereichs-Kopf**: dunkle Kachel mit Icon + großer Titel + Untertitel, halbtransparent über der Szene.

---

## Ansicht 1: HANDEL (Nahansicht An- und Verkauf)

Szene: Ladeninneres mit Holzregalen (Uhren, Gitarren, Bilder, Lampen, Pflanzen), Theke im Vordergrund. Kunde (junger Mann, grüne Jacke) steht vor der Theke und hält den Gegenstand hoch. Betreiber-Figur von hinten links angeschnitten. Wandschild „GUTE DINGE NEUE GESCHICHTEN“ mit kleiner Krone.

Overlays:
- **Kopf:** Icon Handschlag · „HANDEL“ · „Kaufen · Verkaufen · Verhandeln“.
- **Gegenstandskarte** (dunkel, rechts, ca. 50 % Breite): Titel „Gebrauchte Kamera“, darunter Modell „LUMEN S-100“ (erfundene Marke, keine echten Marken). Produktbild. Tabelle mit Trennlinien:
  - Zustand → **Gut** (grün)
  - Marktwert → 320 €
  - Unser Wert → ca. 220 €
- **Verhandlungskarte** (Creme, rechts unter der Gegenstandskarte, etwas breiter):
  - „Forderung:“ links, **„240 €“** groß fett rechts.
  - Kunden-Porträt (klein, rund-eckig) + Sprechblase „Mein letzter Preis.“
  - „Dein Angebot:“ Trennlinie, darunter **„180 €“** zentriert, groß.
  - Schieberegler (grün gefüllt) mit **„–“** links und **„+“** rechts (dunkle quadratische Knöpfe).
  - Grüner Knopf mit Handschlag-Icon **„Angebot machen“**.
  - Roter Knopf mit X **„Ablehnen“**.
- **Besitz-Leiste** (dunkel, unten, volle Breite): Kopf „Dein Besitz (Ladenbestand)“ mit kleiner Goldmünze. 5 quadratische Kacheln nebeneinander, je Bild + Preis: Armbanduhr 450 €, Goldring 320 €, Kamera 220 €, Spielkonsole 180 €, Gitarre 650 €. Waagerecht scrollbar, wenn mehr.

Verhalten: Kunde reagiert sichtbar auf Angebot (nickt, schüttelt Kopf, Gegenangebot erscheint in Sprechblase, geht bei Ablehnung).

---

## Ansicht 2: TIERPENSION (Nahansicht Haustierpension)

Szene: heller Raum mit Hundebetten (grüne Polster), Regal mit Decken/Körben, Bild eines Hundes, Schild „Hier sind Freunde zuhause ♡“. Durch große Öffnung ein umzäunter Außenauslauf mit Rasen, Rampe, Besitzern, die Hunde bringen/abholen. Pflegerin in grünem Polo füttert einen Golden Retriever, weitere Hunde liegen/spielen.

Overlays:
- **Kopf:** Icon Pfote · „TIERPENSION“ · „Liebevolle Betreuung für glückliche Tiere“.
- **Kapazitäts-Kapsel** rechts oben (Creme): Pfote + **„3 / 4 Plätze“**.
- **Hundekarte** (dunkel, links-mittig): Pfeile ‹ › zum Blättern, Porträt, Name **„Bello“**, Rasse „Golden Retriever“, zwei grüne Status-Chips „Zufrieden“ (Stern) und „Frisst gut“ (Herz).
- **Upgrade-Karte** (dunkel, rechts daneben): „Betreuung · Stufe 12 / 100“ + grüner Balken. Liste mit kleinen Gold-Icons: „+1 Platz“, „Schnellere Betreuung“, „Höhere Zufriedenheit“. Grüner Knopf mit Pfeil nach oben **„Upgrade: 1.200 €“**.
- **Platz-Leiste** (dunkel, unten): 4 Kacheln: Bello „Groß“ (ausgewählt, Goldrand), Luna „Mittel“, Max „Klein“, gesperrter Platz mit Schloss „Platz sperrt bei Stufe 20“ (Text besser: „Platz frei ab Stufe 20“).

---

## Ansicht 3: AUSBAU (Gebäudeübersicht, Hauptansicht)

Szene: Gebäude im Schnitt, schräg von oben, Etagen übereinander, vorne Straße mit Parkplätzen. Von oben nach unten:
- Oben: gestrichelter Umriss **„Nächste Etage (noch nicht verfügbar)“** mit „+“ (noch nicht kaufbare Etage).
- Etage: **Tierpension** (Hunde, Pflegerin, Betten).
- Etage: **Wertlager** (Regale mit Kisten, großer Tresor rechts, Mitarbeiter) – **ausgewählt**, mit leuchtendem Goldrahmen um die ganze Etage.
- Erdgeschoss: **Laden** (Theke, Kunden in Schlange) mit rotem Schild **„Personal fehlt“** (Engpass).
- Vorne: Parkplatz mit 2 Autos und 2 leeren Feldern, Text **„2 / 4 Parkplätze belegt“**.

Overlays:
- **Kopf:** Icon Hammer · „AUSBAU“ · „Dein Geschäft. Schritt für Schritt.“
- Links an jeder Etage ein **Etagen-Schild** (dunkel, Icon + Name + Stufe): Tierpension Stufe 12 · Wertlager Stufe 24 (ausgewählt, Goldrand) · Laden Stufe 18. Antippen = Etage auswählen; zweites Antippen bzw. Antippen in die Etage = Kamerafahrt in die Nahansicht.
- **Detailkarte unten** (dunkel, volle Breite): links Vorschaubild der Etage, rechts „Wertlager · Stufe 24 / 100“ + grüner Balken, Liste mit Gold-Icons: „Mehr Kapazität für wertvolle Gegenstände“, „Höhere Sicherheit“, „Schnellere Einlagerung“. Grüner Knopf **„Ausbauen: 2.400 €“** mit Pfeil nach oben.

Engpässe erscheinen als rote Schilder direkt an der betroffenen Etage in der Szene.

---

## Ansicht 4: UMZIEHEN & NEU STARTEN (Rebirth)

Über abgedunkelter Szene, dichtes Layout:
- **Kopf:** Icon Ortsmarke · „Umziehen & neu starten“ · „Größerer Standort. Mehr Möglichkeiten.“
- **Zwei Standortkarten** nebeneinander (Creme oben mit Bild, unten dunkel transparent), Pfeil → dazwischen:
  - Links „Aktueller Standort“ · „Kleiner Laden“ · „Vorstadt“, kleines 2-stöckiges Haus mit grünen Markisen. Werte: 3 Etagen · 4 Parkplätze · Kleines Einzugsgebiet.
  - Rechts „Neuer Standort (Vorschau)“ · „Geschäftshaus“ · „Stadtzentrum“, großes Altbau-Eckhaus. Werte: 4 Etagen · 8 Parkplätze · Großes Einzugsgebiet.
- **Voraussetzungen-Karte** (Creme): Titel „Voraussetzungen für den Neustart“, Liste mit grünen Haken: Etagen vollständig (3 / 3) · Upgrades vollständig · Ansehen erreicht (500 / 500) · Geldziel erreicht (25.000 / 25.000 €) · Keine offenen Kredite. Rechts Kachel „Belohnung:“ Goldmünze mit Stern, **„+12“** groß, „Rebirth-Coins“. Nicht erfüllte Punkte: graues leeres Kästchen statt Haken, Knopf dann deaktiviert.
- **Zwei Infokarten** nebeneinander:
  - Rot hell: Kreispfeil-Icon, Titel **„Wird zurückgesetzt:“** (rot), Liste: Betrieb & Spielgeld · Gebäude und Upgrades · Laufende Aufträge · Mitarbeiter.
  - Grün hell: grüner Stern, Titel **„Bleibt:“**, Liste: Dauerhafte Boni · Freigeschaltete Designs · Erfolge · Rebirth-Coins.
- **Knopfzeile:** links dunkler Rahmen-Knopf „‹ Zurück“, rechts großer grüner Knopf mit Raketen-Icon **„Neustart bestätigen“**.

Hinweis Logik: „Keine offenen Kredite“ = keine laufenden Pfandkredite UND keine Betreiberkredite.

---

## Startbildschirm

- Vollbild-Szene: das Gebäude des aktuellen Standorts als 3D-Schnittansicht in Abendstimmung (oben Tierpension mit Hund im Körbchen, Mitte Wertlager mit Tresor, unten Laden mit Betreiber und Kunde an der Theke), rechts Hundehütte mit Hund im umzäunten Garten, links Auto auf Parkplatz, im Hintergrund Altstadt mit Kirchturm. Szene leicht animiert.
- Oben mittig Logo **„VAULTORIA“** in Gold-Serifen-Versalien mit dunkler Kontur, darüber kleines Dach-Giebel-Element mit Pfote.
- Darunter Claim **„Dein Geschäft. Dein Imperium.“** (weiß, Serife, klein).
- Unten großer dunkelgrüner Knopf mit dünnem Goldrand **„Spielen“** (Serife), rechts daneben quadratischer Knopf gleicher Art mit Zahnrad.

## App-Icon: GEWÄHLT „Goldenes V“ (Julian, 13.10.2026 12:41)

Gewählt ist Entwurf 2: goldenes, genietetes „V“ mit rundem Schlüsselloch-Beschlag in der Mitte auf dunkelgrünem, leicht strukturiertem Grund (`#1E3A2E`). Ausgeschnitten als `icon-goldenes-v.png` (1024×1024, randlos, Ecken rundet iOS selbst). Achtung: hochskaliert aus dem Konzeptbild (Ursprung ca. 320 px). Für den Store-Build das Icon in voller Auflösung neu erzeugen oder nachzeichnen, Motiv und Farben gleich lassen. Auch als Logo auf der Webseite.

### Alle Entwürfe zur Einordnung

Alle auf dunkelgrünem Grund, Gold, abgerundetes Quadrat:
1. **Ladenfront mit Tresortür:** Geschäft mit grüner Markise, riesige goldene Tresortür mit Rad als Eingang, Pfote im Giebel, Aufsteller mit Pfote, Pflanzen.
2. **Gold-„V“ mit Schlüsselloch:** großes genietetes Gold-V, in der Mitte ein runder Schlüsselloch-Beschlag. Flach, gut lesbar auch klein.
3. **Eckhaus mit Tresor und Hund:** 2-stöckiges Haus mit Laden, Tresortür, Hund davor, Laternen.

Entwurf 1 und 3 sind verworfen.

---

## Abgleich mit dem Spielauftrag

- Passt: dunkles Grün/Gold, große Touchflächen, Geld/Ansehen/Engpässe sichtbar, Etagenwechsel, Stufen x / 100, Kosten und Nutzen vor dem Kauf, Rebirth mit Voraussetzungen.
- Ergänzt gegenüber dem ersten Auftrag: **Ansehen (Stern)** als zweite Währung im Kopf, **Rebirth-Coins** als Belohnung, **freigeschaltete Designs** bleiben.
- Wertlager-Nahansicht und Pfand-Ansicht sind in den Bildern nicht gezeichnet: im gleichen Muster bauen (Kopf + Szene + dunkle Detailkarte + grüner Knopf; Pfand mit Creme-Karte wie die Verhandlung: Beleihungsbetrag, Rückzahlung, Frist, Knöpfe „Kredit geben“ / „Ablehnen“). Eingelagerte Kundenware klar markiert („Kundeneigentum“, Schloss-Symbol), verpfändete Ware mit Frist-Chip.
- Keine echten Markennamen auf Gegenständen (deshalb „LUMEN S-100“).

---

# Teil 2: Shop, Ausbau mit Spielgeld, Rebirth-Shop, Bonus & Schutz

Quelle: Julian, 13.10.2026 12:48 („das auch“), Bild `ui-vorgabe-shop.png` (2×2, Hochformat). Ebenfalls verbindlich, ebenfalls KI-Konzeptbild (keine Assets).

## Gemeinsames Muster dieser Menü-Ansichten

Diese vier Ansichten sind **Menüs** (Vollbild-Sheet über abgedunkelter Szene), keine Spielszenen:
- **Kopfbild** oben (ca. 30 % Höhe): warme Ladenszene mit einer **Gastgeber-Figur** pro Menü (Shop: Verkäuferin mit grüner Latzschürze + Golden Retriever; Ausbau: Handwerker mit grüner Kappe, Latzhose und Klemmbrett, grüner Pickup mit Pfote und Hunden; Rebirth: älterer Herr mit Brille, Weste, Fliege + graue Katze; Bonus: Hund und Katze auf der Theke). Im Hintergrund ein Kreidetafel-Schild mit Spruch (siehe je Ansicht). Im Spiel als 3D-Figur in der Szene oder als gerendertes Standbild aus dem eigenen 3D-Material, kein KI-Bild.
- **Titel** links oben in Gold-Serifen-Versalien mit Icon davor, Form „BEREICH · UNTERTITEL“.
- **Währungs-Kapsel** rechts oben (dunkel, halbtransparent): Münze + Betrag groß, darunter Name klein.
- **Karten**: Creme (`#F2E6D2` bis `#F7F1E8`) mit dünnem Goldrand, Titel in dunkler Serife zentriert, Bild/Icon, Nutzen-Liste, unten Knopf über volle Kartenbreite.
- **Hintergrund** zwischen den Karten: warmes dunkles Holzbraun (`#3A2A1C` bis `#5A4230`).
- **Kaufknopf Spielgeld/Coins** zweiteilig: obere Hälfte grün mit Münze + Preis groß, untere Hälfte grün „Kaufen“. **Kaufknopf Echtgeld**: einteilig grün, nur Preis (z. B. „6,99 €“).
- **Deaktiviert**: beide Hälften hellgrau (`#C9C4BC` / Text `#6E6A63`), Text **„Zu wenig Spielgeld“** (bzw. „Zu wenig Rebirth-Coins“). Nur wenn Guthaben < Preis. (Im Bild ist „Tresor verbessern 4.000“ trotz 18.320 grau – das ist nur zur Darstellung des Zustands.)
- **Rebirth-Coins** haben eine eigene Farbe: **Violett** (`#5B2D86` Münze/Banner, Text `#B98BE6`) mit Gold. Nur für Rebirth-Coins verwenden.
- **Level-Punkte**: Reihe kleiner Kreise, gefüllt = erreichte Stufen (Violett), leer = grau; davor „Level 2/10“. Bei 10 Stufen 5 Punkte, je Punkt 2 Stufen (oder 10 kleine Punkte).

## Ansicht 5: VAULTORIA · SHOP

- Titel: Wappen mit Pfote + **„VAULTORIA · SHOP“**. Schild hinten: „ANKAUF · VERKAUF · PFOTE MIT HERZ“ + Pfote.
- **Drei Reiter** (Segment, volle Breite, über den Karten): **Echtgeld** (aktiv: grün mit Goldrand) · **Spielgeld** · **Rebirth-Coins** (inaktiv: fast schwarz-grün `#1A1F1C`, Text weiß). Reiter Spielgeld → Ansicht 6, Reiter Rebirth-Coins → Ansicht 7.
- Reiter Echtgeld, **drei Karten** nebeneinander (auf schmalen iPhones 3 Spalten bleiben, Text klein, Karten hoch):
  1. **Werbefrei** – Symbol durchgestrichenes „AD“ (rot). Text: „Keine Pflichtanzeigen. Belohnungsvideos bleiben freiwillig.“ Chip **„Einmalkauf“** (gold-braun). Knopf **„6,99 €“** (Julian 13.10. 13:07; Bild zeigt noch 4,99 €; Preis kommt aus StoreKit).
  2. **Starterpaket** – Bild Ladenschild mit Pfote und Schriftzug + Goldmünzen. Liste: „Exklusives Shopschild (kosmetisch)“, **„5.000 Spielgeld“** (fett). Knopf **„2,99 €“**.
  3. **Gebäude-Design** – Bild elegante Altbau-Ladenfront mit Schild „VAULTORIA“. Text: „Elegantes Design für dein Pfandhaus (kosmetisch).“ Knopf **„3,99 €“**.
- Darunter dunkler Knopf volle Breite: Kreispfeil-Icon **„Käufe wiederherstellen“** (Pflicht laut Apple).
- Preise immer aus StoreKit laden (lokalisiert), nie fest im Code. Gekaufte Einmalkäufe zeigen statt Preis „Gekauft“ (deaktiviert, Haken).

## Ansicht 6: AUSBAU · SPIELGELD

- Titel: gekreuzte Hämmer + **„AUSBAU · SPIELGELD“**. Kapsel rechts: Münze **„18.320“ / „Spielgeld“**. Schild hinten: „GRÖSSER · BESSER · MEHR TIERE · GLÜCKLICHER“.
- **2×2 Karten**, je Titel, Bild, zwei grüne Haken-Zeilen, zweiteiliger Knopf:
  1. **Verkäufer einstellen** – „Bedient mehr Kunden“, „Schnellerer Verkauf“ – **2.000** · Kaufen.
  2. **Parkplatz erweitern** – „+2 Parkplätze“, „Mehr Kunden gleichzeitig“ – **3.500** · Kaufen.
  3. **Tresor verbessern** – „Mehr Lagerplatz“, „Wertvollere Gegenstände“ – **4.000** · **„Zu wenig Spielgeld“** (deaktiviert-Beispiel).
  4. **Tierplätze erweitern** – „+2 Tierplätze“, „Mehr Betreuung möglich“ – **2.500** · Kaufen.
- Das ist die Listen-Variante zum Ausbau (Teil 1, Ansicht 3). Inhalt kommt aus denselben datengetriebenen Upgrade-Daten; zeigt die jeweils nächsten sinnvollen Käufe. Nutzen konkret beziffern, wo möglich (z. B. „+2 Parkplätze“).
- Hinweis: Im Bild liegt in der Tierpension auch eine **Katze**. Erster Build laut Auftrag: nur Hunde. Katzen = später.

## Ansicht 7: REBIRTH-SHOP

- Titel: violette Münze mit Kreispfeilen + **„REBIRTH-SHOP“**. Kapsel rechts: violette Münze **„24“ / „Rebirth-Coins“** (violetter Text). Schild hinten: „NEUER ANFANG · STÄRKER · FÜR IMMER ∞“.
- Violettes Banner mit Goldrand und Krone: **„Diese Verbesserungen bleiben beim Neustart.“**
- **2×2 Karten** (Titel, Icon links, Wert groß rechts + Erklärung, Level-Zeile, zweiteiliger Knopf mit violetter Münze):
  1. **Mehr Startkapital** – Münzstapel + grüner Pfeil – **„+10 %“** „Mehr Spielgeld beim Neustart.“ – Level 1/5 – **5** · Kaufen.
  2. **Höhere Einnahmen** – Geldsack mit Pfote + Pfeil – **„+5 %“** „Mehr Einnahmen aus allen Quellen.“ – Level 2/10 – **8** · Kaufen.
  3. **Offline-Zeit** – Sanduhr – **„4 → 6 Stunden“** „Längere Offline-Einnahmen.“ – Level 1/5 – **10** · Kaufen.
  4. **Verhandlungsgeschick** – Handschlag – **„+2 %“** „Bessere Preise beim Verhandeln.“ – Level 0/5 – **6** · Kaufen.
- Wertanzeige = Wirkung der **nächsten** Stufe („4 → 6 Stunden“ = jetzt 4, nach Kauf 6). Bei Maximalstufe Knopf „Maximal“ (deaktiviert).
- Kosten steigen je Stufe (datengetrieben). Offline-Zeit ist die im Auftrag geforderte „dauerhafte Verbesserung“ der 4-h-Grenze.

## Ansicht 8: BONUS & SCHUTZ

- Titel: Wappen mit Pfote + **„BONUS & SCHUTZ“**. Schild hinten: „GUTE GESCHÄFTE · GLÜCKLICHE TIERE“ + Pfote.
- **Große Creme-Karte „Freiwillige Belohnung“** (grünes Video-Icon): Untertitel „Schau dir ein Video an und erhalte einen zeitlich begrenzten Bonus.“ Darin zwei Unterkarten:
  - **Offline-Einnahmen verdoppeln** – Münzen mit zwei grünen Pfeilen – „4 Stunden“ – grüner Knopf mit Play-Symbol **„Video ansehen“**.
  - **Kurzer Schutz** – Schild mit Pfote – „30 Minuten“ „Schützt vor Angriffen anderer Spieler.“ – **„Video ansehen“**. → **SPÄTER** (erst mit echten Raubzügen gegen andere Spieler; im ersten Build ausblenden).
- **Creme-Karte „Echtgeld“** (grünes €-Icon): **Schutzpaket · 4 Stunden** – Schild mit Pfote und Uhr – Punkte „Schützt vor Angriffen anderer Spieler.“, „Eigener Angriff beendet den Schutz.“ – grüner Knopf **„0,99 €“**. → **SPÄTER** (gleicher Grund; ein Kauf ohne Wirkung würde in der Apple-Prüfung abgelehnt). Im ersten Build nicht anlegen/ausblenden.
- **Dunkle Karte „Gewähltes Design“** (Goldwappen-Icon): Unterkarte Creme **„Klassische Fassade“** mit Bild der Ladenfront, dunkler Knopf **„Fassade ansehen“** (Kamera fährt zur Gebäudefront).

## Regeln, die aus Teil 2 folgen

- **Belohnungsvideos** sind immer freiwillig, nie Pflicht; bleiben auch nach „Werbefrei“ verfügbar. Belohnung fest und vorher sichtbar (kein Zufall).
- **Pflichtanzeige** nach etwa 15 aktiven Spielminuten, nur an einem ruhigen Moment, nie während Verhandlung, Raubzug, Kauf oder Tutorial; entfällt mit „Werbefrei“.
- **Echtgeld-Käufe erster Build**: Werbefrei **6,99 €** (Karte 13.10. 13:07; Bild zeigt noch 4,99 €), Starterpaket 2,99 €, Gebäude-Design „Klassische Fassade“ 3,99 €. **Später**: Schutzpaket 4 h 0,99 €.
- Kosmetik bleibt beim Rebirth („Freigeschaltete Designs“).
- Alle Kaufknöpfe zeigen Zustand: kaufbar (grün) · zu wenig Guthaben (grau, Text) · gekauft/Maximal (grau, Haken).

## Offener Punkt: Figurenstil

Teil 1 zeigt eher realistische Figuren, Teil 2 eher Cartoon-Figuren (große Augen, weiche Formen). Für das echte 3D-Spiel einen Stil durchziehen; bis Julian entscheidet: **stilisiert-warm wie Teil 2** (leichter als echte 3D-Modelle umzusetzen, auf dem iPhone besser lesbar).

---

# Teil 3: Raubzug-Ablauf (6 Ansichten)

Quelle: Julian, 13.10.2026 12:50, Bild `ui-vorgabe-raubzug.png` (3×2, Hochformat). Verbindlich, KI-Konzeptbild.

**Umfang erster Build:** Raubzüge laufen nur gegen **lokale Trainingsanlagen** (erfundene Rivalen-Lager, im Spiel erzeugt). Keine echten Spieler, keine Daten anderer Spieler, kein Server. Schutz vor Angriffen echter Spieler = **später**.

**Look Raubzug:** dunkler, nächtlicher als der Betrieb. Panels dunkelgrün-schwarz (`#141D19`) mit dünnem Goldrand. **Hauptknöpfe hier gold** (Verlauf `#F0CB62` → `#C99A2E`, Text dunkel `#1C1C1E`, Icon dunkel) statt grün. Grün nur für Bestätigungen/Haken. Wachen mit **roten Sichtkegeln** (halbtransparent `#E0453A`), Fluchtweg/Ausgang **grün leuchtend** (`#3BD16F`, Notausgang-Schild).

Kopfleiste in diesen Bildern: V-Logo + „VAULTORIA“ klein · Münze 12.480 · **violetter Edelstein 12** · Zahnrad (siehe „Offene Entscheidung: Kopfleiste“).

## R1: RAUBZUG PLANEN
- Kopf: Icon Fernglas/Maske · **„RAUBZUG PLANEN“** · Untertitel „Rivalen-Lagerhaus – Ebene 1“.
- Szene: Lagerhaus im Schnitt von schräg oben (wie Gebäudeübersicht), Räume mit Kisten, Tresorraum, Wachen mit roten Sichtkegeln, Kamera-Symbol. Eingezeichnete Route: **weiß gestrichelt** = geplanter Weg mit Wegpunkten (weiße Punkte), **grün gestrichelt** = Fluchtweg zum Ausgang (grünes Laufmann-Schild). Startmarker = Kopf-Symbol der Figur.
- Unten Segment-Schalter volle Breite: **„Manuell“** (aktiv, grün) | **„Automatisch“** (inaktiv, dunkel).
- Goldener Knopf volle Breite mit Play-Symbol: **„Starten“**.
- Manuell: Spieler zeichnet/tippt Wegpunkte, dann Ansicht R3. Automatisch: Ergebnis wird aus Crew, Planung und Sicherheit der Anlage berechnet, direkt Ansicht R4 (mit kurzer Animation).

## R2: DEINE CREW
- Kopf: Personen-Icon · **„DEINE CREW“** · „Spezialisten für diesen Auftrag“.
- **Drei hohe Karten** nebeneinander (grüner Rahmen, dunkel), oben Porträt, darunter:
  - **Die Schlosserin** – „Öffnet selbst komplexe Schlösser.“ – Haken + **15 %** – Werkzeug: Dietriche, Bohrer.
  - **Der Techniker** – „Deaktiviert Sicherheitssysteme.“ – Haken + **10 %** – Werkzeug: Störsender, Gerät.
  - **Der Fahrer** – „Sorgt für eine saubere Flucht.“ – Haken + **8 %** – Werkzeug: Schlüssel, Lieferwagen.
- Prozent = **Anteil an der Beute** für dieses Crewmitglied. Haken = ausgewählt (an/aus antippbar).
- Kapsel: **„Crew-Anteil: 33%“** (Zahl gold) = Summe.
- Goldener Knopf: Personen-Icon **„Crew bestätigen“**.
- Wirkung: jedes Mitglied senkt ein Risiko (Schloss-Zeit, Kameras/Alarm, Fluchtzeit). Weniger Crew = mehr Anteil, mehr Risiko.

## R3: EINBRUCH (manuell)
- Kopf: Laufmann-Icon · **„EINBRUCH“** · „Finde das Ziel und entkomme unbemerkt.“ Rechts **Timer-Kapsel** (Uhr + **„01:24“**, läuft rückwärts) und darunter **Beute-Kapsel** (Münze + **„1.200“**, zählt hoch).
- Szene: Nahansicht im Lager, schräg von oben hinter der Spielfigur (Rucksack, Kappe). Wache mit Taschenlampe/Sichtkegel, Kameras mit roten Kegeln, Tresor mit Goldbarren, grüner Notausgang.
- Steuerung: **virtueller Joystick** unten links (runder dunkler Ring mit Pfeilen, heller Knauf), **Schleich-Knopf** unten rechts (runder Knopf, Symbol geduckte Figur, weißer Ring).
- Wird man im Sichtkegel gesehen: Alarm → weniger Beute bzw. Abbruch. Timer 0 = Abbruch mit dem bis dahin Gesammelten, wenn Ausgang erreicht, sonst nichts.

## R4: RAUBZUG BEENDET
- Kopf: grüner Haken im Kreis · **„RAUBZUG BEENDET“** · „Sauberer Abgang! Dein Team ist entkommen.“
- Szene: Crew sitzt feiernd an offenem Lieferwagen vor Lagerhaus („STORAGE“-Schild, in DE lokalisieren: „LAGER“).
- **Abrechnungskarte** (dunkel, Goldrand): Münzstapel links. „Beute:“ **3.000** · „Crew:“ **−990** · Trennlinie · „Dein Anteil:“ **2.010** (groß, gold; im Bild fälschlich „2,010“ – immer Tausenderpunkt).
- Goldener Knopf: Haus-Icon **„Zurück zum Betrieb“**.
- Rechenregel: Crew = Beute × Crew-Anteil (gerundet), Dein Anteil = Beute − Crew. Verbuchung genau einmal (Raubzug-ID).

## R5: SCHUTZ & BERICHT
- Kopf: Schild-Icon · **„SCHUTZ & BERICHT“** · „Ein Einbruch hat dein Lager getroffen.“
- Szene: aufgebrochene Tresortür, Sicherheitsmann („SECURITY“) mit Tablet und Taschenlampe untersucht Fußspuren, gelber Beweismarker „1“.
- Creme-Karte: Bild Tresor + **„Verlust:“** Münze **400 Spielgeld**.
- Grüne Karte: grünes Schild-Icon **„Kostenloser Schutz aktiv“** · Uhr „Noch 2 Stunden“.
- Dunkler Knopf mit Dokument-Icon: **„Bericht ansehen“**.
- Goldener Knopf mit Schild-Icon: **„Sicherheit verbessern“** (→ Ausbau, Sicherheit).
- **Erster Build:** Diese Ansicht nur für **simulierte Einbrüche durch Spiel-Rivalen** (lokal, nach Spielregeln, z. B. wenn Sicherheit zu niedrig), falls eingebaut; sonst später. Regeln: Verlust nur Spielgeld aus eigenem Bestand, **nie Kundeneigentum, nie Pfänder, nie Tiere**; Verlust gedeckelt (Vorschlag: max. 10 % des Spielgelds). Echte Angriffe anderer Spieler und Schutz dagegen: **später**.

## R6: DEIN NÄCHSTER AUFSTIEG
- Kopf: Diagramm-Pfeil-Icon · **„DEIN NÄCHSTER AUFSTIEG“** · „Wachse in eine neue Stadt und übernimm ein größeres Lagerhaus.“
- Szene: Stadt am Fluss mit Brücke und Hochhäusern, großes Lagerhaus „RIVERSIDE STORAGE“ (DE: z. B. „Flusslager“), Parkplatz, umzäunter Hundeauslauf mit Schäferhund.
- Dunkle Karte: Ortsmarke **„Riverside – Stufe 2“**. Liste mit Icon links, Wert rechts, grüner Haken:
  - Etagen 2 / 2 · Upgrades 6 / 6 · Ansehen 300 / 300 · Spielgeld 50.000 / 50.000 · Kredite zurückgezahlt 3 / 3
- Violetter Knopf/Banner mit Goldrand: Münze **„+12 Rebirth-Coins“**.
- Haus-Icon „Dauerhafte Boni bleiben.“
- Goldener Knopf mit Karten-Icon: **„Vorschau öffnen“** (→ Ansicht 4 „Umziehen & neu starten“).
- Ist die Kurzfassung/Einstieg zu Ansicht 4. Zielwerte sind datengetrieben je Standort (Bild-Werte weichen von Ansicht 4 ab, das ist gewollt: anderer Standort).

---

# Teil 4: Betriebsansichten mit unterer Tab-Leiste (6 Ansichten)

Quelle: Julian, 13.10.2026 12:50, Bild `ui-vorgabe-betrieb.png` (3×2). Verbindlich, KI-Konzeptbild.

## Untere Tab-Leiste (neu, in allen Betriebsansichten)
Dunkle Leiste volle Breite (`#1A1F1C`), 5 gleich breite Tabs, Icon über Text:
**Laden** (Haus) · **Wertlager** (Tresor-Quadrat) · **Personal** (zwei Personen) · **Werkstatt** (Hammer+Schraubenschlüssel) · **Kunden** (Stern).
Aktiv: Icon und Text **gold**, goldene Linie oben am Tab. Inaktiv: hellgrau.

Kopfleiste in diesen Bildern: „VAULTORIA“ in Gold-Serife · Münze + Betrag mit „Spielgeld“ darunter · Stern (ohne Zahl) · Zahnrad. Bereichstitel in großen weißen Versalien direkt über der Szene, Untertitel darunter (ohne Icon-Kachel).

## B1: DEIN ERSTER LADEN (Tutorial, Tab Laden)
- „DEIN ERSTER LADEN“ · „Bediene deinen ersten Kunden.“
- Szene: kleiner Laden schräg von oben, Theke mit Betreiber, Kunde mit Rucksack läuft hinein. **Grüner Pfeil** vom Kunden zur Theke und **Zeigehand** (Tutorial-Hinweis, pulsiert). Aufsteller „VAULTORIA · ANKAUF · PFAND · SERVICE“ mit Waage. Parkplatz mit 2 Autos.
- Grüner Knopf (nicht volle Breite, mittig) mit Person-Icon: **„Kunde bedienen“**.
- Tutorial schaltet Schritt für Schritt frei (Auftrag: nicht alle Systeme beim Start).

## B2: PFANDGESCHÄFT (Tab Laden)
- „PFANDGESCHÄFT“ · „Biete einen fairen Kredit an.“
- Szene wie Handel: Kunde hält Kamera über die Theke, Betreiber von hinten.
- Dunkle Karte: Bild Kamera · **„Verpfändet“** · „Kredit:“ Münze **150 Spielgeld** · Kalender „Frist:“ **2 Spieltage**.
- Zwei Knöpfe nebeneinander: grün mit Haken **„Kredit vergeben“** · rot mit X **„Ablehnen“**.
- Regeln (Auftrag): Kredit wird vom Spielgeld abgezogen; Pfand bis Fristende gesperrt (Schloss-Chip, nicht verkaufbar); Auslösung = Rückzahlung (Kredit + Gebühr) und Rückgabe; sonst nach Frist verkaufbar. Getrennt vom Ankauf.
- **Offen:** Länge eines „Spieltags“. Vorschlag: 1 Spieltag = 1 Stunde Echtzeit (läuft auch offline, Uhr-Manipulation wie beim Offline-Fortschritt abfangen).

## B3: WERTLAGER (Tab Wertlager)
- „WERTLAGER“ · „Sichere Kundeneigentum ein.“
- Szene: Wand mit nummerierten Schließfächern 01–06, eines offen (Gemälde, Uhr, Vase), Mitarbeiterin in Weste zeigt Kunde das Fach.
- Dunkle Karte „Kundeneigentum“: Reihe Kacheln (Taschenuhr, Vase, Gemälde, Geige, Perlenkette). Darunter Fach-Icon **„Lagerplätze: 6 / 10“** + grüner Balken.
- Knöpfe: grün mit Kisten-Icon **„Einlagern“** · gold umrandet (dunkel) mit Handschlag **„Kaufangebot“** (Angebot an den Besitzer, Auftrag).
- Kundeneigentum nie verkaufbar, nie Raubzug-Verlust, eigene Kennzeichnung.

## B4: PERSONAL (Tab Personal)
- „PERSONAL“ · „Stelle die richtigen Mitarbeiter ein.“
- Szene: voller Laden, lange Kundenschlange, **rotes Sanduhr-Symbol** über der Schlange (Engpass „Kunden warten“), ein Mitarbeiter an der Theke, Hund im Korb.
- Drei Porträtkarten: **Verkäufer** (ausgewählt, Goldrand) · **Gutachter** (mit Lupe) · **Tierbetreuer** (mit Hund).
- Creme-Karte: Person-Icon **„Verkäufer · Stufe 8“** · „Bedient Kunden schneller.“ · graue Zeile „Einmalig einstellen“ Münze **2.000 Spielgeld** · grüner Knopf mit Person-Plus **„Einstellen“**.
- Einmalig einstellen, danach verbessern (keine Gehälter, Auftrag). Gutachter = schätzt Werte genauer / bearbeitet Wertlager; Tierbetreuer = Pension.

## B5: WERKSTATT (Tab Werkstatt) – NEU im ersten Build
- „WERKSTATT“ · „Restauriere und erhöhe den Wert.“
- Szene: Werkstatt mit Werkzeugwand, Restaurator mit Dutt und Schürze pinselt einen Holzstuhl.
- Dunkle Karte „Restaurieren“: Vorher/Nachher-Bilder (Pfeil dazwischen) · Münze **350 Spielgeld** · grüner Pfeil „Wertsteigerung möglich“.
- Grüner Knopf mit Hammer: **„Auftrag starten“**.
- Regeln: nur **eigene Ware**, nie Kundeneigentum, nie verpfändete Gegenstände. Dauert Zeit (Fortschrittsbalken), Ergebnis: Zustand +1 Stufe → höherer geschätzter Wert. Kosten und erwartete Wertsteigerung vorher zeigen. Der Gegenstand ist währenddessen nicht verkaufbar.
- Stand im Auftrag als „später“; Julians neuere UI-Vorgabe gilt, also mit rein.

## B6: KUNDEN & ANSEHEN (Tab Kunden) – Stammkunden NEU im ersten Build
- „KUNDEN & ANSEHEN“ · „Zufriedene Kunden kommen wieder.“
- Szene: Kundschaft im Laden, ältere Dame mit Sonnenbrille im Haar und Tuch im Vordergrund, Sprechblase mit Krone **„Stammkunde“**.
- Dunkle Karte „Letzte Transaktion“: Bild Armband · „Armband verpfändet“ · Münze **320 Spielgeld** · „vor 1 Spieltag“ · grüner Haken.
- „Ansehen“: **4 von 5 Sternen** (gold, letzter grau) + goldener Fortschrittsbalken.
- Reihe 4 Kunden-Porträts, erstes mit Krone (Stammkunde, Goldrand).
- Knöpfe: grün mit Sprechblase **„Verhandeln“** · gold umrandet mit Lupe **„Angebot prüfen“**.
- Regeln: Faire Abschlüsse erhöhen Ansehen; Stammkunden kommen öfter und bringen bessere Ware, akzeptieren faire Preise schneller. Ansehen ist Voraussetzung für den Standortwechsel.
- Stand im Auftrag als „später“; Julians neuere UI-Vorgabe gilt, also mit rein.

## Navigation (Vorschlag, wie alles zusammenhängt)
- **Tab-Leiste** unten in allen Betriebsansichten: Laden (Handel + Pfand), Wertlager, Personal, Werkstatt, Kunden.
- **Tierpension, Ausbau, Raubzug, Shop** sind nicht in der Tab-Leiste. Vorschlag: Tierpension und alle Etagen über die **Gebäudeübersicht** (Ausbau, Teil 1 Ansicht 3) antippen; Gebäudeübersicht über ein Gebäude-Symbol oben links unter der Kopfleiste; **Raubzug** und **Shop** als zwei runde Gold-Knöpfe am rechten Rand der Gebäudeübersicht. → **Offene Entscheidung** (siehe unten).

---

# Offene Entscheidungen (Julian)

## 1. Einheitliche Kopfleiste
Die Bilder zeigen drei Varianten:
- Teil 1: „VAULTORIA“ · Lv + XP-Balken · Münze „12.460 €“ · Stern „420“ · Zahnrad
- Teil 3 (Raubzug): V-Logo + „VAULTORIA“ · Münze „12.480“ · **violetter Edelstein „12“** · Zahnrad
- Teil 4 (Betrieb): „VAULTORIA“ Gold-Serife · Münze „3.250 / Spielgeld“ · Stern ohne Zahl · Zahnrad

**Vorschlag (eine Leiste überall):** V-Logo (klein) · „Lv. 28“ mit XP-Balken · Münze + Spielgeld **ohne „€“** (z. B. „12.460“, damit es nicht wie Echtgeld aussieht) · Stern + Ansehen-Zahl · violette Münze + Rebirth-Coins (erst sichtbar ab dem ersten Neustart) · Zahnrad. **Kein Edelstein / keine Premiumwährung**: Echtgeld kauft direkt (Shop, Teil 2), das hält es fair und einfach. Der violette Edelstein im Raubzug-Bild wird als Rebirth-Coins gelesen.

## 2. Navigation
Vorschlag siehe „Navigation“ oben: 5 Tabs wie im Bild + Gebäudeübersicht für Tierpension/Ausbau + Raubzug/Shop als Knöpfe an der Gebäudeübersicht.

## 3. Figurenstil
Siehe Teil 2 („Offener Punkt: Figurenstil“). Raubzug- und Betriebsbilder zeigen wieder eher realistische Figuren.

## 4. Länge eines Spieltags
Vorschlag 1 Spieltag = 1 Stunde Echtzeit (siehe B2).
