
from tabulate import tabulate

class Transaction():
    # This code is used to define new transaction
    def __init__(self):
      self.item = dict()
    # This method is to input new item data
    def add_item(self,item_name,item_price,total_item):
      # This code is to validate the data type is correct
      try:
        item_price = int(item_price)
        total_item = int(total_item)
      except:
        print("Price and total item must be numerical")
      finally:
        self.item.update({item_name:[item_price,total_item]})
        print(f"Item that will be bought is {item_name} with price {item_price} and total item : {total_item} ")

    # This method is to update data in the transaction
    def update_item_name(self, existing_item_name, update_item_name):
      # find if the dictionary has certain key
      if self.item.get(existing_item_name) is not None:
        self.item[update_item_name] = self.item.pop(existing_item_name)
        print(f"Item is successfully updated to {update_item_name}")
      else:
        print("item not found")

    def update_item_price(self, existing_item_name, update_item_price):
      # This code is to validate the data type of item price is correct
      try:
        update_item_price = int(update_item_price)
      except:
        print("Please input price data correctly!")
      finally:
        if self.item.get(existing_item_name) is not None:
          self.item[existing_item_name][0] = update_item_price
          print(f"{existing_item_name} price is successfully updated to {update_item_price}")
        else:
          print("item not found")

    def update_total_item(self, existing_item_name, update_total_item):
      # This code is to validate the data type of total item is correct
      try:
        update_total_item= int(update_total_item)
      except:
        print("Please input total item data correctly!")
      finally:
        if self.item.get(existing_item_name) is not None:
          self.item[existing_item_name][1] = update_total_item
          print(f"Total {existing_item_name} is successfully updated to {update_total_item}")
        else:
          print("item not found")

    # This method is used to delete specific item
    def delete_item(self, existing_item_name):
      if self.item.get(existing_item_name) is not None:
        del self.item[existing_item_name]
        print(f"Item successfully deleted")
      else:
        print("item not found")

    # This method is to reset transaction
    def reset_transaction(self):
      self.item.clear()
      print(f"All transaction data successfully reset")
    
    # This method is to check all transaction details
    def show_order(self):
      show_order = []
      header = ["No.","Nama Item", "Jumlah Item", "Harga/Item", "Total Harga"]
      show_order.append(header)

      n = 0
      
      for key, value in self.item.items():
          n += 1
          table_no = n
          item_name = key
          item_price = value[0]
          total_item = value[1]
          total = total_item * item_price
          item_data = [table_no, item_name, total_item, item_price, total]
          show_order.append(item_data)
      
      print(tabulate(show_order, tablefmt="fancy_grid"))

    # This method is used to calculate all transaction
    def total_transaction(self):
      total = 0
      for key in self.item.values():
        total += (int(key[0]) * int(key[1]))
      if total > 200_000:
        total = total - (total * 0.05)
        print(f"Anda mendapatkan diskon sebesar 5%, sehingga total transaksi anda adalah {total}")
      elif total > 300_000:
        total = total - (total * 0.08)
        print(f"Anda mendapatkan diskon sebesar 8%, sehingga total transaksi anda adalah {total}")
      elif total > 500_000:
        total = total - (total * 0.1)
        print(f"Anda mendapatkan diskon sebesar 10%, sehingga total transaksi anda adalah {total}")
      else:
        print(f"Total belanja anda adalah {total}")
    
       











