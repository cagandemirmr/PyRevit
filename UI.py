# -*- coding: utf-8 -*-
__title__ = "UI"
__doc__     = """Version = 1.0"""

# ╦╔╦╗╔═╗╔═╗╦═╗╔╦╗╔═╗
# ║║║║╠═╝║ ║╠╦╝ ║ ╚═╗
# ╩╩ ╩╩  ╚═╝╩╚═ ╩ ╚═╝
#░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
from Autodesk.Revit.DB import *

#pyRevit
from pyrevit import forms, script

#.NET Imports
import clr
clr.AddReference('System')
from System.Collections.Generic import List

#BU ALAN VISUALIZATION ICIN GEREKLIDIR
from rpw.ui.forms import Console
from rpw.ui.forms import SelectFromList
from rpw.ui.forms import TextInput


# ╦  ╦╔═╗╦═╗╦╔═╗╔╗ ╦  ╔═╗╔═╗
# ╚╗╔╝╠═╣╠╦╝║╠═╣╠╩╗║  ║╣ ╚═╗
#  ╚╝ ╩ ╩╩╚═╩╩ ╩╚═╝╩═╝╚═╝╚═╝
#░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
doc    = __revit__.ActiveUIDocument.Document #type:Document
uidoc  = __revit__.ActiveUIDocument          # __revit__ is internal variable in pyRevit
app    = __revit__.Application
output = script.get_output()                 # pyRevit Output Menu

# ╔╦╗╔═╗╦╔╗╔
# ║║║╠═╣║║║║
# ╩ ╩╩ ╩╩╝╚╝
#░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
#🤖 Automate Your Boring Work Here



#############################################
############## FORM OLUŞTURMA ###############
#############################################


# Asıl Doğrusu C sharp ile yapılandır. rpw suçtur.

'''from pyrevit import forms
ops = ['option1', 'option2', 'option3', 'option4']

ops2= forms.CommandSwitchWindow.show(ops, message='Select Option') #Eğer bir değişkene atarsak ozaman değeri alabiliriz.'''



###############################################
############ FREE FORM ########################
###############################################

from pyrevit import forms


'''ops = ['option1', 'option2', 'option3', 'option4']
switches = ['switch1', 'switch2']
cfgs = {'option1': { 'background': '0xFF55FF'}} #Burada onlara renk veririz.
rops, rswitches = forms.CommandSwitchWindow.show(
    ops,
     switches=switches,
     message='Select Option',
     config=cfgs)

print(rops,rswitches)'''

'''from pyrevit import forms
count = 1
with forms.ProgressBar(title='my command progress message') as pb:
    # do stuff
    pb.update_progress(count, 100)
    count += 1'''

'''matched_str, switches = forms.SearchPrompt.show(
    search_db=['target1', 'target2', 'target3', 'target4'],
     switches=['/switch1', '/switch2'],
     search_tip='pyRevit Search'
     )
'''


######### Kutucuk Seçme

'''from pyrevit import forms
items = ['item1', 'item2', 'item3']
forms.SelectFromList.show(items, button_name='Select Item')'''


'''from pyrevit import forms
items = ['item1', 'item2', 'item3']
forms.SelectFromList.show(items, button_name='Select Item',multiselect=True)'''


# Tag Manager
'''from pyrevit import forms
value = forms.ask_for_string(
             default='some-tag',
             prompt='Enter new tag name:',
             title='Tag Manager')'''


#Sadece tek bir şeyi seçeriz.
'''forms.ask_for_one_item(
             ['test item 1', 'test item 2', 'test item 3'],
             default='test item 2',
             prompt='test prompt',
             title='test title'
         )'''

'''from Autodesk.Revit.UI import TaskDialog, TaskDialogCommonButtons, TaskDialogResult

dialog = TaskDialog("Merhaba Revit")
dialog.MainInstruction = "İşlem Başarılı"
dialog.MainContent = "Veriler güncellendi."
dialog.CommonButtons = TaskDialogCommonButtons.Ok | TaskDialogCommonButtons.Cancel
dialog.DefaultButton = TaskDialogResult.Ok

result = dialog.Show()
if result == TaskDialogResult.Ok:
    print("Tamam tıklandı")'''


'''from Autodesk.Revit.UI import (TaskDialog, TaskDialogCommandLinkId, TaskDialogResult)

dialog = TaskDialog("Karar")
dialog.MainContent = "Yerleştirme yöntemini seçin:"
dialog.AddCommandLink(
    TaskDialogCommandLinkId.CommandLink1,
    "Basit Yerleştirme Noktası",
    "Serbest parçalar için")
dialog.AddCommandLink(
    TaskDialogCommandLinkId.CommandLink2,
    "Yüzey Referansı",
    "Duvar/yüzeye yerleştirir")

result = dialog.Show()
if result == TaskDialogResult.CommandLink1:
    print("Basit yöntem seçildi")
elif result == TaskDialogResult.CommandLink2:
    print("Yüzey referansı seçildi")'''

############################################
################# UI lar ###################
############################################


# -*- coding: utf-8 -*-
from pyrevit import forms
from Autodesk.Revit.DB import *

# Örnek bir liste (Gerçek görünümleri buraya siz aktaracaksınız)
ornek_gorunumler = {}

#İlk başta şu şekilde olsa daha iyi olur.sistem açıldığında ben active viewları kaydetmeye başlayayım bir listeye.
#Tuşa bastığımda sonra Bu listeye geleyim ve onu ekrana yazdırayım.
#Tıkladığımda/seçtiğimde da o view a gideyim.

views = uidoc.GetOpenUIViews() #Pickle ile bu goruntulerı alırız.

for view in views:
    view_element = doc.GetElement(view.ViewId)
    view_id = view.ViewId

    if view_element:
        v_id = view_id.IntegerValue
        v_name = view_element.Name
        ornek_gorunumler[v_name] = doc.GetElement(view_id) #GetElement ile view ları alırız.



# Arayüzü Gösterme Şablonu
secilenler = forms.SelectFromList.show(
    list(ornek_gorunumler.keys()), #Bu parametre list olarak kabul aldığı için keys leri list e çevirdim
    title="Görünüm Listesi",
    button_name="Seçilenleri Sırala",
    multiselect=False
)

if secilenler:
    uidoc.ActiveView = ornek_gorunumler[secilenler] #ActiveView u direkt mevcut view atarak bunu cozeriz.



# TETİKLEME (EVENT HANDLING) KISMI:
# Kullanıcı butona bastıktan sonra ne olacağını SİZ yazmalısınız.
if secilenler:
    # TODO: Seçilen görünümleri döngüye al
    # TODO: UIDocument üzerinden o görünümleri aktif hale getir (ActiveView)
    pass










################################
##### PROJE SEÇİLİ UI LAR COZUMU
################################


# -*- coding: utf-8 -*-
'''__title__ = "Açık Görünümleri\nListele"
__doc__ = "Açık olan tüm pencereleri listeler ve seçilenleri sırayla ekrana getirir."

from Autodesk.Revit.DB import *
from pyrevit import revit, forms

# Aktif dökümanları ve UI dökümanını alıyoruz
uidoc = revit.uidoc
doc = revit.doc

# 1. Kullanıcıya açık olan tüm UI View pencerelerini alıyoruz
open_ui_views = uidoc.GetOpenUIViews()

# 2. Bu pencerelerin ID'lerine karşılık gelen View elemanlarını buluyoruz
# Kolay seçim ve yönetim için bir View nesnesi listesi oluşturuyoruz
open_views = []
view_map = {}  # Görünüm adını UI View nesnesine eşlemek için sözlük

for ui_view in open_ui_views:
    view_id = ui_view.ViewId
    view_element = doc.GetElement(view_id)

    if view_element:
        # Görünüm tipini ve adını birleştirerek güzel bir etiket oluşturuyoruz
        view_label = "[{}] {}".format(view_element.ViewType, view_element.Name)
        open_views.append(view_label)
        # İsmi eşleştirmek için kaydediyoruz
        view_map[view_label] = ui_view

# 3. pyRevit Listbox Arayüzü ile kullanıcının karşısına çıkarıyoruz
if open_views:
    selected_views = forms.SelectFromList.show(
        open_views,
        title="Açık Görünümleri Seçin",
        button_name="Görünümleri Sırala/Aktifleştir",
        multiselect=True  # Birden fazla görünüm seçimine izin ver
    )

    # 4. Kullanıcı seçim yaptıysa, seçilen görünümleri sırayla aktifleştiriyoruz
    if selected_views:
        for view_name in selected_views:
            target_ui_view = view_map[view_name]

            # Görünümü ön plana getirip aktif pencere yapıyoruz
            target_ui_view.ZoomToFit()  # Ekranı ortalar
            uidoc.ActiveView = doc.GetElement(target_ui_view.ViewId)

        # İsteğe bağlı: Seçilen pencereleri ekranda yan yana döşemek (Tile) isterseniz:
        # uidoc.TileWindows()

        forms.alert("Seçilen {} adet görünüm sırayla ön plana getirildi.".format(len(selected_views)), title="Başarılı")
else:
    forms.alert("Açık olan herhangi bir görünüm penceresi bulunamadı.", title="Hata")'''

#🚧 Remove This Code Example
from reusable_code._example import default_print    # import reusable code from .../lib/reusable_code/_example.py
#default_print(btn_name=__title__)                   # Display default print message





#███████████████████████████████████████████████████████████████████████████
# Happy Coding!
