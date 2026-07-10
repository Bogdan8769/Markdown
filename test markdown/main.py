import markdown
import glob
import os

def converteste_md_in_html(fisier_intrare, fisier_iesire, titlu_pagina):

    try:
        with open(fisier_intrare, "r", encoding="utf-8") as f:
            text_md = f.read()

        html_body = markdown.markdown(text_md, extensions=["extra"])

        html_complet = f"""<!DOCTYPE html>
        <html lang="ro">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>{titlu_pagina}</title>
            <style>
                body {{
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    background-color: #121212; 
                    color: #e0e0e0;
                    line-height: 1.6;
                    max-width: 800px; 
                    margin: 0 auto;
                    padding: 40px 20px;
                }}

                h1, h2, h3 {{
                    color: #ffffff;
                    border-bottom: 1px solid #333;
                    padding-bottom: 10px;
                }}

                a {{
                    color: #4da6ff;
                    text-decoration: none;
                }}

                a:hover {{
                    text-decoration: underline;
                }}

                code {{
                    background-color: #1e1e1e;
                    padding: 3px 6px;
                    border-radius: 5px;
                    font-family: 'Courier New', Courier, monospace;
                    color: #ff9d00; 
                }}

                blockquote {{
                    border-left: 4px solid #4da6ff;
                    margin: 0;
                    padding-left: 15px;
                    font-style: italic;
                    color: #a0a0a0;
                }}
            </style>
        </head>
        <body>
        {html_body}
        </body>
        </html>
        """

        with open(fisier_iesire, "w", encoding="utf-8") as f:
            f.write(html_complet)

        print(f"Succes: [{fisier_intrare}] a fost convertit în [{fisier_iesire}].")

    except Exception as e:
        print(f"Eroare la conversia fișierului '{fisier_intrare}': {e}")



print("Încep căutarea fișierelor Markdown...\n")

fisiere_md = glob.glob("*.md")

if len(fisiere_md) == 0:
    print("Nu am găsit niciun fișier .md în acest folder.")
else:

    for fisier in fisiere_md:
        nume_baza = os.path.splitext(fisier)[0]

        fisier_iesire = f"{nume_baza}.html"

        titlu_automat = nume_baza.replace("_", " ").replace("-", " ").title()
        converteste_md_in_html(fisier, fisier_iesire, titlu_automat)

print("\nProcesul de automatizare s-a încheiat!")