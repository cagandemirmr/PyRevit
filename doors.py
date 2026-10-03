# Kapı Listelerini gösteren Liste

import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import FilteredElementCollector, BuiltInCategory


# İlk basta bir formolucak bu formda biz doortype, kaç derece döneceğini ve aks ı belirteceğiz.
doc = __revit__.ActiveUIDocument.Document
#Mevcut Ui documentteki yerlere bak.

#Creating collector instance and collecting all the walls from the model
doors = FilteredElementCollector(doc) #İlk başta biz mevcut dosyayı seçtiğimizi belirtiriz.Bizim ilk yaptığımız işlem filtreleme

doors.OfCategory(BuiltInCategory.OST_Doors).WhereElementIsElementType().ToElements() #Burada classın içerisine girip önce category olarak neyi seçeceğimizi sonra sadece element tyları seçeceğii ve elemanları seçeceğimi belirtirim.



door_list = []
for dt in doors:
    # Revit bazen sistem ailelerinde veya boş tiplerde hata verebilir, kontrol ekliyoruz
    if dt.FamilyName:
        door_list.append(dt.FamilyName)

# Alfabetik olarak sırala
door_list.sort()

'''
# Kapı tiplerinin Family Name ve Type Name bilgilerini birleştirerek listele
door_list = []
for dt in door_types:
    # Revit bazen sistem ailelerinde veya boş tiplerde hata verebilir, kontrol ekliyoruz
    if dt.FamilyName: 
        door_list.append(dt.FamilyName)

# Alfabetik olarak sırala
door_list.sort()

# Sonuçları satır satır birleştir
result = '\n'.join(door_list)

# Ekranda göster
MessageBox.Show(result if result else "Modelde hiç kapı tipi bulunamadı.", "Kapı Tipleri Listesi") '''
