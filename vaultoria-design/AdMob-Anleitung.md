# Vaultoria – Werbung mit Google AdMob einrichten

Stand 14.10.2026, 16:55. Grund: Julian 16:46 „können wir die Werbung jetzt gleich machen, dass die Werbung gleich mit drinnen ist?“ → Werbung kommt in 5.4. AdMob ist kostenlos, Google zahlt dir einen Anteil der Werbeeinnahmen aus.

**Was du am Ende an den Mac gibst (zwei Zeilen, keine Passwörter):**
- App-ID: `ca-app-pub-XXXXXXXXXXXXXXXX~YYYYYYYYYY` (mit **~**)
- Werbeeinheit „Tagesabrechnung“: `ca-app-pub-XXXXXXXXXXXXXXXX/ZZZZZZZZZZ` (mit **/**)

Diese IDs sind nicht geheim (sie stehen später in der App). Bis du sie hast, baut der Mac mit Googles Test-IDs, 5.4 wartet also nicht auf dich.

## Teil A: Konto und App anlegen

1. https://admob.google.com öffnen → **Jetzt starten** → mit deinem Google-Konto anmelden.
2. Land **Deutschland**, Zeitzone **Berlin**, Währung **EUR** → Nutzungsbedingungen bestätigen → **AdMob-Konto erstellen**.
3. Links **Apps** → **App hinzufügen**.
4. Plattform **iOS**.
5. Frage „Ist die App in einem unterstützten App-Shop veröffentlicht?“ → **Nein** (Vaultoria ist noch nicht im Store). Verknüpfen kannst du später.
6. App-Name: `Vaultoria` → **App hinzufügen**.
7. Die angezeigte **App-ID** (`ca-app-pub-…~…`) kopieren und notieren → **Weiter: Anzeigenblock erstellen**.

## Teil B: Werbeeinheit anlegen

Nach UI-Vorgabe 000e: nur Vollbild bei der Tagesabrechnung, höchstens 1 pro Spieltag. Also **Interstitial**, kein Banner, kein Rewarded.

1. Formate-Auswahl → **Interstitial** → **Auswählen**.
2. Name des Anzeigenblocks: `Tagesabrechnung`.
3. Erweiterte Einstellungen: **Anzeigentypen** nur **Display** und **Video** lassen (Standard). Häufigkeitsbegrenzung **nicht** setzen, das regelt das Spiel selbst.
4. **Anzeigenblock erstellen** → die **Anzeigenblock-ID** (`ca-app-pub-…/…`) kopieren und notieren → **Fertig**.

## Teil C: Einwilligung (Pflicht in der EU)

1. Links **Datenschutz und Mitteilungen**.
2. Karte **DSGVO** (Europäische Vorschriften) → **Mitteilung erstellen**.
   - App: **Vaultoria**, Sprache: **Deutsch** (zusätzlich Englisch, wenn angeboten).
   - Datenschutzerklärung-URL: die Datenschutz-Seite der Vaultoria-Webseite (steht in `Vaultoria-Store-Texte.md`; die Seite ist erst online, wenn du die Webseite freigibst).
   - Auswahl für Nutzer: **Einwilligen**, **Nicht einwilligen**, **Optionen verwalten** (Standard lassen).
   - Stil: dunkler Hintergrund, Schrift weiß/silber, Knöpfe grau (kein Blau, kein Gold), wenn der Editor das erlaubt.
   - **Veröffentlichen**.
3. Karte **IDFA-Erklärung** (iOS) → **Mitteilung erstellen** → App **Vaultoria** → Text: „Damit kann dir Werbung angezeigt werden, die besser zu dir passt.“ → **Veröffentlichen**.
4. Karte **US-Bundesstaaten**: kannst du auslassen.

## Teil D: Auszahlung (erst wenn Geld reinkommt nötig)

1. Links **Zahlungen** → **Zahlungsinformationen hinzufügen**.
2. Kontotyp **Privat** (bis du ein Gewerbe hast), Name und **deine echte Adresse**, dann Bankkonto. Google prüft die Adresse später mit einem Brief mit PIN.
3. Steuerinfos ausfüllen, wenn AdMob danach fragt.

Ohne Zahlungsdaten läuft die Werbung trotzdem, das Geld sammelt sich nur an.

## Teil E: Was der Mac damit macht (zur Info)

- Google Mobile Ads SDK und Einwilligungs-SDK über Swift Package Manager.
- In `Info.plist`: `GADApplicationIdentifier` = deine App-ID, die SKAdNetwork-Liste von Google und `NSUserTrackingUsageDescription` (DE „Damit kann dir Werbung angezeigt werden, die besser zu dir passt.“ / EN „This lets us show you ads that are more relevant to you.“).
- Reihenfolge: Einwilligungsdialog → ATT-Abfrage → Werbung laden. Ohne Zustimmung nur nicht personalisierte Werbung.
- Interstitial bei der Tagesabrechnung, nie in den ersten 30 Minuten, nie während Entscheidung oder Einsatz. Mit `noads`, `bundle.company` oder `bundle.ultimate` keine Werbung und keine Abfrage.
- Während der Entwicklung Googles Test-IDs (App `ca-app-pub-3940256099942544~1458002511`, Interstitial `ca-app-pub-3940256099942544/4411468910`). **Nie auf echte Werbung in eigenen Builds tippen**, sonst sperrt Google das Konto. Dein iPhone kann der Mac als Testgerät eintragen.

## Teil F: App-Datenschutz in App Store Connect (vor der 5.4-Einreichung)

https://appstoreconnect.apple.com/apps → **Vaultoria** → links **App-Datenschutz** → **Bearbeiten** (bzw. „Los geht's“).

1. „Erfassen Sie oder Ihre Drittanbieter Daten aus dieser App?“ → **Ja, wir erfassen Daten aus dieser App**.
2. Diese Datentypen anhaken, sonst nichts:
   - **Standort** → **Ungefährer Standort**
   - **Kennungen** → **Geräte-ID**
   - **Nutzungsdaten** → **Produktinteraktion**, **Werbedaten**
   - **Diagnose** → **Absturzdaten**, **Leistungsdaten**, **Andere Diagnosedaten**
3. Für jeden Datentyp die Fragen so beantworten:

| Datentyp | Zwecke | Mit Identität verknüpft? | Für Tracking verwendet? |
|---|---|---|---|
| Ungefährer Standort | Werbung durch Dritte, Analyse | Nein | Nein |
| Geräte-ID | Werbung durch Dritte, Analyse | Nein | **Ja** |
| Produktinteraktion | Werbung durch Dritte, Analyse | Nein | Nein |
| Werbedaten | Werbung durch Dritte, Analyse | Nein | Nein |
| Absturzdaten | Analyse | Nein | Nein |
| Leistungsdaten | Analyse | Nein | Nein |
| Andere Diagnosedaten | Analyse | Nein | Nein |

4. **Veröffentlichen** (das geht erst live, wenn 5.4 freigegeben wird).
5. Altersfreigabe: bei der Frage nach Werbung **Ja**.

Grundlage ist Googles Angabe für das Google Mobile Ads SDK. Kurz vor dem Einreichen gleicht der Mac sie mit der aktuellen Liste von Google ab (Stichwort „Google Mobile Ads SDK App Store data disclosure“); ändert Google etwas, gilt Googles Liste. Eine rechtliche Garantie ist das nicht.

## Später (nicht für 5.4 nötig)

- Nach der Freigabe im App Store: in AdMob **Apps** → **Vaultoria** → **App-Einstellungen** → **App-Shop-Details hinzufügen** → Vaultoria verknüpfen. Erst danach liefert Google volle Werbung.
- `app-ads.txt`: Google zeigt dir eine Zeile, die auf der Startseite der Domain liegen muss, die im App Store als Entwickler-Webseite steht. Das richte ich mit dir ein, wenn die Vaultoria-Webseite live ist.
