import os
from tabulate import tabulate
# import random
import pandas as pd
path = r"D:\Code\Tugas\arknights_operators_dataset.csv"
dataset = pd.read_csv(path, sep=";")

# ===============================================
# General initialize
dataset["Limited"] = dataset["Limited"].fillna("Non-Limited")
dataset = dataset.drop(["DP Cost", "Block", "Event", "EN_Release"], axis=1) # gen ra kedawan -khairil

# Gacha initalize
def prob(row):
    probability = row["Rarity"]

    if pd.isna(probability):
        return "Un-Obtainable Via Gacha"
    
    # aku ra main, tulung benakne probailty ne -khairil
    if probability == 6:
        return 0.000007
    elif probability == 5:
        return 0.000011
    elif probability == 4:
        return 0.0003
    elif probability == 3:
        return 0.001
    elif probability == 2:
        return 0.007
    else:
        return 0.01
dataset["Probability"] = dataset.apply(prob, axis=1) # iki nambah kolom mending di show po ora? -khairil

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
            (df['Rarity'].astype(str) == rarity) # tak gawe as string neng kene gen input e podo sisan -khairil
        ]

        if not hasil.empty:
            print("\nOperator(s) found:")
            print(tabulate(hasil, headers="keys", tablefmt="fancy_grid", showindex=False))
            # print(hasil.to_string(index=False)) <-- iki nggo jogo-jogo nek tabulate e ra work -khairil
        else:
            print(f"\nNo operator found with name containing '{nama}' and rarity '{rarity}'.")
    search(dataset, nama, rarity)
    input()
    bersih()

def gacha():
    welcome("Gacha operator")
    print("yet, no idea how to implemented 'pull' in here\n-khairil")
    input()
    bersih()

def tampil():
    print(tabulate(dataset.head(), headers="keys", tablefmt="simple", showindex=False))
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
