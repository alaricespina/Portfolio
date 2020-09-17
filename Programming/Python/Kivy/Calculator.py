from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.core.window import Window

class YourApp(App):
    def build(self):
        Window.size = (500,300)
        Window.borderless = True

        root_widget = BoxLayout(orientation='vertical')

        output_label = Label(size_hint_y=1)

        button_symbols = ('1', '2', '3', '+',
                          '4', '5', '6', '-',
                          '7', '8', '9', '.',
                          '0', '*', '/', '%',
                          '//','(',")","=")

        button_grid = GridLayout(cols=4, size_hint_y=1)
        for symbol in button_symbols:
            button_grid.add_widget(Button(text=symbol))

        clear_button = Button(text='clear', size_hint_y=1,
                              height=100)

        #----------------------Functions-------------------------

        #Printing the text from selected buttons
        def print_button_text(instance):
            output_label.text += instance.text
        
        #Function to resize the text according to label height 
        def resize_label_text(label, new_height):
            label.font_size = 0.5*label.height
       
        #evaluates then turns int result to string
        def evaluate_result(instance):
            try:
                output_label.text = str(eval(output_label.text))
            except SyntaxError:
                output_label.text = 'Python syntax error!'
       
        #removes all output
        def clear_label(instance):
            output_label.text = ''

        #binds function to all buttons except = since it is [0] on the list of button symbols
        for button in button_grid.children[1:]:                                    
            button.bind(on_press=print_button_text)

        #= sign function
        button_grid.children[0].bind(on_press=evaluate_result)

        #Big clear button function
        clear_button.bind(on_press=clear_label)

        #Automatically gets called everytime there is text
        output_label.bind(height=resize_label_text)

        root_widget.add_widget(output_label)
        root_widget.add_widget(button_grid)
        root_widget.add_widget(clear_button)

        return root_widget


YourApp().run()