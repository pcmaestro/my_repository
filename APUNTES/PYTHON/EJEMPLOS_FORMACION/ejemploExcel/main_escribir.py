import pandas as pd

informacion = {
    "juegos" : ["La oca", "parchis", "ajedrez"],
    "Precios" : [4, 3 , 5],
    }

dataframe = pd.DataFrame(informacion)

writer = pd.ExcelWriter("miexcel.xls", engine = "xlsxwriter")

dataframe.to_excel(writer, sheet_name = "Hoja Juegos", index = False)
writer.save()
print("excel escrito correctamente")