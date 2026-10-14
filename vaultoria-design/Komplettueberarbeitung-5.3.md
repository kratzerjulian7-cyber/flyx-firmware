# Vaultoria – Komplettüberarbeitung 5.3 (verbindlich)

Stand 14.10.2026, 14:40. Julians Auftrag vom 14.10.2026 14:30 und Nachträge 14:36 und 14:43, **wörtlich** unten. Geht bei Widerspruch allen anderen Dateien vor (`Spielkonzept-Pannenhilfe.md`, `UI-Vorgabe-Pannenhilfe.md`, `Erweiterungsplan-Pannenhilfe.md`); diese bleiben als Detail- und Zahlenquelle gültig.

## Einordnung (Docs-Thread)

- **Was 5.3 ist:** ein polierter vertikaler Ausschnitt der ersten Spielphase (erste 30–60 Minuten), gebaut auf 5.1 als technischer Grundlage. Enthält: Starttempo (Erweiterungsplan 5b Punkt 1), Premium-UI und einheitlichen Modelltausch (UI-Vorgabe 000b), E1.6 Transparenz (Plan 5c), **E1.5 komplett** (Plan 5b, inkl. Container und Ausbaustufen) sowie alles unten.
- **Keine Zwischenversion auf TestFlight.** 5.2 wird nicht separat hochgeladen; der nächste Upload ist 5.3, wenn alles unten erfüllt ist.
- **Erst danach** E2 und die folgenden Stufen des Erweiterungsplans.
- **Wo dieser Auftrag Neueres festlegt als die anderen Dateien:**
  - Sichtbare Fahrzeugstatus sind Julians 8: frei · Anfahrt · vor Ort · transportiert Fahrzeug · lädt ab · Rückfahrt · Wartung · Problem. Die feineren Phasen aus Plan 5c Punkt 6 (Aufladen, Tanken, Außer Dienst) bleiben intern und werden auf diese 8 abgebildet.
  - Mitarbeiter: **genau eine** erkennbare Stärke oder Schwäche, dazu Reparatur, Abschleppen, Geschwindigkeit, Zuverlässigkeit, Erfahrung, Schicht/Müdigkeit, Führerscheine (ersetzt für 5.3 die R6-Regel „1 Stärke + 1 Schwäche + max. 1 Eigenschaft“).
  - Höchstens **4 gleichzeitige Aufträge** am Anfang (zusätzlich zum Tagesbudget 8–12).
  - Neu für 5.3: Diagnose vor Ort, zweites Fahrzeug anfordern, Ausgänge „falsch gemeldet“, „Kunde storniert“, „nicht sicher reparierbar“, „Folgeauftrag“; Kosten vorab auch Entsorgung, Partnerkosten, Vertragsboni/-strafen; Bewertung mit Begründung; Kamera folgt eigenem Fahrzeug; Marker beim Herauszoomen kleiner/zusammengefasst; Tag/Abend/Nacht; Sounds und Haptik abschaltbar; Hof mit Werkstatt und Tank-/Ladebereich.
  - Stil: einheitlich, realistische Materialien auf stilisierten Formen, keine Mischung aus fotorealistischen Bildern und Low-Poly-Modellen (präzisiert UI-Vorgabe 000b Punkt 7).
- **Firmenentwicklung (Nachtrag 14:43):** zentrales Fortschrittssystem, 5 Firmenstufen + Bausystem auf freien Hofflächen. In 5.3: **Firmenstufe 1 komplett + Bausystem mit den ersten Ausbauten Richtung Stufe 2** (Erweiterungsplan Teil 2b). Garage/Werkstatt/Leitstelle mit je 3 Stufen entfallen.
- **Monetarisierung (Julian 14.10.2026 14:43, verbindlich):** Das normale Firmenwachstum ist Teil des kostenlosen Spiels. Echtgeld schaltet **nur** besondere Designs, Gebäudevarianten oder Lackierungen frei, **nie** den normalen Ausbau, keine Zeitverkürzung, kein Spielgeld, keine Vorteile. Ob und wann es solche Käufe gibt, entscheidet Julian.
- **Lieferung an Julian:** TestFlight-Build 5.3, Screenshots aller überarbeiteten Bereiche, kurzes Video eines kompletten Einsatzes, Änderungsliste, ehrliche Schwächenliste, Testergebnisse, Sicherung von 5.1.

## Julians Auftrag (wörtlich, 14.10.2026 14:30)

mache das alles 1:1 das ich positiv sehr überrascht bin wenn ich das mir wieder anschaue Dann machen wir keinen kleinen Patch mehr. Claude soll Vaultoria 5.1 komplett durchgehen und aus dem aktuellen Prototyp ein richtiges, zusammenhängendes Spiel machen. Der Kern bleibt Pannenhilfe-Tycoon mit Draufsicht – aber nahezu alles darf verbessert oder neu gebaut werden.
Schick Claude genau das:
Komplettüberarbeitung Vaultoria
Überarbeite Vaultoria vollständig. Ich möchte beim nächsten Öffnen der TestFlight-Version deutlich positiv überrascht sein. Behandle die aktuelle 5.1 nicht als fertiges Spiel, sondern als technische Grundlage.
Unveränderbarer Kern

* Name bleibt Vaultoria.
* Pannenhilfe- und Abschlepp-Tycoon aus der Draufsicht.
* Ich fahre nicht selbst.
* Ich entscheide, welche Mitarbeiter und Fahrzeuge zu welchen Einsätzen fahren.
* Fahrzeuge bewegen sich sichtbar durch eine lebendige Stadt.
* Die Karte bleibt der Mittelpunkt.
* Keine Rückkehr zum Pfandhaus-Spiel.
* Keine überladene Menüstruktur.
* Graphit, Silber und gezieltes Einsatz-Orange bleiben die Designsprache.

Alles andere darf hinterfragt, umgebaut oder ersetzt werden.
1. Zuerst das gesamte Spiel prüfen
Gehe jede vorhandene Ansicht, Funktion, Berechnung und Interaktion durch:

* Was ergibt spielerisch keinen Sinn?
* Wo fehlen Informationen?
* Wo verschwinden Fahrzeuge, Geld, Material oder Zeit ohne Erklärung?
* Welche Schritte wirken wie eine technische Demo?
* Welche Texte sind unverständlich, abgeschnitten oder zu klein?
* Welche Funktionen existieren nur optisch, haben aber keine Wirkung?
* Wo fehlen Animationen, Sounds oder Rückmeldungen?
* Was ist langweilig, hektisch oder unnötig kompliziert?

Nicht nur meine genannten Punkte abarbeiten. Eigenständig alle Schwächen finden und sinnvoll verbessern.
2. Vollständiger Einsatzablauf
Jeder Auftrag benötigt einen nachvollziehbaren Ablauf:

1. Auftrag geht sichtbar und hörbar ein.
2. Einsatzart, Standort, Fahrzeugtyp, Dringlichkeit und Kundenwartezeit werden gezeigt.
3. Einnahmen, Kosten, Risiko und erwarteter Gewinn werden verständlich dargestellt.
4. Spieler wählt Mitarbeiter, Einsatzfahrzeug, Ausrüstung und gegebenenfalls Zielort.
5. Fahrzeug verlässt sichtbar die Zentrale.
6. Route, Verkehr, Ankunftszeit und Status sind sichtbar.
7. Vor Ort erfolgt eine Diagnose.
8. Der Einsatz kann unterschiedliche, aber nachvollziehbare Ausgänge haben.
9. Material wird tatsächlich verbraucht.
10. Bei Bedarf wird ein zweites Fahrzeug angefordert.
11. Abgeschleppte Fahrzeuge werden sichtbar transportiert.
12. Fahrzeug wird am Betriebshof, bei einer Werkstatt, der Polizei oder am Schrottplatz abgeladen.
13. Einsatzfahrzeug fährt anschließend zurück.
14. Erst nach der Rückkehr ist es wieder verfügbar.
15. Danach erscheint eine vollständige Einsatzabrechnung.

Kein Fahrzeug und kein Auftrag darf einfach verschwinden.
3. Kosten und Einnahmen vollständig erklären
Vor jedem Einsatz:

* erwartete Einnahmen
* Kraftstoff
* Ersatzteile
* Mitarbeiterzeit
* Fahrzeugverschleiß
* Entsorgung
* Partnerkosten
* mögliche Vertragsboni oder Strafen
* erwarteter Gewinn
* Hinweis, dass es sich um eine Schätzung handelt

Nach jedem Einsatz:

* tatsächliche Kundenzahlung
* alle tatsächlichen Kosten
* Gewinn oder Verlust
* verbrauchte Materialien
* Mitarbeitererfahrung
* Fahrzeugzustand
* Bewertung mit verständlicher Begründung
* Zielort des Kundenfahrzeugs
* mögliche Folgeaktion

Jede Veränderung des Kontostands muss nachvollziehbar sein. Ergänze ein einfaches Kassenbuch und eine Auftragshistorie.
4. Betriebsmittel und Entsorgung
Ergänze ein verständliches Lager für:

* Batterien
* Pkw- und Transporterreifen
* Kraftstoff
* allgemeine Ersatzteile
* Ölbindemittel

Nach Einsätzen entstehen:

* Altreifen
* defekte Batterien
* Altöl
* beschädigte Teile
* Unfallschrott

Diese landen sichtbar in begrenzten Bereichen des Betriebshofs.

* Entsorgung kann Geld kosten.
* Batterien und Metallschrott können einen kleinen Erlös bringen.
* Fehlende Teile verhindern passende Reparaturen.
* Bestände lassen sich bestellen und werden sichtbar geliefert.
* Keine Verwaltung einzelner Schrauben.
* Bestand bereits bei der Einsatzwahl anzeigen.

5. Betriebshof
Der Betriebshof muss ein echter Bestandteil des Spiels sein:

* sichtbare Stellplätze
* begrenzte Kapazität
* abgestellte Kundenfahrzeuge
* eigene Fahrzeuge
* Reifenlager
* Teilelager
* Entsorgungscontainer
* Werkstatt
* Tank- oder Ladebereich
* später Sammlung und Restaurierung

Fahrzeuge benötigen je nach Größe unterschiedlich viel Platz. Ein voller Hof muss echte Auswirkungen haben. Ausbauten verändern den Hof sichtbar und zeigen vorher Preis sowie konkreten Nutzen.
6. Mitarbeiter
Jeder Mitarbeiter erhält:

* Reparaturfähigkeit
* Abschleppfähigkeit
* Geschwindigkeit
* Zuverlässigkeit
* Erfahrung
* Schicht und Müdigkeit
* benötigte Führerscheine
* genau eine erkennbare Stärke oder Schwäche

Beispiele:

* besonders gut bei Nacht
* schnell, verursacht aber mehr Verschleiß
* langsam, dafür sehr zuverlässig
* Spezialist für Diagnose
* Spezialist für Bergungen

Bei der Auswahl muss verständlich sein, warum jemand geeignet oder ungeeignet ist.
7. Fahrzeuge
Jedes Fahrzeug benötigt:

* klaren Einsatzzweck
* Zustand
* Kraftstoff oder Akkustand
* Ausrüstung
* Geschwindigkeit
* Kapazität
* laufende Kosten
* aktuellen Status
* voraussichtliche Verfügbarkeit

Status:

* frei
* Anfahrt
* vor Ort
* transportiert Fahrzeug
* lädt ab
* Rückfahrt
* Wartung
* Problem

Eigene Fahrzeuge müssen auf der Karte jederzeit klar erkennbar und antippbar sein. Beim Antippen kann die Kamera ihnen folgen.
8. Einsätze und Entscheidungen
Für den Anfang sauber ausarbeiten:

* Batterie leer
* Reifenpanne
* ausgesperrt
* Kraftstoff leer
* kleiner technischer Defekt
* Abschleppen
* einfache Unfallbergung

Nicht jeder Einsatz endet gleich. Der Ausgang wird hauptsächlich durch Mitarbeiter, Fahrzeug, Material und Entscheidung bestimmt. Zufall bleibt nur ein kleiner Faktor.
Mögliche Entwicklungen:

* Reparatur gelingt vor Ort
* zusätzliches Teil wird benötigt
* Kunde muss abgeschleppt werden
* zweites Fahrzeug erforderlich
* Auftrag war falsch gemeldet
* Kunde storniert
* Fahrzeug kann nicht sicher repariert werden
* Folgeauftrag entsteht

9. Spieltempo und Balance

* Ein Spieltag dauert bei 1× ungefähr 18 Minuten.
* Pause, 1×, 2× und 4×.
* Automatische Pause bei dringenden Einsätzen und Entscheidungen.
* Anfangs ungefähr 8–12 Einsätze pro Tag, nicht 43–49.
* Maximal vier gleichzeitige Aufträge am Anfang.
* Ruhige Phasen dürfen existieren, aber nicht langweilig werden.
* Die ersten 30 Minuten müssen verständlich und motivierend sein.
* Geld darf weder bedeutungslos noch dauerhaft knapp sein.
* Fehlentscheidungen müssen spürbar, aber nicht spielzerstörend sein.

10. UI vollständig neu prüfen
Die Karte bleibt zentral. Verwende weiterhin nur:

* Karte
* Flotte
* Zentrale
* Personal

Anforderungen:

* einheitliche Abstände, Rundungen und Schriftgrößen
* keine abgeschnittenen Texte
* mindestens 44 × 44 Punkte große Touchflächen
* normale Ansicht zeigt nur Wichtiges
* vollständige Zahlen hinter „Details“
* klare Auswahlzustände
* verständliche Warnungen
* kein unnötiges Gold
* Orange ausschließlich für Einsätze, Warnungen und aktive Aktionen
* Grün für verfügbar oder erfolgreich
* Rot nur für echte Probleme und Dringlichkeit
* Silber und Graphit als Grundlage
* verschiedene Symbole für jede Einsatzart
* Marker werden beim Herauszoomen kleiner oder zusammengefasst
* Route muss auf jedem Straßenabschnitt erkennbar bleiben
* Geld, Ruf, Zeit und Geschwindigkeit dürfen den Bildschirm nicht überladen

11. Stadt und Präsentation

* Einheitlicher Stil zwischen Fahrzeugen, Gebäuden, Kartenbildern und Stadt.
* Keine Mischung aus fotorealistischen Bildern und unpassenden Low-Poly-Modellen.
* Realistische Materialien dürfen auf stilisierten Formen verwendet werden.
* Verkehr und Stadt sollen belebt wirken.
* Straßenlaternen, Fenster, Scheinwerfer und Rundumlichter sinnvoll einsetzen.
* Tag-, Abend- und Nachtstimmung.
* Dezente Kameraanimationen.
* Keine übertriebenen Effekte oder störendes Leuchten.
* Zentrale und Ausbauten müssen auf der Karte sichtbar wachsen.

12. Sound, Haptik und Rückmeldung
Ergänze hochwertige, dezente Rückmeldungen:

* eingehender Auftrag
* dringender Einsatz
* Fahrzeug startet
* Auftrag erfolgreich
* Auftrag fehlgeschlagen
* Geld erhalten oder bezahlt
* Ausbau abgeschlossen
* Warnung bei fehlendem Material

Sounds und Haptik müssen abschaltbar sein. Keine dauernden oder nervigen Sirenen.
13. Einstieg
Ein neuer Spieler muss ohne Erklärung verstehen:

* wie ein Auftrag angenommen wird
* wie Mitarbeiter und Fahrzeug ausgewählt werden
* was der Einsatz ungefähr kostet
* wie Gewinn entsteht
* warum ein Fahrzeug nicht verfügbar ist
* wohin ein abgeschlepptes Auto gebracht wird
* wie Material nachbestellt wird
* wie der Betrieb wächst

Einführung direkt im echten Spiel, keine lange Textwand. Hinweise nach der ersten erfolgreichen Nutzung nicht erneut anzeigen.
14. Qualität
Vor dem Upload:

* jede Ansicht auf verschiedenen iPhone-Größen prüfen
* keine Platzhalter
* keine abgeschnittenen Texte
* keine wirkungslosen Buttons
* keine unerklärlichen Geldbewegungen
* keine verschwindenden Fahrzeuge
* Speichern und Laden mehrfach testen
* Zeitgeschwindigkeiten müssen dasselbe Ergebnis erzeugen
* flüssige Karte und Animationen
* vollständiger Spieltag im Simulator und auf echtem Gerät
* mindestens zehn unterschiedliche komplette Einsätze durchspielen
* Wirtschaft über mindestens 20 simulierte Spieltage prüfen
* bestehende Spielstände sicher migrieren
* alle automatisierten Tests müssen grün sein

Lieferung
Keine unfertige Zwischenversion hochladen. Erstelle zunächst intern einen vollständigen, polierten vertikalen Ausschnitt des Spiels. Schicke mir erst dann:

* neuen TestFlight-Build
* Screenshots aller überarbeiteten Bereiche
* kurzes Video eines vollständigen Einsatzes
* Liste aller Änderungen
* ehrliche Liste verbleibender Schwächen
* Testergebnisse
* Sicherung der bisherigen Version

Ich möchte nicht nur eine abgearbeitete Liste sehen. Das Spiel soll sich beim nächsten Öffnen zusammenhängend, verständlich, hochwertig und überraschend vollständig anfühlen. Triff eigenständig gute Entscheidungen, wenn Details fehlen. Neue Funktionen sind nur sinnvoll, wenn der bestehende Ablauf dadurch besser wird.
Das ist jetzt ein richtiger Qualitäts-Neuaufbau. Claude soll nicht sofort die gesamten geplanten 100 Spielstunden bauen. Er soll zunächst die vorhandene erste Spielphase so gut machen, dass bereits die ersten 30–60 Minuten wirklich Spaß machen. Danach werden die Langzeit-Erweiterungen daraufgesetzt.

## Nachtrag (wörtlich, Julian 14.10.2026 14:36)

5.3 muss nicht nur vollständig funktionieren, sondern eine eigene Identität und Motivation besitzen. Der Spieler soll nach einem Einsatz freiwillig noch einen Auftrag erledigen wollen. Wachstum muss auf der Karte sichtbar sein, Entscheidungen müssen echte Unterschiede erzeugen und ruhige Momente dürfen nicht leer wirken. Prüfe außerdem Schwierigkeitsgrade, Atmosphäre, Wiederaufnahme, Schutz vor unrettbaren Spielständen und langfristige Motivation. Danach keine weiteren Funktionen hinzufügen, sondern spielen, vereinfachen, ausbalancieren und polieren.

## Nachtrag 2 (wörtlich, Julian 14.10.2026 14:43): Firmenentwicklung

Ja, das gehört unbedingt als zentrales Fortschrittssystem hinein. Nicht nur „Garage Stufe 2“, sondern die Abschleppfirma muss auf der Karte wirklich sichtbar wachsen.
Realistische Firmenentwicklung
Stufe 1 – Kleiner Familienbetrieb

* gemietete kleine Halle
* ein Servicewagen
* ein Abschlepper
* zwei Mitarbeiter
* kleiner Teilebestand
* vier Stellplätze
* einfaches Büro

Stufe 2 – Eigener Betriebshof

* größere Werkstatt
* zusätzliche Fahrzeugstellplätze
* Reifen- und Teilelager
* Lager für Altteile
* Waschplatz
* Aufenthaltsraum
* kleine Leitstelle
* ungefähr vier bis sechs Einsatzfahrzeuge

Stufe 3 – Professioneller Abschleppdienst

* mehrere Werkstattplätze
* großer Verwahrhof
* Schwerlastbereich
* eigene Tankstelle beziehungsweise Ladesäulen
* moderne Leitstelle
* Schulungsraum
* ungefähr acht bis zwölf Fahrzeuge
* Verträge mit Polizei, Werkstätten und Automobilclubs

Stufe 4 – Regionalunternehmen

* zweite Niederlassung in einem anderen Stadtgebiet
* eigener Niederlassungsleiter
* Fahrzeuge starten vom jeweils näheren Standort
* zentrale Lagerverwaltung
* große Lkw- und Busbergungen
* ungefähr 15–25 Fahrzeuge

Stufe 5 – Marktführer der Region

* mehrere Niederlassungen
* rund um die Uhr besetzte Leitstelle
* Schwerlast-, Kran- und Spezialfahrzeuge
* großer Verwaltungs- und Werkstattkomplex
* Autobahn- und Großschadensverträge
* sichtbares Firmengelände als Wahrzeichen der Stadt

So funktioniert der Ausbau
Auf dem Hof befinden sich echte freie Bauflächen. Der Spieler wählt dort beispielsweise:

* zusätzliche Garage
* Werkstattplatz
* Stellplatzfläche
* Lagerhalle
* Reifencontainer
* Entsorgungsbereich
* Leitstelle
* Mitarbeitergebäude
* Tankstelle oder Ladesäule
* Schwerlastgarage
* Sammlungshalle

Der Bau dauert Spielzeit. Währenddessen sieht man Absperrungen, Baufahrzeuge und Baufortschritt. Danach steht dort wirklich das neue Gebäude und Fahrzeuge beziehungsweise Mitarbeiter benutzen es.
Jeder Ausbau benötigt:

* Kaufpreis oder Kredit
* laufende Kosten
* Bauzeit
* ausreichend Grundstück
* teilweise bestimmte Genehmigungen oder Ruf
* einen klaren Nutzen

Beispiel:
Zweite Werkstatthalle
Baukosten: 35.000 €
Bauzeit: 5 Spieltage
Laufende Kosten: 180 € pro Tag
Vorteil: Zwei Fahrzeuge gleichzeitig warten
Wichtig: Das normale Firmenwachstum ist Bestandteil des kostenlosen Spiels. Echtgeld darf nur besondere Designs, Gebäudevarianten oder Lackierungen freischalten – nicht den normalen Ausbau blockieren. Genau dieses sichtbare Wachstum kann die langfristige Motivation für die geplanten 50–100 Stunden liefern.
