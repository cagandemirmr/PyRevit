# PyRevit
Pyrevitte yapmış olduğum çalışmaları buradan takip edebilirsiniz.

# PyRevit te Düzen

<img width="543" height="612" alt="image" src="https://github.com/user-attachments/assets/96b8eace-91da-47b1-9c59-acbc8ed94c5c" />

Kurulumda belki de biraz mücadele ederek şunu öğrendim.Extension dosyası .extension, tab dosyası ise .tab vb. şekilde ayarlanması gerekiyor yoksa plugin açılmıyor.
.extension ın altında lib klasörü bulunur.lib in altında reusable code.py dosyası olur bu py dosyası yinelenen durumlar için kullanılır.Kopylama,filtreleme vb.

.tab ise bizim plug inimimizin UI kısmıdır.İçerisinde tabların farklı alanlarını ifade eden .panel dosyaları vardır.Panellerin altında da .button ile biten dosyalar bulunur.Bu butonların her birinde 96 x 96px boyutlarında png ler bulunur. 


# Plugin de Dash Panel Düzeni

Panel düzenini yaml dosyası belirler.

<img width="779" height="313" alt="image" src="https://github.com/user-attachments/assets/f5fa5438-63b1-4e07-b633-9fe2f071ba05" />
