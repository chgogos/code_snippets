import sys


def main():
    args = sys.argv[1:]  # παραλείπουμε το πρώτο όρισμα που είναι το όνομα του script
    num_args = len(args)

    print(f"Αριθμός ορισμάτων: {num_args}")
    print("Ορίσματα:", args)

    if num_args == 0:
        print("Σφάλμα: Δεν δόθηκε κανένα όρισμα.")
        sys.exit(-1)  
    else:
        print("Επιτυχής είσοδος ορισμάτων.")

    print(f"Python version: {sys.version}")
    print(f"Platform: {sys.platform}")


if __name__ == "__main__":
    main()
