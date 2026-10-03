from Autodesk.Revit.DB import Transaction

doc = __revit__.ActiveUIDocument.Document



t = Transaction(doc,"Deleting All Walls")

t.Start()

#Bizim tüm Create,Update ve Delete işlemini burada yaparız.

t.commit()

'''res = t.GetStatus() #Status un durumunu izlemek için bunu yaparız.

res = t.TransactionStatus.Committed # Bu transaction durumunu izlemek için kullanırız.'''

#t.RollBack() #Tüm yapılan işlemleri geriye alırım.Eğer transaction dan memnun kalmazsam.


