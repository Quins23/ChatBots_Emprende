import streamlit as st
from groq import Groq as _Groq
from dotenv import load_dotenv
import os

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Obtener la API key del archivo .env
api_key = os.getenv('GROQ_API_KEY')

if api_key is None:
    raise ValueError("La API key no está configurada. Asegúrate de que el archivo .env contenga la variable GROQ_API_KEY.")

# Inicializar el cliente de Groq
client = _Groq()

# Establecer la API key en el cliente
client.api_key = api_key

# Función para generar respuestas del asistente
def llamar(text, context):
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": context},
            {"role": "user", "content": text}
        ],
        model="llama3-8b-8192",
        temperature=0.5,
        max_tokens=1000,
        top_p=1,
        stop=None,
        stream=False,
    )
    return chat_completion.choices[0].message.content

if 'nombre' not in st.session_state:
    st.session_state.nombre = ''
if 'nombre_negocio' not in st.session_state:
    st.session_state.nombre_negocio = ''
if 'pregunta1' not in st.session_state:
    st.session_state.pregunta1 = ''
if 'pregunta2' not in st.session_state:
    st.session_state.pregunta2 = ''
if 'pregunta3' not in st.session_state:
    st.session_state.pregunta3 = ''
if 'pregunta4' not in st.session_state:
    st.session_state.pregunta4 = ''
if 'pregunta5' not in st.session_state:
    st.session_state.pregunta5 = ''
if 'pregunta6' not in st.session_state:
    st.session_state.pregunta6 = ''
if 'pregunta7' not in st.session_state:
    st.session_state.pregunta7 = ''
if 'pregunta8' not in st.session_state:
    st.session_state.pregunta8 = ''
if 'pregunta9' not in st.session_state:
    st.session_state.pregunta9 = ''
if 'pregunta10' not in st.session_state:
    st.session_state.pregunta10 = ''
if 'resumen_preguntas' not in st.session_state:
    st.session_state.resumen_preguntas = ''

# Ocultar menú y opciones predeterminadas por sistema de streamlit
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
###

# SIDEBAR LATERAL IZQUIERDO
st.sidebar.image("logo.png", use_column_width=100)

st.sidebar.title('Emprende tu idea')
st.sidebar.write(f'Descubre tu propósito')
###

st.title('¡Bienvenida a descubre tu propósito!')
st.session_state.nombre = st.text_input('Antes de iniciar me gustaría preguntar ¿Cuál es tu nombre?, con esto ya daremos el primer paso para empezar', '')

if st.session_state.nombre:
    st.chat_message('assistant').write(f'¡Hola, {st.session_state.nombre}! Aquí te vamos a ayudar a explorar tus pasiones, habilidades y valores para identificar tu propósito personal y profesional para finalmente saber que ideas geniales pueden adaptarse a ti... ¡Vamos a ello! 🚀 Si estás lista, escribe la palabra “lista” para empezar.')
    
    if st.text_input('Escribe "lista" para empezar:', key='start_input').lower() == 'lista':
        st.chat_message('assistant').write(f'Perfecto {st.session_state.nombre}, para continuar me gustaría saber más sobre ti. Por favor, responde a estas preguntas en orden:')
        
        st.session_state.pregunta1 = st.text_input('1. Cuenta una breve historia sobre ti misma (tus experiencias pasadas, formación, etc)', st.session_state.pregunta1, key='pregunta1_input')
        if st.session_state.pregunta1:
            st.session_state.pregunta2 = st.text_input('2. ¿Cuáles son tus habilidades principales? (por ejemplo, comunicación, diseño gráfico, tecnología)', st.session_state.pregunta2, key='pregunta2_input')
            if st.session_state.pregunta2:
                st.session_state.pregunta3 = st.text_input('3. ¿En qué actividades has trabajado o tienes experiencia?', st.session_state.pregunta3, key='pregunta3_input')
                if st.session_state.pregunta3:
                    st.session_state.pregunta4 = st.text_input('4. ¿Cuáles son tus pasatiempos y qué disfrutas hacer en tu tiempo libre?', st.session_state.pregunta4, key='pregunta4_input')
                    if st.session_state.pregunta4:
                        st.session_state.pregunta5 = st.text_input('5. ¿Cuáles son tus valores y motivaciones personales?', st.session_state.pregunta5, key='pregunta5_input')
                        if st.session_state.pregunta5:
                            st.session_state.pregunta6 = st.text_input('6. Describe una situación en la que hayas tenido éxito o te hayas sentido muy orgullosa de tu trabajo.', st.session_state.pregunta6, key='pregunta6_input')
                            if st.session_state.pregunta6:
                                st.session_state.pregunta7 = st.text_input('7. ¿Qué sueñas hacer?', st.session_state.pregunta7, key='pregunta7_input')
                                if st.session_state.pregunta7:
                                    st.session_state.pregunta8 = st.text_input('8. ¿Qué amas hacer?', st.session_state.pregunta8, key='pregunta8_input')
                                    if st.session_state.pregunta8:
                                        st.session_state.pregunta9 = st.text_input('9. ¿Qué crees que el mundo necesita?', st.session_state.pregunta9, key='pregunta9_input')
                                        if st.session_state.pregunta9:
                                            st.session_state.pregunta10 = st.text_input('10. Menciona una actividad por la que te podrían pagar, en la que harías lo que te gusta y seas buena haciendo. ¿Por qué crees que el mundo necesita eso de ti?', st.session_state.pregunta10, key='pregunta10_input')
                                            if st.session_state.pregunta10:
                                                st.chat_message('assistant').write(f'Excelente {st.session_state.nombre} ya respondiste todas las preguntas, ahora avancemos...')
                                                
                                                if st.session_state.pregunta1 and st.session_state.pregunta2 and st.session_state.pregunta3 and st.session_state.pregunta4 and st.session_state.pregunta5 and st.session_state.pregunta6 and st.session_state.pregunta7 and st.session_state.pregunta8 and st.session_state.pregunta9 and st.session_state.pregunta10:
                                                    
                                                    if not st.session_state.resumen_preguntas:
                                                        resumen_preguntas = llamar(
                                                            f'Analiza la siguiente información y con esa información genera 3 ideas de negocio que se alineen con las habilidades, intereses y valores del usuario, además que cada idea tenga su respectiva explicación:\n{st.session_state.pregunta1}\n{st.session_state.pregunta2}\n{st.session_state.pregunta3}\n{st.session_state.pregunta4}\n{st.session_state.pregunta5}\n{st.session_state.pregunta6}\n{st.session_state.pregunta7}\n{st.session_state.pregunta8}\n{st.session_state.pregunta9}\n{st.session_state.pregunta10}',
                                                            'Eres un experto en desarrollo de ideas de negocios. Analiza la información proporcionada'
                                                        )
                                                        st.session_state.resumen_preguntas = resumen_preguntas
                                                    
                                                    st.chat_message('assistant').write(f'Con la información que has proporcionado, hemos seleccionado 3 ideas que se ajustan perfectamente con tus intereses, valores y habilidades. Aquí tienes:\n\n{st.session_state.resumen_preguntas}\n\nRevisa de forma detallada estas ideas de negocio y una vez lista elije una.')
                                                    
                                                    st.chat_message('assistant').write(f'Escribe el nombre de la idea que más te llamó la atención\n\nEjemplo: "Delicias de la Guajira"')
                                                    st.session_state.nombre_negocio = st.text_input('', '')

                                                    if st.session_state.nombre_negocio:
                                                        st.chat_message('assistant').write(f'Eso es {st.session_state.nombre} has elegido la idea:\n\n{st.session_state.nombre_negocio}\n\n¿Estás lista para continuar?')
                                                        
                                                        if st.text_input('Escribe "lista" para continuar:', key='last_input').lower() == 'lista':
                                                            st.chat_message('assistant').write(f'¡Felicidades por dar el primer paso hacia tu emprendimiento! Recuerda: "El único límite a nuestros logros de mañana está en nuestras dudas de hoy"')