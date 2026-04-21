from database.DB_connect import DBConnect
from model.retailer import Retailer


class DAO():

    @staticmethod
    def getAllAnno():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """SELECT DISTINCT YEAR(Date) AS Year
        from go_daily_sales
        order by YEAR DESC """

        cursor.execute(query)

        res = []
        for row in cursor:
            res.append(row["Year"])

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getAllBrand():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query= """select DISTINCT Product_brand
                from go_products
                order by Product_brand"""

        cursor.execute(query)

        res =[]
        for row in cursor:
            res.append(row["Product_brand"])

        cursor.close()
        cnx.close()
        return res

#QUI COMPILIAMO IL MENU A TENDINA CON OGGETTI
    @staticmethod
    def getAllRetail():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """select *
                from go_retailers
                order by Retailer_name"""

        cursor.execute(query)

        res = []
        for row in cursor:
            #Associare il valore del DB al nome del campo nel DataClass
            res.append(Retailer(
                retailer_code=row["Retailer_code"],#nome DataClass = nome DB
                retailer_name= row["Retailer_name"],
                type=row["Type"],
                country = row["Country"]
            ))

        cursor.close()
        cnx.close()
        return res

#TOP VENDITE
    @staticmethod
    def getTopVendite(anno, brand, r_code):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        # COALESCE(%s, colonna) dice: "Se il parametro è NULL, usa il valore della colonna stessa"
        query = """
                    SELECT s.*, (s.Unit_sale_price * s.Quantity) as Ricavo
                    FROM go_daily_sales s
                    JOIN go_products p ON s.Product_number = p.Product_number
                    WHERE YEAR(s.Date) = COALESCE(%s, YEAR(s.Date))
                      AND p.Product_brand = COALESCE(%s, p.Product_brand)
                      AND s.Retailer_code = COALESCE(%s, s.Retailer_code)
                    ORDER BY Ricavo DESC
                    LIMIT 5
                """

        cursor.execute(query, (anno, brand, r_code))

        res=[]
        for row in cursor:
            res.append(row)

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getStatsVendite(anno, brand, r_code):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """
                SELECT 
                    SUM(s.Unit_sale_price * s.Quantity) as GiroAffari,
                    COUNT(*) as NumeroVendite,
                    COUNT(DISTINCT s.Retailer_code) as NumeroRetailers,
                    COUNT(DISTINCT s.Product_number) as NumeroProdotti
                FROM go_daily_sales s
                JOIN go_products p ON s.Product_number = p.Product_number
                WHERE YEAR(s.Date) = COALESCE(%s, YEAR(s.Date))
                  AND p.Product_brand = COALESCE(%s, p.Product_brand)
                  AND s.Retailer_code = COALESCE(%s, s.Retailer_code)
            """

        cursor.execute(query, (anno, brand, r_code))
        res = cursor.fetchone()  # Restituisce una sola riga con i totali

        cursor.close()
        cnx.close()
        return res