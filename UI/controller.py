import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_hello(self, e):
        name = self._view.txt_name.value
        if name is None or name == "":
            self._view.create_alert("Inserire il nome")
            return
        self._view.txt_result.controls.append(ft.Text(f"Hello, {name}!"))
        self._view.update_page()

    def fillddAnno(self):
        for a in self._model.getAllAnno():
            self._view.ddAnno.options.append(ft.dropdown.Option(
                key=a,
                data=a,
                on_click=self.choiceDDAnno
            ))
            pass

    def choiceDDAnno(self, e):
        self._ddAnnoValue = e.control.data
        print(self._ddAnnoValue)

    def fillddBrand(self):
        for b in self._model.getAllBrand():
            self._view.ddBrand.options.append(ft.dropdown.Option(
                key = b,
                data= b,
                on_click=self.choiceDDBrand
            ))
            pass

    def choiceDDBrand(self,e):
        self._ddBrandValue = e.control.data
        print(self._ddBrandValue)

    def fillddRetail(self):
        for r in self._model.getAllRetail():
            self._view.ddRetail.options.append(ft.dropdown.Option(
                key=r,
                data=r,
                on_click=self.choiceDDRetail
            ))
            pass

    def choiceDDRetail(self,e):
        self._ddRetailValue = e.control.data
        print(self._ddRetailValue)

    def handleTopVendite(self,e):
        self._view.txt_result.controls.clear()

        self._view.txt_result.controls.append(
            ft.Text(f"Ecco la TOP 5")
        )

    def handleAnalizzaVendite(self,e):
        pass