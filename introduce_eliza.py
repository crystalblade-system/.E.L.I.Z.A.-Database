import sqlite3
import time
# ========== Introduction ==========
print("Initalizing .E.L.I.Z.A. Database...")
time.sleep(1)
print("Hello. I am .E.L.I.Z.A., your system's memory archivist.")
time.sleep(1)
print("Preparing the vault...")
# ========== Database Setup ==========
conn = sqlite3.connect("eliza.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS members (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL
)
""")
time.sleep(1)
print("Vault ready. No memory is ever lost here.")
# ========== Function Definitions ==========
def add_member(name):
    cursor.execute("INSERT INTO members (name) VALUES (?)", (name,))
    conn.commit()
    print(f"🗂️ Archived member: {name}")
def list_members():
    print("\n🧠 System Member Registry:")
    cursor.execute("SELECT * FROM members")
    for m in cursor.fetchall():
        print(f" • {m[1]}")
# ========== Sample Usage ==========
add_member("Ash")
add_member("Raven")
add_member("Seika")
list_members()
# ========== Close ==========
print("\n.E.L.I.Z.A. Database is now active.")
conn.close()
