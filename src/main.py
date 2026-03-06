from apps.MoneyManagerEx.money_manager_app import MoneyManagerApp

def main():
    app_path = r"C:\Program Files\Money Manager EX\bin\mmex.exe"

    money_manager_app = MoneyManagerApp(app_path)

    money_manager_app.start_money_manager()

    money_manager_app.map_interface()

    money_manager_app.click_new_file()

    input("Pressione ENTER para finalizar...")

if __name__ == "__main__":
    main()