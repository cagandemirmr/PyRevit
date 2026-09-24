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

## Form Oluşturmak

<img width="401" height="131" alt="image" src="https://github.com/user-attachments/assets/3b275fc5-f607-4ab2-a5fd-39166680a3eb" />


Amaç burada form açmak ve bu formda işlemler yapabilmek.Hatta bu verileri başka yerlere aktarabilmek.
Bunun için ilk olarak form açılabilmesini sağlayabilmek için buton içerisindeki script dosyasını işleyerek yaparız.

```from rpw.ui.forms import Console
    from rpw.ui.forms import SelectFromList

value = SelectFromList('Form Başlığı', ['1','2','3'])
#İlk alanda form başlığı sonraki alanda da seçenekleri belirleriz.
print(value)

# Dictionary
value = SelectFromList('Test Window', {'Text':str, 'Number':int}) #dictionary olarak da değer dondurebiliriz.
# User clicks Text
print(value)
```

### TEXT INPUT

<img width="403" height="130" alt="image" src="https://github.com/user-attachments/assets/c0fd1527-96a0-4c36-bb30-4e201d891281" />


```from rpw.ui.forms import TextInput
  value = TextInput('Title', default="3") #Burada custom olarak text yazabiliriz.
print(value)
```
## TASK DIALOG
<img width="469" height="343" alt="image" src="https://github.com/user-attachments/assets/97de9401-94d7-4019-be69-66e4d2f24210" />

```
from rpw.ui.forms import CommandLink, TaskDialog

commands= [CommandLink('Open Dialog', return_value='Open'),
            CommandLink('Command', return_value=lambda: True)]


dialog = TaskDialog('This TaskDialog has Buttons ',   #Başlık
 title_prefix=False,
            content="Further Instructions",          #Yazı
            commands=commands,                       
             buttons=['Cancel', 'OK', 'RETRY'],
            footer='It has a footer',
            # verification_text='Add Verification Checkbox',
            # expanded_content='Add Expanded Content',
            show_close=True)
dialog.show()
```
