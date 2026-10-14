# Vaultoria 5.3 – Abnahme-Checkliste

Stand 14.10.2026, 16:10 (neuer Block 5.4 vor „Offen“). Hier steht jede Anforderung, die Julian heute zu Vaultoria geschrieben hat, als nummerierter Prüfpunkt mit Quelle. Die Zeiten sind Julians Nachrichten in deutscher Zeit. Die Volltexte stehen wörtlich in `design/Spielkonzept-Pannenhilfe.md` (10:34, 11:06, 11:21), `design/Erweiterungsplan-Pannenhilfe.md` (12:57, 13:05), `design/UI-Vorgabe-Pannenhilfe.md` (13:12, 13:40, 13:50, 13:59) und `design/Komplettueberarbeitung-5.3.md` (14:03 im Plan Teil 5b, 14:15 im Plan Teil 5c, 14:30, 14:36, 14:43, 14:48).

**So wird geprüft:** Der Mac hakt vor dem Upload jeden Punkt mit **„in 5.3“** einzeln ab: ✅ erfüllt, ❌ fehlt, mit einem Satz, wie er es geprüft hat. Punkte mit **„später“** dürfen in 5.3 **nicht** als Platzhalter auftauchen (Regel 10:34: keine Platzhalter-Menüs).

**Widersprüche:** Wenn sich zwei Vorgaben widersprechen, gilt die neuere. Das ist beim Punkt mit **⚠ Neuer gilt** vermerkt.

Spalten: **Nr.** · **Anforderung** · **Quelle** · **Status** · **Begründung / Hinweis**

---

## G. Grundregeln, die überall gelten

| Nr. | Anforderung | Quelle | Status | Begründung / Hinweis |
|---|---|---|---|---|
| G1 | Name bleibt „Vaultoria“; Bundle-ID, Xcode-Projekt, Signierung, ASC-Verknüpfung bleiben | 10:34, 14:30 | in 5.3 | unveränderbarer Kern |
| G2 | Pannenhilfe- und Abschlepp-Tycoon aus der Draufsicht, keine Rückkehr zum Pfandhaus | 10:34, 14:30 | in 5.3 | – |
| G3 | Spieler fährt nicht selbst, keine manuelle Fahrzeugsteuerung | 10:34, 14:30 | in 5.3 | – |
| G4 | Spieler entscheidet, welche Mitarbeiter und Fahrzeuge zu welchen Einsätzen fahren | 14:30 | in 5.3 | – |
| G5 | Karte ist der wichtigste Bildschirm und bleibt der Mittelpunkt | 10:34, 11:21, 14:30 | in 5.3 | – |
| G6 | Nur vier Tabs: Karte · Flotte · Zentrale · Personal; kein fünfter Tab, keine neue Hauptnavigation | 14:15, 14:30 | in 5.3 | Shop, Kasse, Verlauf, Lager, Bauen sind Karten im Tab Zentrale |
| G7 | Keine überladene Menüstruktur, keine unnötigen Menüs | 10:34, 14:30 | in 5.3 | – |
| G8 | **Kein Gold**: Graphit, Silber und gezieltes Einsatz-Orange sind die Designsprache | 13:12, 14:30 | in 5.3 | ⚠ Neuer gilt: „Gold als dezente Akzentfarbe“ (10:34) ist durch 13:12 aufgehoben |
| G9 | Hochwertiger, erwachsener Look; nichts wirkt billig oder „wie für Zweijährige“ | 13:12 | in 5.3 | – |
| G10 | Layout der Konzeptbilder (Karte, Einsatz-Zuteilung, Zentrale) bleibt, Stil/Farben daraus nicht | 13:12 | in 5.3 | Zentrale-Ausbaukarten sind durch das Bausystem ersetzt (siehe F) |
| G11 | Keine echten Automarken oder Logos, Kennzeichen fiktiv | Regel der Konzeptbilder, 13:40 | in 5.3 | – |
| G12 | Realistische Autos, Häuser und Menschen; CC0-Quellen Poly Haven und ambientCG freigegeben | 13:40 | in 5.3 | ⚠ Neuer gilt: ab 14:30 **einheitlicher Stil**: realistische Materialien auf stilisierten Formen, keine Mischung aus fotorealistischen Bildern und Low-Poly-Modellen |
| G13 | Keine bezahlten Dienste oder externen APIs ohne Julians Zustimmung | 10:34 | in 5.3 | Werbe-SDK erst nach Freigabe (siehe P) |
| G14 | Keine Platzhalter, nichts vortäuschen, alle Knöpfe und Abläufe funktionieren wirklich | 10:34, 14:30 | in 5.3 | – |
| G15 | Keine zusätzlichen Systeme erfinden; neue Funktionen nur, wenn der bestehende Ablauf dadurch besser wird | 10:34, 14:30 | in 5.3 | – |
| G16 | Projekt bleibt kompilierbar, Fehler und Warnungen sauber behoben | 10:34 | in 5.3 | – |
| G17 | Auf echtem iPhone-Layout getestet, gut auf kleinen iPhones lesbar | 10:34 | in 5.3 | siehe Q1 |
| G18 | Höchstens eine Hauptentscheidung pro Fenster, keine Textwände, große verständliche Knöpfe | 10:34 | in 5.3 | – |
| G19 | Versionsnummer 5.3, nie niedriger als die höchste hochgeladene Version | Julians Wahl „Version 5.0“ | in 5.3 | Build-Nummer neu |

## S. Sicherung und Spielstände (10:34, 14:30)

| Nr. | Anforderung | Quelle | Status | Begründung / Hinweis |
|---|---|---|---|---|
| S1 | Alter Stand in Git gesichert als `vaultoria-legacy-2.3` | 10:34 | erledigt, muss bestehen bleiben | am Mac erledigt |
| S2 | Sicherung der bisherigen Version (5.1) vor dem Umbau | 14:30 Lieferung | in 5.3 | Tag oder Branch `vaultoria-5.1`, in der Lieferung nennen |
| S3 | Alte Spielstände verursachen nie einen Absturz; inkompatibel → sauberer Neustart mit Hinweis | 10:34 | in 5.3 | `save-defekt-<Datum>.json` |
| S4 | Bestehende Spielstände (5.0/5.1) sicher migrieren | 14:30 | in 5.3 | Schema-Migration mit echtem 5.1-Stand testen |
| S5 | Pfandhaus-Systeme bleiben aus der sichtbaren App entfernt (Pfandhaus, Handel, Käufer, Marktpreise, Museum, alte Auktionen, Rufgruppen, Konkurrenten, Versicherungsbüro, Rebirth, Imperium, Tierpension, Raubzüge, alter Baumodus, alte Währungen) | 10:34 | in 5.3 | Die späteren Behörden-Auktionen (E17) sind ein neues Pannenhilfe-System, kein Pfandhaus-Rest |

## K. Kernablauf und Startumfang (10:34)

| Nr. | Anforderung | Quelle | Status | Begründung / Hinweis |
|---|---|---|---|---|
| K1 | Einsatz erscheint auf der Stadtkarte | 10:34 | in 5.3 | – |
| K2 | Problem, Entfernung, Dringlichkeit und erwartete Bezahlung sichtbar | 10:34 | in 5.3 | ergänzt durch T1 und A2 |
| K3 | Einsatzfenster: Art der Panne, Fahrzeugtyp des Kunden, Entfernung, Dringlichkeit, Belohnung, benötigte Ausrüstung, geschätzte Dauer; annehmen oder ablehnen | 10:34 | in 5.3 | – |
| K4 | Einsatzfahrzeug fährt sichtbar und flüssig über die Straßen; man erkennt jederzeit, wer wohin fährt | 10:34 | in 5.3 | – |
| K5 | Vor Ort wird der Auftrag automatisch bearbeitet | 10:34 | in 5.3 | jetzt mit Diagnose (A7) |
| K6 | Gelegentliche kurze Entscheidung (z. B. „Schaden größer als gemeldet“: zweiten Wagen / Reparatur versuchen / abbrechen), nicht bei jedem Einsatz | 10:34 | in 5.3 | – |
| K7 | Fahrzeug fährt zurück | 10:34 | in 5.3 | ⚠ Neuer gilt: „oder direkt zum nächsten Einsatz“ (10:34) entfällt, weil 14:30 sagt: erst nach der Rückkehr wieder verfügbar (A14) |
| K8 | Geld, Erfahrung und Kundenbewertung nach dem Einsatz | 10:34 | in 5.3 | – |
| K9 | Fahrzeuge müssen gewartet werden (Wartung funktioniert wirklich) | 10:34 | in 5.3 | – |
| K10 | Zentrale ausbauen; jeder Ausbau logisch, sichtbar und zeigt vorher seine Auswirkung; keine schwebenden Upgrade-Knöpfe, keine unverständlichen Prozentwerte | 10:34 | in 5.3 | ⚠ Neuer gilt: Ausbau läuft über das Bausystem (F7–F14) |
| K11 | Ausbau-Liste 10:34: Stellplatz, Ersatzteillager in 5.3 (Stellplatzfläche, Lagerhalle); kleine Werkstatt, Tankstelle, Ladepunkt und verbesserte Leitstelle später | 10:34 | teils in 5.3 | ⚠ Neuer gilt: Firmenentwicklung 14:43 ordnet Werkstattplatz und kleine Leitstelle Firmenstufe 2 zu, Tankstelle/Ladesäulen Firmenstufe 3. In 5.3 hat die gemietete Halle einen einfachen Wartungsplatz und eine einfache Zapfstelle, damit Wartung und Tanken (K9, B3) funktionieren |
| K12 | Startbesetzung: 1 Servicewagen, 1 Abschleppwagen, 2 Mitarbeiter, eine Zentrale | 10:34, 14:43 | in 5.3 | = Firmenstufe 1 |
| K13 | Servicewagen schnell, für Batterie/Reifen/Kleinreparatur, kann nicht abschleppen; Abschleppwagen langsamer, teurer, transportiert, nur begrenzt reparieren | 10:34 | in 5.3 | – |
| K14 | Falsches Fahrzeug → dauert länger, bringt weniger oder braucht zweites Fahrzeug | 10:34 | in 5.3 | – |
| K15 | Wirtschaft: Einnahmen (Vergütung, Reparatur, Abschleppen, gute Bewertungen), Ausgaben (Gehälter, Kraftstoff, Wartung, Ersatzteile, neue Fahrzeuge, Ausbauten) | 10:34 | in 5.3 | – |
| K16 | Tagesabrechnung mit Einnahmen, Kosten, Reingewinn | 10:34 | in 5.3 | jetzt mit Fixkosten (T7) |
| K17 | Speichern und Laden, Spielstand bleibt nach Neustart | 10:34 | in 5.3 | – |
| K18 | Abnahme 10:34: neues Spiel → erster Einsatz → Auswahl → Fahrt → Bearbeitung → Geld/Bewertung → Rückkehr → Wartung → Ausbau kaufen → Spielstand nach Neustart da | 10:34 | in 5.3 | als ein durchgespielter Ablauf im Video (L3) |
| K19 | Große Welt mit mehreren Vierteln; wischen und zoomen | 11:06 | in 5.3 | 7 Viertel seit 1.2; die Freischaltung der Viertel wird in E8 neu geregelt |
| K20 | Man sieht die Werkstatt bzw. Firma beim Ausbau sichtbar wachsen | 11:06, 14:43 | in 5.3 | Bausystem mit Baustelle (F10) |

## P8. Die 8 Pflichtpunkte der ersten Version (11:21)

| Nr. | Anforderung | Quelle | Status | Begründung / Hinweis |
|---|---|---|---|---|
| P8-1 | Einsatzwarteschlange: mehrere Pannen gleichzeitig, man muss priorisieren | 11:21 | in 5.3 | höchstens 4 gleichzeitig am Anfang (Z5) |
| P8-2 | Countdown: Kunden warten nicht unbegrenzt | 11:21 | in 5.3 | Kundenwartezeit im Fenster (A2) |
| P8-3 | Live-Status je Einsatz | 11:21 | in 5.3 | ⚠ Neuer gilt: statt „Anfahrt → vor Ort → Reparatur → Rückfahrt“ die 8 Fahrzeugstatus aus 14:30 (B9) |
| P8-4 | Verkehr: Stau verlängert die Anfahrt, andere Route kann schneller sein | 11:21 | in 5.3 | – |
| P8-5 | Fahrzeugzustand: tanken, laden, reparieren, warten | 11:21 | in 5.3 | – |
| P8-6 | Mitarbeiterschichten: niemand arbeitet dauerhaft | 11:21 | in 5.3 | jetzt mit Müdigkeit (M6) |
| P8-7 | Bewertungen: schnelle Hilfe → besserer Ruf → bessere Aufträge | 11:21 | in 5.3 | Bewertung mit Begründung (T12) |
| P8-8 | Einsatzbericht: Einnahmen, Kosten, Dauer, Gewinn nach jedem Auftrag | 11:21 | in 5.3 | vollständig nach T9–T15 |
| P8-9 | Priorität: bewegte Karte, echte Routen, mehrere gleichzeitige Einsätze statt vieler Menüs | 11:21 | in 5.3 | – |
| P8-10 | Spätere Ideen von 11:21 (Verträge mit Polizei, Versicherungen, Autohäusern, Werkstätten, Automobilclubs, Gemeinden; große Ereignisse; Regionen; Spezialfahrzeuge; mehrere Zentralen mit Geschäftsführer; zufällige Entscheidungen wie Ölverlust oder Zahlungsprobleme) | 11:21 | später (E2–E19, Firmenstufen 2–5) | Julian: „spätere Erweiterungen“. Ausnahme: „zweites Fahrzeug anfordern“ ist ab 14:30 in 5.3 (A10) |

## R. Erweiterungsplan: Auftrag (12:57) und Regeln R1–R8 (13:05)

| Nr. | Anforderung | Quelle | Status | Begründung / Hinweis |
|---|---|---|---|---|
| R0 | Erste Welt für 50–100 Stunden, Systeme schrittweise freischalten, Einstieg bleibt einfach, Karte zentral | 12:57 | Rahmen ab 5.3, Inhalte später | 5.3 = erste 30–60 Minuten (14:30 Schluss) |
| R1 | Spieltag ca. 18 Minuten bei 1×, erste Welt ca. 300 Spieltage | 13:05, 14:30 | in 5.3 | seit 5.1 drin, bleibt |
| R2 | Zeitsteuerung Pause/1×/2×/4×, Auto-Pause bei dringenden Einsätzen und Entscheidungen | 13:05, 14:30 | in 5.3 | seit 5.1 drin, bleibt |
| R3 | Ausgänge hauptsächlich aus Mitarbeiter, Fahrzeug, Ausrüstung/Material, Entscheidung (und Wetter); Zufall nur klein | 13:05, 14:30 | in 5.3 | ⚠ Neuer gilt: war für E4 geplant, 14:30 holt die Ausgänge nach 5.3. Wetter erst mit E2 |
| R4 | Betriebshof keine Gelddruckmaschine: Standgebühren mit Platz-, Verwaltungs- und Sicherheitskosten | 13:05 | später (E6, Firmenstufe 2) | in 5.3: Hof-Plätze, voller Hof wirkt, laufende Gebäudekosten; Standgebühren noch nicht |
| R5 | Rechtliche Abläufe für Spieler in 3 Schritten: Kontakt, Frist, Abholung/Verkauf/Auktion | 13:05 | später (E6/E17) | – |
| R6 | Mitarbeiter mit erkennbarer Stärke und Schwäche | 13:05 | in 5.3 | ⚠ Neuer gilt: 14:30 „genau **eine** erkennbare Stärke **oder** Schwäche“ ersetzt „Stärke + Schwäche + max. eine Eigenschaft“ |
| R7 | Architektur für weitere Welten; zweite Welt erst in späterem Update, Ausblick nach Welt 1 | 13:05 | Architektur in 5.3 (seit 5.1), Inhalt später (E19) | – |
| R8 | 50–100 Stunden nicht durch Wiederholung, regelmäßig Neues | 13:05 | ab 5.3 für die erste Phase, danach je Update | in 5.3: 7 Einsatzarten × 8 Entwicklungen, Bauziele, Firmenaufstieg in Sicht |
| R9 | Die 14 Erweiterungsthemen (Einsatzdauer, Ausgänge, Autobahn, Mitarbeiterwerte, Fahrzeugklassen, Lkw/Bus/Großunfall, Gebiete, Verträge, Ruf/Ziele/Statistik, Betriebshof, Standgebühren, Standzeiten, Auktionen/Kaufangebote, Sammlung) | 12:57 | teils in 5.3, Rest später | in 5.3: Dauer, Ausgänge, Mitarbeiterwerte, Ruf, Hof-Grundumfang, Größen-Platzbedarf. Rest E2–E19 nach Plan Teil 5 |
| R10 | Zuerst nur E1 bauen und testen | 13:05 | erledigt in 5.1 | danach von Julian erweitert (14:03 bis 14:48) |

## L13. Lesbarkeit nach 5.0 (13:50, in 5.1 erledigt, muss bleiben)

| Nr. | Anforderung | Quelle | Status | Begründung / Hinweis |
|---|---|---|---|---|
| L13-1 | Route kräftiger mit dunklem Rand, auf jedem Straßenabschnitt erkennbar | 13:50, 14:30 | in 5.3 (bleibt) | – |
| L13-2 | Orange als Funktionsfarbe: Einsatzmarker, Warnungen, Rundumlichter | 13:50 | in 5.3 (bleibt) | ⚠ Neuer gilt: 14:30 präzisiert „Orange **ausschließlich** für Einsätze, Warnungen und aktive Aktionen“ |
| L13-3 | Touchflächen mindestens 44 × 44 pt, auch Zeitknöpfe | 13:50, 14:30 | in 5.3 (bleibt) | – |
| L13-4 | Eigene Fahrzeuge stark gekennzeichnet (Plakette mit Statuspunkt, Ring) | 13:50, 14:30 | in 5.3 (bleibt) | Statusfarben an B9 anpassen |
| L13-5 | Verschiedene Symbole je Einsatzart | 13:50, 14:30 | in 5.3 (bleibt) | jetzt 7 Arten (E1–E7) |
| L13-6 | Bewertung startet als „Neu“, Sterne erst durch echte Einsätze | 13:50 | in 5.3 (bleibt) | – |
| L13-7 | Ausbauen zeigt Preis und Nutzen | 13:50 | in 5.3 (bleibt) | jetzt im Bau-Sheet (F9) |
| L13-8 | Kartenbilder stilistisch passend zur Stadt, kein Fotorealismus in Low-Poly-Stadt | 13:50, 14:30 | in 5.3 | ⚠ Neuer gilt: siehe G12 |
| L13-9 | Großer freier Hof hinter der Zentrale für sichtbares Wachstum | 13:50 | in 5.3 | ⚠ Neuer gilt: wird ab 14:43 zu echten Bauflächen (F7) |
| L13-10 | Grundoptik nicht erneut verändern | 13:50 | in 5.3 | ⚠ Neuer gilt: 13:59 „mache die UI besser, viel besser“ erlaubt das Premium-Niveau; Farben und Layout bleiben |

## U. UI auf Premium-Niveau und Modelltausch (13:59)

| Nr. | Anforderung | Quelle | Status | Begründung / Hinweis |
|---|---|---|---|---|
| U1 | UI „viel besser“: Premium-Panels, Typografie, Abstände, Animationen, Haptik | 13:59 | in 5.3 | UI-Vorgabe 000b |
| U2 | Modelle einheitlich realistisch tauschen (Autos, Häuser, Menschen) | 13:59 | in 5.3 | ⚠ Neuer gilt: 14:30 „realistische Materialien auf stilisierten Formen, einheitlicher Stil“ |
| U3 | Farbe und Layout bleiben | 13:59 | in 5.3 | – |

## Z. Zielorte und Betriebsmittel E1.5 (14:03)

| Nr. | Anforderung | Quelle | Status | Begründung / Hinweis |
|---|---|---|---|---|
| Z1 | Abgeschleppte Fahrzeuge verschwinden nie | 14:03, 14:30 | in 5.3 | – |
| Z2 | Nach der Bergung Ziel wählen: eigener Hof, Partnerwerkstatt, Polizei, Schrottplatz, Kundenwerkstatt | 14:03, 14:30 | in 5.3 | – |
| Z3 | Abgeschlepptes Auto bleibt während der Fahrt sichtbar auf dem Abschlepper | 14:03, 14:30 | in 5.3 | – |
| Z4 | Abschlepper bleibt bis Abladen und Rückfahrt belegt | 14:03, 14:30 | in 5.3 | – |
| Z5 | Starttempo: anfangs ca. 8–12 Einsätze pro Spieltag (nicht 43–49), mit größerer Flotte mehr | 14:03, 14:30 | in 5.3 | dazu max. 4 gleichzeitige Aufträge am Anfang (14:30) |
| Z6 | Fahrzeuge auf dem eigenen Hof stehen sichtbar und belegen Platz | 14:03, 14:30 | in 5.3 | – |
| Z7 | Lager für Batterien, Reifen (Pkw/Transporter, Lkw später), Kraftstoff, Ersatzteile, Ölbindemittel; fünf verständliche Bestände | 14:03, 14:30 | in 5.3 | Lkw-Reifen mit E15 |
| Z8 | Einsätze verbrauchen passendes Material wirklich | 14:03, 14:30 | in 5.3 | – |
| Z9 | Altreifen, defekte Batterien, Altöl, beschädigte Teile, Unfallschrott landen sichtbar in begrenzten Bereichen | 14:03, 14:30 | in 5.3 | – |
| Z10 | Entsorgung kostet (Altreifen, Altöl), Batterien und Metallschrott bringen kleinen Erlös | 14:03, 14:30 | in 5.3 | – |
| Z11 | Lagerplatz/Container voll → bestimmte Einsätze nicht annehmbar | 14:03 | in 5.3 | mit Grund anzeigen (T18) |
| Z12 | Lager, Reifencontainer, Recyclingbereich ausbaubar | 14:03 | in 5.3 | als Gebäude im Bausystem (F12) |
| Z13 | Keine Verwaltung einzelner Schrauben, keine unnötigen Menüs; Bestand in der Zentrale und bei der Einsatzwahl | 14:03, 14:30 | in 5.3 | – |
| Z14 | Bestände bestellen, sichtbar geliefert | 14:30 | in 5.3 | – |
| Z15 | Fehlende Teile verhindern passende Reparaturen | 14:30 | in 5.3 | – |
| Z16 | Großer Betriebshof mit Standgebühren, Auktionen und Sammlung | 14:03 | später (E6, E12, E17) | Julian: „bleibt später in E6“ |

## T. Transparenz und Details (14:15)

| Nr. | Anforderung | Quelle | Status | Begründung / Hinweis |
|---|---|---|---|---|
| T1 | Vor der Zuteilung: erwartete Einnahmen, Kraftstoff, Material/Ersatzteile, anteilige Mitarbeiterkosten/-zeit, Verschleiß, mögliche Zusatzkosten, erwarteter Gewinn | 14:15, 14:30 | in 5.3 | – |
| T2 | Zusätzlich vorher: Entsorgung, Partnerkosten, mögliche Vertragsboni oder Strafen, Risiko | 14:30 | in 5.3 | Zeilen erscheinen nur, wenn sie anfallen. Vertragsboni/-strafen fallen erst mit Verträgen (E9) an, also keine leere Zeile vorher |
| T3 | Schätzwerte klar gekennzeichnet („ca.“, Spanne, Hinweis „Schätzung“) | 14:15, 14:30 | in 5.3 | – |
| T4 | Normalansicht zeigt nur den erwarteten Gewinn, „Details“ öffnet die volle Aufschlüsselung; Karte nicht überladen | 14:15, 14:30 | in 5.3 | – |
| T5 | Während des Einsatzes sichtbar: Status, Restdauer, Mehrkosten, Probleme, Zielort, Verfügbarkeit | 14:15 | in 5.3 | – |
| T6 | Einfaches Kassenbuch; jede Kontostandänderung nachvollziehbar | 14:15, 14:30 | in 5.3 | Test: Summe Kassenbuch = Kontostandänderung |
| T7 | Tägliche Fixkosten sichtbar | 14:15 | in 5.3 | inkl. laufender Gebäudekosten (F11) |
| T8 | Auftragshistorie | 14:15, 14:30 | in 5.3 | – |
| T9 | Nach jedem Einsatz vollständige Abrechnung: tatsächliche Kundenzahlung | 14:15, 14:30 | in 5.3 | – |
| T10 | … alle tatsächlichen Kosten, Gewinn oder Verlust | 14:15, 14:30 | in 5.3 | – |
| T11 | … Verbrauch/verbrauchte Materialien | 14:15, 14:30 | in 5.3 | – |
| T12 | … Bewertung **mit verständlicher Begründung** | 14:15, 14:30 | in 5.3 | – |
| T13 | … Erfahrung der Mitarbeiter | 14:15, 14:30 | in 5.3 | – |
| T14 | … Fahrzeugzustand | 14:15, 14:30 | in 5.3 | – |
| T15 | … Zielort des Kundenfahrzeugs und mögliche Folgeaktion | 14:15, 14:30 | in 5.3 | – |
| T16 | Lagerbestände sichtbar | 14:15 | in 5.3 | – |
| T17 | Eindeutige Fahrzeugstatus | 14:15 | in 5.3 | siehe B9 |
| T18 | Gründe für ungeeignete Fahrzeuge (und Mitarbeiter) | 14:15, 14:30 | in 5.3 | – |
| T19 | Kaufbestätigungen | 14:15 | in 5.3 | – |
| T20 | Sichtbare Rückmeldung bei Geldbewegungen | 14:15, 14:30 | in 5.3 | – |
| T21 | Verständliche Ersthinweise | 14:15 | in 5.3 | siehe Teil E (Einstieg) |
| T22 | Erst diesen Ablauf sauber machen, bevor Wetter, weitere Gebiete oder neue Fahrzeugklassen kommen | 14:15 | in 5.3 | Wetter E2, Gebiete E8, Fahrzeugklassen E10+ |

## A. Vollständiger Einsatzablauf (14:30 Teil 2)

| Nr. | Anforderung | Quelle | Status | Begründung / Hinweis |
|---|---|---|---|---|
| A1 | Auftrag geht sichtbar und **hörbar** ein | 14:30 | in 5.3 | – |
| A2 | Einsatzart, Standort, Fahrzeugtyp, Dringlichkeit, Kundenwartezeit sichtbar | 14:30 | in 5.3 | – |
| A3 | Einnahmen, Kosten, Risiko, erwarteter Gewinn verständlich | 14:30 | in 5.3 | T1–T4 |
| A4 | Spieler wählt Mitarbeiter, Fahrzeug, **Ausrüstung** und ggf. Zielort | 14:30 | in 5.3 | – |
| A5 | Fahrzeug verlässt sichtbar die Zentrale | 14:30 | in 5.3 | – |
| A6 | Route, Verkehr, Ankunftszeit, Status sichtbar | 14:30 | in 5.3 | – |
| A7 | Vor Ort erfolgt eine **Diagnose** | 14:30 | in 5.3 | – |
| A8 | Unterschiedliche, nachvollziehbare Ausgänge | 14:30 | in 5.3 | siehe E8–E15 |
| A9 | Material wird tatsächlich verbraucht | 14:30 | in 5.3 | – |
| A10 | Bei Bedarf **zweites Fahrzeug** anfordern | 14:30 | in 5.3 | – |
| A11 | Abgeschleppte Fahrzeuge sichtbar transportiert | 14:30 | in 5.3 | – |
| A12 | Abladen am Hof, bei Werkstatt, Polizei oder Schrottplatz | 14:30 | in 5.3 | – |
| A13 | Einsatzfahrzeug fährt danach zurück | 14:30 | in 5.3 | – |
| A14 | Erst nach der Rückkehr wieder verfügbar | 14:30 | in 5.3 | – |
| A15 | Danach vollständige Einsatzabrechnung | 14:30 | in 5.3 | – |
| A16 | Kein Fahrzeug und kein Auftrag verschwindet einfach | 14:30 | in 5.3 | – |

## H. Betriebshof (14:30 Teil 5)

| Nr. | Anforderung | Quelle | Status | Begründung / Hinweis |
|---|---|---|---|---|
| H1 | Sichtbare Stellplätze, begrenzte Kapazität | 14:30 | in 5.3 | – |
| H2 | Abgestellte Kundenfahrzeuge und eigene Fahrzeuge sichtbar | 14:30 | in 5.3 | – |
| H3 | Reifenlager, Teilelager, Entsorgungscontainer sichtbar | 14:30 | in 5.3 | – |
| H4 | Werkstatt und Tank- oder Ladebereich | 14:30 | in 5.3 (einfach) | ⚠ Neuer gilt (14:43): Firmenstufe 1 ist eine gemietete kleine Halle, in 5.3 mit einfachem Wartungsplatz und einfacher Zapfstelle. Größere Werkstatt ab Firmenstufe 2, eigene Tankstelle/Ladesäulen ab Firmenstufe 3 |
| H5 | Später Sammlung und Restaurierung | 14:30 | später (E12, E14) | – |
| H6 | Platzbedarf nach Fahrzeuggröße | 14:30 | in 5.3 | Pkw 1, Transporter 2 Einheiten |
| H7 | Voller Hof hat echte Auswirkungen | 14:30 | in 5.3 | Ziel „eigener Hof“ gesperrt, mit Grund |
| H8 | Ausbauten verändern den Hof sichtbar und zeigen vorher Preis und konkreten Nutzen | 14:30, 14:43 | in 5.3 | – |

## M. Mitarbeiter (14:30 Teil 6)

| Nr. | Anforderung | Quelle | Status | Begründung / Hinweis |
|---|---|---|---|---|
| M1 | Reparaturfähigkeit | 10:34, 14:30 | in 5.3 | – |
| M2 | Abschleppfähigkeit | 10:34, 14:30 | in 5.3 | – |
| M3 | Geschwindigkeit | 10:34, 14:30 | in 5.3 | – |
| M4 | Zuverlässigkeit | 10:34, 14:30 | in 5.3 | – |
| M5 | Erfahrung | 14:30 | in 5.3 | ⚠ Neuer gilt: 10:34 „nur vier Werte“ ist durch 14:30 erweitert; keine Talentbäume |
| M6 | Schicht und Müdigkeit | 11:21, 14:30 | in 5.3 | – |
| M7 | Benötigte Führerscheine | 14:30 | in 5.3 | – |
| M8 | Genau eine erkennbare Stärke oder Schwäche (z. B. gut bei Nacht, schnell aber mehr Verschleiß, langsam aber zuverlässig, Diagnose-Spezialist, Bergungs-Spezialist) | 14:30 | in 5.3 | siehe R6 |
| M9 | Bei der Auswahl ist verständlich, warum jemand geeignet oder ungeeignet ist | 14:30 | in 5.3 | – |

## B. Fahrzeuge (14:30 Teil 7)

| Nr. | Anforderung | Quelle | Status | Begründung / Hinweis |
|---|---|---|---|---|
| B1 | Klarer Einsatzzweck | 14:30 | in 5.3 | – |
| B2 | Zustand | 10:34, 14:30 | in 5.3 | – |
| B3 | Kraftstoff oder Akkustand | 10:34, 14:30 | in 5.3 | – |
| B4 | Ausrüstung | 10:34, 14:30 | in 5.3 | – |
| B5 | Geschwindigkeit | 10:34, 14:30 | in 5.3 | – |
| B6 | Kapazität | 14:30 | in 5.3 | – |
| B7 | Laufende Kosten | 14:30 | in 5.3 | – |
| B8 | Aktueller Status und voraussichtliche Verfügbarkeit | 14:30 | in 5.3 | – |
| B9 | Status genau diese 8: frei · Anfahrt · vor Ort · transportiert Fahrzeug · lädt ab · Rückfahrt · Wartung · Problem | 14:30 | in 5.3 | ⚠ Neuer gilt: ersetzt 11:21 und die 11 Status aus Plan 5c; feinere Phasen nur intern |
| B10 | Eigene Fahrzeuge jederzeit klar erkennbar und antippbar | 14:30 | in 5.3 | – |
| B11 | Beim Antippen kann die Kamera dem Fahrzeug folgen | 14:30 | in 5.3 | – |

## E. Einsätze und Entwicklungen (14:30 Teil 8)

| Nr. | Anforderung | Quelle | Status | Begründung / Hinweis |
|---|---|---|---|---|
| E1 | Batterie leer | 10:34, 14:30 | in 5.3 | – |
| E2 | Reifenpanne | 10:34, 14:30 | in 5.3 | – |
| E3 | Ausgesperrt | 10:34, 14:30 | in 5.3 | – |
| E4 | Kraftstoff leer | 14:30 | in 5.3 | ⚠ Neuer gilt: 10:34 hieß es „falscher Kraftstoff“. 14:30 nennt „Kraftstoff leer“; der Mac kann „falscher Kraftstoff“ als Variante behalten |
| E5 | Kleiner technischer Defekt | 10:34, 14:30 | in 5.3 | – |
| E6 | Abschleppen | 10:34, 14:30 | in 5.3 | – |
| E7 | Einfache Unfallbergung | 14:30 | in 5.3 | ⚠ Neuer gilt: 7 Einsatzarten statt 6 (10:34) |
| E8 | Entwicklung: Reparatur gelingt vor Ort | 14:30 | in 5.3 | – |
| E9 | Entwicklung: zusätzliches Teil wird benötigt | 14:30 | in 5.3 | – |
| E10 | Entwicklung: Kunde muss abgeschleppt werden | 14:30 | in 5.3 | – |
| E11 | Entwicklung: zweites Fahrzeug erforderlich | 14:30 | in 5.3 | – |
| E12 | Entwicklung: Auftrag war falsch gemeldet | 14:30 | in 5.3 | – |
| E13 | Entwicklung: Kunde storniert | 14:30 | in 5.3 | – |
| E14 | Entwicklung: Fahrzeug kann nicht sicher repariert werden | 14:30 | in 5.3 | – |
| E15 | Entwicklung: Folgeauftrag entsteht | 14:30 | in 5.3 | – |
| E16 | Ausgang hauptsächlich durch Mitarbeiter, Fahrzeug, Material, Entscheidung; Zufall klein | 13:05, 14:30 | in 5.3 | – |

## W. Spieltempo und Balance (14:30 Teil 9)

| Nr. | Anforderung | Quelle | Status | Begründung / Hinweis |
|---|---|---|---|---|
| W1 | Spieltag ca. 18 Minuten bei 1× | 13:05, 14:30 | in 5.3 | – |
| W2 | Pause, 1×, 2×, 4× | 13:05, 14:30 | in 5.3 | – |
| W3 | Auto-Pause bei dringenden Einsätzen und Entscheidungen | 13:05, 14:30 | in 5.3 | – |
| W4 | Anfangs ca. 8–12 Einsätze pro Tag | 14:03, 14:30 | in 5.3 | – |
| W5 | Maximal 4 gleichzeitige Aufträge am Anfang | 14:30 | in 5.3 | – |
| W6 | Ruhige Phasen erlaubt, aber nicht langweilig oder leer | 14:30, 14:36 | in 5.3 | – |
| W7 | Erste 30 Minuten verständlich und motivierend; die ersten 30–60 Minuten machen wirklich Spaß | 14:30 | in 5.3 | – |
| W8 | Geld weder bedeutungslos noch dauerhaft knapp | 14:30 | in 5.3 | Wirtschaft über 20 Tage prüfen (Q9) |
| W9 | Fehlentscheidungen spürbar, aber nicht spielzerstörend | 14:30 | in 5.3 | – |

## I. UI (14:30 Teil 10)

| Nr. | Anforderung | Quelle | Status | Begründung / Hinweis |
|---|---|---|---|---|
| I1 | Einheitliche Abstände, Rundungen, Schriftgrößen | 13:59, 14:30 | in 5.3 | – |
| I2 | Keine abgeschnittenen Texte | 14:30 | in 5.3 | – |
| I3 | Touchflächen mindestens 44 × 44 pt | 13:50, 14:30 | in 5.3 | – |
| I4 | Normalansicht zeigt nur Wichtiges, volle Zahlen hinter „Details“ | 14:15, 14:30 | in 5.3 | – |
| I5 | Klare Auswahlzustände | 14:30 | in 5.3 | – |
| I6 | Verständliche Warnungen | 14:30 | in 5.3 | – |
| I7 | Kein unnötiges Gold | 13:12, 14:30 | in 5.3 | gar kein Gold (G8) |
| I8 | Orange nur für Einsätze, Warnungen, aktive Aktionen | 14:30 | in 5.3 | – |
| I9 | Grün für verfügbar oder erfolgreich | 14:30 | in 5.3 | – |
| I10 | Rot nur für echte Probleme und Dringlichkeit | 14:30 | in 5.3 | – |
| I11 | Silber und Graphit als Grundlage | 13:12, 14:30 | in 5.3 | – |
| I12 | Verschiedene Symbole je Einsatzart | 13:50, 14:30 | in 5.3 | – |
| I13 | Marker werden beim Herauszoomen kleiner oder zusammengefasst | 14:30 | in 5.3 | – |
| I14 | Route auf jedem Straßenabschnitt erkennbar | 13:50, 14:30 | in 5.3 | – |
| I15 | Geld, Ruf, Zeit und Geschwindigkeit überladen den Bildschirm nicht | 14:30 | in 5.3 | – |

## C. Stadt und Präsentation (14:30 Teil 11)

| Nr. | Anforderung | Quelle | Status | Begründung / Hinweis |
|---|---|---|---|---|
| C1 | Einheitlicher Stil zwischen Fahrzeugen, Gebäuden, Kartenbildern, Stadt | 13:50, 14:30 | in 5.3 | – |
| C2 | Keine Mischung aus fotorealistischen Bildern und unpassenden Low-Poly-Modellen; realistische Materialien auf stilisierten Formen | 14:30 | in 5.3 | CC0 Poly Haven/ambientCG/Kenney einheitlich angepasst |
| C3 | Verkehr und Stadt wirken belebt | 14:30 | in 5.3 | – |
| C4 | Straßenlaternen, Fenster, Scheinwerfer, Rundumlichter sinnvoll | 14:30 | in 5.3 | – |
| C5 | Tag-, Abend- und Nachtstimmung | 14:30 | in 5.3 | Dämmerung am Morgen und ab 20 Uhr. Durchgehender Nachtbetrieb kommt erst mit Nachtdienst (Firmenstufe 5) |
| C6 | Dezente Kameraanimationen | 14:30 | in 5.3 | – |
| C7 | Keine übertriebenen Effekte oder störendes Leuchten | 13:12, 14:30 | in 5.3 | – |
| C8 | Zentrale und Ausbauten wachsen sichtbar auf der Karte | 11:06, 14:30, 14:43 | in 5.3 | – |

## N. Sound, Haptik, Rückmeldung (14:30 Teil 12)

| Nr. | Anforderung | Quelle | Status | Begründung / Hinweis |
|---|---|---|---|---|
| N1 | Eingehender Auftrag | 14:30 | in 5.3 | Ton + Haptik |
| N2 | Dringender Einsatz | 14:30 | in 5.3 | – |
| N3 | Fahrzeug startet | 14:30 | in 5.3 | – |
| N4 | Auftrag erfolgreich | 14:30 | in 5.3 | – |
| N5 | Auftrag fehlgeschlagen | 14:30 | in 5.3 | – |
| N6 | Geld erhalten oder bezahlt | 14:30 | in 5.3 | – |
| N7 | Ausbau abgeschlossen | 14:30 | in 5.3 | – |
| N8 | Warnung bei fehlendem Material | 14:30 | in 5.3 | – |
| N9 | Sounds und Haptik abschaltbar, keine dauernden oder nervigen Sirenen | 14:30 | in 5.3 | Töne nur aus Apple-Frameworks oder bereits freigegebenen Quellen |

## EI. Einstieg (14:30 Teil 13)

| Nr. | Anforderung | Quelle | Status | Begründung / Hinweis |
|---|---|---|---|---|
| EI1 | Ohne Erklärung verständlich, wie ein Auftrag angenommen wird | 14:30 | in 5.3 | – |
| EI2 | … wie Mitarbeiter und Fahrzeug ausgewählt werden | 14:30 | in 5.3 | – |
| EI3 | … was der Einsatz ungefähr kostet | 14:30 | in 5.3 | – |
| EI4 | … wie Gewinn entsteht | 14:30 | in 5.3 | – |
| EI5 | … warum ein Fahrzeug nicht verfügbar ist | 14:30 | in 5.3 | – |
| EI6 | … wohin ein abgeschlepptes Auto gebracht wird | 14:30 | in 5.3 | – |
| EI7 | … wie Material nachbestellt wird | 14:30 | in 5.3 | – |
| EI8 | … wie der Betrieb wächst | 14:30 | in 5.3 | Firmenstufe + Bauflächen |
| EI9 | Einführung direkt im echten Spiel, keine Textwand; Hinweise nach erster erfolgreicher Nutzung nicht erneut | 14:15, 14:30 | in 5.3 | – |

## MO. Motivation (Nachtrag 14:36)

| Nr. | Anforderung | Quelle | Status | Begründung / Hinweis |
|---|---|---|---|---|
| MO1 | Eigene Identität und Motivation, nicht nur vollständig funktionierend | 14:36 | in 5.3 | – |
| MO2 | Nach einem Einsatz will man freiwillig noch einen Auftrag erledigen | 14:36 | in 5.3 | – |
| MO3 | Wachstum auf der Karte sichtbar | 14:36, 14:43 | in 5.3 | – |
| MO4 | Entscheidungen erzeugen echte Unterschiede | 14:36 | in 5.3 | – |
| MO5 | Ruhige Momente wirken nicht leer | 14:36 | in 5.3 | – |
| MO6 | Schwierigkeitsgrade geprüft | 14:36 | in 5.3 | Ergebnis in der Schwächenliste nennen |
| MO7 | Atmosphäre geprüft | 14:36 | in 5.3 | – |
| MO8 | Wiederaufnahme geprüft (Weiterspielen nach Pause/Neustart verständlich) | 14:36 | in 5.3 | – |
| MO9 | Schutz vor unrettbaren Spielständen (z. B. Pleite ohne Ausweg) | 14:36 | in 5.3 | – |
| MO10 | Langfristige Motivation geprüft | 14:36 | in 5.3 | Firmenaufstieg als sichtbares Ziel |
| MO11 | Danach keine weiteren Funktionen, sondern spielen, vereinfachen, ausbalancieren, polieren | 14:36 | in 5.3 | – |

## F. Firmenentwicklung und Bausystem (14:43)

| Nr. | Anforderung | Quelle | Status | Begründung / Hinweis |
|---|---|---|---|---|
| F1 | Firma wächst wirklich sichtbar auf der Karte, nicht nur „Garage Stufe 2“ | 14:43 | in 5.3 | ⚠ Neuer gilt: ersetzt Garage/Werkstatt/Leitstelle mit je 3 Stufen |
| F2 | Firmenstufe 1 „Kleiner Familienbetrieb“: gemietete kleine Halle, 1 Servicewagen, 1 Abschlepper, 2 Mitarbeiter, kleiner Teilebestand, 4 Stellplätze, einfaches Büro | 14:43 | in 5.3 | – |
| F3 | Firmenstufe 2 „Eigener Betriebshof“ (größere Werkstatt, Stellplätze, Reifen-/Teile-/Altteillager, Waschplatz, Aufenthaltsraum, kleine Leitstelle, 4–6 Fahrzeuge) | 14:43 | Bauten Richtung Stufe 2 in 5.3, Aufstieg später (E6) | – |
| F4 | Firmenstufe 3 „Professioneller Abschleppdienst“ | 14:43 | später (E9–E15) | – |
| F5 | Firmenstufe 4 „Regionalunternehmen“ mit zweiter Niederlassung | 14:43 | später (E16–E18) | – |
| F6 | Firmenstufe 5 „Marktführer der Region“ | 14:43 | später (E19 + Endziel) | – |
| F7 | Echte freie Bauflächen auf dem Hof | 14:43 | in 5.3 | – |
| F8 | Bau-Auswahl auf der Fläche (in 5.3: Stellplatzfläche, Reifencontainer, Entsorgungsbereich, Lagerhalle, zusätzliche Garage) | 14:43 | in 5.3 | Werkstattplatz, Waschplatz, Mitarbeitergebäude, Leitstelle, Tankstelle/Ladesäule, Schwerlastgarage, Sammlungshalle kommen später mit ihrer Firmenstufe |
| F9 | Jeder Ausbau zeigt Kaufpreis oder Kredit, laufende Kosten, Bauzeit, Flächenbedarf, Voraussetzung (Genehmigung/Ruf), klaren Nutzen | 14:43 | in 5.3 | – |
| F10 | Bau dauert Spielzeit: Absperrungen, Baufahrzeuge, Baufortschritt sichtbar | 14:43 | in 5.3 | – |
| F11 | Danach steht das Gebäude wirklich dort, Fahrzeuge bzw. Mitarbeiter benutzen es | 14:43 | in 5.3 | – |
| F12 | Kredit als Alternative zum Kaufpreis | 14:43 | in 5.3 | – |
| F13 | Anzeige der Firmenstufe mit Fortschritt zum Aufstieg | 14:43 | in 5.3 | – |
| F14 | Normales Firmenwachstum ist Teil des kostenlosen Spiels | 14:43, 14:48 | in 5.3 | – |

## P. Preismodell (14:48)

| Nr. | Anforderung | Quelle | Status | Begründung / Hinweis |
|---|---|---|---|---|
| P1 | App kostenlos, komplette erste Welt spielbar; normaler Ausbau nie blockiert | 14:48 | in 5.3 | ⚠ Neuer gilt: ersetzt 14:43 „Echtgeld nur Designs“ |
| P2 | Shop ohne neuen Tab (Karte „Premium“ in der Zentrale), Käufe wiederherstellen | 14:48 | in 5.3 | – |
| P3 | Premium-Servicewagen 2,49 € (`premium.service`, +15 % Tempo) | 14:48 | in 5.3 | – |
| P4 | Premium-Abschlepper 3,99 € (`premium.tow`, eigene Animation, 15 % schneller laden) | 14:48 | in 5.3 | – |
| P5 | Premium-Zentrale 3,49 € (`premium.hq`, nur Optik) | 14:48 | in 5.3 | – |
| P6 | Werbung (automatisch) und „Werbung entfernen“ 5,99 € (`noads`) | 14:48 | später (wenn ein Werbe-SDK freigegeben ist) | Julian muss einen Werbeanbieter freigeben (G13). Bis dahin ist 5.3 werbefrei und `noads` ausgeblendet |
| P7 | Premium-Schwerlastfahrzeug 4,99 €, Premium-Fuhrpark 8,99 €, Premium-Unternehmen 12,99 € | 14:48 | später (mit Schwerlast-Update E15) | Inhalt existiert vorher nicht |
| P8 | Premium-Gebiet „Flughafen- und Eventbezirk“ 8,99 € (`area.event`) | 14:48 | später (Update P1) | – |
| P9 | Vaultoria Ultimate 17,99 € | 14:48 | später (mit P1, E15 und Werbe-SDK) | – |
| P10 | Spätere Erweiterungen: Zusatzregion 5,99 €, große Welt 8,99 €, Welt + Spezialfahrzeug 11,99 €, Designs 1,49–2,49 € | 14:48 | später | – |
| P11 | In-App-Käufe in App Store Connect angelegt (A1–A3) | 14:48 | in 5.3 (Julian) | Anleitung `AppStoreConnect-InApp-Kaeufe.md`, Teil A |

## Q. Qualität vor dem Upload (14:30 Teil 14)

| Nr. | Anforderung | Quelle | Status | Begründung / Hinweis |
|---|---|---|---|---|
| Q1 | Jede Ansicht auf verschiedenen iPhone-Größen geprüft | 14:30 | in 5.3 | mindestens SE, 6,1", 6,9" |
| Q2 | Keine Platzhalter | 10:34, 14:30 | in 5.3 | – |
| Q3 | Keine abgeschnittenen Texte | 14:30 | in 5.3 | – |
| Q4 | Keine wirkungslosen Buttons | 10:34, 14:30 | in 5.3 | – |
| Q5 | Keine unerklärlichen Geldbewegungen | 14:30 | in 5.3 | – |
| Q6 | Keine verschwindenden Fahrzeuge | 14:30 | in 5.3 | – |
| Q7 | Speichern und Laden mehrfach getestet | 14:30 | in 5.3 | – |
| Q8 | Alle Zeitgeschwindigkeiten erzeugen dasselbe Ergebnis | 14:30 | in 5.3 | Seed-Test 1× gegen 4× |
| Q9 | Wirtschaft über mindestens 20 simulierte Spieltage geprüft | 14:30 | in 5.3 | – |
| Q10 | Flüssige Karte und Animationen | 10:34, 14:30 | in 5.3 | 60 fps auf kleinen iPhones |
| Q11 | Vollständiger Spieltag im Simulator **und** auf echtem Gerät | 14:30 | in 5.3 | – |
| Q12 | Mindestens 10 unterschiedliche komplette Einsätze durchgespielt | 14:30 | in 5.3 | – |
| Q13 | Bestehende Spielstände sicher migriert | 14:30 | in 5.3 | S4 |
| Q14 | Alle automatisierten Tests grün | 14:30 | in 5.3 | – |
| Q15 | Keine unfertige Zwischenversion hochladen; erst intern ein polierter vertikaler Ausschnitt | 14:30 | in 5.3 | 5.2 wird nicht einzeln hochgeladen |

## L. Lieferung an Julian (14:30)

| Nr. | Anforderung | Quelle | Status | Begründung / Hinweis |
|---|---|---|---|---|
| L1 | Neuer TestFlight-Build (5.3) | 14:30 | in 5.3 | – |
| L2 | Screenshots aller überarbeiteten Bereiche | 14:30 | in 5.3 | als ZIP (Julians Wunsch: ZIP mit allen Bildern) |
| L3 | Kurzes Video eines vollständigen Einsatzes | 14:30 | in 5.3 | – |
| L4 | Liste aller Änderungen | 14:30 | in 5.3 | – |
| L5 | Ehrliche Liste verbleibender Schwächen | 14:30 | in 5.3 | – |
| L6 | Testergebnisse | 14:30 | in 5.3 | – |
| L7 | Sicherung der bisherigen Version | 14:30 | in 5.3 | S2 |
| L8 | Das Spiel fühlt sich zusammenhängend, verständlich, hochwertig und überraschend vollständig an, nicht wie eine abgearbeitete Liste | 14:30 | in 5.3 | ehrliches Selbsturteil des Mac in L5 |

## 5.4 Update nach Julians Test von 5.3 (15:57)

Gilt für den nächsten Build 5.4 zusätzlich zu allen Punkten oben. ⚠ Neuer gilt: Die hier vorgezogenen Punkte ersetzen bei P6–P10, F4/R7 (zweite Welt) und R9 (Gebiete) den Status „später“.

| Nr. | Anforderung | Quelle | Status | Begründung / Hinweis |
|---|---|---|---|---|
| V1 | Alle 14 Kaufpositionen eingebaut und kaufbar (15 Produkte, siehe `AppStoreConnect-InApp-Kaeufe.md` Teil A) | 15:57 | in 5.4 | ⚠ Neuer gilt: ersetzt „nur 3 in 5.3“ |
| V2 | Jeder Kauf liefert echten, spielbaren Inhalt (kein leeres Produkt) | 10:34, 14:48 | in 5.4 | Regel G14 |
| V3 | Werbung über einen kostenlosen Anbieter + „Werbung entfernen“ wirkt sofort | 14:48, 15:57 | in 5.4 | Anbieter in der Lieferung nennen, Datenschutz/ATT |
| V4 | Premium-Schwerlastfahrzeug mit eigenen großen Aufträgen | 14:48, 15:57 | in 5.4 | Plan 5d Punkt 8 |
| V5 | Premium-Gebiet „Flughafen- und Eventbezirk“ sichtbar, per Kauf freischaltbar, mit VIP-/Event-Aufträgen | 14:48, 15:57 | in 5.4 | P1 vorgezogen |
| V6 | Zusatzregion Bergland (Kauf) mit eigenen Einsätzen | 14:48, 15:57 | in 5.4 | – |
| V7 | Zweite Welt Küstenstadt (Kauf) mit eigener Firma; Weltwechsel | 14:48, 15:57 | in 5.4 | ⚠ Neuer gilt: R7 „zweite Welt erst später“ |
| V8 | Welt + Spezialfahrzeug (Hafen-Bergekran) | 14:48, 15:57 | in 5.4 | Auslegung als Paket, Julian kann korrigieren |
| V9 | Mindestens drei Design-Produkte (nur Optik) | 14:48, 15:57 | in 5.4 | – |
| V10 | Pakete Premium-Fuhrpark, Premium-Unternehmen, Ultimate schalten alle Teile frei | 14:48 | in 5.4 | bereits besessene Teile anzeigen |
| V11 | Optik dunkler und abwechslungsreicher, nicht „hell und eintönig“ | 15:57 | in 5.4 | UI 000f Punkt 1 |
| V12 | Keine komisch herumstehenden Autos: geparkte Autos ausgerichtet, keine Überschneidungen | 15:57 | in 5.4 | – |
| V13 | Jedes Fenster schließbar (✕ und Wischen), auch Flotte | 15:57 | in 5.4 | – |
| V14 | Fahrzeugbefehle: Tanken, Warten/Reparieren, Zur Zentrale, Folgen, Einsatz zuweisen | 15:57 | in 5.4 | – |
| V15 | Automatisch tanken unter 20 % (abschaltbar) | 15:57 | in 5.4 | Startwert des Docs-Threads |
| V16 | Betriebshof abgelegen am Stadtrand, nicht mittig, freie Fläche ringsum | 15:57 | in 5.4 | – |
| V17 | Hof-Objekte antippbar (Halle, Zapfstelle, Lager, Container, Stellplätze, Büro, Bauflächen) | 15:57 | in 5.4 | – |
| V18 | Baufläche erweiterbar: angrenzendes Grundstück mit Spielgeld kaufen | 15:57 | in 5.4 | 3 Erweiterungen, je +2 Bauflächen |
| V19 | Größere Welt | 15:57 | in 5.4 | – |
| V20 | Gebiete mit Spielgeld kaufbar (Wohnviertel + Bahnhof, Gewerbegebiet, Autobahn, Industriehafen, Land/Vororte) | 15:57 | in 5.4 | ⚠ Neuer gilt: E8 vorgezogen |
| V21 | Gesperrte Gebiete sichtbar, mit Preis, Voraussetzung und Nutzen beim Antippen | 15:57 | in 5.4 | – |
| V22 | Alles aus dem Block „in 5.3“ bleibt erfüllt (keine Rückschritte) | – | in 5.4 | – |

## O. Offen bei Julian

- App-Icon: Silber oder das bestehende Icon behalten. Bis zu seiner Entscheidung bleibt das bestehende.
- In-App-Käufe A1–A15 in App Store Connect anlegen (Anleitung Teil A); A10–A15 erst nach Bestätigung der IDs durch den Mac.
