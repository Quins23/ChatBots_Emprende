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

# Inicializar el estado de sesión para la Fase 4
if 'nombre' not in st.session_state:
    st.session_state.nombre = ''
if 'predis_info' not in st.session_state:
    st.session_state.predis_info = ''
if 'tipo_publicacion' not in st.session_state:
    st.session_state.tipo_publicacion = ''
if 'plantilla_seleccionada' not in st.session_state:
    st.session_state.plantilla_seleccionada = ''
if 'publicacion_final' not in st.session_state:
    st.session_state.publicacion_final = ''
if 'enlace_publicacion' not in st.session_state:
    st.session_state.enlace_publicacion = ''
if 'enlace_logo' not in st.session_state:
    st.session_state.enlace_logo = ''
if 'enlace_canva' not in st.session_state:
    st.session_state.enlace_canva = ''

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
st.sidebar.write(f'Lanzate')
###

st.title('¡Bienvenida a lanzate!')

st.session_state.nombre = st.text_input('Antes de iniciar me gustaría preguntar ¿Cuál es tu nombre?, con esto ya daremos el primer paso para empezar', '')

if st.session_state.nombre:
    st.chat_message('assistant').write(
        f'¡Hola, {st.session_state.nombre}! Aquí, lanzarse es la garantía para seguir avanzando. '
        'Ten en cuenta que “la única diferencia entre el éxito y el fracaso es la habilidad de tomar acción” '
        '(Alexander Graham Bell). 💡☎️'
    )
    st.chat_message('assistant').write(
        'Es momento de lanzar tu negocio al mundo. '
        'Vamos a crear tu primera publicación promocional usando Predis.AIEstás preparada para empezar? '
        'Escribe "preparada" para continuar. 😊'
    )

    if st.text_input('Escribe "preparada" para empezar:', key='start_input').lower() == 'preparada':
        st.chat_message('assistant').write(
            '¡Genial! Vamos a guiarte paso a paso para crear una publicación impactante que presente tu negocio al mundo. '
            'Sigue estas instrucciones:\n\n'
            '1. Abre Predis.AI (https://predis.ai) y creemos nuestra cuenta usando las opciones que nos aparecen. Podemos hacerlo con nuestro correo Gmail 🔴 dándole la opción en Google o nuestra cuenta de Facebook. 😅🔵\n'
            '2. Luego de creada nuestra cuenta, hacemos clic en "Crear nuevo +" en el menú lateral de la parte superior izquierda.\n'
            '3. En la ventana que aparecerá, seleccionamos "Negocios para publicar".\n'
            'Responde estas preguntas sobre tu negocio dentro de cada recuadro:\n'
            '- ¿Cómo describes tu empresa en pocas palabras?\n'
            '- ¿Qué vendes o promocionas?\n'
            '- ¿Quién es tu cliente ideal?\n'
            '- ¿Qué beneficios obtienen tus clientes?\n\n'
            'Debes ser precisa para que la IA pueda generar una publicación personalizada y acorde con las necesidades de tu negocio. Cuando hayas terminado, escribe "siguiente".'
        )

        if st.text_input('Escribe "siguiente" para continuar:', key='next_input').lower() == 'siguiente':
            st.chat_message('assistant').write(
                '4. ¡Perfecto! Ahora vamos a configurar los detalles de tu publicación 🤓:\n\n'
                '- A la derecha de la pantalla:\n'
                '- Elige el tipo de publicación: imagen, video o carrusel.\n'
                '- Selecciona "DEJA QUE LA AI DECIDA" para las plantillas.\n\n'
                'Ajusta el número de variantes de 1 a 7, para tener distintos tipos de ejemplos de publicaciones. Te sugerimos que elijas la opción 3 😉.\n\n'
                '- Si deseas publicar una Imagen, elige la relación de aspecto adecuada para la red social donde publicarás. Para efectos de este ejercicio, trabajaremos con 1:1. \n\n'
                'En el caso de que elijas video, escoge las plantillas para la publicación (tipo Short , Long, Voiceover para poner nuestra voz a los videos o una plantilla propia). Para efectos de este ejercicio, te recomendamos que escojas Short. En cuanto a la longitud del título del vídeo entre Corto, Medio o Largo. Elige en este caso según tu preferencia en cuanto a longitud del video.\n\n'
                'Cuando hayas completado esta parte, escribe "lista". 👀'
            )

            if st.text_input('Escribe "lista" para continuar:', key='ready_input').lower() == 'lista':
                st.chat_message('assistant').write(
                    '5. Ahora haz clic en "Más ajustes" y:\n\n'
                    '● Cambia el idioma de entrada y salida a Español.\n\n'
                    '● En "Temas de publicaciones", selecciona el tipo de contenido que desees para tu primera publicación. Te recomendamos que sea entre promocional o educativo.\n\n'
                    'Una vez completado esto, dale a “generar”. La plataforma creará varias opciones de publicaciones promocionales basadas en la información que proporcionaste.\n\n'
                    'Revisa las opciones generadas y selecciona la que mejor represente tu negocio. Si necesitas hacer ajustes, puedes editarla directamente en Predis.AI.\n\n'
                    'Cuando hayas elegido tu publicación final, escribe "terminado". 🤯'
                )

                if st.text_input('Escribe "terminado" cuando hayas terminado:', key='done_input').lower() == 'terminado':
                    st.chat_message('assistant').write(
                        f'¡Felicidades, {st.session_state.nombre}! 🎉 Has creado tu primera publicación. Este es un gran paso para lanzar tu negocio al mundo. Recuerda que una buena publicación de lanzamiento debe:\n\n'
                        '1. Captar la atención de tu audiencia\n\n'
                        '2. Comunicar claramente el valor de tu negocio\n\n'
                        '3. Motivar a tu audiencia a tomar acción (el call-to-action o llamado a la acción)\n\n'
                        '¿Estás lista para compartir tu publicación en redes sociales? Toma tu tiempo, no hay prisa, cuando estés lista, escribe "lista" para continuar.'
                    )

                    if st.text_input('Escribe "lista" para continuar', key='share_input').lower() == 'lista':
                        st.chat_message('assistant').write(
                            f'¡Fantástico! Es hora de que el mundo conozca tu negocio. Comparte tu publicación en las redes sociales que elegiste y prepárate para recibir feedback y posibles clientes.\n\n'
                            'Recuerda, este es solo el comienzo. Continúa creando contenido valioso y promocionando tu negocio de manera constante.\n\n'
                            'Ahora, ¡comparte el enlace de la publicación para culminar este Programa y graduarte en ideación de modelos de negocio usando herramientas de inteligencia artificial! (también envíanos el enlace a tu logo para poder revisarlo). 😄'
                        )
                        
                        st.session_state.enlace_publicacion = st.text_input('Comparte el enlace de tu publicación:')
                        st.session_state.enlace_logo = st.text_input('Comparte el enlace de tu logo:')
                        st.session_state.enlace_canva = ('https://www.canva.com/design/DAGKqOD7Hcw/yENnVLwX2aMJvHFK69zhkA/view?utm_content=DAGKqOD7Hcw&utm_campaign=designshare&utm_medium=link&utm_source=publishsharelink&mode=preview')

                        if st.session_state.enlace_publicacion and st.session_state.enlace_logo:
                            st.chat_message('assistant').write(
                                f'¡Hemos llegado al final! Ahora el mundo conocerá tu negocio. Comparte tu publicación en las redes sociales que elegiste y prepárate para recibir feedback y posibles clientes.\n\n'
                                'Ten en mente que este es solo el comienzo. Continúa creando contenido de valor y promocionando tu negocio de manera constante a lo largo del tiempo.\n\n'
                                f'¡Felicidades por llegar tan lejos, {st.session_state.nombre}! Has completado con éxito todas las fases del Programa y ahora estás lista para emprender tu viaje como empresaria. ¡Mucha suerte en tu nueva aventura! 🚀💪\n\n'
                                'Estos fueron los resultados de tu trabajo en este Programa, para que los recuerdes como símbolo de tu esfuerzo y dedicación:\n\n'
                                f'Business Model Canvas: {st.session_state.enlace_canva}\n\n'
                                f'Logo: {st.session_state.enlace_logo}\n\n'
                                f'Publicación: {st.session_state.enlace_publicacion}'
                            )
                            