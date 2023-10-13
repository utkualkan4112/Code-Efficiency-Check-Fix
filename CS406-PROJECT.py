import openai
import sys
import tkinter as tk
import tkinter.font as tkFont

def show_reformatted_code(response: str):
    sentences = response.split(".")
    for sentence in sentences:
        print(sentence)

#openai.api_key = "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"

def fix_performance(current_code: str):

    responseOfApi = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system",
             "content": "Your job is to detect,classify and fixperformance-related bugs in a given C++ code - which can be sequential, OpenMP-based (CPU parallel) or CUDA-based (GPU Parallel)." \
                        "Here are the categories of the causes of inefficiency and their subcategories." \
                        "CAUSES OF INEFFICIENCY" \
                        "A. Inefficient algorithm, data structure, computational kernel, and their implementation (IAD) " \
                        "A-1) Computationally expensive operation" \
                        "A-2) Redundant operations" \
                        "A-3) Unnecessary operations" \
                        "A-4) Inefficient data-structure" \
                        "" \
                        "B. Inefficient code for underlying micro-architecture (MA)" \
                        "B-1) Inefficiency due to memory/data locality:" \
                        " B-1-a) Inefficient cache access:" \
                        " B-1-b) Inefficient GPU-memory access:" \
                        "B-2) Sub-optimal code generation by compiler:" \
                        "B-2-a) Loop unrolling:" \
                        "   B-2-b) Function inlining:" \
                        "C. Missing parallelism (MP)" \
                        "C-1) SIMD parallelism" \
                        "C-2) GPU parallelism" \
                        "C-3) Task parallelism" \
                        "" \
                        "" \
                        "D. Inefficient parallelization (PO)" \
                        "" \
                        "E. Inefficient Concurrency control (ICS)" \
                        "These performance bugs include unnecessary locks (3), inappropriate lock granularity (1), use of inefficient locking mechanism (1), and unnecessary thread synchronization (2)." \
                        "" \
                        "F. Inefficient memory management (IMM)" \
                        "memory leak, redundant memory allocation, and repeated calls for allocation." \
                        "" \
                        "" \
                        "G. Other forms of inefficiencies Our study finds a small set of other forms of inefficiencies including unintentional programming logic error (PE), IO inefficiency (IO), compiler regression (CR), and unnecessary process communication (UPC)."},
            {"role": "user", "content": "Please find and fix the inefficiency problem in this code: \n" + current_code},


        ]
    )
    responseText = responseOfApi.choices[0].message.content

    return responseText
def find_inefficieny_category(current_code: str):

    responseOfApi = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system",
             "content": "Your job is to detect and classify performance-related bugs in a given C++ code - which can be sequential, OpenMP-based (CPU parallel) or CUDA-based (GPU Parallel)." \
                        "Here are the categories of the causes of inefficiency and their subcategories." \
                        "CAUSES OF INEFFICIENCY" \
                        "A. Inefficient algorithm, data structure, computational kernel, and their implementation (IAD) " \
                        "A-1) Computationally expensive operation" \
                        "A-2) Redundant operations" \
                        "A-3) Unnecessary operations" \
                        "A-4) Inefficient data-structure" \
                        "" \
                        "B. Inefficient code for underlying micro-architecture (MA)" \
                        "B-1) Inefficiency due to memory/data locality:" \
                        "	B-1-a) Inefficient cache access:" \
                        "	B-1-b) Inefficient GPU-memory access:" \
                        "B-2) Sub-optimal code generation by compiler:" \
                        "B-2-a) Loop unrolling:" \
                        "   B-2-b) Function inlining:" \
                        "C. Missing parallelism (MP)" \
                        "C-1) SIMD parallelism" \
                        "C-2) GPU parallelism" \
                        "C-3) Task parallelism" \
                        "" \
                        "" \
                        "D. Inefficient parallelization (PO)" \
                        "" \
                        "E. Inefficient Concurrency control (ICS)" \
                        "These performance bugs include unnecessary locks (3), inappropriate lock granularity (1), use of inefficient locking mechanism (1), and unnecessary thread synchronization (2)." \
                        "" \
                        "F. Inefficient memory management (IMM)" \
                        "memory leak, redundant memory allocation, and repeated calls for allocation." \
                        "" \
                        "" \
                        "G. Other forms of inefficiencies Our study finds a small set of other forms of inefficiencies including unintentional programming logic error (PE), IO inefficiency (IO), compiler regression (CR), and unnecessary process communication (UPC)."},
            {"role": "user", "content": "Please find the inefficiency category in this code:" + current_code}

        ]
    )
    responseText = responseOfApi.choices[0].message.content

    return responseText


def set_api_key(user_key:str,entry_box: tk.Entry):
    print(user_key)
    openai.api_key = user_key
    print(openai.api_key)
    entry_box.delete(0, tk.END)
    entry_box.insert(0,"Your API key has been set as " +openai.api_key )
class tkinterApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title("CS406-PERFORMANCE-TOOL")
        width = 1450
        height = 900
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}

        for F in (HomePage,performance_classification_page,performance_fixing_page):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(HomePage)


    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


def destroy_application(self):
    self.root.destroy()
    sys.exit(1)

class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        width = 1350
        height = 700
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()

        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)

        GMessage_335 = tk.Message(self)
        ft = tkFont.Font(family='Times', size=26)
        GMessage_335["font"] = ft
        GMessage_335["fg"] = "#333333"
        GMessage_335["justify"] = "left"
        GMessage_335["text"] = "WELCOME TO PARALLEL PROGRAMMING PERFORMANCE TOOL"
        GMessage_335["width"] = 1200
        GMessage_335.place(x=160, y=60)

        GMessage_808 = tk.Message(self)
        ft = tkFont.Font(family='Times', size=15)
        GMessage_808["font"] = ft
        GMessage_808["fg"] = "#333333"
        GMessage_808["justify"] = "left"
        GMessage_808["text"] = "This program uses the OpenAI's Chat-GPT API to both detect/classify causes of inefficiency in your\n" \
                               "sequential, OpenMP-based (CPU parallel) or CUDA-based (GPU Parallel) and fix them.\n" \
                               "The provided categories below are from the paper An Empirical Study of High Performance Computing (HPC) Performance Bugs\n\n" \
                        "Here are the categories of the causes of inefficiency and their subcategories.\n" \
                        "A. Inefficient algorithm, data structure, computational kernel, and their implementation (IAD)\n " \
                        "   A-1) Computationally expensive operation\n" \
                        "   A-2) Redundant operations\n" \
                        "   A-3) Unnecessary operations\n" \
                        "   A-4) Inefficient data-structure\n" \
                        "" \
                        "B. Inefficient code for underlying micro-architecture (MA)\n" \
                        "   B-1) Inefficiency due to memory/data locality:\n" \
                        "       B-1-a) Inefficient cache access:\n" \
                        "       B-1-b) Inefficient GPU-memory access:\n" \
                        "   B-2) Sub-optimal code generation by compiler:\n" \
                        "       B-2-a) Loop unrolling:\n" \
                        "       B-2-b) Function inlining:\n" \
                        "C. Missing parallelism (MP)\n" \
                        "   C-1) SIMD parallelism\n" \
                        "   C-2) GPU parallelism\n" \
                        "   C-3) Task parallelism\n" \
                        "" \
                        "" \
                        "D. Inefficient parallelization (PO)\n" \
                        "" \
                        "E. Inefficient Concurrency control (ICS)\n" \
                        "   These performance bugs include unnecessary locks (3), inappropriate lock granularity (1), use of inefficient locking mechanism (1), and unnecessary thread synchronization (2).\n" \
                        "" \
                        "F. Inefficient memory management (IMM)\n" \
                        "   memory leak, redundant memory allocation, and repeated calls for allocation.\n" \
                        "" \
                        "" \
                        "G. Other forms of inefficiencies Our study finds a small set of other forms of inefficiencies including unintentional programming logic error (PE), IO inefficiency (IO), compiler regression (CR), and unnecessary process communication (UPC).\n"

        GMessage_808.place(x=40, y=170)

        GButton_537 = tk.Button(self)
        ft = tkFont.Font(family='Times',size=15)
        GButton_537["font"] = ft
        GButton_537["bg"] = "#FFFFFF"
        GButton_537["fg"] = "#000000"
        GButton_537["text"] = "DETECT AND CLASSIFY PERFORMANCE BUGS IN YOUR CODE"
        GButton_537.place(x=850, y=250)
        GButton_537["command"] = lambda : controller.show_frame(performance_classification_page)

        GButton_378 = tk.Button(self)
        GButton_378["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=15)
        GButton_378["font"] = ft
        GButton_378["fg"] = "#000000"
        GButton_378["justify"] = "center"
        GButton_378["text"] = "FIX PERFORMANCE BUGS IN YOUR CODE"
        GButton_378.place(x=850, y=450)
        GButton_378["command"] = lambda : controller.show_frame(performance_fixing_page)

        api_entry_label = tk.Label(self, text="Enter your OPENAI API key:")
        api_entry_label.place(x= 720, y=850)
        submit_button = tk.Button(self, text="Submit", command=lambda: set_api_key(api_entry_box.get(), api_entry_box) )
        submit_button.place(x= 1250, y=850)
        api_entry_box = tk.Entry(self,highlightthickness= 1,width = 60)
        api_entry_box.place(x= 870, y=850)

    def GButton_537_command(self):
        print("command")

    def GButton_378_command(self):
        print("command")

class performance_classification_page(tk.Frame):
    def execute_multiple_commands(self):
        self.ai_response.delete("1.0", tk.END)
        self.retrieve_and_analyze()
    def waiting_message(self):
        self.ai_response.insert(tk.END, "Waiting for response from Chat-GPT\n")
    def retrieve_and_analyze(self):
        user_input = self.messages.get("2.0", "end-1c")
        print(user_input)
        try:
            response = find_inefficieny_category(user_input)
        except:
            self.ai_response.insert(tk.END, "An Error has been received from Chat-GPT. Please try again\n")
        else:
            print(response)
            sentences = response.split(".")
            for sentence in sentences:
                self.ai_response.insert(tk.END, sentence + "\n")

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        ft = tkFont.Font(family='Times', weight="bold", size=15)
        page_label = tk.Label(self, text="DETECT AND CLASSIFY PERFORMANCE BUGS IN YOUR CODE",font = ft, pady=20)
        info_label = tk.Label(self,text="Please ONLY enter your code to the below box. The prompts are written in the background.")

        page_label.grid(row=0, column=0)
        info_label.grid(row=1, column=0)

        self.messages = tk.Text(self , width=80, border=2, relief="solid")
        self.messages.grid(row=2, column=0, padx=10, pady=10, columnspan=2)
        self.messages.insert(tk.END, "Please enter your code below this line.PLEASE DON'T DELETE THIS LINE")

        ft_GPT = tkFont.Font(family='Times', weight="bold", size=10)
        GPT_response_label = tk.Label(self, text="CHAT-GPT'S RESPONSE", font = ft_GPT, pady=20)
        GPT_response_label.grid(row=1, column=3)
        page_label.grid(row=0, column=0)

        self.ai_response = tk.Text(self ,width=80, border=2, relief="solid")
        self.ai_response.grid(row=2, column=3, padx=10, pady=10, columnspan=2)
        self.ai_response.insert(tk.END, "Waiting for response from Chat-GPT\n")

        home_page_button = tk.Button(self, text="Return to home page",
                                     command=lambda: controller.show_frame(HomePage))
        home_page_button.place(x = 1200 , y = 10 )

        submit_button = tk.Button(self, text="Submit Code", command=self.execute_multiple_commands, relief="solid")
        submit_button.place(x=100, y=550)
        clear_button = tk.Button(self, text="Clear Text Above", command=lambda: self.ai_response.delete("1.0", tk.END), relief="solid")
        clear_button.grid(row=3, column=3, padx=10, pady=10)

        clear_submit_text_button = tk.Button(self, text="Clear Text Above", command=lambda: self.messages.delete("2.0", tk.END),
                                             relief="solid")
        clear_submit_text_button.place(x=300, y=550)


class performance_fixing_page(tk.Frame):
    def retrieve_and_fix(self):
        self.ai_response.delete("1.0", tk.END)
        user_input = self.messages.get("2.0", "end-1c")
        print(user_input)
        try:
            response = fix_performance(user_input)
        except:
            self.ai_response.insert(tk.END, "An Error has been received from Chat-GPT. Please try again\n")
        else:
            sentences = response.split(".")
            for sentence in sentences:
                self.ai_response.insert(tk.END, sentence)
            print(response)

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        ft = tkFont.Font(family='Times', weight="bold" ,size=15)
        page_label = tk.Label(self, text="FIX PERFORMANCE BUGS IN YOUR CODE", font = ft, pady=20)
        info_label = tk.Label(self, text="Please ONLY enter your code to the below box. The prompts are written in the background.")

        page_label.grid(row= 0, column=0)
        info_label.grid(row=1, column=0)

        self.messages = tk.Text(self, width=80 , border=2, relief="solid")
        self.messages.grid(row=2, column=0, padx=10, pady=10, columnspan=2)
        self.messages.insert(tk.END, "Please enter your code below this line.PLEASE DON'T DELETE THIS LINE")

        ft_GPT = tkFont.Font(family='Times', weight="bold", size=10)
        GPT_response_label = tk.Label(self, text="CHAT-GPT'S RESPONSE", font = ft_GPT,  pady=20)

        GPT_response_label.grid(row=1, column=3)
        page_label.grid(row=0, column=0)
        self.ai_response = tk.Text(self, width=80, border=2, relief="solid")
        self.ai_response.grid(row=2, column=3, padx=10, pady=10, columnspan=2)
        self.ai_response.insert(tk.END, "Waiting for response from Chat-GPT\n")

        home_page_button = tk.Button(self, text="Return to home page",
                                     command=lambda: controller.show_frame(HomePage))

        home_page_button.place(x = 1200 , y = 10 )


        submit_button = tk.Button(self, text="Submit Code", command=self.retrieve_and_fix,relief="solid")
        submit_button.place(x = 100, y = 550)

        clear_button = tk.Button(self, text="Clear Text Above", command=lambda: self.ai_response.delete("1.0", tk.END),
                                 relief="solid")
        clear_button.grid(row=3, column=3, padx=10, pady=10)

        clear_submit_text_button = tk.Button(self, text="Clear Text Above",
                                             command=lambda: self.messages.delete("2.0", tk.END),
                                             relief="solid")
        clear_submit_text_button.place(x= 300, y = 550)





if __name__ == "__main__":
    app = tkinterApp()
    app.mainloop()



