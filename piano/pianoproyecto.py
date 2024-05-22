from tkinter import *
import pygame
import time

class AF:
    def __init__(self, states, alphabet, transitions, initial_state, accepting_states):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.current_state = initial_state
        self.accepting_states = accepting_states
        pygame.mixer.init()

    def process_input(self, input_string):
        current_state = self.current_state

        for symbol in input_string:
            if symbol in self.alphabet:
                self.play_sound(symbol)
                pygame.time.delay(1000)
            else:
                self.play_sound("error")
                return False

            current_state = self.transitions.get(current_state, {}).get(symbol, None)
            if current_state is None:
                self.play_sound("error")
                return False

        return current_state in self.accepting_states

    def play_sound(self, note):
        sound_files = {
            'Do': 'music/do.mp3',
            'Re': 'music/re.mp3',
            'Mi': 'music/mi.mp3',
            'Sol': 'music/sol.mp3',
            'La': 'music/la.mp3',
            'Si': 'music/si.mp3',
            'error': 'music/error.mp3'
        }
        sound_file = sound_files.get(note)
        if sound_file:
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()
        else:
            print(f"No se encontró el archivo de sonido para la nota {note}")

states = ['q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10',
          'q11', 'q12', 'q13', 'q14', 'q15', 'q16', 'q17', 'q18', 'q19', 'q20',
          'q21', 'q22']
alphabet = ['Do', 'Re', 'Mi', 'Sol', 'La', 'Si']
transitions = {
    'q0': {'Sol': 'q1'},
    'q1': {'Sol': 'q2'},
    'q2': {'Re': 'q3'},
    'q3': {'Re': 'q4'},
    'q4': {'Mi': 'q5'},
    'q5': {'Mi': 'q6'},
    'q6': {'Re': 'q7'},
    'q7': {'Do': 'q8'},
    'q8': {'Do': 'q9'},
    'q9': {'Si': 'q10'},
    'q10': {'Si': 'q11'},
    'q11': {'La': 'q12'},
    'q12': {'La': 'q13'},
    'q13': {'Sol': 'q14'},
    'q14': {'Re': 'q15'},
    'q15': {'Re': 'q16'},
    'q16': {'Do': 'q17'},
    'q17': {'Do': 'q18'},
    'q18': {'Si': 'q19'},
    'q19': {'Si': 'q20'},
    'q20': {'La': 'q21'},
    'q21': {'Sol': 'q22'}
}
initial_state = 'q0'
accepting_states = ['q22']

fa = AF(states, alphabet, transitions, initial_state, accepting_states)

class VentanaEm:
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title("Proyecto de Teoría de la Computación")
        self.ventana.geometry("700x700")
        self.ventana.configure(bg='black')

        self.ventana.columnconfigure(0, weight=1)
        self.ventana.rowconfigure(0, weight=1)
        self.ventana.rowconfigure(1, weight=1)
        self.ventana.rowconfigure(2, weight=1)
        self.ventana.rowconfigure(3, weight=1)
        self.ventana.rowconfigure(4, weight=1)

        self.label1 = Label(self.ventana, text="Estrellita ¿Dónde estás?", bg='white', font=('Arial', 20))
        self.label1.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

        self.label2 = Label(self.ventana, text="Sol Sol Re Re Mi Mi Re\n"
                                               "Do Do Si Si La La Sol\n"
                                               "Re Re Do Do Si Si La\n"
                                               "Re Re Do Do Si Si La\n"
                                               "Sol Sol Re Re Mi Mi Re\n"
                                               "Do Do Si Si La La Sol", bg='#DEB887', font=('Arial', 15))
        self.label2.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')

        self.text1 = Entry(self.ventana, bg='#F5F5DC', font=('Arial', 15))
        self.text1.grid(row=2, column=0, padx=10, pady=10, sticky='nsew')

        self.boton_reproducir = Button(self.ventana, text="Reproducir Canción", command=self.verificar_cancion)
        self.boton_reproducir.grid(row=4, column=0, padx=10, pady=10, sticky='nsew')

        imagen = PhotoImage(file="img/piano.png")
        self.label3 = Label(self.ventana, image=imagen)
        self.label3.grid(row=5, column=0, padx=10, pady=10, sticky='nsew')
        self.label3.image = imagen

        self.ventana.mainloop()

    def verificar_cancion(self):
        entrada = self.text1.get()
        note = entrada.split()

        if fa.process_input(note):
            resultado = "La canción 'Estrellita ¿Dónde Estás?' ha sido reconocida."
        else:
            resultado = "La canción 'Estrellita ¿Dónde Estás?' no ha sido reconocida."

        self.mostrar_resultado(resultado)
        self.ventana.update()
        time.sleep(1)

    def mostrar_resultado(self, resultado):
        resultado_ventana = Toplevel(self.ventana)
        resultado_ventana.title("Resultado")
        label_resultado = Label(resultado_ventana, text=resultado)
        label_resultado.pack()

Objeto_ventana = VentanaEm()