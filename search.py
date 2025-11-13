import os
from tabulate import tabulate
import pandas as pd
dataset = pd.read_csv(r"D:\Code\Tugas\arknights_operators_dataset.csv", sep=";")

# ===============================================
dataset["Limited"] = dataset["Limited"].fillna("Non-Limited")
dataset = dataset.drop(["DP Cost", "Block", "Event", "EN_Release"],axis=1)

# ===============================================
def main():
    bersih()
    while True:
        menu()
        option = input("Masukkan Opsi\n>> ").lower()
        match option:
            case "a":
                bersih()
                cari()
            case "b":
                bersih()
                gacha()
            case "c":
                bersih()
                tampil()
            case _:
                bersih()
                print("Masukkan input dengan benar\n\n")
                continue

def cari():
    welcome("Pencarian operator")
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
            print(tabulate(hasil, headers="keys", tablefmt="fancy_grid", showindex=False))
            # print(hasil.to_string(index=False))
        else:
            print(f"\nNo operator found with name containing '{nama}' and rarity '{rarity}'.")
    search(dataset, nama, rarity)
    input()
    bersih()

def gacha():
    welcome("Gacha operator")
    print("I have no idea")
    input()
    bersih()

def tampil():
    print(dataset.head())
    print("\n\nDataset last updated 12 November 2025")
    input()

# ===============================================
def bersih():
    os.system("cls")

def welcome(args):
    print("=" * 40)
    print("=", args.center(36, " "), "=")
    print("=" * 40)

def menu():
    print("Mau ngapain?")
    print("A. Pencarian Operator")
    print("B. Gacha")
    print("C. Tampilkan Dataset")
    print(" ")

# ===============================================
if __name__ == "__main__":
    main()
