

#Manage > Project Parameters ta Type of Parameter:Text, Group parameter under: Identity Data

import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import FilteredElementCollector, BuiltInCategory,Transaction,TransactionGroup #Toplu transaction yapmak için transactiongroup u seçeriz.

doc = __revit__.ActiveUIDocument.Document




sheet_collector = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Sheets)\
                                               .WhereElementIsNotElementType()\
                                               .ToElements() #Ekstra bir filtre ekleriz.

tg = TransactionGroup(doc,"Update and Delete")
tg.Start()

t = Transaction(doc,"Update Sheets Parameters")

t.Start()


#Yeni bir parametre belirlemek için transaction işlemi yapmamız gerekir.

for sheet in sheet_collector:
    custom_param = sheet.LookupParameter("CUSTOM_PARAM")
    if custom_param:
        custom_param.Set("Example value")



t.Commit()





t = Transaction(doc,"Deleting All Walls") #Bir duvarı sildiğinde otomatikman pencereyi de silmiş olursun.

t.Start()



wall_id_collector = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Walls)\
                                               .WhereElementIsNotElementType()\
                                               .ToElementIds()

for wall_id in wall_id_collector:
    doc.Delete(wall_id)




t.Commit()

tg.Assimilate()
