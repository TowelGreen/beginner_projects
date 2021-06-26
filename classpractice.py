


class Phone_Retail:

  
  phones={'iphone10':900,
        'samsung21':1000,
        'samsungfold2':3000,
        'samsungfe':700}



  def __init__(self,phone,price):
    self.phone=phone
    self.price=price
    if phone=='samsung21':
      print('Samsung21 is 1000$ plus tax')
    else:
      if phone=='iphone10':
        print('iphone10 is 1000$ plus tax')
      if phone=='samsungfold2':
        print('samsungfold2 is 3000$ plus tax')
      if phone=='samsungfold2':
        print('samsungfe is 700$ plus tax')
    

  def tax(self,price):
    self.price = price
    if price >= 1000:
      price=price*1.09
      print("with tax final price")
      print('Your final price is {} do you accept'.format(price))
    else:
      price=price * 1.07
      print("with tax final price")
      print('Your final price is {} do you accept'.format(price)) 
  


      

  def confirm(self):
    print('y/n')
    inputs=input('')
    if inputs=='y':
      print('YOur order is place')
    else:
      if inputs=='n':
        print('Order is cancelled')

      


if __name__ == '__main__':
  print('1=iphone10=900$','2=samsung21=1000$','3=samsungfold2=3000$','4=samsungfe=700$')
  print("tax for phones over 1000 is 9% and for below thousand 7%")
  cust1=Phone_Retail('samsung21',1000)
  cust1.tax(1000)
  cust1.confirm()
  
  


  



