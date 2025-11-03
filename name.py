if __name__ == '__main__':
    #Tema:3  Catalog de elevi

    # --- Date inițiale ---
    elevi = ["Ana", "Bogdan", "Carmen", "Darius", "Elena"]
    note = [9, 7, 10, 4, 8]
    absente = [1, 0, 2, 3, 0]

    elev_nou = "Felix"
    nota_elev_nou = 6
    elev_de_sters = "Darius"
    interogari_nume = ["Ana", "Mara", "Elena", "stop"]

   # A : Afișare și prelucrare

    print("\n--- A1. Lista elevilor cu notele lor ---")
    for i in range(len(elevi)):
        print(f"{elevi[i]} are nota {note[i]}")

    # -------------------
    # A2 : Nota maximă și minimă
    print("\n--- A2. Nota maximă și minimă ---")
    nota_max = max(note)
    nota_min = min(note)

    # găsim toți elevii cu nota maximă și minimă
    elevi_max = [elevi[i] for i in range(len(note)) if note[i] == nota_max]
    elevi_min = [elevi[i] for i in range(len(note)) if note[i] == nota_min]

    print(f"Nota maximă este {nota_max}, obținută de: {', '.join(elevi_max)}")
    print(f"Nota minimă este {nota_min}, obținută de: {', '.join(elevi_min)}")

    # -------------------
    # A3 : Media clasei
    print("\n--- A3. Media clasei ---")
    media_clasei = sum(note) / len(note)
    print(f"Media clasei este: {media_clasei:.2f}")

    # -------------------
    # A4: Elevii promovați (nota ≥ 5)
    print("\n--- A4. Elevii promovați ---")
    for i in range(len(note)):
        if note[i] >= 5:
            print(f"{elevi[i]} este promovat cu nota {note[i]}")

    #  B : Actualizări

    # B5. +1 punct fiecărei note (maxim 10)
    print("\n--- B5. +1 punct fiecărei note ---")
    for i in range(len(note)):
        note[i] = min(note[i] + 1, 10)  # nu depășește 10
    print("Note actualizate:", note)

    # B6. Adaugă elevul predefinit
    print("\n--- B6. Adaugă elevul nou ---")
    elevi.append(elev_nou)
    note.append(nota_elev_nou)
    print("Elevi după adăugare:", elevi)
    print("Note după adăugare:", note)

    # B7. Șterge elevul predefinit
    print("\n--- B7. Șterge elevul predefinit ---")
    if elev_de_sters in elevi:
        index_sters = elevi.index(elev_de_sters)
        elevi.pop(index_sters)
        note.pop(index_sters)
        print(f"{elev_de_sters} a fost șters din catalog.")
    else:
        print(f"{elev_de_sters} nu există în listă.")
    print("Elevi actualizați:", elevi)
    print("Note actualizate:", note)

    # B8. Afișează lista actualizată
    print("\n--- B8. Lista actualizată elev–notă ---")
    for i in range(len(elevi)):
        print(f"{elevi[i]} are nota {note[i]}")

    #  C – Căutări și statistici

    # C9. Căutări de nume cu while
    print("\n--- C9. Căutări de nume ---")
    i = 0
    while i < len(interogari_nume):
        nume = interogari_nume[i]
        if nume == "stop":
            break
        if nume in elevi:
            index = elevi.index(nume)
            print(f"{nume} are nota {note[index]}")
        else:
            print(f"{nume} nu există în catalog.")
        i += 1

    # C10. Număr promovați / respinși
    print("\n--- C10. Număr promovați și respinși ---")
    promovati = 0
    respinsi = 0
    for n in note:
        if n >= 5:
            promovati += 1
        else:
            respinsi += 1
    print(f"Promovați: {promovati}, Respinși: {respinsi}")

    # C11. Media promovaților
    print("\n--- C11. Media promovaților ---")
    note_promovati = [n for n in note if n >= 5]
    if len(note_promovati) > 0:
        media_promovati = sum(note_promovati) / len(note_promovati)
        print(f"Media promovaților este: {media_promovati:.2f}")
    else:
        print("Nu există elevi promovați.")
