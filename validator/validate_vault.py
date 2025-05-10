import json
import hashlib
import argparse
import datetime

def hash_doc(doc):
    content = json.dumps(doc, sort_keys=True).encode("utf-8")
    return hashlib.sha256(content).hexdigest()

def validate_vault(file_path):
    print(f"\nValidating {file_path}...")

    try:
        with open(file_path, "r") as f:
            vault = json.load(f)
    except Exception as e:
        return print(f"ERROR: Could not read file. {e}")

    if "vault_id" not in vault or "document" not in vault:
        return print("ERROR: Missing vault_id or document field.")

    computed_hash = hash_doc(vault["document"])
    if computed_hash != vault.get("integrity_check"):
        return print("ERROR: Integrity check failed. Document hash mismatch.")

    try:
        ts = datetime.datetime.fromisoformat(vault["created_at"])
        print("✓ Timestamp valid:", ts)
    except Exception:
        return print("ERROR: Invalid timestamp format.")

    print("✓ Vault ID:", vault["vault_id"])
    print("✓ Hash validated.")
    print("✓ Signature:", vault.get("signature", "[None Provided]"))
    print("\nVault document is valid.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="Path to .claro.vault file")
    args = parser.parse_args()
    validate_vault(args.file)
