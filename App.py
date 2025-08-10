from classes.Cliente import Cliente
from frontend.GUI_Login import GUI_Login
from frontend.GUI_ControlEscolar import GUI_ControlEscolar

if __name__ == "__main__":
    TEST_CLIENT = Cliente()
    TEST_CLIENT.set_Username("ZGrupo935@admin.com")

    app = GUI_ControlEscolar(TEST_CLIENT)
    # app = GUI_Login()
    app.mainloop()