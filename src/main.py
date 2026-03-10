from apps.MoneyManagerEx.money_manager_app import MoneyManagerApp
from Services.new_db import NewDatabase
from desktop_automation.controls.import_csv import importcsv
from desktop_automation.controls.export_csv import exportcsv

def main():
    app_path = r"C:\Program Files\Money Manager EX\bin\mmex.exe"

    input_data_path = r'"D:\7-GitHub\RPA-Financeiro-Python\src\data\input\extrato_money_manager_ex_250_linhas.csv"'

    export_file_path = r'"D:\7-GitHub\RPA-Financeiro-Python\src\data\output\export_csv.csv"'

    money_manager_app = MoneyManagerApp(app_path)

    money_manager_app.start_money_manager()

    money_manager_app.create_database(r'"D:\7-GitHub\RPA-Financeiro-Python\src\data\output\MinhaNovaBase"')

    new_database = NewDatabase(money_manager_app.window)

    new_database.complete_setup("Ze das couves", "USD", "Conta Principal", "01/01/2024")

    import_csv = importcsv(money_manager_app.window)
    import_csv.click_import_csv(input_data_path)

    export_csv = exportcsv(money_manager_app.window)
    export_csv.click_export_csv(export_file_path)

    input("Pressione ENTER para finalizar...")

if __name__ == "__main__":
    main()