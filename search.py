import os
from tabulate import tabulate
# import random
import pandas as pd
path = "datasets/Arknights_Operators.csv"
dataset = pd.read_csv(path, sep=";")

# ===============================================
# General initialize
dataset["Limited"] = dataset["Limited"].fillna("Non-Limited")
dataset = dataset.drop(["DP Cost", "Block", "Event", "EN_Release", "Birthday"], axis=1) # gen ra kedawan -khairil

# Gacha initalize
def prob(row):
    probability = row["Rarity"]

    if pd.isna(probability):
        return ""
    
    if probability == 6:
        return 0.02
    elif probability == 5:
        return 0.08
    elif probability == 4:
        return 0.5
    elif probability == 3:
        return 0.4
    else:
        return "Un-Obtainable Via Gacha"
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
    out()
    bersih()

def gacha():
    welcome("Gacha operator")
    print("yet, no idea how to implemented 'pull' in here\n-khairil")
    out()
    bersih()

def tampil():
    print(tabulate(dataset.head(), headers="keys", tablefmt="fancy_grid", showindex=False))
    print("Menampilkan 5 data teratas...")
    print("\n\nDataset last updated 12 November 2025\n")
    welcome("Display Dataset")
    menuTampil()

# ===============================================
def bersih():
    os.system("cls")

def welcome(args):
    print("=" * 40)
    print("=", args.center(36, " "), "=")
    print("=" * 40)

def out():
    input("Tekan Enter untuk lanjut...")
    bersih()

def menu():
    print("Mau ngapain?")
    print("A. Pencarian Operator")
    print("B. Gacha")
    print("C. Tampilkan Dataset")
    print(" ")

def menuTampil():
    print("Mau ngapain?")
    print("1. Semua Operator")
    print("2. Rarity")
    print("3. Stat")
    print("4. Back")

    while True:
        try:
            option = int(input("Masukkan Opsi\n>>"))
        except ValueError:
            bersih()
            print("Input harus berupa angka (1, 2, 3, 4)")
            menuTampil()
        
        if option == 1:
            bersih()
            print(tabulate(dataset, headers="keys", tablefmt="fancy_grid", showindex=False))
            out()
            menuTampil()
        elif option == 2:
            out()
            # nampilke kabeh karakter sek ndue rarity tertentu
            menuTampil()
        elif option == 3:
            out()
            # iki digawe bercabang neh apik ketok e, modelan quantile wingi nganggo stat operator e
            menuTampil()
        elif option == 4:
            bersih()
            break
        else:
            bersih()
            print("Input tidak diketahui")
            continue

# ===============================================
if __name__ == "__main__":
    main()
