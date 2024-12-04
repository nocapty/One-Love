from tkinter import *

class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        Label(self,
              text = "Fill in the blanks for a loving message."
              ).grid(row = 0, column = 0, columnspan = 2, sticky = W)
        
        Label(self,
              text = "Name:"
              ).grid( row = 1, column = 0, columnspan = 2, sticky = W)
        self.name_ent = Entry(self)
        self.name_ent.grid(row = 1, column = 1, sticky = W)
        
        Label(self,
              text = "Verb:"
              ).grid(row = 2, column = 0, sticky = W)
        self.verb_ent = Entry(self)
        self.verb_ent.grid(row = 2, column = 1, sticky = W)

        Label(self,
              text = "Plural Noun:"
             ).grid(row = 3, column = 0, sticky = W)
        self.noun_ent = Entry(self)
        self.noun_ent.grid(row = 3, column = 1, sticky = W)

        Label(self,
              text = "Adjective(s):"
              ).grid(row = 4, column = 0, sticky = W)
        
        self.is_wonderful = BooleanVar()
        Checkbutton(self,
                    text = "Wonderful",
                    variable = self.is_wonderful
                    ).grid(row = 4, column = 1, sticky = W)
        
        self.is_beautiful = BooleanVar()
        Checkbutton(self,
                    text = "Beautiful",
                    variable = self.is_beautiful
                    ).grid(row = 4, column = 2, sticky = W)
        
        self.is_happy = BooleanVar()
        Checkbutton(self,
                    text = "Happy",
                    variable = self.is_happy
                    ).grid(row = 4, column = 3, sticky = W)
        
        Label(self,
              text = "Verb(ing):"
              ).grid(row = 5, column = 0, sticky = W)
        
        self.verb_end = StringVar()
        self.verb_end.set(None)

        verb_endings = ["cherishing", "amazing", "enjoying"]
        column = 1
        for end in verb_endings:
            Radiobutton(self,
                        text = end,
                        variable = self.verb_end,
                        value = end
                        ).grid(row = 5, column = column, sticky = W)
            column += 1
            
            Button(self,
                   text = "Click for story",
                   command = self.tell_story
                   ).grid(row = 6, column = 0, sticky = W)
            
            self.story_txt = Text(self, width = 75, height = 10, wrap = WORD)
            self.story_txt.grid(row = 7, column = 0, columnspan = 4)

    def tell_story(self):
        name = self.name_ent.get()
        noun = self.noun_ent.get()
        verb = self.verb_ent.get()
        adjectives = ""
        if self.is_wonderful.get():
            adjectives += "wonderful "
        if self.is_beautiful.get():
            adjectives += "beautiful, "
        if self.is_happy.get():
            adjectives = "happy, "
        verb_end = self.verb_end.get()

        story = name 
        story += " you're a "
        story += adjectives
        story += "person worthy of all the "
        story += noun
        story += " in the the world. "
        story += "You deserve to be treated with "
        story += noun
        story += " and respect. "
        story += "You're "
        story += verb_end
        story += " in your own skin and embrace it. Grab yourself a drink and be "
        story += adjectives
        story += "with the life you live. The world don't care about your loneliness, so enjoy your life and "
        story += verb
        story += " yourself."

        self.story_txt.delete(0.0, END)
        self.story_txt.insert(0.0, story)

root = Tk()
root.title("One Love")
app = Application(root)
root.mainloop()








