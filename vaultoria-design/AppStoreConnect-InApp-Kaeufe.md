# Vaultoria – In-App-Käufe in App Store Connect anlegen

Stand 14.10.2026, 16:55. **Neu (Julian 16:46): „Werbung entfernen“ 6,99 €, Werbung schon in 5.4, alle 14 Produkte gehen mit 5.4 in die Prüfung.** Alle 14 Produkte für 5.4 (Julian 15:57). **Alle Product-IDs sind vom Mac endgültig festgelegt.** Sie stehen so in `Shop.swift` und `Vaultoria.storekit`. Grundlage: Julians Preismodell vom 14.10.2026 14:48 (`design/Komplettueberarbeitung-5.3.md`, Nachtrag 3) und `design/Erweiterungsplan-Pannenhilfe.md` Teil 2c.

**Product-IDs buchstabengenau übernehmen** (am besten kopieren). Eine Product-ID lässt sich nach dem Anlegen **nie mehr ändern oder wiederverwenden**.

**Wann anlegen:** Alle 14 Produkte kannst du sofort anlegen. Eingereicht werden alle 14 zusammen mit dem 5.4-Build.

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

## Teil A: Alles für 5.4 anlegen (14 Produkte)

Alle Produkte haben den Typ **Nicht-Verbrauchsartikel**. Vor jede ID kommt `com.julian.vaultoria.` (in der Tabelle schon ausgeschrieben).

| Nr. | Referenzname | Produkt-ID | Preis | Anzeigename (DE) | Beschreibung (DE) | Inhalt |
|---|---|---|---:|---|---|---|
| A1 | Werbung entfernen | `com.julian.vaultoria.noads` | **6,99 €** | Werbung entfernen | Entfernt die automatische Werbung dauerhaft. | = auch dein „Werbefrei-Paket“ |
| A2 | Premium-Servicewagen | `com.julian.vaultoria.premium.service` | 2,49 € | Premium-Servicewagen | Exklusiver Servicewagen mit Spezialisierung. | – |
| A3 | Premium-Abschlepper | `com.julian.vaultoria.premium.tow` | 3,99 € | Premium-Abschlepper | Exklusiver Abschlepper mit eigener Animation. | – |
| A4 | Premium-Schwerlastfahrzeug | `com.julian.vaultoria.premium.heavy` | 4,99 € | Premium-Schwerlastfahrzeug | Besonderes Fahrzeug für große Aufträge. | – |
| A5 | Premium-Zentrale | `com.julian.vaultoria.premium.hq` | 3,49 € | Premium-Zentrale | Exklusiver Betriebshof mit Beleuchtung. | – |
| A6 | Premium-Fuhrpark | `com.julian.vaultoria.premium.fleet` | 8,99 € | Premium-Fuhrpark | Alle drei Premium-Einsatzfahrzeuge. | A2 + A3 + A4 |
| A7 | Premium-Unternehmen | `com.julian.vaultoria.bundle.company` | 12,99 € | Premium-Unternehmen | Werbefrei, Premium-Fuhrpark und -Zentrale. | A1 + A2 + A3 + A4 + A5 |
| A8 | Vaultoria Ultimate | `com.julian.vaultoria.bundle.ultimate` | 17,99 € | Vaultoria Ultimate | Werbefrei und alle Premium-Inhalte. | A1 + A2 + A3 + A4 + A5 + A9 |
| A9 | Flughafen- und Eventbezirk | `com.julian.vaultoria.area.event` | 8,99 € | Flughafen- und Eventbezirk | Neues Gebiet mit VIP- und Event-Aufträgen. | Premium-Gebiet |
| A10 | Zusatzregion Seeufer | `com.julian.vaultoria.region.extra` | 5,99 € | Seeufer | Neue Region am Seeufer mit eigenen Einsätzen. | kleine Zusatzregion |
| A11 | Große Welt Umland Ost | `com.julian.vaultoria.world.large` | 8,99 € | Umland Ost | Große neue Welt mit eigener Firma. | große neue Welt |
| A12 | Welt Bergland mit Bergekran | `com.julian.vaultoria.world.special` | 11,99 € | Bergland mit Bergekran | Neue Welt Bergland mit exklusivem Bergekran. | Welt + Spezialfahrzeug |
| A13 | Design Carbon | `com.julian.vaultoria.design.carbon` | 1,49 € | Design Carbon | Carbon-Optik für deine Einsatzfahrzeuge. | nur Optik |
| A14 | Design Nachtlicht | `com.julian.vaultoria.design.night` | 2,49 € | Design Nachtlicht | Nachtlicht-Optik für Fahrzeuge und Zentrale. | nur Optik |

**Deine 14 Positionen:** „Werbung entfernen“ und „Werbefrei-Paket“ sind ein Produkt (A1). Dafür gibt es zwei Designs (A13, A14). Das ergibt 14 Produkte. Die Texte sind Vorschläge und passen in Apples Grenzen (Name höchstens 30, Beschreibung höchstens 45 Zeichen). Du kannst sie ändern, die IDs nicht.

**A1 (Werbung entfernen) auf 6,99 € umstellen:** A1 steht bei dir schon mit 6,99 € drin. Das passt jetzt, du musst nichts ändern. 5.4 enthält Werbung (Google AdMob), deshalb kommt A1 mit allen anderen Käufen in die 5.4-Einreichung. Das AdMob-Konto legst du nach `AdMob-Anleitung.md` an.

## Prüfungsnotiz (bei jedem Kauf gleich, Namen anpassen)

> Purchase location: tab "Zentrale" → card "Premium". This is a one-time, non-consumable unlock of [PRODUCT NAME]. The complete main world is fully playable without any purchase; purchases never block normal progress. "Restore Purchases" is available in Settings and at the bottom of the Premium card.

(Deutsch zum Verständnis: Kauf im Tab „Zentrale“ → Karte „Premium“. Einmaliger Kauf, die Hauptwelt ist ohne Kauf vollständig spielbar, „Käufe wiederherstellen“ steht in den Einstellungen.)

## Was sich am Store-Eintrag mit 5.4 ändert

- **App-Informationen / Altersfreigabe:** 5.4 zeigt Werbung, also bei der Frage nach Werbung **Ja**.
- **App-Datenschutz:** vor der 5.4-Einreichung neu ausfüllen, Schritt für Schritt in `AdMob-Anleitung.md`, Teil F.
- **Store-Texte:** Nur Käufe nennen, die im Build kaufbar sind. Die Texte schreibe ich neu, sobald 5.3 spielbar ist.

## Hinweis zu den Paketen

Apple rechnet bei Paketen bereits gekaufte Teile nicht automatisch an. Der Shop sollte bei einem Paket deshalb anzeigen, welche Teile du schon besitzt. Den Preis kann das Spiel nicht selbst senken. Möglich ist nur, Pakete auszublenden, wenn schon alle Teile gekauft sind. Das setzt der Mac so um, außer du willst es anders.
