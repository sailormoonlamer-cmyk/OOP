import random
import datetime

#Шаблон банковского счета 
class BankAccount:
  
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance
        self.account_number = self.get_account_number()
        self.created_at = datetime.datetime.now()
        self.transaction_history = []
    
    def get_account_number(self):
        return f'{random.randint(1000,9999)}-{random.randint(1000,9999)}'

    def deposit(self, amount):
        if amount <= 0:
            print("ОШИБКА!!! Сумма должна быть больше нуля!! ")
            return False
        
        self.balance += amount
        transaction = f'Пополнение: +{amount}руб. | Баланс:{self.balance}руб.'
        self.transaction_history.append(transaction)
        print(f'Счет пополнен на {amount}руб. | текущий баланс {self.balance}руб.')
        return True
 
    def withdraw(self, amount):
        if amount <= 0:
            print("ОШИБКА!!! Сумма должна быть больше нуля!! ")
            return False
        
        if amount > self.balance:
            print(f'НЕ ДОСТАТОЧНО СТРЕДСТВ| на балансе: {self.balance}')
            return False
        
        self.balance -= amount
        transaction = f'Cнятие: -{amount}руб. | Баланс:{self.balance}руб.'
        self.transaction_history.append(transaction)
        print(f'Снято {amount}руб. | текущий баланс {self.balance}руб.')
        return True

    def transfer(self, amount, target_account):
        if amount <= 0:
            print("ОШИБКА!!! Сумма должна быть больше нуля!! ")
            return False
            
        if amount > self.balance:
            print(f'НЕ ДОСТАТОЧНО СТРЕДСТВ| на балансе: {self.balance}')
            return False
        
        self.balance -= amount
        transaction = f'Перевод: -{amount}руб. на счет {target_account.account_number}| Баланс:{self.balance}руб.'
        self.transaction_history.append(transaction)
        
        target_account.balance += amount
        transaction = f'Перевод: +{amount}руб. c счета {self.balance}| Баланс:{target_account.balance}руб.'
        self.transaction_history.append(transaction)
        
        print(f'Переведено {amount}руб. на счет {target_account.account_number}| ваш баланс {self.balance}руб.')
        return True
 
    def get_balance(self):
        return self.balance
   
    def show_transaction(self):
        if not self.transaction_history:
            print("История операций пуста!! ")
            return
        print(F'История операций для счета {self.account_number}')
        for i, transaction in enumerate(self.transaction_history):
            print(f'{i+1}, {transaction}')
        print("-" * 50)    

    def __str__(self):
        return f'Счет: {self.account_number}|Владелец:{self.owner}|Баланс:{self.balance} рублей' 
       
class Bank:         
    def __init__(self, name):
        self.name = name
        self.accounts = []
  
    def create_account(self, owner, initial_balance = 0):
        for account in self.accounts:
            if account.owner.lower() == owner.lower():
                print(f"У пользователя {owner} уже есть счет {account.account_number}")
                return None
            
        new_account = BankAccount(owner, initial_balance)  # СОЗДАЕМ ОБЪЕКТ ОТ КЛАССА  BankAccount
        
        self.accounts.append(new_account)
        
        print("Счет успешно создан")
        print(f'Владелец: {owner}|номер счета:{new_account.account_number}|начальный баланс:{initial_balance}руб')
        return new_account
    
    def find_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        return None
    
    def find_accounts_by_owner(self, owner):
        found = []
        for account in self.accounts:
            if account.owner.lower() == owner.lower():
                found.append(account)
        return found
                
    def get_total_balance(self):
        total = 0
        for account in self.accounts:
            total += account.balance
        return total
    
    def show_all_accounts(self):
        if not self.accounts:
            print("В банке нет счетов")
            return
        print(f"Все в банке '{self.name}' ")
        for i , account in enumerate(self.accounts):
            print(f'{i+1}. {account}')
            
        print(f'Общая сумма средств в банке: {self.get_total_balance()} рублей ')
        
    def delete_account(self, account_number):
        account = self.find_account(account_number)
        
        if not account:
            print(f'Счет {account_number} не найден! ')
            return False
        
        if account.balance != 0:
            print(f"Нельзя закрыть счет с остатком {account.balance} рублей ")
            print("Сначала снимите все деньги")
            return False
        
        self.accounts.remove(account)
        print(f'Счет {account_number} закрыт! ')
        return True
  
def print_menu():    
    print("МОЙ БАНК")
    print("="*50)
    print('1. Создать свой счет')
    print('2. Посмотреть все счета')
    print('3. Пополнить счет')
    print('4. Снять деньги со счета')
    print('5. Перевести деньги между счетами ')
    print('6. Проверить баланс счета ')
    print('7. История операций')
    print('8. Найти счет по номеру')
    print('9. Найти счет по владельцу')
    print('10. Закрыть счет')
    print('11. Общая статистика банка')
    print('0. выход')
    print("="*50)
    
def main():
    bank = Bank("Мой банк")
    bank.create_account("Иван Петров", 50000)
    bank.create_account("Мария Иванова", 80000)
    bank.create_account("Алексей Петров", 20000)
    
    print("Добро пожаловать в банк! ")
    while True:
        print_menu()
        choice = input("Выберите действие: ").strip()
        
        if choice == '1':
            print("Создание нового счета: ")
            owner = input("Введите свое имя: ").strip()
            if not owner:
                print("Имя не может быть пустым!! ")
                
                continue
            balance = input("Введите начальный баланс: ").strip()
            if balance:
                balance = float(balance)
                if balance < 0:
                    print("Баланс не может быть отрицательным!!! ")
                    continue
            else:
                balance = 0
            bank.create_account(owner, balance)  
            print(" ")     
         
        elif choice == '2':
            bank.show_all_accounts()
    
        elif choice == "3":
            account_number = input("Введите номер счета: ").strip()
            account = bank.find_account(account_number)
            if not account:
                print(f"Счет {account_number} не найден! ")
                continue
            amount = float(input("Введите сумму пополнения ").strip())
            account.deposit(amount)
            print(" ")
             
        elif choice == '4':
            account_number = input("Введите номер счета: ").strip()
            account = bank.find_account(account_number)
            if not account:
                print(f"Счет {account_number} не найден! ")
                continue
            amount = float(input("Введите сумму снятия ").strip())
            account.withdraw(amount)
            print(" ")
            
        elif choice == '5':
            user1 = input("Введите номер счета отправителя: ").strip()
            from_user1 = bank.find_account(user1)
            if not from_user1:
                print(f"Счет {user1} не найден! ")
                continue
            user2 = input("Введите номер счета получателя: ")
            to_user2 = bank.find_account(user2)
            if not to_user2:
                print(f"Счет {user2} не найден! ")
                continue
            amount = float(input("Введите сумму перевода: ").strip())
            from_user1.transfer(amount, to_user2)
            print(" ")
        
        elif choice == '6':                                                                                 
            account_number = input("Введите номер счета: ").strip()
            account = bank.find_account(account_number)                                                             
            if not account:
                print("Счет не найден! ")
                continue
            print(f'Баланс счета:{account} руб')
            
        elif choice == '7':
            account_number = input("Введите номер счета: ").strip()
            account = bank.find_account(account_number)
            if not account:
                print(f'Счет {account_number} не найден!')
                continue
            
        elif choice == '8':
            account_number = input("Введите номер счета: ").strip()
            account = bank.find_account(account_number)
            if account:
                print(account)
            else:
                print(f'Счет {account_number} не найден!')
                
        elif choice == '9':
            owner = input("Введите имя владельца: ").strip()
            account = bank.find_account(account_number)
            if account:
                print(account)
            else:
                print("Счета владельца не найдены!")
        
        elif choice == '10':
            account_number = input("Введите номер счета: ").strip()
            if bank.delete_account(account_number):
                print("Счет успешно закрыт!")
            else:
                print("Счеь не удалось закрыть!")
            
        elif choice == '11':
            print(f'Навазние банка:{bank.name}')
            print(f'Количетсво счетов:{len(bank.accounts)}')
            print(f'Общий баланс::{bank.get_total_balance()}')
            
        elif choice == '0':
            print("Спасибо за использование банком!")
            break
                     
            
if __name__ == "__main__":
    main()        