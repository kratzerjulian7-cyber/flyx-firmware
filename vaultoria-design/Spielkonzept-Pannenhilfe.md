# Vaultoria – Spielkonzept Pannenhilfe (verbindlich)

Stand 14.10.2026, 10:34. **Ersetzt alles Frühere.** Das Pfandhaus-, Handels-, Auktions-, Museums-, Raubzug- und Imperium-Spiel (Spielkonzept Teile A–L, UI-Vorgabe 1.0–4.0) ist eingestellt und liegt nur noch als Archiv in `archiv-pfandhaus/`. App-Name „Vaultoria“, Bundle-ID com.julian.vaultoria, Xcode-Projekt und Signierung bleiben.

Aussehen und Bedienung jeder Ansicht: `UI-Vorgabe-Pannenhilfe.md`. Bei Widerspruch gilt für Regeln dieser Text, für Aussehen die UI-Vorgabe.

## 1. Julians Auftrag (wörtlich, 14.10.2026 10:34)

> WICHTIGER NEUAUFTRAG: Vaultoria wird vollständig ersetzt.
>
> Das bisherige Pfandhaus-, Handels-, Auktions-, Museums-, Raubzug- und Imperium-Spiel wird nicht weiterentwickelt. Entferne diese Spielinhalte vollständig aus der sichtbaren App und ersetze das Spiel durch einen Pannenhilfe- und Abschlepp-Tycoon.
>
> Der Name der App bleibt „Vaultoria“. Bundle-ID, Xcode-Projekt, Signierung, App-Store-Verknüpfung und technische App-Struktur müssen erhalten bleiben.
>
> SICHERUNG
>
> Bevor du etwas entfernst:
>
> 1. Sichere den aktuellen Stand vollständig in Git.
> 2. Erstelle einen eindeutig benannten Tag oder Branch:
>    vaultoria-legacy-2.3
> 3. Danach darf die sichtbare App vollständig durch das neue Spiel ersetzt werden.
> 4. Alter Code darf entfernt werden, wenn er nicht mehr benötigt wird.
> 5. Alte Speicherstände dürfen niemals Abstürze verursachen. Bei inkompatiblen Spielständen soll automatisch ein sauberer Neustart des neuen Spiels erfolgen.
>
> NEUES SPIELKONZEPT
>
> Vaultoria wird ein Pannenhilfe- und Abschlepp-Tycoon mit einer übersichtlichen Draufsicht.
>
> Der Spieler fährt kein Fahrzeug selbst. Er leitet eine Pannenhilfezentrale, nimmt Einsätze an, weist Mitarbeiter und Fahrzeuge zu und beobachtet die Fahrzeuge live auf der Karte.
>
> Der Kernablauf:
>
> 1. Ein Einsatz erscheint auf der Stadtkarte.
> 2. Der Spieler sieht Problem, Entfernung, Dringlichkeit und erwartete Bezahlung.
> 3. Der Spieler wählt einen Mitarbeiter und ein geeignetes Fahrzeug.
> 4. Das Einsatzfahrzeug fährt sichtbar über die Karte.
> 5. Vor Ort wird der Auftrag automatisch bearbeitet.
> 6. Bei besonderen Problemen erscheint eine kurze Entscheidung.
> 7. Das Fahrzeug fährt zurück oder direkt zum nächsten Einsatz.
> 8. Der Spieler erhält Geld, Erfahrung und Kundenbewertung.
> 9. Fahrzeuge müssen gewartet und die Zentrale ausgebaut werden.
>
> KEIN SELBSTFAHREN
>
> Es darf ausdrücklich keine manuelle Fahrzeugsteuerung geben.
>
> Das Spiel wird vollständig aus einer Tycoon-Draufsicht bedient:
>
> - Fahrzeuge bewegen sich automatisch.
> - Routen werden auf der Karte angezeigt.
> - Der Spieler verteilt Einsätze.
> - Der Spieler verwaltet Mitarbeiter, Fahrzeuge und Standorte.
> - Entscheidungen erfolgen über kurze, leicht verständliche Fenster.
>
> STARTVERSION
>
> Die erste vollständig spielbare Version enthält ausschließlich:
>
> - eine kleine Stadtkarte
> - eine Pannenhilfezentrale
> - einen Servicewagen
> - einen Abschleppwagen
> - zwei startende Mitarbeiter
> - sechs Einsatzarten
> - Einsatzverteilung
> - automatische Routen und sichtbare Fahrzeugbewegungen
> - Einsatzfortschritt
> - Bezahlung und Kundenbewertung
> - Kraftstoff und Fahrzeugzustand
> - Fahrzeugwartung
> - einfache Ausbauten der Zentrale
> - Tagesabrechnung
> - Speichern und Laden
>
> EINSATZARTEN
>
> 1. Batterie leer
> 2. Reifenpanne
> 3. Fahrzeug abgeschlossen
> 4. falscher Kraftstoff
> 5. technischer Defekt
> 6. Fahrzeug abschleppen
>
> Jeder Einsatz benötigt bestimmte Fähigkeiten oder Ausrüstung. Wird ein falsches Fahrzeug geschickt, kann der Auftrag länger dauern, weniger Geld bringen oder ein zweites Fahrzeug benötigen.
>
> FAHRZEUGE
>
> Servicewagen:
> - schnell
> - geeignet für Batterien, Reifen und kleinere Reparaturen
> - kann kein Fahrzeug abschleppen
>
> Abschleppwagen:
> - langsamer
> - höhere Betriebskosten
> - kann defekte Fahrzeuge transportieren
> - nur begrenzte Reparaturmöglichkeiten
>
> Jedes Fahrzeug besitzt:
>
> - Geschwindigkeit
> - Zustand
> - Kraftstoffverbrauch
> - Wartungskosten
> - verfügbare Ausrüstung
> - aktuellen Einsatz
> - verbleibende Fahr- oder Arbeitszeit
>
> MITARBEITER
>
> Mitarbeiter besitzen zunächst nur vier leicht verständliche Werte:
>
> - Reparatur
> - Abschleppen
> - Geschwindigkeit
> - Zuverlässigkeit
>
> Keine komplizierten Talentbäume oder riesigen Statistikseiten.
>
> STADTKARTE
>
> Die Karte ist der wichtigste Bildschirm der App.
>
> Sie zeigt:
>
> - Straßen
> - Zentrale
> - Einsatzorte
> - Kundenfahrzeuge
> - eigene Einsatzfahrzeuge
> - aktuelle Routen
> - Ankunftszeit
> - Status jedes Einsatzes
>
> Fahrzeuge müssen sich sichtbar und flüssig über die Straßen bewegen. Der Spieler soll jederzeit erkennen, welches Fahrzeug wohin fährt.
>
> EINSATZFENSTER
>
> Ein Einsatzfenster zeigt kompakt:
>
> - Art der Panne
> - Fahrzeugtyp des Kunden
> - Entfernung
> - Dringlichkeit
> - erwartete Belohnung
> - benötigte Ausrüstung
> - geschätzte Dauer
>
> Danach wählt der Spieler:
>
> - Mitarbeiter
> - Einsatzfahrzeug
> - Auftrag annehmen oder ablehnen
>
> BESONDERE ENTSCHEIDUNGEN
>
> Gelegentlich erscheint während eines Einsatzes eine einfache Entscheidung, zum Beispiel:
>
> „Der Schaden ist größer als gemeldet.“
>
> - zweiten Wagen anfordern
> - Reparatur versuchen
> - Auftrag abbrechen
>
> Diese Entscheidungen dürfen nicht bei jedem Einsatz erscheinen.
>
> ZENTRALE UND UPGRADES
>
> Ausbauten müssen logisch und sichtbar sein:
>
> - zusätzlicher Stellplatz
> - kleine Werkstatt
> - Ersatzteillager
> - Tankstelle
> - Ladepunkt für Elektrofahrzeuge
> - verbesserte Leitstelle
>
> Keine schwebenden Upgrade-Knöpfe und keine unverständlichen Prozentwerte. Jeder Ausbau zeigt vorher klar seine Auswirkung.
>
> WIRTSCHAFT
>
> Einnahmen:
>
> - Einsatzvergütung
> - Reparaturen
> - Abschleppkosten
> - gute Kundenbewertungen
>
> Ausgaben:
>
> - Gehälter
> - Kraftstoff
> - Wartung
> - Ersatzteile
> - neue Fahrzeuge
> - Ausbauten
>
> Am Tagesende erscheint eine kurze Abrechnung mit Einnahmen, Kosten und Reingewinn.
>
> BEDIENUNG UND DESIGN
>
> - hochwertiges dunkles Tycoon-Design
> - Gold als dezente Vaultoria-Akzentfarbe
> - keine überladenen Textwände
> - große verständliche Buttons
> - höchstens eine Hauptentscheidung pro Fenster
> - wichtige Informationen müssen ohne Erklärung verständlich sein
> - keine unnötigen Menüs
> - flüssige Animationen
> - gut auf kleinen iPhone-Displays lesbar
>
> ENTFERNEN
>
> Folgende alte Spielsysteme vollständig aus der neuen sichtbaren Version entfernen:
>
> - Pfandhaus
> - Gegenstandshandel
> - Käufer und Sammler
> - Marktpreise
> - Museum
> - Auktionen
> - Rufgruppen
> - Konkurrenten
> - Versicherungsbüro
> - Rebirth
> - altes Imperium
> - Tierpension
> - Raubzüge
> - alter Baumodus
> - alte Handelswährungen und Speicherstände
>
> ENTWICKLUNGSREGELN
>
> - Keine Platzhalter-Menüs für spätere Funktionen einbauen.
> - Keine zusätzlichen Systeme erfinden.
> - Zuerst einen unterhaltsamen und vollständig funktionierenden Kern entwickeln.
> - Bestehende technische Komponenten nur wiederverwenden, wenn sie zum neuen Spiel passen.
> - Keine wichtigen Funktionen lediglich vortäuschen.
> - Alle Buttons und Abläufe müssen tatsächlich funktionieren.
> - Keine bezahlten Dienste oder externen APIs ohne vorherige Zustimmung.
> - Das Projekt muss nach jedem größeren Schritt kompilierbar bleiben.
> - Fehler und Warnungen sauber beheben.
> - Auf einem echten iPhone-Layout testen.
>
> ABNAHME
>
> Die erste Version ist fertig, wenn folgender Ablauf vollständig funktioniert:
>
> 1. Neues Spiel starten.
> 2. Ersten Einsatz auf der Karte erhalten.
> 3. Mitarbeiter und Fahrzeug auswählen.
> 4. Fahrzeug fährt sichtbar zum Einsatz.
> 5. Auftrag wird bearbeitet.
> 6. Geld und Bewertung werden korrekt gutgeschrieben.
> 7. Fahrzeug kehrt zurück.
> 8. Fahrzeug kann gewartet werden.
> 9. Ein Ausbau kann gekauft werden.
> 10. Spielstand bleibt nach einem Neustart erhalten.
>
> Arbeite selbstständig weiter und stelle nur Rückfragen, wenn eine Entscheidung technisch wirklich nicht ohne mich getroffen werden kann. Am Ende liefere eine Zusammenfassung der entfernten Systeme, des neuen Aufbaus, der Tests und Screenshots aller wichtigen Ansichten.

## 2. Ergänzung Julian (wörtlich, 14.10.2026 11:06)

> noch viel viel mehr machen große welt machen eine sehr große welt man soll sehen können wie die werkstatt größer wird wenn man es upgradet

Gemeint (vom Koordinator bestätigt): eine sehr große Welt mit mehreren Vierteln, durch die man wischt und zoomt. Zentrale und Werkstatt wachsen auf der Karte sichtbar mit jedem Ausbau, jeder Ausbau ist ein eigenes Gebäudeteil mit kurzer Bau-Animation. Umsetzung: `UI-Vorgabe-Pannenhilfe.md` Teil 12.

## 3. Ergänzung Julian (wörtlich, 14.10.2026 11:21)

> Noch ein paar Sachen würden das Spiel deutlich besser machen, ohne es wieder so kompliziert wie Vaultoria vorher zu machen.
> Für die erste Version
>
> * Einsatzwarteschlange: Mehrere Pannen erscheinen gleichzeitig. Du musst priorisieren.
> * Countdown: Kunden warten nicht unbegrenzt.
> * Live-Status: Anfahrt → vor Ort → Reparatur → Rückfahrt.
> * Verkehr: Stau verlängert die Anfahrt; andere Route kann schneller sein.
> * Fahrzeugzustand: Tanken, laden, reparieren und warten.
> * Mitarbeiterschichten: Niemand kann dauerhaft arbeiten.
> * Bewertungen: Schnelle Hilfe verbessert deinen Ruf und bringt bessere Aufträge.
> * Einsatzbericht: Einnahmen, Kosten, Dauer und Gewinn nach jedem Auftrag.
>
> Sehr gute spätere Erweiterungen
> Verträge
>
> * Polizei
> * Versicherungen
> * Autohäuser
> * Werkstätten
> * Automobilclubs
> * Gemeinden
>
> Diese liefern regelmäßige Aufträge, verlangen aber kurze Reaktionszeiten.
> Große Ereignisse
>
> * Massenkarambolage
> * Unwetter
> * Glatteis
> * Festival mit vielen Falschparkern
> * Autobahnsperrung
> * Hochwasser
> * Wintereinbruch
>
> Dabei müssen mehrere Fahrzeuge gleichzeitig koordiniert werden.
> Unterschiedliche Regionen
>
> * Innenstadt: Verkehr und Falschparker
> * Autobahn: schwere Unfälle und lange Strecken
> * Land: wenige, aber weit entfernte Einsätze
> * Berge: schwierige Bergungen
> * Industriegebiet: LKW und schwere Fahrzeuge
>
> Spezielle Fahrzeuge
>
> * mobiler Batteriedienst
> * Plattform-Abschlepper
> * schwerer Berge-LKW
> * Kranwagen
> * mobile Elektro-Ladestation
> * Ersatzteiltransporter
>
> Mehrere Zentralen
> Später kaufst du neue Standorte. Jeder Standort benötigt Fahrzeuge und Personal. Ein Geschäftsführer übernimmt einfache Einsätze automatisch.
> Zufällige Entscheidungen
> Beispielsweise:
> Das Unfallfahrzeug verliert Öl.
>
> * Feuerwehr anfordern
> * Spezialfahrzeug schicken
> * Auftrag abbrechen
>
> Oder:
> Der Kunde kann nicht sofort bezahlen.
>
> * Rechnung ausstellen
> * Barzahlung verlangen
> * Fahrzeug einbehalten
>
> Solche Entscheidungen nur gelegentlich, damit es übersichtlich bleibt.
> Weitere sinnvolle Bilder
> Als Nächstes könnten wir visuell zeigen:
>
> 1. Flottenübersicht mit Fahrzeugzustand und Wartung
> 2. Personalansicht mit verfügbaren Fahrern
> 3. Einsatzbericht nach erfolgreicher Pannenhilfe
> 4. Nacht-/Regenkarte mit mehreren Notfällen
> 5. Große Autobahnbergung als späteres Spielziel
>
> Am wichtigsten sind jetzt aber eine bewegte Karte, echte Routen und mehrere gleichzeitige Einsätze. Genau daraus entsteht der Spielspaß – nicht aus vielen Menüs.

**Einordnung:** Die 8 Punkte unter „Für die erste Version“ gehören verbindlich in die erste Version. Alles unter „Sehr gute spätere Erweiterungen“ (Verträge, große Ereignisse, Regionen, Spezialfahrzeuge, mehrere Zentralen, zufällige Entscheidungen) kommt erst später und wird jetzt nicht gebaut, auch nicht als Platzhalter. Priorität: bewegte Karte, echte Routen, mehrere gleichzeitige Einsätze. Umsetzung: `UI-Vorgabe-Pannenhilfe.md` Teil 13.
