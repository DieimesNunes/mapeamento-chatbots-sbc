import csv
import bibtexparser

arquivo_bib = "chatbot_anais.bib"
arquivo_csv = "chatbot_anais.csv"

with open(arquivo_bib, "r", encoding="utf-8") as bib_file:
    biblioteca = bibtexparser.load(bib_file)

with open(arquivo_csv, "w", newline="", encoding="utf-8-sig") as csv_file:
    campos = [
        "id",
        "title",
        "author",
        "year",
        "booktitle",
        "doi",
        "url"
    ]

    writer = csv.DictWriter(csv_file, fieldnames=campos)
    writer.writeheader()

    for artigo in biblioteca.entries:
        writer.writerow({
            "id": artigo.get("ID", ""),
            "title": artigo.get("title", ""),
            "author": artigo.get("author", ""),
            "year": artigo.get("year", ""),
            "booktitle": artigo.get("booktitle", ""),
            "doi": artigo.get("doi", ""),
            "url": artigo.get("url", "")
        })

print(f"Concluído! {len(biblioteca.entries)} registros exportados.")
print(f"Arquivo gerado: {arquivo_csv}")