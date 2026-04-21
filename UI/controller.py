import flet as ft

from model.retailer import Retailer


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._ddAnnoValue = None
        self._ddBrandValue = None
        self._ddRetailValue  = None


    def fillddAnno(self):
        self._view.ddAnno.options.append(ft.dropdown.Option(
            key="None", text="Nessun filtro", data=None, on_click=self.choiceDDAnno
        ))
        for a in self._model.getAllAnno():
            self._view.ddAnno.options.append(ft.dropdown.Option(
                key=str(a),
                text=str(a),
                data=a,
                on_click=self.choiceDDAnno
            ))
            pass

    def choiceDDAnno(self, e):
        self._ddAnnoValue = e.control.data
        print(self._ddAnnoValue)


    def fillddBrand(self):
        self._view.ddBrand.options.append(ft.dropdown.Option(
            key="None", text="Nessun filtro", data=None, on_click=self.choiceDDBrand
        ))
        for b in self._model.getAllBrand():
            self._view.ddBrand.options.append(ft.dropdown.Option(
                key = b,
                text=b,
                data= b,
                on_click=self.choiceDDBrand
            ))
            pass

    def choiceDDBrand(self,e):
        self._ddBrandValue = e.control.data
        print(self._ddBrandValue)


#IL MENù A TENDINA è STATO POPOLATO CON OGGETTI
#così si ha immediatamente accesso a tutte le colonne del DB
    def fillddRetail(self):
        self._view.ddRetail.options.append(ft.dropdown.Option(key="None", text="Nessuna opzione"))
        for r in self._model.getAllRetail():
            self._view.ddRetail.options.append(ft.dropdown.Option(
                key=str(r.retailer_code), #stringa univoca
                text=r.retailer_name, #ciò che l'utente legge
                data=r, #passiamo l'intero oggetto che però Flet nasconde
                on_click=self.choiceDDRetail
            ))
            pass

    def choiceDDRetail(self,e):
        self._ddRetailValue = e.control.data
        print(self._ddRetailValue)


    def handleTopVendite(self,e):
        self._view.txt_result.controls.clear()
        anno = self._ddAnnoValue
        brand = self._ddBrandValue

        # Gestione Retailer
        r_code = self._ddRetailValue.retailer_code if self._ddRetailValue else None
        top_cinque = self._model.getTopVendite(anno, brand, r_code)

        if not top_cinque:
            self._view.txt_result.controls.append(ft.Text("Nessuna vendita trovata."))
        else:
            self._view.txt_result.controls.append(ft.Text(f"Top 5 vendite:", weight="bold"))
            for v in top_cinque:
                # v è un dizionario perché nel DAO abbiamo usato dictionary=True
                self._view.txt_result.controls.append(
                    ft.Text(f"Retailer_code: {v['Retailer_code']} | Data: {v['Date']} | Ricavo: {v['Ricavo']:.2f}")
                )

        self._view.update_page()


    def handleAnalizzaVendite(self, e):
        #Pulizia della ListView dei risultati prima di scrivere i nuovi
        self._view.txt_result.controls.clear()

        # 1. Recupero parametri
        #Se l'utente ha scelto "Nessuna opzione", assegniamo None
        anno = self._ddAnnoValue if self._ddAnnoValue != "Nessuna opzione" else None
        brand = self._ddBrandValue if self._ddBrandValue != "Nessuna opzione" else None
        r_code = self._ddRetailValue.retailer_code if self._ddRetailValue else None

        stats = self._model.getStatsVendite(anno, brand, r_code)

        #Output a video
        if stats['GiroAffari'] is None:  # Se non ci sono vendite, SUM restituisce None
            self._view.txt_result.controls.append(ft.Text("Nessuna vendita trovata per i filtri selezionati."))
        else:
            self._view.txt_result.controls.append(ft.Text(f"Statistiche vendite:", weight="bold", size=20))
            self._view.txt_result.controls.append(ft.Text(f"Giro d'affari: {stats['GiroAffari']:.2f} €"))
            self._view.txt_result.controls.append(ft.Text(f"Numero di vendite: {stats['NumeroVendite']}"))
            self._view.txt_result.controls.append(ft.Text(f"Numero di retailers coinvolti: {stats['NumeroRetailers']}"))
            self._view.txt_result.controls.append(ft.Text(f"Numero di prodotti coinvolti: {stats['NumeroProdotti']}"))

        self._view.update_page()