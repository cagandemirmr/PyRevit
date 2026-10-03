

#Manage > Project Parameters ta Type of Parameter:Text, Group parameter under: Identity Data

import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import FilteredElementCollector, BuiltInCategory,Transaction

doc = __revit__.ActiveUIDocument.Document




sheet_collector = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Sheets)\
                                               .WhereElementIsNotElementType()\
                                               .ToElements() #Ekstra bir filtre ekleriz.

t = Transaction(doc,"Update Sheets Parameters")

t.Start()

'''
Yeni bir parametre belirlemek için transaction işlemi yapmamız gerekir.'''

for sheet in sheet_collector:
    custom_param = sheet.LookupParameter("CUSTOM_PARAM")
    if custom_param:
        custom_param.Set("Example value")



t.Commit()
