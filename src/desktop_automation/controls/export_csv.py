class exportcsv:
    def __init__(self, window):
        self.window = window

    def click_export_csv(self, file_name, account_name="Conta Principal", preset="preset"):
        self.window.child_window(title_re="File").click_input()
        self.window.child_window(title_re="Export as").click_input()
        self.window.child_window(auto_id="6062").click_input()

        self.window.child_window(auto_id="10100").click_input()
        self.window.child_window(auto_id="1001", control_type="Edit").type_keys(file_name)
        self.window.child_window(auto_id="1", control_type="Button").click_input()


        self.window.child_window(auto_id="10103", control_type="ComboBox").select(account_name)
        self.window.child_window(auto_id="5102", control_type="ComboBox").select(preset)

        self.window.child_window(auto_id="10095", control_type="Button").click_input()

        self.window.child_window(auto_id="CommandButton_2", control_type="Button").click_input()

        self.window.child_window(auto_id="5101", control_type="Button").click_input()