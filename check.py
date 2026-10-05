#!/usr/bin/env python3
"""Vergleicht frisch abgerufene Stände (found.json) mit versions.json.
found.json: [{"product": "...", "version": "..." | null, "date": "YYYY-MM-DD" | null}]
Gibt neue Stände als JSON aus. Mit --apply "Produkt A|Produkt B" werden diese in versions.json übernommen."""
import json, re, sys, datetime
from pathlib import Path

HERE = Path(__file__).parent

def vkey(v):
    return tuple(int(x) for x in re.findall(r"\d+", v or ""))

def is_newer(old, new):
    if new.get("version") and old.get("version"):
        if vkey(new["version"]) != vkey(old["version"]):
            return vkey(new["version"]) > vkey(old["version"])
    if new.get("date") and (not old.get("date") or new["date"] > old["date"]):
        return True
    return bool(new.get("version")) and not old.get("version")

def main():
    db = json.loads((HERE / "versions.json").read_text())
    found = {f["product"]: f for f in json.loads((HERE / "found.json").read_text())}
    items = {i["product"]: i for i in db["items"]}
    if len(sys.argv) > 2 and sys.argv[1] == "--apply":
        for i in sys.argv[2].split("|"):
            f = found[i]
            items[i]["version"] = f.get("version") or items[i]["version"]
            items[i]["date"] = f.get("date") or items[i]["date"]
            if f.get("notes"): items[i]["notes"] = f["notes"]
        db["updated"] = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        (HERE / "versions.json").write_text(json.dumps(db, indent=2, ensure_ascii=False) + "\n")
        print("übernommen:", sys.argv[2]); return
    new = [{"product": k,
            "old": items[k].get("version") or items[k].get("date"),
            "new": f.get("version") or f.get("date"), "url": f.get("notes") or items[k]["notes"]}
           for k, f in found.items() if k in items and is_newer(items[k], f)]
    print(json.dumps(new, indent=2, ensure_ascii=False))

main()
