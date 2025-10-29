print(" ")
import pandas as pd
dataset = pd.read_csv(r"D:\Code\Tugas\arknights_operators_dataset.csv")
# ===============================================
print("Arknights type shit".center(40, "="))

nama = str(input("Masukkan nama operator : ").strip())
rarity = str(input("Masukkan rarity operator : ").strip())


def search(df, nama, rarity):
    nama = nama.lower()

    hasil = df[
        (df['Name'].str.lower().str.contains(nama, na=False)) &
        (df['Rarity'].astype(str) == rarity)
    ]

    if not hasil.empty:
        print("\nOperator(s) found:")
        print(hasil.to_string(index=False))  # Display results without index
    else:
        print(f"\nNo operator found with name containing '{nama}' and rarity '{rarity}'.")

search(dataset, nama, rarity)

