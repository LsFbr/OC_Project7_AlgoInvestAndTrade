def combinaisons(objets, index=0, chemin=None):
    if chemin is None:
        chemin = []

    print(
        f"Appel: index={index}, objet={objets[index] if index < len(objets) else 'None'}, chemin={chemin}"
    )

    if index == len(objets):
        print(f"✅ Combinaison trouvée: {chemin}")
        return

    # Ne pas prendre l'objet courant
    combinaisons(objets, index + 1, chemin)

    # Prendre l'objet courant
    chemin.append(objets[index])
    print(f"Appending index={index}, objet={objets[index]}")
    combinaisons(objets, index + 1, chemin)

    print(f"Popping {objets[index]}")
    chemin.pop()  # On nettoie pour revenir à l'état précédent

    print(
        f"Retour arrière: index={index}, objet={objets[index] if index < len(objets) else 'None'}, chemin={chemin}"
    )


objets = ["a", "b", "c"]
combinaisons(objets)
