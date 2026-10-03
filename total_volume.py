"""Calculate total Volumes of the wall."""

__title__ ='Total\nVolume'
__author__ = 'Cosmos'

import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import FilteredElementCollector, BuiltInCategory

doc = __revit__.ActiveUIDocument.Document
#Mevcut Ui documentteki yerlere bak.

#Creating collector instance and collecting all the walls from the model
walls = FilteredElementCollector(doc)
#Once bir obje atarız.Burada hangi dosyada çalışıyoruz onu belirlemek için ihtiyacımız var.
walls.OfCategory(BuiltInCategory.OST_Walls)
#Sonra o methodu seçerim ancak oradaki bir parametreyi seçerim burada bu durum duvarlardır.
walls.WhereElementIsNotElementType()
#Buradan tam aramadığımız tipleri sileriz.

#iterate walls and collect column data
total_value = 0.0
for wall in walls:
    vol_param = wall.LookupParameter("Volume")
    if vol_param:
        total_value = total_value + vol_param.AsDouble()
    #Bu sayede tipi değiştiririz cunku string de gelebilir.

print(total_value)
