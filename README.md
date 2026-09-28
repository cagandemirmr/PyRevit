# PyRevit
Pyrevitte yapmış olduğum çalışmaları buradan takip edebilirsiniz.

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


