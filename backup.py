from instructor import llamar
import streamlit as st

# with open("style.css") as f:
#     st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# col1, col2 = st.columns([1, 3])

# with col1:
#     st.image("logo.png", use_column_width=True)

# with col2:
    # st.image("logo.png")
    
st.title("Emprende tu idea")
    
    # with st.chat_message("assistant"):
    #     st.markdown("Registro")
    

    # Username = st.text_input("Crea un nombre de usuario", placeholder="Quin")
    # correo = st.text_input("Introduce tu correo aquí", placeholder="micorreo@correo.com")
    # contraseña = st.text_input("Crea una contraseña", placeholder="123456")

    # submit_button = st.button("Enviar")

    # if submit_button:
    #     datos_usuario = {
    #         "Username": Username,
    #         "correo": correo,
    #         "contraseña": contraseña
    #     }

    #     respuesta=llamar(datos_usuario)
        
    #     st.success("¡Datos enviados con éxito!") 
        
if "messages" not in st.session_state: 
    st.session_state.messages = [] 
if "first_message" not in st.session_state: 
    st.session_state.first_message = True

for message in st.session_state.messages: 
    with st.chat_message(message["role"]): 
        st.markdown(message["content"])

if st.session_state.first_message: 
    with st.chat_message("assistant"):
        st.markdown("¡Bienvenida a emprende tu idea!")
        st.markdown("Comecemos este proceso, por lo que te pido por favor que escribas un simple 'Hola emprende tu idea, me llamo Sandra'")
        

    st.session_state.messages.append({"role": "assistant", "content": "¡Bienvenido a emprende tu idea!"})
    st.session_state.first_message = False

if prompt := st.chat_input("¿cómo puedo ayudarte?"):
    
    with st.chat_message("user"):
        st.markdown (prompt)    
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"): 
        st.markdown(llamar(prompt))
    st.session_state.messages.append({"role": "assistant", "content": llamar(prompt)})
    
# IA
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq()

def llamar(text):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": (
                    "Hola, IA. Necesito que ayudes a una emprendedora a descubrir su propósito."
                    "Por favor, pídele que proporcione la siguiente información en orden:\n"
                    "1. Una breve historia sobre sí misma (experiencias pasadas, formación, etc.).\n"
                    "2. Sus habilidades principales (por ejemplo, cocina, diseño gráfico, programación).\n"
                    "3. Actividades en las que destaca o tiene experiencia.\n"
                    "4. Sus pasatiempos y lo que disfruta hacer en su tiempo libre.\n"
                    "5. Sus valores y motivaciones personales.\n"
                    "6. Alguna situación en la que haya tenido éxito o se haya sentido muy orgullosa de su trabajo.\n"
                    "7. Que es buena haciendo.\n"
                    "8. Que ama hacer.\n"
                    "9. Que cree que el mundo necesita.\n"
                    "10. Si considera que le pueden pagar por hacer lo que le gusta o es buena haciendo.\n"
                    "11. Si considera que lo que hace el mundo lo necesita.\n"
                    "Usa esta información para generar y sugerirle tres ideas de negocio que se alineen con sus habilidades, intereses, valores y principalmente las ideas en las que se combine o se alinee perfectamente con sus gustos, en lo que es buena, y que principalmente pueda servir como fuente de ingresos.\n"
                    "Al final preguntale si alguna de las ideas de negocio llamó su atención. Si responde que sí, entonces dile que continue a la siguiente fase. Si responde que no, entonces dale nuevas ideas de negocio. Indicale que marque 1 si quiere continuar o que marque 2 si quiere nuevas ideas. si marca 2, muestrale más ideas de negocio."
                )          
            },
            {
                "role": "user",
                "content": f"{text}"
            }
        ],

        model="llama3-8b-8192",

        temperature=0.5,

        max_tokens=1000,

        top_p=1,

        stop=None,

        stream=False,
    )

    return chat_completion.choices[0].message.content

## Segunda fase 
import streamlit as st
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq()

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

def generar_nombres_negocio(sector, caracteristicas):
    prompt = f"Genera 10 posibles nombres para un negocio en el sector de {sector} que sea {caracteristicas}."
    nombres = llamar(prompt, "Eres un asistente creativo que ayuda a generar nombres de negocios.")
    nombres_list = nombres.strip().split('\n')
    nombres_list = [nombre.strip() for nombre in nombres_list if nombre.strip()]
    return nombres_list

def generar_propuesta_valor(producto, segmento):
    prompt = f"Genera tres propuestas de valor para un negocio que ofrece {producto} a {segmento}."
    propuestas = llamar(prompt, "Eres un experto en desarrollo de negocios.")
    propuestas_list = propuestas.strip().split('\n')
    propuestas_list = [propuesta.strip() for propuesta in propuestas_list if propuesta.strip()]
    return propuestas_list

# Inicializar el estado de sesión
if 'nombre' not in st.session_state:
    st.session_state.nombre = ''
if 'nombres' not in st.session_state:
    st.session_state.nombres = []
if 'propuestas' not in st.session_state:
    st.session_state.propuestas = []
if 'descripcion_ingles' not in st.session_state:
    st.session_state.descripcion_ingles = ''
if 'propuesta_mejorada' not in st.session_state:
    st.session_state.propuesta_mejorada = ''
if 'segmento_cliente' not in st.session_state:
    st.session_state.segmento_cliente = ''
if 'necesidades_problemas' not in st.session_state:
    st.session_state.necesidades_problemas = ''
if 'relaciones_clientes' not in st.session_state:
    st.session_state.relaciones_clientes = ''
if 'resumen_segmento' not in st.session_state:
    st.session_state.resumen_segmento = ''

st.title('Emprende tu idea')
st.session_state.nombre = st.text_input('¡Bienvenida a la Fase 2! ¿Cuál es tu nombre?', '')

if st.session_state.nombre:
    st.chat_message('assistant').write(f'¡Hola, {st.session_state.nombre}! Ahora que ya tienes claro tu propósito, es momento de transformar tu idea inicial en un concepto de negocio sólido y viable. Aquí trabajaremos en el desarrollo del nombre, logo, propuesta de valor y una parte del Canvas de Modelo de Negocio. ¡Vamos a ello! 🚀 Si estás preparada, escribe la palabra “lista” para empezar.')

    if st.text_input('Escribe "lista" para empezar:', '').lower() == 'lista':
        sector = st.text_input('Introduce el sector de tu negocio:')
        caracteristicas = st.text_input('Introduce una o más características deseadas (por ejemplo, innovador, atractivo, etc.):')

        if sector and caracteristicas:
            if not st.session_state.nombres:
                st.session_state.nombres = generar_nombres_negocio(sector, caracteristicas)
            st.chat_message('assistant').write(f'¡Gracias, {st.session_state.nombre}! Aquí tienes 10 posibles nombres para tu negocio en el sector de {sector}, que sea {caracteristicas}:')

            for nombre_negocio in st.session_state.nombres:
                st.write(f'{nombre_negocio}')

            nombre_elegido = st.text_input('Por favor, elige el nombre que más te guste y escríbelo. De lo contrario, si se te ocurre un nombre con el que te identificas aún más, por favor escríbelo para continuar con el siguiente paso:', '')

            if nombre_elegido:
                st.chat_message('assistant').write(f'Has elegido el nombre: {nombre_elegido}. ¡Vamos al siguiente paso!')

                st.chat_message('assistant').write(f'¡Perfecto, {nombre_elegido} es un gran nombre! Ahora que tenemos un nombre para tu negocio, es momento de crear el logo. Diseñar un logo es crucial porque será la cara visible de tu marca. Vamos a utilizar Canva y su herramienta MagicDesign para ayudarte a crear un logotipo profesional y atractivo. Para comenzar, necesito que describas brevemente el concepto de tu logo. Por ejemplo, si tu negocio es de comida saludable y sostenible, podrías decir "Logo para negocio de comida saludable sostenible". Por favor, escribe una breve descripción del concepto de tu logo.')

                concepto_logo = st.text_input('Descripción del concepto de tu logo:', '')

                if concepto_logo:
                    if not st.session_state.descripcion_ingles:
                        st.session_state.descripcion_ingles = llamar(f'Translate the following description to English: "{concepto_logo}"', "You are a translator. Translate the following text to English.")
                    st.chat_message('assistant').write(f'¡Gracias, {st.session_state.nombre}! 😄 Aquí tienes tu descripción de logo en inglés, que necesitarás para usar en Canva MagicDesign:\n\n{st.session_state.descripcion_ingles}\n\nPor favor, copia y pega esta descripción en MagicDesign de Canva (en la barra superior, pega el texto en inglés y presiona Enter o dale click a la lupa). Una vez realizado lo anterior, selecciona entre las plantillas disponibles la más alineada con tu logo y empieza a diseñar.\n\nAquí tienes el enlace para empezar:\n\n[Enlace Canva: https://www.canva.com/magic-home](https://www.canva.com/magic-home)\n\n¡Recuerda que tu logo debe reflejar los valores y la misión de tu negocio! Si necesitas inspiración, piensa en los colores y elementos gráficos que mejor representen tu marca. ¡Estoy aquí para cualquier duda o ayuda que necesites! 👀\n\nUna vez terminado tu logo, escribe “logo listo” para avanzar al siguiente paso.')

                    if st.text_input('Escribe "logo listo" para avanzar al siguiente paso:', '').lower() == 'logo listo':
                        st.chat_message('assistant').write('¡Excelente! Ahora que tienes tu logo, podemos avanzar al siguiente paso. 🚀')

                        st.chat_message('assistant').write('¡Genial, estamos avanzando! 😋 Ahora trabajemos en tu propuesta de valor. Por favor, introduce el producto o servicio que ofreces y el segmento de mercado al que te diriges. Ejemplo: "Zapatos artesanales, mujeres jóvenes urbanas".')

                        producto_segmento = st.text_input('Introduce tu producto o servicio y el segmento de mercado al que te diriges:', '')

                        if producto_segmento:
                            producto, segmento = producto_segmento.split(',')
                            producto = producto.strip()
                            segmento = segmento.strip()
                            if not st.session_state.propuestas:
                                st.session_state.propuestas = generar_propuesta_valor(producto, segmento)
                            st.chat_message('assistant').write(f'¡Gracias, {st.session_state.nombre}! Aquí tienes una propuesta de valor desarrollada para tu negocio que ofrece {producto} a {segmento}:')
                            for i, propuesta in enumerate(st.session_state.propuestas):
                                st.write(f'{propuesta}')

                            diferenciacion = st.text_input('Ahora, por favor describe cómo este negocio puede diferenciarse de sus competidores y proporcionar valor a sus clientes:', '')

                            if diferenciacion:
                                if not st.session_state.propuesta_mejorada:
                                    st.session_state.propuesta_mejorada = llamar(f'Mejora la siguiente propuesta de valor con la información adicional: "{diferenciacion}"', "Eres un experto en desarrollo de negocios.")
                                st.chat_message('assistant').write(f'Vamos a mejorar tu propuesta de valor con la información que me has dado. Aquí tienes tu propuesta de valor mejorada:\n\n{st.session_state.propuesta_mejorada}\n\nPor favor, revisa esta propuesta de valor que se ajusta a la información brindada y puedes usar para seguir desarrollando tu idea de negocio.')

                                respuesta = st.text_input('Cuando estés lista, escribe "lista" para continuar.')

                                if respuesta.lower() == 'lista':
                                    st.chat_message('assistant').write('¡Bien! Ahora que hemos completado la parte de la propuesta de valor, vamos a trabajar en el Segmento de Clientes.')

                                    st.chat_message('assistant').write('Voy a hacerte algunas preguntas para definir tu segmento de clientes.🤓 Trata de ser lo más específica posible con tus respuestas para que podamos crear un perfil claro de tus clientes ideales. Aquí van las preguntas:\n\n1. Describe los principales segmentos de clientes a los que te diriges. ¿Quiénes son tus clientes ideales y cuáles son sus características demográficas (edad, género, ubicación) y psicográficas (intereses, valores, estilo de vida)?\nEjemplo: "Mujeres de 25-40 años, interesadas en la moda sostenible, que viven en áreas urbanas."\n\n2. ¿Cuáles son las necesidades y problemas específicos de cada segmento de clientes que tu producto o servicio puede resolver?\nEjemplo: "Mis clientes necesitan ropa de moda que sea ecológica y asequible."\n\n3. ¿Qué tipo de relación tienes con cada segmento de clientes? ¿Cómo varían sus expectativas y comportamientos?\nEjemplo: "Mis clientes esperan una atención personalizada y rápida respuesta a sus consultas."')

                                    st.session_state.segmento_cliente = st.text_input('1. Describe los principales segmentos de clientes a los que te diriges (demográficas y psicográficas):', st.session_state.segmento_cliente)
                                    st.session_state.necesidades_problemas = st.text_input('2. ¿Cuáles son las necesidades y problemas específicos de cada segmento de clientes que tu producto o servicio puede resolver?', st.session_state.necesidades_problemas)
                                    st.session_state.relaciones_clientes = st.text_input('3. ¿Qué tipo de relación tienes con cada segmento de clientes? ¿Cómo varían sus expectativas y comportamientos?', st.session_state.relaciones_clientes)

                                    if st.session_state.segmento_cliente and st.session_state.necesidades_problemas and st.session_state.relaciones_clientes:
                                        if not st.session_state.resumen_segmento:
                                            resumen_segmento = llamar(
                                                f'Analiza la siguiente información y proporciona un resumen estructurado con los detalles del segmento de clientes pero extiende un poco el concepto para su entendimiento:\n\n1. Segmento de Clientes:\nDemográficas: {st.session_state.segmento_cliente}\nPsicográficas: {st.session_state.segmento_cliente}\n\n2. Necesidades y Problemas:\n{st.session_state.necesidades_problemas}\n\n3. Relaciones con los Clientes:\n{st.session_state.relaciones_clientes} al finalizar haces un resumen con la información del usuario para explicarle cual es su segmento de clientes',
                                                'Eres un experto en desarrollo de negocios. Analiza la información proporcionada y proporciona un resumen estructurado de los segmentos de clientes, necesidades y problemas, y relaciones con los clientes.'
                                            )
                                            st.session_state.resumen_segmento = resumen_segmento

                                        st.chat_message('assistant').write(f'¿Estamos trabajando bastante, verdad?🤯 Con la información que me has proporcionado, he creado un perfil detallado de tu segmento de clientes. Aquí tienes:\n\n{st.session_state.resumen_segmento}\n\nPor favor, revisa esta información de forma detallada y analiza para continuar con la creación de tu modelo de negocios.')

                                        if st.text_input('Escribe "lista" para continuar').lower() == 'lista':
                                            st.chat_message('assistant').write('¡Bien! Segmento de Clientes está listo. Recuerda, conocer a tus clientes es clave para ofrecerles productos y servicios que realmente valoren. ¡Esto te ayudará a crear una propuesta de valor única y relevante! Vamos a registrar tu Segmento de Clientes en la plantilla del Business Model Canvas. Aquí tienes el enlace para comenzar a llenar tu Canvas:\n\n[Enlace Canva: https://www.canva.com/design/DAGKqOD7Hcw/TnApmoBw8WAzy151RcS5Gw/edit?utm_content=DAGKqOD7Hcw&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton]\n\nRecuerda: Cada vez que termines una parte del Business Model Canvas, vas a pegarlo en la plantilla, para ir visualizando tu modelo de negocio. Te recordaremos el enlace al final de cada parte para que lo realices. 😉')
                                            st.chat_message('assistant').write('¡Genial! Ahora que hemos completado la parte del Segmento de Clientes, pasemos a la siguiente sección del Business Model Canvas: Canales.')

import streamlit as st
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq()

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

# Inicialización del estado de la sesión
if "messages" not in st.session_state:
    st.session_state.messages = []
if "first_message" not in st.session_state:
    st.session_state.first_message = True
if "asking_name" not in st.session_state:
    st.session_state.asking_name = True
if "asking_questions" not in st.session_state:
    st.session_state.asking_questions = False
if "business_ideas" not in st.session_state:
    st.session_state.business_ideas = []
if "generated_ideas" not in st.session_state:
    st.session_state.generated_ideas = []
if "chosen_idea" not in st.session_state:
    st.session_state.chosen_idea = ""
if "name" not in st.session_state:
    st.session_state.name = ""

# Función para mostrar mensajes
def show_messages():
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# Función para manejar la entrada del usuario
def handle_user_input(prompt):
    if st.session_state.name:
        st.session_state.name = prompt
        st.session_state.asking_name = False
        st.session_state.asking_questions = True
        welcome_message = f"¡Encantada de conocerte, {st.session_state.name}! Para comenzar en este primer módulo llamado Descubre tu Idea, me gustaría saber más sobre ti. Por favor, responde a estas preguntas en orden:"
        st.session_state.messages.append({"role": "assistant", "content": welcome_message})
        questions = """
        1. Cuenta una breve historia sobre ti misma (tus experiencias pasadas, formación, etc.).
        2. ¿Cuáles son tus habilidades principales? (por ejemplo, comunicación, diseño gráfico, tecnología).
        3. ¿En qué actividades has trabajado o tienes experiencia?
        4. ¿Cuáles son tus pasatiempos y qué disfrutas hacer en tu tiempo libre?
        5. ¿Cuáles son tus valores y motivaciones personales?
        6. Describe una situación en la que hayas tenido éxito o te hayas sentido muy orgullosa de tu trabajo.
        7. ¿Qué sueñas hacer?
        8. ¿Qué amas hacer?
        9. ¿Qué crees que el mundo necesita?
        10. Menciona una actividad por la que te podrían pagar, en la que harías lo que te gusta y seas buena haciendo. ¿Por qué crees que el mundo necesita eso de ti?
        """
        st.session_state.messages.append({"role": "assistant", "content": questions})
    elif st.session_state.asking_questions:
        st.session_state.business_ideas.append(prompt)
        if len(st.session_state.business_ideas) == 10:
            context = "Usa las siguientes respuestas del usuario para generar tres ideas de negocio que se alineen con las habilidades, intereses y valores del usuario:\n" + "\n".join(st.session_state.business_ideas)
            ideas_response = llamar("", context)
            st.session_state.generated_ideas = ideas_response.split('\n')  # Guardar las ideas generadas
            st.session_state.asking_questions = False
            st.session_state.messages.append({"role": "assistant", "content": f"¡Gracias por compartir tu historia, {st.session_state.name}! Me encantó conocerte. Basándome en tus respuestas, aquí tienes algunas ideas de negocio que podrían alinearse con tus pasiones y habilidades:\n\n" + ideas_response})
            st.session_state.messages.append({"role": "assistant", "content": "¿Cuál de estas ideas te gustaría desarrollar más a fondo? Por favor, escribe el nombre de la idea que elijas para continuar."})
        else:
            next_question = f"Pregunta {len(st.session_state.business_ideas) + 1}"
            st.session_state.messages.append({"role": "assistant", "content": next_question})
    else:
        if prompt.lower() == "sí" or prompt.lower() == "si":
            st.session_state.messages.append({"role": "assistant", "content": f"¡Felicidades por dar el primer paso hacia tu emprendimiento! Recuerda: 'El único límite a nuestros logros de mañana está en nuestras dudas de hoy'. ¡Vamos por ello!"})
            st.session_state.messages.append({"role": "assistant", "content": "Ya estás lista para el siguiente paso que es desarrollar tu idea."})
        elif prompt.lower() == "no":
            st.session_state.messages.append({"role": "assistant", "content": f"No te preocupes, {st.session_state.name}. A veces, encontrar la idea indicada lleva tiempo. ¡Sigue explorando tus opciones! Escríbeme una nueva idea de negocio que tengas en mente, y estaremos aquí para apoyarte en cada paso del camino."})
            st.session_state.messages.append({"role": "assistant", "content": "¿Qué deseas hacer? ¿Escoger otra idea de las tres que te presenté anteriormente o que genere nuevas ideas teniendo en cuenta la misma información que me brindaste? Para la primera opción escribe el número 1 y para la segunda escribe el número 2 para continuar."})
        elif prompt == "1":
            ideas_response = "\n".join(st.session_state.generated_ideas)  # Mostrar las ideas generadas nuevamente
            st.session_state.messages.append({"role": "assistant", "content": f"¡Claro que sí, {st.session_state.name}! Aquí están las ideas generadas nuevamente:\n\n" + ideas_response})
            st.session_state.messages.append({"role": "assistant", "content": "Escribe el nombre de la idea que te llama más la atención para continuar."})
        elif prompt == "2":
            context = "Genera nuevas ideas de negocio basadas en las siguientes respuestas del usuario:\n" + "\n".join(st.session_state.business_ideas)
            new_ideas_response = llamar("", context)
            st.session_state.generated_ideas = new_ideas_response.split('\n')  # Guardar las nuevas ideas generadas
            st.session_state.messages.append({"role": "assistant", "content": new_ideas_response})
            st.session_state.messages.append({"role": "assistant", "content": "Escribe el nombre de la idea que te llama más la atención para continuar."})
        else:
            st.session_state.chosen_idea = prompt
            st.session_state.messages.append({"role": "assistant", "content": f"¡Excelente elección, {st.session_state.name}! Has decidido trabajar en {st.session_state.chosen_idea}. ¿Estás lista para continuar con esta idea de negocio? Escribe 'sí' para confirmar o 'no' para repetir el proceso de generación de ideas."})

# Interfaz de usuario de Streamlit
st.image("logo.png", use_column_width=200)

st.title("Emprende tu idea")

# Mensaje de bienvenida
st.session_state.name = st.text_input({"role": "assistant", "content": "¡Hola! Bienvenida a la fase de descrube tu propósito, para comenzar escribe tu nombre:"})

# Mostrar los mensajes anteriores
show_messages()
