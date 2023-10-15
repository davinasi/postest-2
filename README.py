# postest-2
import getpass
# PROGRAM LOGIN SEDERHANA
print ('__________________')
print ('login program kami')
print ('__________________')

username_1=input('buat username baru anda: ') 
password_1=input('buat password baru anda: ') 
print('\n--------DATA DIKONFIRMASI--------')

username_2=input('\nmasukan username anda: ')
password_2= getpass.getpass ('masukan kata sandi: ')

if username_2==username_1 and password_2==password_1:
    print('-----------------------------------------------')
    print('login diterima, selamat datang '+username_1+ '..')
    print('-----------------------------------------------')


from prettytable import PrettyTable

class Product:
    def __init__(self, name, price,stock):
        self.name = name
        self.price = price
        self.stock = stock


class Store:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def view_products(self):
        table = PrettyTable()
        table.field_names = ["Product Name", "Price","stock"]
        for product in self.products:
            table.add_row([product.name, product.price, product.stock])
        print(table)

# Role Pembeli
def buyer_menu(store):
    print("Welcome, Customer!")
    store.view_products()
    print ("Silahkan hubungi sales untuk promo menarik")
    print ("Mr. Pandu : 085752358477")
    print ("atau kunjungi website kami www.hondanusantara.com")




# Role Admin
def admin_menu(store):
    
    print("Welcome, Admin!")
    while True:
        store.view_products()
        print("\nMenu:")
        print("1. Add Product")
        print("2. Delete Product")
        print("3. View Products")
        print("4. replace PRICE AND STOCK")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            stock = int(input("Enter product stock: "))
            product = Product(name, price, stock)
            store.add_product(product)
            print("Product added successfully.")

        elif choice == 2:
            name_to_delete = input("Enter the product name to delete: ")
            product_found = False

            # Find and delete the product by name
            for product in store.products:
                if product.name == name_to_delete:
                    store.products.remove(product)
                    print("Product deleted successfully.")
                    product_found = True
                    break
            


        elif choice == 3:
            store.view_products()

        elif choice == 4:
            name_to_replace = input("Enter the product name to replace: ")
            new_price = float(input("Enter the new product price: "))
            new_stock = int(input("Enter the new product stock: "))
            product_found = False
            for product in store.products:
                if product.name == name_to_replace:
                    product.price = new_price
                    product.stock = new_stock
                    print("Product information replaced successfully.")
                    product_found = True
                    break

            if not product_found:
                print("Product not found.")

        elif choice == 5:
            print("admin logged out.")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    store = Store()

    # Dummy products for demonstration
    store.add_product(Product("NEW HONDA HRV 1.5 S CVT", 375.900 , 23))
    store.add_product(Product("NEW HONDA CRV 2.0 i-VTEC", 525.300, 190))
    store.add_product(Product("NEW HONDA CIVIC 1.5 CVT Turbo RS", 601.400, 67))

    print("Choose your role:")
    print("1. Customer")
    print("2. Admin")
    role = int(input("Enter your role choice: "))

    if role == 1:
        buyer_menu(store)

    elif role == 2:
        admin_menu(store)





