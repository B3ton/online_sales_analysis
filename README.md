# Online Sales Analysis

Python projekat koji demonstrira analizu prodajnih podataka i osnovno upravljanje proizvodima i korpom kupca.

## Klase i funkcionalnosti

### `Product`

- Čuva naziv, cijenu i količinu proizvoda.
- Prikazuje informacije o proizvodu.
- Ažurira količinu proizvoda.

### `ProductManager`

- Čuva listu dostupnih proizvoda.
- Dodaje i prikazuje proizvode.
- Izračunava ukupnu vrijednost inventara.
- Uklanja proizvod prema nazivu.

### `Cart`

- Čuva proizvode dodate u korpu.
- Dodaje proizvode u korpu.
- Prikazuje sadržaj korpe.
- Izračunava ukupnu vrijednost korpe.

## Pokretanje

```powershell
python main.py
```

## Sigurnost

Datoteka `config.json` i snimci ekrana su zanemareni kroz `.gitignore`, tako da poverljive konfiguracione podatke i međukorake ne bi trebalo dodavati u Git ili GitHub repozitorijum.
