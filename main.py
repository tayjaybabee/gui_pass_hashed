
import tkinter
import PySimpleGUI as gui


from model.security import pwd_context

class LoginWindow:
    
    class Layout:
        def __init__(self):
            """
            
            Instantiate the layout for the LoginWindow
            
            Functions:
                None

            Attributes:
                layout (Union): A list containing three lists of layout elements. When one imagines the GUI as a grid of elements on a canvas each list would represent a row of elements.

            """
            u_name_ln = [
                    gui.Text("Screen name", key="LABEL_SN"),
                    gui.InputText("", key="INPUT_SN")
                    ]
            
            pwd_input = [
                    gui.Text("Password", key='LABEL_PW'),
                    gui.InputText(password_char='*', key='INPUT_PW')
                    ]
            
            buttons = [
                    gui.Button("Sign in", key='BTTN_SIGN_IN', enable_events=True),
                    gui.Button("Cancel", key="BTTN_SIGN_IN_CANCEL", enable_events=True)
                    ]
            
            self.layout = [
                    u_name_ln,
                    pwd_input,
                    buttons
                    ]
            
    def __init__(self):
        """

        Instantiate an instance of the 'LoginWindow'.

        Functions:
            begin(): Start assembled window.

        Attributes:
            win(PySimpleGUI.Window): A PySimpleGUI.Window object ready to be read.

        """
        super().__init__()
    
        self.win = gui.Window('Test Login Window',
                              layout=self.Layout().layout)
        
    def begin(self):
        """
        
        Start the authentication window.

        Returns:
            None

        """
        while True:
            
            event, value = self.win.read(100)
            
            if event is None:
                self.win.close()
                print("Exiting due to 'X' button being pressed")
                exit()
                
            # React to clicking the 'sign in' button.
            if event == 'BTTN_SIGN_IN':
                gui.PopupOK("Sign in button was pressed!")
                u_name = value['INPUT_SN']
                passwd = pwd_context.hash(str(self.win['INPUT_PW']))
                print(f"Data received: {u_name} | {passwd}")
                self.win['INPUT_SN'].update('')
                self.win['INPUT_PW'].update('')
                self.win.refresh()
            
            # React to clicking the 'Cancel' button.
            if event == 'BTTN_SIGN_IN_CANCEL':
                confirm = gui.PopupYesNo("Are you sure you want to leave?")
                print("User pressed cancel button!")
                
                # Confirm with user that they'd like to leave the program.
                if confirm.lower() == 'yes':

                    # Close the window, notify the console, and exit the program.
                    self.win.close()
                    print("Exiting due to 'cancel' button being pressed")
                    exit()

                else:
                    # Notify the console of the failure to confirm program exit.
                    print("User doesn't want to exit.")


login_win = LoginWindow()
login_win.begin()
