# PyRevit
Pyrevitte yapmış olduğum çalışmaları buradan takip edebilirsiniz.

## RevitApi En iyi Kaynaklar

Revit Developer Guide ile neyi neden seçeceğini veya nerede ne işlem yapılır bunu bilmekiçin iyi bir kaynak oluşturmaktadır.

https://help.autodesk.com/view/RVT/2017/ENU/?guid=GUID-A2686090-69D5-48D3-8DF9-0AC4CC4067A5

İlgili Komutları aramak için ise şu site güzel.

https://www.revitapidocs.com/2017.1/263cf06b-98be-6f91-c4da-fb47d01688f3.htm

# PyRevit te Düzen

<img width="543" height="612" alt="image" src="https://github.com/user-attachments/assets/96b8eace-91da-47b1-9c59-acbc8ed94c5c" />

Kurulumda belki de biraz mücadele ederek şunu öğrendim.Extension dosyası .extension, tab dosyası ise .tab vb. şekilde ayarlanması gerekiyor yoksa plugin açılmıyor.
.extension ın altında lib klasörü bulunur.lib in altında reusable code.py dosyası olur bu py dosyası yinelenen durumlar için kullanılır.Kopylama,filtreleme vb.

.tab ise bizim plug inimimizin UI kısmıdır.İçerisinde tabların farklı alanlarını ifade eden .panel dosyaları vardır.Panellerin altında da .button ile biten dosyalar bulunur.Bu butonların her birinde 96 x 96px boyutlarında png ler bulunur. 

Hook ise bir islem olduğunda verileri karsılaştırmaya yarar.


# Plugin de Dash Panel Düzeni

Panel düzenini yaml dosyası belirler.

<img width="779" height="313" alt="image" src="https://github.com/user-attachments/assets/f5fa5438-63b1-4e07-b633-9fe2f071ba05" />

# UI ve Dialog Geliştirme

Burada amaç form oluşturma ve burada bazı tepkileri oluşturmak.
Bunun için Window Presentation Foundation ve Model-View-Modelview ı ogrenmek gereklidir.
Ama bunlar daha advance konulardır.PRW ise donma sorunlarından dolayı terk edilmiştir.


## Form Oluşturmak

<img width="700" height="116" alt="image" src="https://github.com/user-attachments/assets/5a1866b3-3f1c-4eb0-ac17-769e1e1ae16b" />

``` from pyrevit import forms
ops = ['option1', 'option2', 'option3', 'option4']
forms.CommandSwitchWindow.show(ops, message='Select Option')
# ops2= forms.CommandSwitchWindow.show(ops, message='Select Option') #Eğer bir değişkene atarsak ozaman değeri alabiliriz.
```

## FLEX FORM

<img width="706" height="113" alt="image" src="https://github.com/user-attachments/assets/4ed428fc-f9ff-4a8c-8930-bc07d3cd5dcb" />

Burada Serbest sitil takılırız.

``` from pyrevit import forms
ops = ['option1', 'option2', 'option3', 'option4']
switches = ['switch1', 'switch2']
cfgs = {'option1': { 'background': '0xFF55FF'}} #Burada onlara renk veririz.
rops, rswitches = forms.CommandSwitchWindow.show(
    ops,
     switches=switches,
     message='Select Option',
     config=cfgs)
```

## Loading Bar
Ben bu kodu çalıştırdım ancak bir şey görmedim.
``` from pyrevit import forms
count = 1
with forms.ProgressBar(title='my command progress message') as pb:
    # do stuff
    pb.update_progress(count, 100)
    count += 1
```

## Seçme İşlemi
<img width="610" height="740" alt="image" src="https://github.com/user-attachments/assets/306378b4-2cfb-43e2-aa4d-1b3ad61a7878" />

```from pyrevit import forms
items = ['item1', 'item2', 'item3']
forms.SelectFromList.show(items, button_name='Select Item')
```
Çoklu Seçim İçin

<img width="612" height="742" alt="image" src="https://github.com/user-attachments/assets/04383500-5e3f-4d3e-bc7a-542ce4408ed0" />

```from pyrevit import forms
items = ['item1', 'item2', 'item3']
forms.SelectFromList.show(items, button_name='Select Item',multiselect=True)
```
## Ask_for_string
<img width="483" height="196" alt="image" src="https://github.com/user-attachments/assets/d0e1eb1b-91f8-4b79-bc32-20a0e5ad00b0" />

```
from pyrevit import forms
value = forms.ask_for_string(
             default='some-tag',
             prompt='Enter new tag name:',
             title='Tag Manager')
```
## ask_for_one_string

<img width="487" height="333" alt="image" src="https://github.com/user-attachments/assets/9723f489-d000-4fb3-9bb2-74bfcba19b1e" />

```
forms.ask_for_unique_string(
            prompt='Enter a Unique Name',
             title="Hello",
             reserved_values=['Ehsan', 'Gui', 'Guido'])
```

## ask_for_one_item

<img width="485" height="185" alt="image" src="https://github.com/user-attachments/assets/cc69ba18-a109-4b60-a999-ebf8d5c0b414" />


```
forms.ask_for_one_item(
             ['test item 1', 'test item 2', 'test item 3'],
             default='test item 2',
             prompt='test prompt',
             title='test title'
         )
```

# Kullanıcı Onayı Alma

<img width="439" height="185" alt="image" src="https://github.com/user-attachments/assets/014dd70a-0046-4941-8cb5-eb341e8cedc6" />

Sadece bilgi vermek amaçlıdır.
```
from Autodesk.Revit.UI import TaskDialog, TaskDialogCommonButtons, TaskDialogResult

dialog = TaskDialog("Merhaba Revit")
dialog.MainInstruction = "İşlem Başarılı"
dialog.MainContent = "Veriler güncellendi."
dialog.CommonButtons = TaskDialogCommonButtons.Ok | TaskDialogCommonButtons.Cancel
dialog.DefaultButton = TaskDialogResult.Ok

result = dialog.Show()
if result == TaskDialogResult.Ok:
    print("Tamam tıklandı")
```

<img width="443" height="241" alt="image" src="https://github.com/user-attachments/assets/a3338a5e-aa99-4115-be62-1980635df28f" />

```
from Autodesk.Revit.UI import (TaskDialog, TaskDialogCommandLinkId, TaskDialogResult)

dialog = TaskDialog("Karar")
dialog.MainContent = "Yerleştirme yöntemini seçin:"
dialog.AddCommandLink( #Seçenek belirtmek için addcommandlink kullanırız.
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
    print("Yüzey referansı seçildi")
```
