from database.DB_connect import DBConnect


class DAO():

    @staticmethod
    def getAllAnno():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """SELECT YEAR(Date) AS Year
        from go_daily_sales"""

        cursor.execute(query)

        res = ["Nessuna opzione"]
        for row in cursor:
            if row["Year"] not in res:
                res.append(row["Year"])

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getAllBrand():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query= """select Product_brand
                from go_products"""

        cursor.execute(query)

        res =["Nessuna opzione"]
        for row in cursor:
            if row["Product_brand"] not in res:
                res.append(row["Product_brand"])

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getAllRetail():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """select Retailer_name
                from go_retailers"""

        cursor.execute(query)

        res = ["Nessuna opzione"]
        for row in cursor:
            if row["Retailer_name"] not in res:
                res.append(row["Retailer_name"])

        cursor.close()
        cnx.close()
        return res
    
