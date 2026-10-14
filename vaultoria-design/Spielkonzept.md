# Vaultoria – Spielkonzept (verbindlicher Gesamtstand für den Mac-Build)

**Stand: Julian, 13.10.2026 13:09 – Sammlung 1 abgeschlossen. Sammlung 2 (Teil D, ab 13:20) und Sammlung 3 (Teil E, abgeschlossen 13:37) ergänzen diesen Stand und gehen bei Widerspruch vor.**

Aufbau:
- **Teil A** – Julians vollständiger Übergabeauftrag (13:09), wörtlich. Grundlage für alles.
- **Teil B** – Festlegungen, die Julian per Karte oder Bild getroffen hat, und Präzisierungen aus der UI-Vorgabe. Gehen Teil A vor, wo sie konkreter oder neuer sind.
- **Teil C** – Annahmen und offene Entscheidungen.
- **Teil D** – Sammlung 2 (Julian, ab 13:20) und ENTWURF Wirtschaftsmodell (Zahlen, Julian entscheidet).
- **Teil E** – Sammlung 3 (Julian, 13:37): acht Anforderungen, alle im ersten Build, mit Startwerten.

Visuelle Vorlage: `UI-Vorgabe.md` (20 Ansichten + Icon + Startbildschirm als Text, Bilder im selben Ordner).

---

# Teil A – Übergabeauftrag (Julian, 13.10.2026 13:09, wörtlich)

Baue die erste spielbare Version von **Vaultoria**, einem iPhone-Tycoon im Hochformat. Prüfe zuerst das vorhandene Projekt und setze anschließend einen zusammenhängenden Spielablauf um. Liefere nicht nur eine Planung oder funktionslose Menüs.

### 1. Flyx Fix ablösen

**Flyx Fix wird eingestellt und durch Vaultoria ersetzt. Flyx Map und Flyx Cut bleiben unverändert bestehen.**

- Sichere den bisherigen Flyx-Fix-Stand durch Git oder ein wiederherstellbares Archiv.
- Entferne eindeutig zu Flyx Fix gehörende Dateien, Targets, Navigation und aktive Projektverweise.
- Behalte gemeinsam genutzte Bestandteile.
- Lösche keine fremden Projekte, Cloud-Daten oder App-Store-Einträge.
- Dokumentiere, was entfernt, übernommen und neu erstellt wurde.

### 2. Ziel und Spielprinzip

Vaultoria verbindet **Handel, Aufbewahrung, Haustierbetreuung und Raubzüge**.

Der Spieler beginnt klein, verdient Geld, kauft Einrichtungen, verbessert Personal und Gebäude und steigt zum Millionär beziehungsweise Milliardär im Spiel auf.

**Eatventure dient als Referenz für den Betriebsablauf:**

Kunden bedienen → Einnahmen investieren → Einrichtungen verbessern → Personal einstellen → Engpässe lösen → Standort abschließen → in einer besseren Welt neu anfangen.

Der Spieler führt den Betrieb wie einen Tycoon. **Keine selbst gesteuerte Besitzerfigur im normalen Geschäftsalltag.** Manuelle Steuerung ist für Raubzüge vorgesehen.

Langfristiges Ziel: 50.000 täglich aktive Spieler bis Oktober 2029. Das ist ein Geschäftsziel, keine Prognose oder Abnahmebedingung.

### 3. Geschäftsbereiche

Geschäftsbereiche schrittweise freischalten, beginnend mit An- und Verkauf. Der Spieler entscheidet, welche Bereiche er besonders ausbaut.

| Bereich | Regeln |
|---|---|
| **An- und Verkauf** | Waren kaufen, verhandeln, gegebenenfalls restaurieren und weiterverkaufen. |
| **Wertlager** | Kundeneigentum gegen Gebühren aufbewahren. Kaufangebote an den Besitzer sind möglich. |
| **Pfandhaus** | Kredit gegen einen Gegenstand vergeben. Verkauf erst nach Nichtauslösung und Fristablauf. |
| **Haustierpension** | Hunde und weitere Tiere betreuen; Besitzer zahlen Gebühren. |

Kein klassisches Übernachtungshotel mit Restaurant und Zimmerreinigung.

**Eigentum immer klar kennzeichnen:** „Kundeneigentum“, „Verpfändet“ oder „Dein Besitz“. Fristen und Verpflichtungen anzeigen.

### 4. Handel und Kunden

Vorgesehen sind:

- Waren wie Uhren, Schmuck, Kunst, Elektronik, Instrumente, Möbel und Sammlerstücke.
- Plausible Werte nach Zustand, Echtheit, Herkunft und Seltenheit.
- Verhandlungen mit Gegenangeboten und möglichem Abbruch.
- Überraschende Fundstücke und Fälschungen.
- Bewertungen durch Experten.
- Restaurierung und Aufarbeitung.
- Schneller Händlerverkauf oder Warten auf bessere Käufer.
- Auktionen für nicht ausgelöste Pfandstücke.
- Suchaufträge von Kunden.
- Eigene Sammlung und Ausstellungen.
- Verdächtige Angebote mit bewusstem Risiko.
- Individuelle Kunden und Stammkunden.
- Mitarbeiter automatisieren Routinegeschäfte innerhalb gesetzter Preisgrenzen.

**Ansehen steigt durch gute Angebote, faire Preise und gute Arbeit.** Schlechte Behandlung und entdeckte Unterschlagung können es senken.

Spieler-Handelsmarkt erst später.

### 5. Unterschlagung

Der Spieler kann eingelagerte Kundengegenstände riskant unterschlagen und verkaufen.

Bei Entdeckung drohen **Entschädigung und Rufverlust**. Die Mechanik darf kein grenzenloser Geldgenerator sein.

Kundenansprüche dürfen durch Rebirth nicht verschwinden. Für die erste Version darf dieses System zurückgestellt werden, bleibt aber Teil der Gesamtvision.

### 6. Haustierpension

- Tiere mit Namen, Charakter und Vorlieben.
- Sichtbare Betreuung, Fütterung, Spielen und Ruhe.
- Tierpfleger, Betreuungsplätze und Außenanlagen.
- Zufriedene Besitzer werden Stammkunden.
- Upgrades verbessern Kapazität und Betreuung.

**Tiere werden weder gestohlen noch verletzt.** Spieler dürfen Sicherheit und Betreuung unterschiedlich priorisieren, ohne Tiere zu Raubzugbeute zu machen.

### 7. Gebäude, Grundstück und Upgrades

**Keine freie Grundrissplanung.** Vorgegebene Räume, Einrichtungen, Etagen und Erweiterungen kaufen und verbessern.

Dazu gehören:

- Verkaufsräume, Lager, Tresore, Werkstätten und Tierbereiche;
- mehrere Räume pro Etage;
- Aufzüge und Wege;
- Parkplatz und zusätzliche Stellplätze;
- Zufahrt, Eingang und Lieferbereich;
- Tierauslauf und Außenanlagen;
- Umbau bei laufendem Betrieb.

Etwa **100 Upgradestufen pro Einrichtung** als vorläufiger Richtwert. Werte datengetrieben konfigurieren.

Wichtige Meilensteine verändern sichtbar Ausstattung, Kapazität oder Arbeitsplätze. Nicht jede Stufe benötigt ein neues Modell.

Upgrades beeinflussen Einnahmen, Bearbeitungsgeschwindigkeit, Kapazität und Personalbedarf. Kosten und Nutzen vorher anzeigen.

Keine detaillierte Verwaltung von Zugangsberechtigungen.

### 8. Personal und Wirtschaft

- Personal einmalig einstellen und upgraden.
- Verkäufer, Gutachter, Tierpfleger, Wachen und später Betriebsleiter.
- **Keine laufenden Gehälter, Miete oder Wartungsgebühren.**
- Engpässe deutlich zeigen: Wartezeiten, Personalmangel, volle Lager und fehlende Kapazität.
- Verständliche Einnahmen- und Betriebsübersicht.
- Geldabflüsse durch Warenankauf, Ausbau, Personalverbesserungen, Restaurierung, Transporte und Ausrüstung.

Weitere geplante Systeme: bewachte Transporte und Versicherung.

**Offline-Produktion:** anfangs vier Stunden, durch Upgrades verlängerbar. Einnahmen nachvollziehbar berechnen und nur einmal auszahlen.

### 9. Kredite und Geldmangel

Bei Geldmangel Rettungsaufträge und Betreiberkredite anbieten.

Vorläufiges Betreiber-Kreditlimit: **höchstens der aktuelle eigene Geldbestand**. Kundengeld zählt nicht dazu. Rückzahlung und Gebühren transparent darstellen.

Betreiberkredite strikt von den an Kunden vergebenen Pfandkrediten unterscheiden.

Kreditgeld darf weder Gewinne noch Rebirth-Belohnungen künstlich erhöhen.

### 10. Standortentwicklung und Rebirth

Zunächst ein aktiver Standort. Mehrere gleichzeitige Standorte sind nicht beschlossen.

Sieben langfristige Größenrichtungen:

1. Kleiner Laden in einer Nebenstraße.
2. Zweistöckiger Betrieb in der Ortsmitte.
3. Geschäftshaus in einer Kleinstadt.
4. Größerer Betrieb am Stadtrand mit Lagerhalle.
5. Premiumhaus im wohlhabenden Viertel.
6. Unternehmenssitz mit Seitenflügeln.
7. Markantes Großstadtgebäude mit großen Außen- und Logistikbereichen.

Etagenzahlen und Größen sind vorläufig.

**Standortwechsel funktioniert als Rebirth.**

Voraussetzungen:

- alle erforderlichen Etagen gekauft;
- erforderliche Einrichtungen vollständig verbessert;
- festgelegtes Ansehen erreicht;
- festgelegten Geldbetrag erreicht;
- Betreiberkredite zurückgezahlt.

Der Spieler kann zunächst weiterspielen, um mehr Rebirth-Coins zu verdienen.

Beim Rebirth:

- normaler Betrieb, Einrichtungen, Personal und gewöhnliches Spielgeld werden zurückgesetzt;
- Kundenverträge und Tierbetreuung vorher ordentlich abwickeln;
- neuer Aufbau in einer besseren Welt;
- neues Startguthaben;
- mehr Kunden und bessere Verdienstmöglichkeiten;
- **Rebirth-Coins und gekaufte dauerhafte Boni bleiben erhalten.**

Rebirth-Shop:

- mehr Startkapital;
- höhere Einnahmen;
- bessere Verhandlungen;
- längere Offline-Produktion.

Vorher exakt anzeigen, was verschwindet, was bleibt und welche Belohnung entsteht.

Kundeneigentum nicht als eigenes Vermögen bewerten. Kreditgeld nicht belohnen. Bereits belohnten Fortschritt nicht erneut abrechnen.

**Gekaufte dauerhafte Produkte dürfen durch Rebirth nicht unbeabsichtigt entzogen werden.** Die Behandlung von Designs und Verbrauchsgütern ausdrücklich definieren.

### 11. Raubzüge

Langfristig zeitversetzte Angriffe auf gespeicherte Spieleranlagen.

Zwei auswählbare Modi:

- **Manuell:** Dieb steuern und auf Situationen reagieren.
- **Automatisch:** Route, Ausrüstung und Aktionen planen; der Dieb führt sie aus.

Gleiche Grundregeln und vergleichbare Ausrüstung. Kein pauschaler Bonus für manuelle Steuerung.

Mechaniken:

- Tresore knacken;
- Kameras und Laser umgehen;
- Wachen ablenken;
- Wege und Flucht planen;
- Zeit und Tragfähigkeit beachten;
- mehr Beute erschwert die Flucht;
- rechtzeitig abbrechen können.

Spezialisten engagieren, beispielsweise Schlossknacker, Techniker und Fahrer. Sie erhalten einen vorher vereinbarten **Prozentsatz der Beute**.

Weitere Funktionen: Angriffsberichte, Kamerabilder, Spuren, Revanchen, Ranglisten, Freundesbesuche und kostenlose Testeinbrüche.

### 12. Verteidigung und Schutz

Spieler entscheiden selbst, welche Bereiche sie stärker absichern.

- PvP erst nach sicherer Lernphase.
- Gegner mit vergleichbarer tatsächlicher Stärke.
- Nur begrenzter, klar angezeigter Bestand angreifbar.
- Verlustobergrenzen gegen wiederholtes Leerplündern.
- Kostenloser Schutz nach schweren Angriffen.
- Zeitlich begrenzte Schilde durch Werbung oder Kauf.
- Eigener Angriff beendet Schutz, mit Warnung vorher.
- Schutzverlängerung begrenzen.
- Gebäude, Tiere und gekaufte Premiumwährung bleiben sicher.

Konkrete Zeiten, Preise und Verlustgrenzen noch nicht beschlossen. Werte aus Bildern sind Beispiele.

### 13. Grafik und UI

**Die bestätigten Vaultoria-Konzeptbilder sind die visuelle Vorlage.** Wenn sie im Projekt nicht vorliegen, nicht behaupten, sie gesehen zu haben.

Gewünschte Gestaltung:

- echte 3D-Spielwelt mit fester leicht erhöhter Kamera;
- 2,5D-Gebäudeübersicht im Hochformat;
- einsehbare Räume;
- Bereiche antippen und in nähere Ansichten wechseln;
- bewegte Kunden, Mitarbeiter, Tiere und Fahrzeuge;
- auch Detailansichten als animierte Spielszenen;
- neutrale beziehungsweise dunkle Oberfläche;
- Creme, gedecktes Grün und Gold;
- hochwertige, zurückhaltende Gestaltung;
- wenig Text und übersichtliche Bedienelemente.

Personen zeigen Waren, reagieren auf Angebote und gehen nach dem Geschäft. Mitarbeiter transportieren Gegenstände. Tiere spielen und ruhen.

Keine statischen Konzeptbilder als Ersatz für tatsächliche Spielmechanik.

Abweichungen von der bestätigten Gestaltung benennen und anhand echter Spielansichten abstimmen. Keine pixelgleiche Umsetzung versprechen, bevor passende Modelle und Animationen existieren.

**App-Name: Vaultoria.** Mehrere Icon-Entwürfe existieren; die endgültige Variante wurde noch nicht ausgewählt. *(→ inzwischen gewählt, siehe Teil B1)*

### 14. Sound

Lebendige, zurückhaltende Geschäftsatmosphäre mit Kunden, Tieren, Kasse, Türen und Tresoren.

Musik, Sound und Vibration getrennt einstellbar.

### 15. Apple-Technik und offene Grenzen

**Nur für Werbung ist ein Drittanbieter erlaubt. Der Rest soll ausschließlich über Apple laufen.**

Prüfe aktuelle geeignete Apple-Technologien:

- Swift;
- RealityKit oder geeignete Alternative innerhalb der Vorgabe;
- SwiftUI;
- StoreKit;
- Game Center;
- CloudKit.

Keine externen Spielserver oder kostenpflichtigen Dienste eigenständig einrichten.

**Sichere echte Spieler-Raubzüge sind technisch noch ungeklärt.** CloudKit nicht als Ersatz für beliebige vertrauenswürdige Serverlogik darstellen.

Für die erste Version lokale Trainingsanlagen verwenden. Keine Bots als echte Spieler ausgeben.

Spielregeln und Speicherung so trennen, dass eine später geprüfte Online-Lösung ergänzt werden kann. Grenzen des lokalen Manipulationsschutzes ehrlich dokumentieren.

### 16. Werbung und Käufe

Freiwillige Belohnungsvideos für:

- begrenzte Offline-Verdopplung;
- kleine Geldboni;
- kurze Schilde;
- Bauzeitverkürzung;
- zusätzliche eigene Raubzugbelohnung ohne Zusatzverlust beim Gegner;
- Trainingsversuche und ausgewählte Designs.

Nach etwa **15 Minuten aktiver Spielzeit** eine Pflichtanzeige beim nächsten natürlichen Übergang. Keine Unterbrechung von Verhandlung, Einbruch oder Kauf.

**Werbefrei als Einmalkauf:** Preis offen zwischen 4,99 € und 9,99 €. Entfernt Pflichtanzeigen; Belohnungsvideos bleiben freiwillig. *(→ inzwischen 6,99 €, siehe Teil B1)*

Weitere Angebote: Starterpaket, Designs, Spielgeldpakete, Booster, Bauzeitbeschleunigung; Saisonpass später.

Echtgeld, Spielgeld und Rebirth-Coins eindeutig unterscheiden.

Für Entwicklung Testanzeigen und StoreKit-Testkonfiguration verwenden. Nicht verfügbare Anzeigen nicht als angesehen verbuchen. Auch ohne Werbung spielbar bleiben.

### 17. Rechtliche und veröffentlichungsbezogene Prüfung

Prüfe aktuelle offizielle Anforderungen für die vorgesehenen Märkte. Quellen und offene Punkte dokumentieren. Keine garantierte Rechtskonformität behaupten.

- Tatsächliche Datenverarbeitung und Werbe-SDK erfassen.
- Erforderliche Einwilligungen und Tracking-Anfragen korrekt behandeln.
- Datenschutzangaben, Datenschutzerklärung und App-Verhalten müssen übereinstimmen.
- Altersfreigabe und Umgang mit Minderjährigen prüfen.
- Anbieterinformationen und Supportkontakt aus echten Betreiberangaben erstellen; nichts erfinden.
- Erforderliche Kontolöschung und Wiederherstellungsfunktionen berücksichtigen.
- Käufe, Abbrüche, ausstehende Transaktionen, Erstattungen und Wiederherstellung behandeln.
- Keine irreführenden Angebote oder versehentlichen Käufe.
- Für Version 1 keine bezahlten Zufallsbelohnungen.
- Nur eigene oder passend lizenzierte Assets nutzen; Herkunft dokumentieren.
- Keine fremden Marken, Figuren oder Gestaltung kopieren.
- Namen Vaultoria vor Veröffentlichung auf mögliche Konflikte prüfen.
- Betreiber-, Händler-, Steuer- und mögliche arbeitsvertragliche Anforderungen offen prüfen lassen.
- Keine Veröffentlichung oder kostenpflichtige Bestellung allein aufgrund dieses Auftrags.

Spielwährungen und Gegenstände haben keinen zugesicherten Echtgeld-Auszahlungswert.

### 18. Erste spielbare Version

Baue zunächst:

- einen vollständigen kleinen Betrieb;
- einen zweiten Standort;
- Handel und einfache Verhandlungen;
- korrekt getrennte Lager- und Pfandvorgänge;
- kleine sichtbare Tierpension;
- Einrichtungen, Personal und Upgrades;
- Ansehen und Engpassanzeigen;
- vier Stunden Offline-Produktion;
- zuverlässiges Speichern;
- einen vollständigen Rebirth;
- lokale manuelle und automatische Trainings-Raubzüge;
- Testintegration für Werbung und Käufe.

Langfristige Funktionen zurückstellen, aber nicht stillschweigend aus der Gesamtvision streichen.

Das Ziel von **300–500 aktiven Spielstunden** gilt langfristig. Es darf nicht bloß durch Wartezeiten und höhere Preise entstehen.

### 19. Verifikation und Übergabe

Prüfe insbesondere:

- Eigentum, Pfandfristen und Warenbuchungen;
- Verhandlungen und Gewinnberechnung;
- Betreiberkredite und Kundenkredite;
- Rebirth und einmalige Coinvergabe;
- Offline-Auszahlungen und Uhrzeitänderungen;
- Raubzug-Abbrüche und einmalige Ergebnisverbuchung;
- Käufe, Werbefrei und Werbebelohnungen;
- Speichern und Wiederherstellung;
- verschiedene iPhone-Größen;
- Animationen, Kamera, Bedienung und Performance.

Liefere einen startbaren Build und berichte:

1. Was funktioniert?
2. Wie starte ich ihn?
3. Was wurde geprüft?
4. Was fehlt noch?
5. Welche technischen oder rechtlichen Entscheidungen sind offen?

**Beginne mit der Umsetzung. Keine reine Planung, keine funktionslosen Menüs und keine Erfolgsaussagen für ungeprüfte Funktionen.**

---

# Teil B – Festlegungen und Präzisierungen (gehen Teil A vor)

## B1. Entscheidungen per Karte
- **App-Icon: „Goldenes V“** (goldenes, genietetes V mit Schlüsselloch auf Dunkelgrün), Julian 13.10. 12:41. Datei `icon-goldenes-v.png`; für den Store in voller Auflösung neu erzeugen.
- **Werbefrei: 6,99 €**, Einmalkauf, Julian 13.10. 13:07.
- **Kauf-IDs (Code 1.0):** `com.julian.vaultoria.adfree` (6,99 €), `com.julian.vaultoria.starterpack` (2,99 €), `com.julian.vaultoria.design.classicfacade` (3,99 €).
- **Projekt:** Name Vaultoria, Ordner `/Volumes/LifeEmpire/Programme/Vaultoria`, Bundle `com.julian.vaultoria`. Alles zu Julians Projekten liegt auf `/Volumes/LifeEmpire`.

## B2. Flyx Fix
- Bereinigung läuft bereits über den Mac-Thread „Flyx Fix bauen“ (Ordner → Papierkorb; Webseite bereinigt).
- **Schritt im Mac-Build trotzdem:** vor jedem Entfernen prüfen, ob ein Git-Stand oder ein wiederherstellbares Archiv von Flyx Fix existiert (z. B. ZIP auf `/Volumes/LifeEmpire`); wenn nicht, erst anlegen. Danach das Entfernte dokumentieren (Teil A §1).

## B3. Standorte im ersten Build
- Genau **ein aktiver Standort**. Der „zweite Standort“ aus §18 ist das **Rebirth-Ziel** (Größenrichtung 2 „Zweistöckiger Betrieb in der Ortsmitte“), kein paralleler Betrieb.

## B4. Shop und Käufe (UI-Vorgabe Teil 2)
- **Erster Build (StoreKit):** Werbefrei 6,99 € (nicht verbrauchbar), Starterpaket 2,99 € (einmal kaufbar; exklusives Shopschild + 5.000 Spielgeld, Spielgeld genau einmal pro Transaktion), Gebäude-Design „Klassische Fassade“ 3,99 € (nicht verbrauchbar, kosmetisch). „Käufe wiederherstellen“ im Shop.
- **Später:** Schutzpaket 4 h 0,99 € und „Kurzer Schutz“ per Video (erst mit echten Raubzügen), Spielgeldpakete, Booster, Bauzeitbeschleunigung, Saisonpass.
- **Rebirth und Käufe (§10 „ausdrücklich definieren“):** Designs, Werbefrei und Shopschild bleiben immer. Bereits gutgeschriebenes Spielgeld aus Käufen ist gewöhnliches Spielgeld und wird beim Rebirth zurückgesetzt; das vor dem Kauf im Shop anzeigen. Laufende Booster laufen bis zum Ablauf weiter. Rebirth-Coins und Rebirth-Shop-Boni bleiben.
- Rebirth-Shop: Mehr Startkapital, Höhere Einnahmen, Verhandlungsgeschick, Offline-Zeit (UI-Vorgabe Ansicht 7).

## B5. Rebirth genauer
- Neustart-Knopf gesperrt, bis Kundenverträge (Wertlager, laufende Pfänder) und Tierbetreuung abgewickelt sind; eigene Zeilen in der Voraussetzungsliste („Kundenverträge abgewickelt x / y“, „Tiere abgeholt x / y“). Hilfe: Schalter „Keine neuen Verträge annehmen“.
- Belohnung aus tatsächlich verdientem Gewinn/Fortschritt, nicht aus Kontostand; Kreditgeld und Kundeneigentum zählen nicht; Fortschritt nur einmal belohnt (Rebirth-ID).
- Nach der letzten Standortstufe: weitere Herausforderungen und Ausbauziele (später).

## B6. Bereiche im ersten Build (aus UI-Vorgabe)
- Tab-Leiste: Laden (Handel + Pfand), Wertlager, Personal, Werkstatt, Kunden. Dazu Tierpension und Ausbau über die Gebäudeübersicht, Raubzug und Shop.
- **Werkstatt (Restaurieren)** und **Stammkunden** sind im ersten Build (UI-Vorgabe B5/B6). Restaurieren nur für „Dein Besitz“.
- Tierpension erster Build: Hunde; weitere Tiere (z. B. Katzen, im Shop-Bild zu sehen), sobald Modelle da sind.
- Kredite: Pfand- und Betreiberkredite höchstens in Höhe des eigenen Spielgelds; Kundengeld zählt nicht.

## B7. Raubzug im ersten Build
- Nur lokale Trainingsanlagen („Rivalen-Lagerhaus“ o. ä.), klar als Training gekennzeichnet, keine erfundenen Spielernamen.
- Ablauf laut UI-Vorgabe Teil 3: Planen (Manuell/Automatisch) → Crew (Prozentanteile) → Einbruch (Timer, Beute, Joystick, Schleichen) → Abrechnung. Ergebnis genau einmal verbuchen (Raubzug-ID), Abbruch jederzeit.
- Simulierte Einbrüche in den eigenen Betrieb nur lokal nach Spielregeln, falls eingebaut: Verlust nur aus eigenem Spielgeld, gedeckelt (Vorschlag max. 10 %), nie Kundeneigentum, Pfänder, Tiere oder Gebäude.

## B8. Werbung
- Pflichtanzeige nach ca. 15 aktiven Minuten (App im Vordergrund mit Eingaben, Offline-Zeit zählt nicht), beim nächsten ruhigen Übergang; nie während Verhandlung, Einbruch, Kauf oder Tutorial.
- Belohnungsvideos immer freiwillig, Bonus fest und vorher sichtbar. Erster Build: Offline-Verdopplung und kleiner Geldbonus. Schilde später.

## B9. Darstellung
- ~~Spielgeld ohne „€“~~ → **ersetzt durch F2 (14.10):** Beträge im Laden in Euro mit realistischen Preisen; Rebirth-Coins violett.
- Hauptknöpfe grün (Betrieb) bzw. gold (Raubzug), Creme-Karten, Goldrahmen (UI-Vorgabe).

---

# Teil C – Annahmen und offene Entscheidungen

## Annahmen (gelten, bis Julian anders entscheidet)
1. Karten-Entscheidungen nach dem Auftragstext bleiben gültig: Icon „Goldenes V“ (12:41) und Werbefrei 6,99 € (13:07), obwohl der Auftrag (13:09) noch „offen“ sagt.
2. „Zweiter Standort“ im ersten Build = Rebirth-Ziel, kein Parallelbetrieb.

## Offen (Julian)
1. **Premiumwährung:** §12 erwähnt „gekaufte Premiumwährung“, das Raubzug-Bild zeigt einen violetten Edelstein. Vorschlag (Karte offen): keine Premiumwährung im ersten Build, Echtgeld kauft direkt.
2. **Bauzeiten:** §16 nennt Bauzeitverkürzung, die UI-Bilder zeigen sofortige Käufe. Vorschlag: kurze Bauzeiten nur für Etagen und große Meilensteine (Umbau bei laufendem Betrieb), Einrichtungsstufen sofort.
3. **Figurenstil:** stilisiert (Shop-Bilder) oder realistisch (Betrieb/Raubzug). Karte offen, Vorschlag stilisiert.
4. **Navigation** und **einheitliche Kopfleiste:** Vorschläge am Ende von `UI-Vorgabe.md`.
5. **Länge eines Spieltags** (Pfandfristen): **vorerst 1 Spieltag = 10 Minuten Echtzeit** (so in Vaultoria 1.0 gebaut, 13.10.2026). Früherer Vorschlag war 1 Stunde.
6. **Unterschlagung** (§5): Vorschlag für den ersten Build zurückstellen (laut §5 erlaubt).
7. Konkrete Schutzzeiten, Preise, Verlustgrenzen (§12): später.

---

# Teil D – Sammlung 2 (ab 13.10.2026 13:20)

Ergänzt Teil A–C und geht bei Widerspruch vor. Julian sammelt weiter, bis er „fertig“ sagt.

## D1. Julians Punkte (13:20, wörtlich)

- **Raubzüge:** Etwa 20 % des eigenen Vermögens als angreifbarer Anteil – vorläufiger Wert. Kundeneigentum und gekaufte Premiumwährung zählen nicht dazu. Das bedeutet zunächst nicht 20 % Verlust bei jedem Angriff.
- **Rache:** Ein erfolgreicher Gegenangriff kann das gestohlene Geld plus zusätzliche Beute zurückbringen. Keine garantierte Auszahlung; gegenseitige Angriffe dürfen kein unbegrenztes Geld erzeugen.
- **Wachhunde:** Eigene ausgebildete Hunde als Sicherheitsoption. Pensionstiere bleiben geschützt.
- **VIP-Betreuung:** Besonders hochwertige Betreuung darf entsprechend teuer sein.
- **Standortwechsel:** Statt den alten Betrieb einfach zu löschen, verkaufen oder einen Geschäftsführer einsetzen, der ihn weiterführt. Das nehmen wir als Änderungskandidaten für Rebirth auf; Erlös und passive Einnahmen sind noch offen.
- **Prüfungsereignis bei Unterschlagung, Sammlungsalbum, Themenwochen und Auktionen sowie sichtbare Kundenreaktionen und passende Effekte:** aufgenommen.
- **Gilden:** vorerst offen.

Als Nächstes: die 20-%-Regel und den weiterlaufenden alten Betrieb sauber mit Wirtschaft und Rebirth verbinden (→ D2, D3).

Einordnung für den Mac-Build:
- Echte Angriffe zwischen Spielern kommen nicht in den ersten Build (Teil B7). Die Regeln aus D2 gelten im ersten Build nur für Trainings-Raubzüge und für simulierte Einbrüche in den eigenen Betrieb. Die Datenstruktur soll D2 aber schon abbilden (Vermögen, angreifbarer Anteil, Verlustgrenzen), damit PvP später ohne Umbau dazukommt.
- Wachhunde: im ersten Build als Sicherheits-Einrichtung (Hundezwinger mit Ausbaustufen) möglich, getrennt von der Pension. Pensionstiere sind nie Wachhunde und nie betroffen.
- VIP-Betreuung: Pensions-Stufe mit höherem Preis pro Tier und höheren Anforderungen (Ausstattung, Personal). Erster Build optional.
- Prüfungsereignis, Sammlungsalbum, Themenwochen, Auktionen, Kundenreaktionen/Effekte: aufgenommen, Umfang im ersten Build nach §18; Unterschlagung samt Prüfungsereignis darf zurückgestellt werden (§5).
- Gilden: nicht bauen.

## D2. ENTWURF – 20-%-Regel und Rache (Zahlen vorläufig, Julian entscheidet)

**Vermögen (V)** = eigenes Spielgeld in der Kasse + eigene Ware zum Händler-Ankaufswert − offene Betreiberkredite.
Zählt nicht: Kundeneigentum, Kundengeld im Wertlager, Pfänder bis zum Verfall, Gebäude und Einrichtungen, Tiere, Rebirth-Coins, alles mit Echtgeld Gekaufte.

**Angreifbarer Anteil (A)** = 20 % von V, im Raubzug-Bildschirm des Opfers und des Angreifers als Zahl sichtbar.

**Beute pro Angriff**
- Ein Angriff erbeutet je nach Erfolg 0–50 % von A, also höchstens 10 % von V.
- Typisch (mittlere Sicherheit, ordentlicher Lauf): 20–30 % von A = **4–6 % von V**.
- Sicherheit senkt den Beuteanteil: Kameras, Laser, Tresorstufe und Wachhunde je bis −10 Prozentpunkte, zusammen höchstens −30. Wachhund: je Hund −5, höchstens 4 Hunde.

**Verlustgrenzen beim Opfer**
- Höchstens 20 % von V in 24 Stunden (also höchstens einmal A komplett).
- Kostenloser Schutz 4 Stunden nach einem Verlust ab 8 % von V oder nach 2 Angriffen innerhalb von 6 Stunden. Danach 8 Stunden, wenn es am selben Tag wieder passiert.
- Höchstens 3 Angriffe pro 24 Stunden auf denselben Spieler, vom selben Angreifer höchstens 1.
- Neue Spieler sind bis zum ersten Rebirth nicht angreifbar.

**Geld, das beim Angriff verschwindet (Abflüsse)**
- Crew-Anteile (10–40 % der Beute) gehen an niemanden, sie verschwinden.
- Ware aus der Beute wird zum Hehlerpreis (60 % des Werts) gutgeschrieben.
- Dadurch bekommt der Angreifer immer weniger, als das Opfer verliert.

**Rache**
- Nur gegen genau den Angreifer, innerhalb von 24 Stunden, einmal pro erlittenem Angriff. Auf eine Rache gibt es keine Gegen-Rache.
- Gleiche Regeln wie ein normaler Angriff, keine garantierte Auszahlung.
- **ENTSCHIEDEN (Karte 13:37):** Ein Racheangriff beendet den eigenen Schutz nicht (Ausnahme zu §12: „Eigener Angriff beendet Schutz“).
- Zurückgeholt wird höchstens der gestohlene Betrag (aus dem angreifbaren Anteil des Angreifers).
- **Rache-Bonus:** zusätzlich bis 25 % des gestohlenen Betrags. Der Bonus ist neu erzeugtes Geld, aber gedeckelt auf 25 % des Gestohlenen und auf höchstens 1 Stunde eigener Betriebseinnahmen. Den Bonus gibt es nur, wenn der erlittene Verlust mindestens 1 % von V war.

**Warum gegenseitige Angriffe kein Geld erzeugen**
Beispiel: A stiehlt B 1.000. Nach Crew (20 %) bleiben A 800. B holt sich per Rache 1.000 + 250 Bonus zurück und zahlt seiner Crew 20 %, bleibt bei 1.000. Bilanz beider zusammen: −200 (A) und 0 (B) → immer negativ. Selbst ohne Crew bleibt der Bonus durch die Deckel kleiner als die Hehler- und Crew-Abflüsse. Abgesprochenes Hin- und Her-Angreifen lohnt sich nie.

**Raubzüge im Verhältnis zum Betrieb**
- Ziel: Raubzüge bringen einem aktiven Spieler höchstens 20–30 % seines Gesamteinkommens, der Betrieb bleibt Hauptquelle.
- Erster Build (Training): feste Trainingsbeute ≈ 15 Minuten Betriebseinnahmen. Die ersten 3 Trainings pro Tag zahlen voll, danach 25 %.
- Gegner bei späterem PvP: gleiche Standortstufe und Vermögen zwischen 0,5- und 2-fach.

**Simulierte Einbrüche im ersten Build** (Teil B7): Verlust höchstens 10 % von V, folgt denselben Sicherheitsabzügen.

## D3. ENTWURF – Alter Betrieb beim Rebirth (Zahlen vorläufig, Julian entscheidet)

**ENTSCHIEDEN (Julian, Karte 13:37): Beides wählbar.** Beim Rebirth wählt der Spieler für den alten Standort Verkaufen oder Geschäftsführer. Die Zahlen unten bleiben Entwurf.

Beim Rebirth wählt der Spieler für den alten Standort:

**Variante A – Verkaufen**
- Erlös = 25 % des investierten Ausbauwerts (alles Spielgeld, das in Etagen und Einrichtungen geflossen ist).
- Ausgezahlt wird der Erlös **nicht als Spielgeld**, weil das beim Rebirth sowieso zurückgesetzt wird, sondern als **Rebirth-Coin-Bonus von +15 %** auf die Coins dieses Rebirths.
- **ENTSCHIEDEN (Karte 13:37):** Erlös nur als Coin-Bonus, kein Startkapital.

**Variante B – Geschäftsführer einsetzen**
- Einmalige Kosten vor dem Rebirth: 10 % des Rebirth-Geldbetrags (Personal einmalig, keine laufenden Kosten).
- Der alte Standort läuft „eingefroren“ weiter: Einnahmen = **5 % seiner letzten Stundeneinnahmen**, gutgeschrieben als Spielgeld am aktuellen Standort. Keine Ausbauten mehr, keine Kunden-Interaktion, nicht angreifbar. Ansehen kann man ihn als ruhige Ansicht.
- Zählt zur Offline-Grenze (4 Stunden), wird mit der normalen Offline-Abrechnung ausgezahlt.
- Rebirth-Coins dieses Rebirths werden normal vergeben, nur ohne den Verkaufsbonus.

**Grenzen gegen entwertetes Rebirth und endloses Passiveinkommen**
- Summe aller Geschäftsführer-Einnahmen höchstens **15 % der aktuellen Betriebseinnahmen**. Wer im neuen Standort wächst, bekommt mehr, wer nichts tut, nicht.
- Jeder weitere alte Standort zählt weniger: 1. = 100 %, 2. = 50 %, 3. = 25 %, ab dem 4. = 10 %.
- Höchstens 3 Geschäftsführer gleichzeitig. Für einen vierten muss ein alter Standort nachträglich verkauft werden; das bringt dann nur einen kleinen Spielgeld-Erlös (Vorschlag 5 % des Ausbauwerts) und keinen Coin-Bonus mehr.
- Neue Standorte verdienen pro Stufe deutlich mehr (Richtwert ×5 bis ×10), daher bleibt der alte Betrieb immer ein Zubrot.

Beispiel: Standort 1 verdient am Ende 1.000 pro Minute. Mit Geschäftsführer wären das 50 pro Minute. Standort 2 startet mit 200 pro Minute → Deckel 15 % = 30 pro Minute. Wächst Standort 2 auf 10.000 pro Minute, bringt Standort 1 die vollen 50 (0,5 %). Der Bonus hilft am Anfang etwas und wird dann unwichtig.

**Für den ersten Build:** Es gibt nur ein Rebirth (Standort 1 → 2). Variante A und B werden eingebaut (entschieden), Grenzen wie oben. Geschäftsführer-Typen siehe E2.4.

## D4. Entweder-oder-Punkte (alle entschieden)

1. ~~Alter Betrieb~~ **ENTSCHIEDEN 13:37: beides wählbar.**
2. ~~Verkaufserlös~~ **ENTSCHIEDEN 13:37: Rebirth-Coin-Bonus (+15 %), kein Startkapital.**
3. ~~Rache und Schutz~~ **ENTSCHIEDEN 13:37: Rache beendet den eigenen Schutz nicht (Ausnahme zu §12).**
4. ~~Sicherheit wirkt auf~~ **ENTSCHIEDEN 13:37: die Beute pro Angriff; der angreifbare Anteil bleibt fest bei 20 %.**

Alle vier Punkte aus D4 sind entschieden, alle wie vorgeschlagen.

---

# Teil E – Sammlung 3 (abgeschlossen 13.10.2026 13:37)

Ergänzt Teil A–D und geht bei Widerspruch vor. Laut Julian sind Preise, Wahrscheinlichkeiten und Bonuswerte noch offen, und nicht alles muss in den ersten Build. Alle acht Punkte kommen in den ersten Build (Karte 14:03); die Zahlen sind Startwerte.

## E1. Julians Anforderungen (13:37, wörtlich)

1. **Kundenwünsche erkennen:** Gespräche und Reaktionen geben Hinweise, ob Kunden schnell Geld brauchen, einen passenden Käufer suchen oder sichere Aufbewahrung bevorzugen.
2. **Sicherheit kombinieren:** Wachhunde, Kameras und Wachen arbeiten zusammen. Ein Hund entdeckt beispielsweise einen Eindringling, eine Kamera verfolgt ihn und eine Wache reagiert. Kombinationen müssen Gegenmaßnahmen zulassen.
3. **Beute strategisch auswählen:** Gegenstände unterscheiden sich in Wert, Gewicht und benötigter Entwendungszeit. Begrenzte Tragfähigkeit macht die Auswahl wichtig.
4. **Geschäftsführer mit Stärken:** Für weitergeführte alte Standorte unterschiedliche Geschäftsführer wählen – mit Schwerpunkten auf Gewinn, Ruf oder Sicherheit.
5. **Ansehen je Geschäftsbereich:** Handel, Wertlager, Pfandgeschäft und Tierpension besitzen getrennte Rufwerte. Gute Tierbetreuung schafft nicht automatisch Vertrauen für wertvolle Kunst.
6. **Warenpakete ankaufen:** Nachlässe oder größere Sammlungen als Paket anbieten. Der Spieler prüft Stichproben und entscheidet anhand von Preis, Unsicherheit und Lagerkapazität.
7. **Schaufenster gestalten:** Eigene Waren ausstellen. Die Auswahl beeinflusst, welche Käufer und Interessen angezogen werden. Kundeneigentum nicht ungefragt als Verkaufsware präsentieren.
8. **Spezialisierung wählen:** Viele günstige Geschäfte oder wenige hochwertige Kunden ermöglichen unterschiedliche Strategien. Beide Wege sollen sinnvoll spielbar sein.

Preise, Wahrscheinlichkeiten und Bonuswerte sind noch offen. Diese Anforderungen ergänzen die bisherigen Sammlungen; ihre Aufnahme bedeutet nicht, dass alle bereits im ersten Build umgesetzt werden müssen.

## E2. Umfang: alle 8 Punkte im ersten Build (entschieden 14:03)

Julian hat per Karte entschieden (14:03), dass alle acht Anforderungen in den ersten Build kommen. Alle Zahlen unten sind **Startwerte (ENTWURF)**. Der Mac-Build setzt sie direkt um, und zwar als Werte in einer zentralen Balancing-Datei, nicht fest im Code verteilt, damit Julian sie später ändern kann.

### E2.1 Kundenwünsche erkennen
- Jeder Kunde hat genau einen Wunsch: **schnell Geld** (passt zu Pfand), **Käufer gesucht** (passt zu Ankauf), **sicher aufbewahren** (passt zum Wertlager) oder **neutral**. Verteilung zum Start: 30 / 30 / 25 / 15 %.
- Im Gespräch zeigt sich der Hinweis zu 70 % eindeutig (Satz plus Symbol), zu 30 % nur andeutungsweise. „Nachfragen“ macht ihn sicher, kostet aber 3 Sekunden Kundengeduld.
- Passendes Angebot: +5 Ruf im jeweiligen Bereich, und die Annahmechance steigt um 20 Prozentpunkte. Unpassendes Angebot: kein Ruf, Annahmechance −10 Prozentpunkte.

### E2.2 Sicherheit kombinieren
- **Kette:** Hund erkennt (Radius 3 m, reagiert auf Geräusche) → Alarmstufe 1. Kamera erfasst (Sichtkegel 60°) → Alarmstufe 2, Wache wird gerufen. Wache erreicht den Dieb (Anlaufzeit 8 Sekunden) → Lauf endet, der Dieb behält 50 % der bis dahin getragenen Beute.
- **Gegenmaßnahmen:** Leckerli lenkt den Hund 10 Sekunden ab. Störsender schaltet eine Kamera 8 Sekunden ab (Ausrüstung, 2 Ladungen pro Lauf). Lärmquelle lockt die Wache 12 Sekunden weg. Ohne Sichtkontakt fällt der Alarm nach 15 Sekunden eine Stufe.
- **Erster Build:** voll in den Trainingsanlagen. Im eigenen Betrieb wirkt die Kette bei simulierten Einbrüchen: jedes Element −5 bis −10 Prozentpunkte Beute, alle drei zusammen zusätzlich −5. Gesamt höchstens −30 (D2).
- Wachhunde sind eigene, ausgebildete Hunde aus dem Hundezwinger. Pensionstiere sind nie beteiligt.

### E2.3 Beute strategisch auswählen
- Jeder Gegenstand hat Wert, Gewicht und Entwendungszeit. Startwerte je Art:

| Art | Gewicht | Entwendungszeit |
|---|---|---|
| Bargeldbündel | 1 kg | 2 s |
| Schmuck | 0,5 kg | 4 s |
| Uhr | 0,3 kg | 3 s |
| Elektronik | 4 kg | 5 s |
| Goldbarren | 12 kg | 6 s |
| Kunstwerk | 8 kg | 10 s |

- Tragfähigkeit des Diebs: 20 kg. Fahrer in der Crew und das Taschen-Upgrade bringen je +10 kg.
- Ab 50 % Last ist der Dieb 15 % langsamer, ab 80 % Last 30 % langsamer. Die Beute lässt sich jederzeit abwerfen.

### E2.4 Geschäftsführer mit Stärken (ersetzt den Standard-Geschäftsführer aus D3)
Beim Rebirth mit Variante B (D3) wählt der Spieler einen von drei Typen. Die Kosten sind für alle gleich: einmalig 10 % des Rebirth-Geldbetrags.

| Typ | Passive Einnahmen | Zusatzwirkung |
|---|---|---|
| Gewinn | 7 % der letzten Stundeneinnahmen | – |
| Ruf | 4 % | neuer Standort startet mit Ruf 100 in jedem Bereich, dazu +10 % Rufgewinn |
| Sicherheit | 4 % | aktueller Betrieb: −5 Prozentpunkte Beute bei Einbrüchen (zählt in den −30-Deckel) |

Die Grenzen aus D3 gelten weiter: alle Geschäftsführer zusammen höchstens 15 % der aktuellen Einnahmen, mit abnehmender Wirkung je weiterem Standort.

### E2.5 Ansehen je Geschäftsbereich
Siehe E3.

### E2.6 Warenpakete ankaufen
- **Freischaltung:** ab Handels-Ruf 300.
- **Angebot:** etwa alle 20 Minuten aktiver Spielzeit ein Paket („Nachlass“ oder „Sammlung“) mit 8–20 Stück. Es ist 10 Minuten gültig, und es gibt immer nur ein offenes Angebot.
- **Wert und Preis:** Der Verkäufer verlangt 60–80 % des Schätzwerts. Der echte Wert liegt zwischen −40 % und +40 % des Schätzwerts, und 0–25 % der Stücke sind Fälschungen.
- **Stichproben:** 3 Stück prüfen ist gratis. Jede weitere Prüfung kostet 2 % des Paketpreises oder läuft über den Gutachter. Jede Stichprobe engt die Spanne um etwa 10 Prozentpunkte ein.
- **Lager:** Das Paket braucht so viele freie Lagerplätze, wie es Stück hat. Ist zu wenig Platz frei, kann der Spieler trotzdem kaufen, verkauft den Überschuss dann aber sofort zu 50 % an einen Händler. Das wird vor dem Kauf angezeigt.

### E2.7 Schaufenster gestalten
- **Plätze:** 3 zum Start, durch Ausbau bis 8.
- **Nur eigene Ware:** Kundeneigentum und noch nicht verfallene Pfänder sperrt die Oberfläche („Kundeneigentum – nicht ausstellbar“).
- **Wirkung:** Jedes ausgestellte Stück erhöht die Chance auf Käufer seiner Kategorie um 5 %, je Kategorie höchstens um 40 %. Stücke über dem Premium-Schwellwert ziehen mehr Premium-Kunden an.
- **Verkauf:** Ausgestellte Ware ist verkäuflich, Käufer zahlen darauf +10 %.

### E2.8 Spezialisierung wählen
- **Wahl:** ab Etage 2 des Standorts. Bis dahin ist der Betrieb neutral.
- **Wechsel:** einmal pro Standort kostenlos, danach kostet er 10 % des aktuellen Spielgelds. Beim Rebirth wird die Spezialisierung zurückgesetzt.
- **Masse:** +30 % Kundenfrequenz, −10 % Marge, Kunden warten weniger lang.
- **Premium:** −40 % Kundenfrequenz, +50 % Durchschnittswert je Geschäft, Ruf wirkt doppelt auf hochwertige Kunden.
- **Balancing-Ziel:** Bei gleichem Ausbau liegen beide Wege höchstens ±10 % auseinander, gemessen in Einnahmen pro Stunde. Der Test prüft das.

## E3. ENTWURF – Ansehen je Geschäftsbereich (ersetzt das einfache Ansehen)

Bisher gab es ein einziges Ansehen (Stern in der Kopfleiste, Rebirth-Voraussetzung, Sterne im Tab Kunden). Neu:

- **Vier Rufwerte:** Handel, Wertlager, Pfandgeschäft, Tierpension. Jeder läuft von 0 bis 1.000 und wird freigeschaltet, sobald der Bereich offen ist.
- **Was sie steuern:** welche Kunden in diesem Bereich kommen. Je höher der Bereichs-Ruf, desto wertvollere Ware, Einlagerungen, Pfänder oder anspruchsvollere Tiere (VIP-Betreuung, D1). Beispiel: Kunst über einem bestimmten Wert kommt nur bei Handels-Ruf ab 600.
- **Kein Übertrag** (entschieden 14:03): Gute Tierbetreuung hebt nur den Pensions-Ruf.
- **Gesamtansehen** = Durchschnitt der freigeschalteten Bereiche; das ist die Rebirth-Voraussetzung (entschieden 14:03). Es steht weiter als Stern in der Kopfleiste. Im Tab Kunden stehen die vier Werte einzeln mit Balken (UI-Vorgabe B6 entsprechend erweitern).
- **Was den Ruf bewegt:** faire Abschlüsse, passendes Angebot zum Kundenwunsch (E2 #1), pünktliche Rückgabe, gute Betreuung → plus. Schlechte Behandlung, verlorene oder beschädigte Kundensachen, entdeckte Unterschlagung → minus, nur im betroffenen Bereich.
- **Rebirth:** Rufwerte werden mit dem Standort zurückgesetzt. Ein Rebirth-Shop-Bonus „Startansehen“ ist denkbar, kommt aber nicht in den ersten Build (Rebirth-Shop hat genau 4 Boni, §10).

## E4. Entweder-oder-Punkte (alle entschieden)

1. ~~Rebirth-Voraussetzung Ansehen~~ **ENTSCHIEDEN 14:03: Gesamtansehen (Durchschnitt der freigeschalteten Bereiche).**
2. ~~Übertrag zwischen Bereichen~~ **ENTSCHIEDEN 14:03: kein Übertrag.**
3. ~~Umfang erster Build~~ **ENTSCHIEDEN 14:03: alle 8 Punkte im ersten Build.**

---

# Teil F – Sammlung 4 (ab 14.10.2026 07:09)

Ergänzt Teil A–E und geht bei Widerspruch vor.

## F1. Julians Punkte (14.10. 07:09, wörtlich)

> es soll mit echtem geld sein und nicht mit spielgeld das ist unrealistisch das ist nicht gut und den kredit und alles besser erklären und die normale ansicht soll von viel weiter oben kommen nicht von so komisch schräg

## F2. Euro statt Spielgeld (ersetzt B9)

- Alle Beträge im Betrieb stehen als **Euro mit realistischen Preisen** da: Kontostand „12.460 €“, Ankauf „200 €“, Kredit „150 €“. Das Wort „Spielgeld“ und Goldmünzen als Ladenwährung entfallen überall (Spiel, Shop-Texte, Store-Texte).
- Es bleibt Geld **im Spiel**: Es kann nie ausgezahlt und nie gegen echtes Geld getauscht werden. Echtes Geld gibt der Spieler nur über die drei Shop-Käufe aus (Preise aus StoreKit). Das steht einmal in den Einstellungen und in den Store-Texten, damit es keine Verwechslung mit Echtgeld-Glücksspiel gibt.
- **Rebirth-Coins** bleiben eine eigene violette Währung (Julian hat dazu nichts geändert). Keine Premiumwährung (C1 unverändert).
- **ENTWURF realistische Startwerte** (ersetzen die Zahlen in UI-Vorgabe Teil 8, Julian kann ändern):

| Was | Bisher | Neu |
|---|---|---|
| Startkapital | 1.000 | **5.000 €** |
| Ankauf / Verkauf Armbanduhr | 200 / 330 | **200 € / 330 €** |
| Pfandkredit Kamera | 150, Gebühr 30 | **150 €, Gebühr 15 € (10 %)** |
| Theke ausbauen (erste Stufen) | 100 | **250 €** (+12 % je Stufe) |
| Verkäufer einstellen (einmalig) | 600 | **1.500 €** |
| Wertlager freischalten | 1.500 | **4.500 €** |
| Lagergebühr pro Fach und Spieltag | – | **12 €** |
| Restaurierung Stuhl | 350 | **80 € Material**, Wert 300 € → 520 € |
| Tierpension freischalten | 6.000 | **18.000 €** |
| Geldziel Neustart Standort 1 | 25.000 | **250.000 €** |
| Geldziel Standort 2 | 50.000 | **500.000 €** |
| Starterpaket (2,99 €) | 5.000 Spielgeld | **5.000 € Startkapital im Spiel** |

Kunden-Einnahmen werden so angehoben, dass die Zeitpunkte aus UI-Vorgabe Teil 8 gleich bleiben.

## F3. Kredit und alle Systeme erklären

- Jedes System bekommt beim ersten Mal eine **Erklärkarte** mit drei Schritten in Euro-Beispielen und danach einen „?“-Knopf (UI-Vorgabe K5).
- **Pfandkredit** (Kunde leiht von dir): Du zahlst 150 € aus, der Kunde lässt die Kamera als Sicherheit da, holt sie in 2 Spieltagen gegen 165 € ab, sonst gehört sie dir. Auf der Karte steht immer die Rückzahlungssumme.
- **Bank-Kredit** (du leihst dir Geld, §-Regel „Kredit ≤ eigener Bestand“): Erklärkarte zeigt Betrag, Zinsen pro Spieltag, automatische Rückzahlung und dass offene Kredite den Neustart blockieren. ENTWURF: 5 % Zinsen auf die ganze Laufzeit, Rückzahlung in 5 Spieltagen.
- Weitere Erklärkarten: Ankauf & Verkauf, Wertlager, Werkstatt, Personal, Tierpension, Raubzug, Neustart.

## F4. Hauptansicht von weit oben

- Laden-Hauptansicht (B1) fast als Draufsicht (≈ 70°), gerade ausgerichtet, ohne seitliche Drehung, weit herausgezoomt. Gebäudeübersicht (A3) gerade von vorne und deutlich von oben statt 20° gedreht. Schräge Blicke nur noch in Nahansichten (Theke, Raubzug). Details: UI-Vorgabe Regel 6.



---

# Teil G – Überarbeitungsliste nach Screenshot-Prüfung (14.10.2026 07:45)

Julian hat alle 25 Screenshots von Build 1.0 geprüft. Diese Liste gilt verbindlich und geht bei Widerspruch vor Teil A–F. **Seine Reihenfolge (G1, „Meine Reihenfolge“) ist die Arbeitsreihenfolge.** Neue Inhalte kommen zuletzt (Punkt 8): „Jetzt nicht noch 20 neue Funktionen einbauen.“

## G1. Julians Liste (wörtlich)

> Ich habe alle 25 aktuellen Screenshots geprüft. Ehrlich: Vaultoria sieht bereits nach einem richtigen Mobile-Game aus. Es fehlt nicht an Inhalt – das größte Problem ist momentan, dass die vielen guten Systeme auf dem kleinen Bildschirm teilweise zu voll und unübersichtlich wirken.
> Unbedingt zuerst verbessern
>
> 1. Mehr vom Spiel, weniger Benutzeroberfläche
> Auf manchen Bildschirmen verdecken Menüleisten, Aufgaben, Hinweise und Karten fast die komplette Spielwelt. Besonders beim Handel sieht man vom Laden kaum noch etwas.
> Lösung:
>    * Aufgabenleiste einklappbar machen
>    * Besitz nur als kleine Leiste zeigen und beim Antippen öffnen
>    * Große Fenster als Bottom-Sheet einblenden
>    * Während kein Menü geöffnet ist, mindestens 60–70 % der Spielwelt zeigen
> 2. Texte und Buttons größer und ruhiger
> Auf einem echten iPhone sind einige Erklärungen, Werte und graue Texte sehr klein. Besonders Shop, Rebirth-Shop, Bank und Betriebsübersicht.
>    * Mindestens 16 pt für wichtige Texte
>    * Serifenschrift nur für Überschriften und Vaultoria-Branding
>    * Erklärungen kürzen
>    * Wichtigste Zahl pro Karte deutlich hervorheben
>    * Nicht mehr als einen grünen Hauptbutton pro Fenster
> 3. Navigation überall gleich halten
> Die untere Navigation verändert sich zwischen den Bildschirmen. Dadurch kann man schnell die Orientierung verlieren.
> Mein Vorschlag:
>    * Laden
>    * Besitz
>    * Personal
>    * Werkstatt
>    * Mehr
> Unter „Mehr“ kommen Kunden, Album, Aufträge, Statistik und Einstellungen. Wertlager und Tierpension können direkt über das Gebäude geöffnet werden.
> 4. Tutorial nicht alles gleichzeitig erklären
> „Dein erster Laden“ ist gut, aber Titel, Hand-Symbol, Besitzleiste und Handelssystem erscheinen gleichzeitig.
> Besserer Start:
>    1. Kunde kommt herein
>    2. Kunde antippen
>    3. Gegenstand prüfen
>    4. Preis einstellen
>    5. Gegenstand kaufen
>    6. Restaurieren oder direkt verkaufen
>    7. Erst danach Personal und Ausbau zeigen
>
> Optisch verbessern
>
> * Die gold-grün-braune Gestaltung passt sehr gut zum Pfandhaus-Thema.
> * Die Spielwelt braucht aber mehr Kontrast: Laden, Werkstatt, Wertlager und Tierpension sollten jeweils eigene Farben, Beleuchtung und Ausstattung bekommen.
> * Kunden sollten bessere Schatten, deutlichere Gesichter und abwechslungsreichere Kleidung erhalten.
> * Bei Verkäufen fehlen noch befriedigende Effekte: Geld zählt hoch, Gegenstand bewegt sich über den Tresen, Kunde reagiert und der Ruf steigt sichtbar.
> * Leere Flächen im Shop entfernen. Nicht verfügbare Käufe entweder ausblenden oder mit „Demnächst“ versehen.
> * Die abgerundeten oberen Shop-Fenster passen noch nicht ganz zur restlichen Oberfläche. Alle Fenster sollten dieselbe Formensprache verwenden.
>
> Spielerisch verbessern
> Der stärkste Spielablauf sollte immer sein:
> Gegenstand entdecken → Wert einschätzen → verhandeln → verbessern → verkaufen oder sammeln → Laden ausbauen
> Diesen Ablauf würde ich stärker ins Zentrum stellen. Personal, Tiere, Bank und Raubzüge sind Erweiterungen davon.
> Besonders gute Ergänzungen wären:
>
> * Seltenheitsstufen und besondere Fundstücke
> * Fälschungen, beschädigte Ware und versteckte Merkmale
> * Kunden mit unterschiedlichen Persönlichkeiten
> * Stammkunden, Sammler und betrügerische Kunden
> * Ereignisse wie Flohmarkt, Nachlass, Auktion oder prominenter Kunde
> * Vergleich: Einkaufspreis, Reparaturkosten und erwarteter Gewinn
> * Entscheidung: schnell verkaufen oder auf den richtigen Käufer warten
> * Gegenstände direkt im Laden sichtbar ausstellen
> * Mitarbeiter mit echten Stärken und Schwächen
>
> Raubzüge
> Der Raubzug ist eine starke Abwechslung und kann ein echtes Werbemerkmal werden. Aktuell wirkt er optisch aber noch deutlich einfacher als das Hauptspiel.
> Verbesserungen:
>
> * Sichtkegel verständlicher, aber leicht transparenter
> * Ziel und Ausgang deutlich markieren
> * Wachhunde, Kameras, Bewegungsmelder und verschlossene Räume
> * Auswahl zwischen sicherer kleiner Beute und riskanter wertvoller Beute
> * Gegenstände sichtbar tragen
> * Vibration und Zeitlupe bei knappem Entkommen
> * Automatik bringt weniger Beute als manuelles Spielen
> * Konsequenzen wie Verletzungen, Verlust oder vorübergehend höheres Risiko
>
> Umzug und Rebirth
> Der Bildschirm enthält aktuell zu viele Informationen auf einmal. Vor dem Neustart braucht es eine einfache Zusammenfassung:
>
> * Du verlierst: Geld, Ladenstufen und normale Gegenstände
> * Du behältst: gekaufte Designs, Werbefreiheit und dauerhafte Boni
> * Du erhältst: 20 Rebirth-Coins
> * Neuer Standort: mehr Etagen, Kunden und Funktionen
>
> Danach erst ein deutliches Bestätigungsfenster.
> Meine Reihenfolge
>
> 1. Oberfläche entschlacken
> 2. Tutorial verbessern
> 3. Navigation vereinheitlichen
> 4. Verkauf und Verhandlung befriedigender animieren
> 5. Räume optisch unterscheiden
> 6. Raubzüge ausbauen
> 7. Wirtschaft und Preise ausbalancieren
> 8. Neue Inhalte ergänzen
>
> Wichtig: Jetzt nicht noch 20 neue Funktionen einbauen. Das Spiel besitzt bereits genug Systeme. Die nächste Entwicklungsphase sollte dafür sorgen, dass sich Kaufen, Verhandeln, Restaurieren und Verkaufen richtig gut anfühlt. Das macht Vaultoria wesentlich wertvoller als noch mehr Menüpunkte.

## G2. Was sich dadurch an früheren Festlegungen ändert

1. **Tab-Leiste** jetzt dauerhaft: Laden · Besitz · Personal · Werkstatt · Mehr (ersetzt Laden · Wertlager · Personal · Werkstatt · Kunden). Wertlager und Tierpension öffnet man über ihre Etage im Gebäude. Kunden, Album, Aufträge, Statistik und Einstellungen liegen unter „Mehr“. Was noch nicht gebaut ist, ist ausgeblendet oder trägt „Demnächst“.
2. **Tutorial** folgt den 7 Schritten (Kaufen → Prüfen → Preis → Kaufen → Restaurieren oder Verkaufen, erst dann Personal und Ausbau). Pfand, Wertlager und Raubzug kommen nach Schritt 7. Neue Fassung in UI-Vorgabe Teil 8.
3. **Raubzug:** „Automatik bringt weniger Beute als manuelles Spielen“ ersetzt „manuell und automatisch gleichwertig“ (Teil A). ENTWURF: Automatik bringt 70 % der Beute, die beim manuellen Spielen möglich ist. Konsequenzen wie Verletzung der Crew sind nur vorübergehend (Crew-Mitglied 1 Spieltag nicht verfügbar). Tiere bleiben nie verletzt und nie Beute.
4. **Rebirth-Belohnung** im Beispiel jetzt 20 Rebirth-Coins (bisher +12). Vor dem Neustart kommt zuerst eine einfache Zusammenfassung mit vier Blöcken, erst danach das Bestätigungsfenster (UI-Vorgabe A4).
5. **Ergänzungen** (Seltenheit, Fälschungen, Persönlichkeiten, Ereignisse usw.) sind als Ideen notiert. Was davon in Teil A, D oder E schon steht, wird in Punkt 8 umgesetzt, nicht vorher.
