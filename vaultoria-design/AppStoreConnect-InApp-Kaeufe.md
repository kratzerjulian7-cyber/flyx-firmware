# Vaultoria – In-App-Käufe in App Store Connect anlegen

Stand 14.10.2026, 16:10. Umgebaut auf alle 14 Kaufpositionen für 5.4 (Julian 15:57). Die Product-IDs der ersten 9 hat der Mac bestätigt, sie stehen so in `Shop.swift` und `Vaultoria.storekit`. Die IDs der Welt- und Design-Produkte (A10–A15) sind **Vorschläge**, bis der Mac sie bestätigt. Grundlage: Julians Preismodell vom 14.10.2026 14:48 (`design/Komplettueberarbeitung-5.3.md`, Nachtrag 3) und `design/Erweiterungsplan-Pannenhilfe.md` Teil 2c.

**Product-IDs buchstabengenau übernehmen** (am besten kopieren). Eine Product-ID lässt sich nach dem Anlegen **nie mehr ändern oder wiederverwenden**. Die mit „Vorschlag“ markierten erst anlegen, wenn der Mac sie bestätigt hat.

**Deine 14 Positionen = 15 Produkte in App Store Connect:** „Werbung entfernen“ und „Werbefrei-Paket“ sind dasselbe (gleicher Inhalt, gleicher Preis) und damit **ein** Produkt. „Einzelne Designs“ sind drei eigene Produkte.

**Wann anlegen:** Alle Produkte in Teil A kommen mit **5.4**. Anlegen kannst du sie sofort, einreichen nur zusammen mit dem 5.4-Build, der sie wirklich enthält.

## Vorher einmal prüfen

1. https://appstoreconnect.apple.com öffnen, oben **Geschäft** (früher „Vereinbarungen, Steuern und Bankdaten“). Die **Vereinbarung für kostenpflichtige Apps** muss aktiv sein. Weil Flyx Map schon 1,99 € kostet, ist sie wahrscheinlich aktiv.
2. Der Build mit dem Shop (5.4) muss in App Store Connect hochgeladen sein. Den Screenshot für die Prüfung liefert der Mac.

## So legst du jeden Kauf an

1. https://appstoreconnect.apple.com/apps → **Vaultoria**.
2. Links unter **Monetarisierung** → **In-App-Käufe** → **+** (bzw. „Erstellen“).
3. **Typ:** Nicht-Verbrauchsartikel. **Referenzname** und **Produkt-ID** aus der Tabelle unten eintragen → **Erstellen**.
4. **Verfügbarkeit:** alle Länder und Regionen (Standard lassen).
5. **Preisplan** → **Preis hinzufügen** (bzw. „Preis festlegen“) → Basisland **Deutschland (EUR)** → Preis aus der Tabelle wählen → **Weiter** → die anderen Länder automatisch übernehmen lassen → **Bestätigen**.
6. **App Store-Lokalisierung** → **+** → **Deutsch** → **Anzeigename** und **Beschreibung** aus der Tabelle einsetzen (höchstens 30 bzw. 45 Zeichen, die Texte unten passen). Optional später noch Englisch.
7. **Prüfungsinformationen:** den Screenshot der Premium-Karte vom Mac hochladen und die **Prüfungsnotiz** unten einsetzen → **Sichern**.
8. Der Status wird zu **„Bereit zur Einreichung“**.
9. Den **ersten** Kauf reichst du zusammen mit einer App-Version ein. Dafür auf der Versionsseite (z. B. 5.3) im Bereich **In-App-Käufe und Abonnements** die Käufe auswählen und dann die Version einreichen.

## Teil A: Alles für 5.4 anlegen (15 Produkte)

Alle Produkte haben den Typ **Nicht-Verbrauchsartikel**.

| Nr. | Deine Position | Referenzname | Produkt-ID | Preis | Anzeigename (DE) | Beschreibung (DE) |
|---|---|---|---|---:|---|---|
| A1 | 1 Werbung entfernen + 8 Werbefrei-Paket | Werbung entfernen | `com.julian.vaultoria.noads` | 5,99 € | Werbung entfernen | Entfernt die automatische Werbung dauerhaft. |
| A2 | 2 Premium-Servicewagen | Premium-Servicewagen | `com.julian.vaultoria.premium.service` | 2,49 € | Premium-Servicewagen | Exklusiver Servicewagen mit Spezialisierung. |
| A3 | 3 Premium-Abschlepper | Premium-Abschlepper | `com.julian.vaultoria.premium.tow` | 3,99 € | Premium-Abschlepper | Exklusiver Abschlepper mit eigener Animation. |
| A4 | 4 Premium-Schwerlastfahrzeug | Premium-Schwerlastfahrzeug | `com.julian.vaultoria.premium.heavy` | 4,99 € | Premium-Schwerlastfahrzeug | Besonderes Fahrzeug für große Aufträge. |
| A5 | 5 Premium-Zentrale | Premium-Zentrale | `com.julian.vaultoria.premium.hq` | 3,49 € | Premium-Zentrale | Exklusiver Betriebshof mit Beleuchtung. |
| A6 | 6 Premium-Fuhrpark | Premium-Fuhrpark | `com.julian.vaultoria.premium.fleet` | 8,99 € | Premium-Fuhrpark | Alle drei Premium-Einsatzfahrzeuge. |
| A7 | 7 Premium-Gebiet | Flughafen- und Eventbezirk | `com.julian.vaultoria.area.event` | 8,99 € | Flughafen- und Eventbezirk | Neues Gebiet mit VIP- und Event-Aufträgen. |
| A8 | 9 Premium-Unternehmen | Premium-Unternehmen | `com.julian.vaultoria.bundle.company` | 12,99 € | Premium-Unternehmen | Werbefrei, Premium-Fuhrpark und -Zentrale. |
| A9 | 10 Vaultoria Ultimate | Vaultoria Ultimate | `com.julian.vaultoria.bundle.ultimate` | 17,99 € | Vaultoria Ultimate | Werbefrei und alle Premium-Inhalte. |
| A10 | 11 Kleine Zusatzregion | Zusatzregion Bergland | `com.julian.vaultoria.world.region` (Vorschlag) | 5,99 € | Bergland | Neue Region mit Passstraßen und Bergungen. |
| A11 | 12 Große neue Welt | Welt Küstenstadt | `com.julian.vaultoria.world.large` (Vorschlag) | 8,99 € | Küstenstadt | Zweite Spielwelt mit eigener Firma. |
| A12 | 13 Welt inkl. Spezialfahrzeug | Welt Küstenstadt + Hafenkran | `com.julian.vaultoria.world.special` (Vorschlag) | 11,99 € | Küstenstadt + Hafenkran | Zweite Welt mit exklusivem Hafen-Bergekran. |
| A13 | 14 Design | Design Lackierung Nachtschicht | `com.julian.vaultoria.design.paint.night` (Vorschlag) | 1,49 € | Lackierung Nachtschicht | Mattes Graphit mit orangem Streifen. |
| A14 | 14 Design | Design Zentrale Backstein | `com.julian.vaultoria.design.hq.brick` (Vorschlag) | 1,99 € | Zentrale Backstein-Klassik | Klassische Backsteinfassade für die Zentrale. |
| A15 | 14 Design | Design Fuhrpark Retro | `com.julian.vaultoria.design.fleet.retro` (Vorschlag) | 2,49 € | Fuhrpark Retro-Lackierung | Retro-Lackierung für alle eigenen Fahrzeuge. |

Namen von Region, Welt und Designs sind Arbeitsnamen des Docs-Threads und fiktiv. Du kannst sie vor dem Anlegen ändern, Anzeigename höchstens 30, Beschreibung höchstens 45 Zeichen.

## Prüfungsnotiz (bei jedem Kauf gleich, Namen anpassen)

> Purchase location: tab "Zentrale" → card "Premium". This is a one-time, non-consumable unlock of [PRODUCT NAME]. The complete main world is fully playable without any purchase; purchases never block normal progress. "Restore Purchases" is available in Settings and at the bottom of the Premium card.

(Deutsch zum Verständnis: Kauf im Tab „Zentrale“ → Karte „Premium“. Einmaliger Kauf, die Hauptwelt ist ohne Kauf vollständig spielbar, „Käufe wiederherstellen“ steht in den Einstellungen.)

## Was sich am Store-Eintrag mit 5.4 ändert

- **App-Informationen / Altersfreigabe:** 5.4 zeigt Werbung, also bei der Frage nach Werbung **Ja**.
- **App-Datenschutz:** Die Angaben des Werbeanbieters eintragen (der Mac nennt den Anbieter) (Tabelle in `Vaultoria-Store-Texte.md`, Teil Datenschutz). Wenn der Anbieter trackt, braucht der Build den ATT-Hinweis.
- **Store-Texte:** Nur Käufe nennen, die im Build kaufbar sind. Die Texte schreibe ich neu, sobald 5.3 spielbar ist.

## Hinweis zu den Paketen

Apple rechnet bei Paketen bereits gekaufte Teile nicht automatisch an. Der Shop sollte bei einem Paket deshalb anzeigen, welche Teile du schon besitzt. Den Preis kann das Spiel nicht selbst senken. Möglich ist nur, Pakete auszublenden, wenn schon alle Teile gekauft sind. Das setzt der Mac so um, außer du willst es anders.
