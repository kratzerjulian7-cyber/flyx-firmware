# Vaultoria – In-App-Käufe in App Store Connect anlegen

Stand 14.10.2026, 15:00. Grundlage: Julians Preismodell vom 14.10.2026 14:48 (`design/Komplettueberarbeitung-5.3.md`, Nachtrag 3) und `design/Erweiterungsplan-Pannenhilfe.md` Teil 2c.

**Product-IDs sind Platzhalter.** Der Mac bestätigt die endgültigen IDs aus dem Code. Eine Product-ID lässt sich nach dem Anlegen **nie mehr ändern oder wiederverwenden**, also erst anlegen, wenn der Mac die ID bestätigt hat.

**Wann anlegen:** nur die Produkte, die im eingereichten Build wirklich kaufbar sind. Für 5.3 sind das die Produkte 1–4. Die Produkte 5–9 kommen erst mit dem passenden Update. „Werbefrei-Paket“ und „Werbung entfernen“ sind **ein** Produkt (gleicher Inhalt, gleicher Preis).

## Vorher einmal prüfen

1. https://appstoreconnect.apple.com öffnen, oben **Geschäft** (früher „Vereinbarungen, Steuern und Bankdaten“). Die **Vereinbarung für kostenpflichtige Apps** muss aktiv sein. Weil Flyx Map schon 1,99 € kostet, ist sie wahrscheinlich aktiv.
2. Der Build mit dem Shop (5.3) muss in App Store Connect hochgeladen sein. Den Screenshot für die Prüfung liefert der Mac.

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

## Die Käufe

| Nr. | Wann anlegen | Referenzname | Produkt-ID (Platzhalter) | Preis | Anzeigename (DE) | Beschreibung (DE) |
|---|---|---|---|---:|---|---|
| 1 | 5.3 | Werbung entfernen | `com.julian.vaultoria.removeads` | 5,99 € | Werbung entfernen | Entfernt die automatische Werbung dauerhaft. |
| 2 | 5.3 | Premium-Servicewagen | `com.julian.vaultoria.vehicle.service` | 2,49 € | Premium-Servicewagen | Exklusiver Servicewagen mit Spezialisierung. |
| 3 | 5.3 | Premium-Abschlepper | `com.julian.vaultoria.vehicle.tow` | 3,99 € | Premium-Abschlepper | Exklusiver Abschlepper mit eigener Animation. |
| 4 | 5.3 | Premium-Zentrale | `com.julian.vaultoria.hq` | 3,49 € | Premium-Zentrale | Exklusiver Betriebshof mit Beleuchtung. |
| 5 | mit Schwerlast-Update | Premium-Schwerlastfahrzeug | `com.julian.vaultoria.vehicle.heavy` | 4,99 € | Premium-Schwerlastfahrzeug | Besonderes Fahrzeug für große Aufträge. |
| 6 | mit Nr. 5 | Premium-Fuhrpark | `com.julian.vaultoria.fleet` | 8,99 € | Premium-Fuhrpark | Alle drei Premium-Einsatzfahrzeuge. |
| 7 | mit Nr. 5 | Premium-Unternehmen | `com.julian.vaultoria.bundle.business` | 12,99 € | Premium-Unternehmen | Werbefrei, Premium-Fuhrpark und -Zentrale. |
| 8 | mit Update P1 | Flughafen- und Eventbezirk | `com.julian.vaultoria.area.airport` | 8,99 € | Flughafen- und Eventbezirk | Neues Gebiet mit VIP- und Event-Aufträgen. |
| 9 | mit Nr. 5 und Nr. 8 | Vaultoria Ultimate | `com.julian.vaultoria.bundle.ultimate` | 17,99 € | Vaultoria Ultimate | Werbefrei und alle Premium-Inhalte. |

Spätere Erweiterungen (Zusatzregion 5,99 €, große Welt 8,99 €, Welt mit Spezialfahrzeug 11,99 €, Designs 1,49–2,49 €) bekommen eigene Zeilen, sobald sie gebaut sind.

## Prüfungsnotiz (bei jedem Kauf gleich, Namen anpassen)

> Purchase location: tab "Zentrale" → card "Premium". This is a one-time, non-consumable unlock of [PRODUCT NAME]. The complete main world is fully playable without any purchase; purchases never block normal progress. "Restore Purchases" is available in Settings and at the bottom of the Premium card.

(Deutsch zum Verständnis: Kauf im Tab „Zentrale“ → Karte „Premium“. Einmaliger Kauf, die Hauptwelt ist ohne Kauf vollständig spielbar, „Käufe wiederherstellen“ steht in den Einstellungen.)

## Was sich am Store-Eintrag mit 5.3 ändert

- **App-Informationen / Altersfreigabe:** Bei der Frage nach Werbung **Ja** angeben, sobald der Build Werbung zeigt.
- **App-Datenschutz:** Die Angaben des Werbeanbieters eintragen (Tabelle in `Vaultoria-Store-Texte.md`, Teil Datenschutz). Wenn der Anbieter trackt, braucht der Build den ATT-Hinweis.
- **Store-Texte:** Nur Käufe nennen, die im Build kaufbar sind. Die Texte schreibe ich neu, sobald 5.3 spielbar ist.

## Hinweis zu den Paketen

Apple rechnet bei Paketen bereits gekaufte Teile nicht automatisch an. Der Shop sollte bei einem Paket deshalb anzeigen, welche Teile du schon besitzt. Den Preis kann das Spiel nicht selbst senken. Möglich ist nur, Pakete auszublenden, wenn schon alle Teile gekauft sind. Das setzt der Mac so um, außer du willst es anders.
