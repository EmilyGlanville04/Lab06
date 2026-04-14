from database.DAO import DAO


class Model:
    def __init__(self):
        pass

    def getAllAnno(self):
        return DAO.getAllAnno()
    def getAllBrand(self):
        return DAO.getAllBrand()

    def getAllRetail(self):
        return DAO.getAllRetail()