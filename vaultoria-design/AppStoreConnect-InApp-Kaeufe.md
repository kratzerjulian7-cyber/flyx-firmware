# Vaultoria – In-App-Käufe in App Store Connect anlegen

Stand 14.10.2026, 15:05 (Product-IDs vom Mac bestätigt, stehen so in `Shop.swift` und `Vaultoria.storekit`). Grundlage: Julians Preismodell vom 14.10.2026 14:48 (`design/Komplettueberarbeitung-5.3.md`, Nachtrag 3) und `design/Erweiterungsplan-Pannenhilfe.md` Teil 2c.

**Die Product-IDs sind endgültig.** Bitte buchstabengenau übernehmen (am besten kopieren). Eine Product-ID lässt sich nach dem Anlegen **nie mehr ändern oder wiederverwenden**.

**Wann anlegen:** nur die Produkte, die im eingereichten Build wirklich kaufbar sind. Das sind für 5.3 **die 3 Produkte in Teil A**. Die Produkte in Teil B kommen erst mit dem passenden Update. „Werbefrei-Paket“ und „Werbung entfernen“ sind **ein** Produkt (gleicher Inhalt, gleicher Preis).

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

## Teil A: Jetzt für 5.3 anlegen (3 Käufe)

| Nr. | Referenzname | Produkt-ID | Typ | Preis | Anzeigename (DE) | Beschreibung (DE) | Wirkung im Spiel |
|---|---|---|---|---:|---|---|---|
| A1 | Premium-Servicewagen | `com.julian.vaultoria.premium.service` | Nicht-Verbrauchsartikel | 2,49 € | Premium-Servicewagen | Exklusiver Servicewagen mit Spezialisierung. | eigenes Modell, +15 % Tempo |
| A2 | Premium-Abschlepper | `com.julian.vaultoria.premium.tow` | Nicht-Verbrauchsartikel | 3,99 € | Premium-Abschlepper | Exklusiver Abschlepper mit eigener Animation. | eigenes Modell, 15 % schneller auf- und abladen |
| A3 | Premium-Zentrale | `com.julian.vaultoria.premium.hq` | Nicht-Verbrauchsartikel | 3,49 € | Premium-Zentrale | Exklusiver Betriebshof mit Beleuchtung. | nur Optik |

## Teil B: Später anlegen (6 Käufe, erst mit dem passenden Update)

| Nr. | Wann | Referenzname | Produkt-ID | Typ | Preis | Anzeigename (DE) | Beschreibung (DE) |
|---|---|---|---|---|---:|---|---|
| B1 | sobald ein Werbe-SDK freigegeben und im Build ist | Werbung entfernen | `com.julian.vaultoria.noads` | Nicht-Verbrauchsartikel | 5,99 € | Werbung entfernen | Entfernt die automatische Werbung dauerhaft. |
| B2 | mit dem Schwerlast-Update | Premium-Schwerlastfahrzeug | `com.julian.vaultoria.premium.heavy` | Nicht-Verbrauchsartikel | 4,99 € | Premium-Schwerlastfahrzeug | Besonderes Fahrzeug für große Aufträge. |
| B3 | mit B2 | Premium-Fuhrpark | `com.julian.vaultoria.premium.fleet` | Nicht-Verbrauchsartikel | 8,99 € | Premium-Fuhrpark | Alle drei Premium-Einsatzfahrzeuge. |
| B4 | mit B1 und B2 | Premium-Unternehmen | `com.julian.vaultoria.bundle.company` | Nicht-Verbrauchsartikel | 12,99 € | Premium-Unternehmen | Werbefrei, Premium-Fuhrpark und -Zentrale. |
| B5 | mit Update P1 | Flughafen- und Eventbezirk | `com.julian.vaultoria.area.event` | Nicht-Verbrauchsartikel | 8,99 € | Flughafen- und Eventbezirk | Neues Gebiet mit VIP- und Event-Aufträgen. |
| B6 | mit B1, B2 und B5 | Vaultoria Ultimate | `com.julian.vaultoria.bundle.ultimate` | Nicht-Verbrauchsartikel | 17,99 € | Vaultoria Ultimate | Werbefrei und alle Premium-Inhalte. |

Spätere Erweiterungen (Zusatzregion 5,99 €, große Welt 8,99 €, Welt mit Spezialfahrzeug 11,99 €, Designs 1,49–2,49 €) bekommen eigene Zeilen, sobald sie gebaut sind.

## Prüfungsnotiz (bei jedem Kauf gleich, Namen anpassen)

> Purchase location: tab "Zentrale" → card "Premium". This is a one-time, non-consumable unlock of [PRODUCT NAME]. The complete main world is fully playable without any purchase; purchases never block normal progress. "Restore Purchases" is available in Settings and at the bottom of the Premium card.

(Deutsch zum Verständnis: Kauf im Tab „Zentrale“ → Karte „Premium“. Einmaliger Kauf, die Hauptwelt ist ohne Kauf vollständig spielbar, „Käufe wiederherstellen“ steht in den Einstellungen.)

## Was sich am Store-Eintrag mit 5.3 ändert

- **App-Informationen / Altersfreigabe:** 5.3 zeigt noch **keine Werbung**, also bei der Frage nach Werbung **Nein**. Auf **Ja** stellen, sobald ein Build mit Werbe-SDK eingereicht wird.
- **App-Datenschutz:** Erst mit dem Werbe-SDK die Angaben des Werbeanbieters eintragen (Tabelle in `Vaultoria-Store-Texte.md`, Teil Datenschutz). Wenn der Anbieter trackt, braucht der Build den ATT-Hinweis.
- **Store-Texte:** Nur Käufe nennen, die im Build kaufbar sind. Die Texte schreibe ich neu, sobald 5.3 spielbar ist.

## Hinweis zu den Paketen

Apple rechnet bei Paketen bereits gekaufte Teile nicht automatisch an. Der Shop sollte bei einem Paket deshalb anzeigen, welche Teile du schon besitzt. Den Preis kann das Spiel nicht selbst senken. Möglich ist nur, Pakete auszublenden, wenn schon alle Teile gekauft sind. Das setzt der Mac so um, außer du willst es anders.
