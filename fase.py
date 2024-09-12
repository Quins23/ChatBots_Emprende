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

# Configuración de la aplicación
st.set_page_config(page_title="Mi Aplicación con Pestañas", layout="wide")

# Función para la primera pestaña
def fase1():
    
    if 'nombre' not in st.session_state:
        st.session_state.nombre_fase1 = ''
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
    st.session_state.nombre_fase1 = st.text_input('Antes de iniciar me gustaría preguntar ¿Cuál es tu nombre?, con esto ya daremos el primer paso para empezar', key='inicio_fase1')

    if st.session_state.nombre_fase1:
        st.chat_message('assistant').write(f'¡Hola, {st.session_state.nombre_fase1}! Aquí te vamos a ayudar a explorar tus pasiones, habilidades y valores para identificar tu propósito personal y profesional para finalmente saber que ideas geniales pueden adaptarse a ti... ¡Vamos a ello! 🚀 Si estás lista, escribe la palabra “lista” para empezar.')
        
        if st.text_input('Escribe "lista" para empezar:', key='start_input').lower() == 'lista':
            st.chat_message('assistant').write(f'Perfecto {st.session_state.nombre_fase1}, para continuar me gustaría saber más sobre ti. Por favor, responde a estas preguntas en orden:')
            
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
                                                    st.chat_message('assistant').write(f'Excelente {st.session_state.nombre_fase1} ya respondiste todas las preguntas, ahora avancemos...')
                                                    
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
                                                            st.chat_message('assistant').write(f'Eso es {st.session_state.nombre_fase1} has elegido la idea:\n\n{st.session_state.nombre_negocio}\n\n¿Estás lista para continuar?')
                                                            
                                                            if st.text_input('Escribe "lista" para continuar:', key='last_input').lower() == 'lista':
                                                                st.chat_message('assistant').write(f'¡Felicidades por dar el primer paso hacia tu emprendimiento! Recuerda: "El único límite a nuestros logros de mañana está en nuestras dudas de hoy"')

# Función para la segunda pestaña
def fase2():
    
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
    if 'canales_preferidos' not in st.session_state:
        st.session_state.canales_preferidos = ''
    if 'uso_canales' not in st.session_state:
        st.session_state.uso_canales = ''
    if 'canales_rentables' not in st.session_state:
        st.session_state.canales_rentables = ''
    if 'resumen_canales' not in st.session_state:
        st.session_state.resumen_canales = ''
    if 'relaciones_cliente' not in st.session_state:
        st.session_state.relaciones_cliente = ''
    if 'estrategias_fidelizacion' not in st.session_state:
        st.session_state.estrategias_fidelizacion = ''
    if 'programas_servicios' not in st.session_state:
        st.session_state.programas_servicios = ''
    if 'resumen_relaciones' not in st.session_state:
        st.session_state.resumen_relaciones = ''
    if 'recursos_tipos' not in st.session_state:
        st.session_state.recursos_tipos = ''
    if 'recursos_clave' not in st.session_state:
        st.session_state.recursos_clave = ''
    if 'recursos_necesarios' not in st.session_state:
        st.session_state.recursos_necesarios = ''
    if 'resumen_recursos' not in st.session_state:
        st.session_state.resumen_recursos = ''
    if 'actividades_importantes' not in st.session_state:
        st.session_state.actividades_importantes = ''
    if 'actividades_esenciales' not in st.session_state:
        st.session_state.actividades_esenciales = ''
    if 'actividades_principales' not in st.session_state:
        st.session_state.actividades_principales = ''
    if 'resumen_actividades' not in st.session_state:
        st.session_state.resumen_actividades = ''
    if 'socios_principales' not in st.session_state:
        st.session_state.socios_principales = ''
    if 'socios_clave' not in st.session_state:
        st.session_state.socios_clave = ''
    if 'socios_actividades' not in st.session_state:
        st.session_state.socios_actividades = ''
    if 'resumen_socios' not in st.session_state:
        st.session_state.resumen_socios = ''

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
    st.sidebar.write(f'Desarrolla tu idea')
    ###

    st.title('¡Bienvenida a desarrolla tu idea!')

    st.session_state.nombre = st.text_input('Antes de iniciar me gustaría preguntar ¿Cuál es tu nombre?, con esto ya daremos el primer paso para empezar', key='inicio_fase2')

    if st.session_state.nombre:
        st.chat_message('assistant').write(f'¡Hola, {st.session_state.nombre}! Es momento de transformar tu idea inicial en un concepto de negocio sólido y viable. Aquí trabajaremos en el desarrollo del nombre, logo, propuesta de valor y una parte del Canvas de Modelo de Negocio. ¡Vamos a ello! 🚀 Si estás preparada, escribe la palabra “lista” para empezar.')

        if st.text_input('Escribe "lista" para empezar:', key='start_input').lower() == 'lista':
            sector = st.text_input('Introduce el sector de tu negocio:', key='sector_input')
            caracteristicas = st.text_input('Introduce una o más características deseadas (por ejemplo, innovador, atractivo, etc.):', key='caracteristicas_input')

            if sector and caracteristicas:
                if not st.session_state.nombres:
                    st.session_state.nombres = generar_nombres_negocio(sector, caracteristicas)
                st.chat_message('assistant').write(f'¡Gracias, {st.session_state.nombre}! Aquí tienes 10 posibles nombres para tu negocio en el sector de {sector}, que sea {caracteristicas}:')

                for nombre_negocio in st.session_state.nombres:
                    st.write(f'{nombre_negocio}')

                nombre_elegido = st.text_input('Por favor, elige el nombre que más te guste y escríbelo. De lo contrario, si se te ocurre un nombre con el que te identificas aún más, por favor escríbelo para continuar con el siguiente paso:', key='nombre_elegido_input')

                if nombre_elegido:
                    st.chat_message('assistant').write(f'Has elegido el nombre: {nombre_elegido}. ¡Vamos al siguiente paso!')

                    st.chat_message('assistant').write(f'¡Perfecto, {nombre_elegido} es un gran nombre! Ahora que tenemos un nombre para tu negocio, es momento de crear el logo. Diseñar un logo es crucial porque será la cara visible de tu marca. Vamos a utilizar Canva y su herramienta MagicDesign para ayudarte a crear un logotipo profesional y atractivo. Para comenzar, necesito que describas brevemente el concepto de tu logo. Por ejemplo, si tu negocio es de comida saludable y sostenible, podrías decir "Logo para negocio de comida saludable sostenible". Por favor, escribe una breve descripción del concepto de tu logo.')

                    concepto_logo = st.text_input('Descripción del concepto de tu logo:', key='concepto_logo_input')

                    if concepto_logo:
                        if not st.session_state.descripcion_ingles:
                            st.session_state.descripcion_ingles = llamar(f'Translate the following description to English: "{concepto_logo}"', "You are a translator. Translate the following text to English.")
                        st.chat_message('assistant').write(f'¡Gracias, {st.session_state.nombre}! 😄 Aquí tienes tu descripción de logo en inglés, que necesitarás para usar en Canva MagicDesign:\n\n{st.session_state.descripcion_ingles}\n\nPor favor, copia y pega esta descripción en MagicDesign de Canva (en la barra superior, pega el texto en inglés y presiona Enter o dale click a la lupa). Una vez realizado lo anterior, selecciona entre las plantillas disponibles la más alineada con tu logo y empieza a diseñar.\n\nAquí tienes el enlace para empezar:\n\n[Enlace Canva: https://www.canva.com/magic-home](https://www.canva.com/magic-home)\n\n¡Recuerda que tu logo debe reflejar los valores y la misión de tu negocio! Si necesitas inspiración, piensa en los colores y elementos gráficos que mejor representen tu marca. ¡Estoy aquí para cualquier duda o ayuda que necesites! 👀\n\nUna vez terminado tu logo, escribe “logo listo” para avanzar al siguiente paso.')

                        if st.text_input('Escribe "logo listo" para avanzar al siguiente paso:', key='logo_listo_input').lower() == 'logo listo':
                            st.chat_message('assistant').write('¡Excelente! Ahora que tienes tu logo, podemos avanzar al siguiente paso. 🚀')

                            st.chat_message('assistant').write('¡Genial, estamos avanzando! 😋 Ahora trabajemos en tu propuesta de valor. Por favor, introduce el producto o servicio que ofreces y el segmento de mercado al que te diriges. Ejemplo: "Zapatos artesanales, mujeres jóvenes urbanas".')

                            producto_segmento = st.text_input('Introduce tu producto o servicio y el segmento de mercado al que te diriges:', key='producto_segmento_input')

                            if producto_segmento:
                                producto, segmento = producto_segmento.split(',')
                                producto = producto.strip()
                                segmento = segmento.strip()
                                if not st.session_state.propuestas:
                                    st.session_state.propuestas = generar_propuesta_valor(producto, segmento)
                                st.chat_message('assistant').write(f'¡Gracias, {st.session_state.nombre}! Aquí tienes una propuesta de valor desarrollada para tu negocio que ofrece {producto} a {segmento}:')
                                for i, propuesta in enumerate(st.session_state.propuestas):
                                    st.write(f'{propuesta}')

                                diferenciacion = st.text_input('Ahora, por favor describe cómo este negocio puede diferenciarse de sus competidores y proporcionar valor a sus clientes:', key='diferenciacion_input')

                                if diferenciacion:
                                    if not st.session_state.propuesta_mejorada:
                                        st.session_state.propuesta_mejorada = llamar(f'Mejora la siguiente propuesta de valor con la información adicional: "{diferenciacion}"', "Eres un experto en desarrollo de negocios.")
                                    st.chat_message('assistant').write(f'Vamos a mejorar tu propuesta de valor con la información que me has dado. Aquí tienes tu propuesta de valor mejorada:\n\n{st.session_state.propuesta_mejorada}\n\nPor favor, revisa esta propuesta de valor que se ajusta a la información brindada y puedes usar para seguir desarrollando tu idea de negocio.')

                                    respuesta = st.text_input('Cuando estés lista, escribe "lista" para continuar.', key='propuesta_lista_input')

                                    if respuesta.lower() == 'lista':
                                        st.chat_message('assistant').write('¡Bien! Ahora que hemos completado la parte de la propuesta de valor, vamos a trabajar en el Segmento de Clientes.')

                                        st.chat_message('assistant').write('Voy a hacerte algunas preguntas para definir tu segmento de clientes. Por favor, responde con la mayor claridad posible para obtener el mejor resultado.\n\n1. Describe los principales segmentos de clientes a los que te diriges (demográficas y psicográficas):\nEjemplo: "Mujeres entre 25 y 40 años, interesadas en moda sostenible y ecológica."\n\n2. ¿Cuáles son las necesidades y problemas específicos de cada segmento de clientes que tu producto o servicio puede resolver?\nEjemplo: "Mis clientes necesitan ropa de moda que sea ecológica y asequible."\n\n3. ¿Qué tipo de relación tienes con cada segmento de clientes? ¿Cómo varían sus expectativas y comportamientos?\nEjemplo: "Mis clientes esperan una atención personalizada y rápida respuesta a sus consultas."')

                                        st.session_state.segmento_cliente = st.text_input('1. Describe los principales segmentos de clientes a los que te diriges (demográficas y psicográficas):', st.session_state.segmento_cliente, key='segmento_cliente_input')
                                        st.session_state.necesidades_problemas = st.text_input('2. ¿Cuáles son las necesidades y problemas específicos de cada segmento de clientes que tu producto o servicio puede resolver?', st.session_state.necesidades_problemas, key='necesidades_problemas_input')
                                        st.session_state.relaciones_clientes = st.text_input('3. ¿Qué tipo de relación tienes con cada segmento de clientes? ¿Cómo varían sus expectativas y comportamientos?', st.session_state.relaciones_clientes, key='relaciones_clientes_input')

                                        if st.session_state.segmento_cliente and st.session_state.necesidades_problemas and st.session_state.relaciones_clientes:
                                            if not st.session_state.resumen_segmento:
                                                resumen_segmento = llamar(
                                                    f'Analiza la siguiente información y proporciona un resumen estructurado con los detalles del segmento de clientes pero extiende un poco el concepto para su entendimiento:\n\n1. Segmento de Clientes:\nDemográficas: {st.session_state.segmento_cliente}\nPsicográficas: {st.session_state.segmento_cliente}\n\n2. Necesidades y Problemas:\n{st.session_state.necesidades_problemas}\n\n3. Relaciones con los Clientes:\n{st.session_state.relaciones_clientes} al finalizar haces un resumen con la información del usuario para explicarle cual es su segmento de clientes',
                                                    'Eres un experto en desarrollo de negocios. Analiza la información proporcionada y proporciona un resumen estructurado de los segmentos de clientes, necesidades y problemas, y relaciones con los clientes.'
                                                )
                                                st.session_state.resumen_segmento = resumen_segmento

                                            st.chat_message('assistant').write(f'¿Estamos trabajando bastante, verdad?🤯 Con la información que me has proporcionado, he creado un perfil detallado de tu segmento de clientes. Aquí tienes:\n\n{st.session_state.resumen_segmento}\n\nPor favor, revisa esta información de forma detallada y analiza para continuar con la creación de tu modelo de negocios.')

                                            if st.text_input('Escribe "lista" para continuar', key='segmento_canva').lower() == 'lista':
                                                st.chat_message('assistant').write('¡Bien! Segmento de Clientes está listo. Recuerda, conocer a tus clientes es clave para ofrecerles productos y servicios que realmente valoren. ¡Esto te ayudará a crear una propuesta de valor única y relevante! Vamos a registrar tu Segmento de Clientes en la plantilla del Business Model Canvas. Aquí tienes el enlace para comenzar a llenar tu Canvas:\n\n[Enlace Canva: https://www.canva.com/design/DAGKqOD7Hcw/yENnVLwX2aMJvHFK69zhkA/view?utm_content=DAGKqOD7Hcw&utm_campaign=designshare&utm_medium=link&utm_source=publishsharelink&mode=preview]\n\nRecuerda: Cada vez que termines una parte del Business Model Canvas, vas a pegarlo en la plantilla, para ir visualizando tu modelo de negocio. Te recordaremos el enlace al final de cada parte para que lo realices. 😉')

                                                st.chat_message('assistant').write('¡Genial! Ahora que hemos completado la parte del Segmento de Clientes, pasemos a la siguiente sección del Business Model Canvas: Canales.')

                                                st.chat_message('assistant').write(f'¡Perfecto, {st.session_state.nombre}! Ahora vamos a trabajar en los canales a través de los cuales tu negocio se comunicará y llegará a tus clientes. Es importante definir claramente estos canales para asegurar que tu propuesta de valor llegue de la mejor manera posible a tus clientes ideales. Escribe "lista" para continuar. 😶')

                                                if st.text_input('Escribe "lista" para continuar:', key='canales_start_input').lower() == 'lista':
                                                    st.chat_message('assistant').write('Vamos a definir tus canales de comunicación y distribución. Intenta ser lo más específica posible con tus respuestas para que podamos crear una estrategia clara y efectiva. Aquí van las preguntas:\n\n1. Identifica los canales a través de los cuales tus clientes prefieren recibir información sobre tu producto o servicio. ¿Prefieren canales online (como redes sociales, correos electrónicos, sitios web) o offline (como tiendas físicas, ferias, eventos)? ¿O una combinación de ambos?\n\n- Ejemplo: "Mis clientes prefieren enterarse de mis productos a través de WhatsApp, Instagram y Facebook."\n\n2. Describe cómo utilizas cada canal en las diferentes etapas del ciclo de compra: conocimiento (cómo los clientes descubren tu negocio), evaluación (cómo comparan tu oferta con la competencia), compra (cómo adquieren tu producto o servicio), entrega (cómo reciben el producto o servicio), y post-venta (cómo se les brinda soporte y seguimiento).\n\n- Ejemplo: "Utilizo Instagram para dar a conocer mi negocio, mi cuenta de WhatsApp Business para que los clientes evalúen mis productos mediante el chat, el chat de WhatsApp Business para la compra, y el servicio de mensajería Coordinadora para la entrega."\n\n3. ¿Qué canales son más rentables y efectivos para llegar a tus clientes? ¿Cómo puedes optimizar el uso de estos canales para mejorar la experiencia del cliente?\n\n- Ejemplo: "Instagram y WhatsApp Business son más rentables y efectivos para mí. Puedo mejorar mi presencia en Instagram y personalizar los mensajes que le envío a mis clientes por WhatsApp Business para una mejor experiencia del cliente."\n\nPor favor, responde a cada una de estas preguntas en orden.')

                                                    st.session_state.canales_preferidos = st.text_input('1. Identifica los canales preferidos:', st.session_state.canales_preferidos, key='canales_preferidos_input')
                                                    st.session_state.uso_canales = st.text_input('2. Describe el uso de los canales en las diferentes etapas del ciclo de compra:', st.session_state.uso_canales, key='uso_canales_input')
                                                    st.session_state.canales_rentables = st.text_input('3. ¿Qué canales son más rentables y efectivos para llegar a tus clientes?', st.session_state.canales_rentables, key='canales_rentables_input')

                                                    if st.session_state.canales_preferidos and st.session_state.uso_canales and st.session_state.canales_rentables:
                                                        if not st.session_state.resumen_canales:
                                                            resumen_canales = llamar(
                                                                f'Analiza la siguiente información y proporciona un resumen estructurado con los detalles de los canales propuestos:\n\n1. Canales Preferidos:\n{st.session_state.canales_preferidos}\n\n2. Uso de Canales en el Ciclo de Compra:\n{st.session_state.uso_canales}\n\n3. Rentabilidad y Efectividad de los Canales:\n{st.session_state.canales_rentables}',
                                                                'Eres un experto en desarrollo de negocios y desarrollo de modelos de negocio. Analiza la información proporcionada y proporciona un resumen estructurado de los canales propuestos.'
                                                            )
                                                            st.session_state.resumen_canales = resumen_canales

                                                        st.chat_message('assistant').write(f'¡Perfecto! Aquí tienes un resumen de los canales propuestos para tu negocio:\n\n{st.session_state.resumen_canales}\n\nPor favor, revisa esta información y asegúrate de que refleja los canales más efectivos para llegar a tus clientes y entregarles tu propuesta de valor.')

                                                        if st.text_input('Escribe "lista" para continuar:', key='canales_canva').lower() == 'lista':
                                                            st.chat_message('assistant').write('¡Bien hecho! Ahora que hemos definido los canales, puedes registrarlos en la plantilla del Business Model Canvas. Aquí tienes el enlace nuevamente:\n\n[Enlace Canva: https://www.canva.com/design/DAGKqOD7Hcw/yENnVLwX2aMJvHFK69zhkA/view?utm_content=DAGKqOD7Hcw&utm_campaign=designshare&utm_medium=link&utm_source=publishsharelink&mode=preview]\n\nVamos a continuar con la siguiente sección del Business Model Canvas: Relaciones con los Clientes.')
                                                            
                                                            # Sección de Relaciones con los Clientes
                                                            st.chat_message('assistant').write('¡Hora de descansar! Cuando termines de agregar esta sección a tu canva, tomemos un break. Recuerda que para trabajar con grandes niveles de concentración durante periodos prolongados necesitamos periodos cortos de relajación de entre 5 y 10 minutos (técnica Pomodoro). Toma 10 minutos para estirar tus articulaciones, beber o comer algo y volver con toda la energía. Una vez lista, escribe "lista" para continuar.')

                                                            if st.text_input('Escribe "lista" para continuar:', key='descanso_input').lower() == 'lista':
                                                                st.chat_message('assistant').write('En este momento vamos a enfocarnos en las relaciones que establecerás con tus clientes. Definir claramente estas relaciones te ayudará a construir una base de clientes leales y satisfechos. ¡Vamos a ello! 😏')

                                                                st.chat_message('assistant').write('Voy a hacerte algunas preguntas para definir las relaciones con tus clientes. Intenta ser lo más específica posible con tus respuestas para que podamos crear una estrategia clara y efectiva. Estas son las preguntas:\n\n1. ¿Qué tipo de relación espera cada segmento de clientes que establezcas con ellos? ¿Es una relación personal (como atención personalizada, consultoría), automatizada (como emails automáticos, chatbots), comunitaria (como grupos de WhatsApp o comunidades, grupos de redes sociales), u otra?\n\n- Ejemplo: "Mis clientes esperan una relación personal donde reciban atención individualizada y recomendaciones personalizadas."\n\n2. ¿Cómo mantienes y fortaleces la relación con tus clientes? ¿Qué estrategias utilizas para fidelizar a tus clientes y aumentar su satisfacción?\n\n- Ejemplo: "Mantengo la relación con mis clientes a través de mensajes por WhatsApp semanales, seguimiento personalizado y promociones exclusivas."\n\n3. Describe cualquier programa de referidos, soporte al cliente, o servicios adicionales que ofrezcas para mantener una relación sólida con tus clientes.\n\n- Ejemplo: "Ofrezco un programa de referidos donde los clientes obtienen descuentos por cada compra que realiza un referido que traen, y proporciono soporte 24/7 a través de un chat en vivo."')

                                                                st.session_state.relaciones_cliente = st.text_input('1. ¿Qué tipo de relación espera cada segmento de clientes que establezcas con ellos?', st.session_state.relaciones_cliente, key='relaciones_clientes_entrada')
                                                                st.session_state.estrategias_fidelizacion = st.text_input('2. ¿Cómo mantienes y fortaleces la relación con tus clientes? ¿Qué estrategias utilizas para fidelizar a tus clientes y aumentar su satisfacción?', st.session_state.estrategias_fidelizacion, key='estrategias_fidelizacion_entrada')
                                                                st.session_state.programas_servicios = st.text_input('3. Describe cualquier programa de referidos, soporte al cliente, o servicios adicionales que ofrezcas para mantener una relación sólida con tus clientes.', st.session_state.programas_servicios, key='programas_servicios_entrada')

                                                                if st.session_state.relaciones_cliente and st.session_state.estrategias_fidelizacion and st.session_state.programas_servicios:
                                                                    if not st.session_state.resumen_relaciones:
                                                                        resumen_relaciones = llamar(
                                                                            f'Analiza la siguiente información y proporciona un resumen estructurado sobre las relaciones con los clientes:\n\n1. Tipo de relación esperada por el cliente:\n{st.session_state.relaciones_cliente}\n\n2. Estrategias para mantener y fortalecer la relación con el cliente:\n{st.session_state.estrategias_fidelizacion}\n\n3. Programas de lealtad, soporte al cliente y servicios adicionales:\n{st.session_state.programas_servicios}',
                                                                            'Eres un experto en desarrollo de negocios y desarrollo de modelos de negocio. Analiza la información proporcionada y realiza un resumen detallado sobre la relación con los clientes.'
                                                                        )
                                                                        st.session_state.resumen_relaciones = resumen_relaciones

                                                                    st.chat_message('assistant').write(f'¡Graciaaas, {st.session_state.nombre}! 😊 Con la información que me has proporcionado, he creado un perfil detallado de tus relaciones con los clientes. Aquí lo tienes:\n\n{st.session_state.resumen_relaciones}\n\n')

                                                                    st.chat_message('assistant').write('Por favor, revisa esta información de forma detallada. Una vez que estés preparada, continuaremos con el Business Model Canvas. Escribe "lista" para continuar.')

                                                                    if st.text_input('Escribe "lista" para continuar:', key='relaciones_canva').lower() == 'lista':
                                                                        st.chat_message('assistant').write('Aquí tienes el enlace para registrar las Relaciones con los Clientes en tu Canvas:\n\n[Enlace Canva: https://www.canva.com/design/DAGKqOD7Hcw/yENnVLwX2aMJvHFK69zhkA/view?utm_content=DAGKqOD7Hcw&utm_campaign=designshare&utm_medium=link&utm_source=publishsharelink&mode=preview]\n\n¡Otro paso dado! Felicidades, avanzas muy bien. Ahora vamos a pasar a los recursos claves de tu proyecto.')

                                                                        # Sección de recursos clave
                                                                        st.chat_message('assistant').write(f'¡Eres increíble, {st.session_state.nombre}! 🥳 Ahora vamos a identificar los Recursos Clave que necesitarás para que tu negocio funcione de manera efectiva. Estos recursos son esenciales para crear, entregar y mantener tu propuesta de valor. ¡Escribe "lista" para empezar!')
                                                                        
                                                                        if st.text_input('Escribe "lista" para continuar:', key='recursos_preguntas').lower() == 'lista':
                                                                            st.chat_message('assistant').write('Te haré las siguientes preguntas para definir los recursos clave de tu negocio. 🔑 Intenta ser lo más específica posible con tus respuestas para que podamos identificar con precisión lo que necesitas. Aquí van las preguntas:\n\n1. ¿Cuáles son los recursos físicos, intelectuales, humanos y financieros que son cruciales para la operación de tu negocio? Piensa en equipos, propiedades, patentes, derechos de autor, empleados clave, y financiación necesaria.- Ejemplo: "Necesito un local comercial, equipo de cocina industrial, derechos de una patente, un equipo de marketing y financiación inicial."\n\n2. ¿Qué activos son indispensables para la creación, entrega y mantenimiento de tu propuesta de valor? Estos pueden incluir productos físicos, tecnología, datos, y relaciones con proveedores. - Ejemplo: "Para mi negocio, los ingredientes orgánicos de alta calidad, una plataforma de ecommerce robusta, y datos de clientes son esenciales."\n\n3. ¿Qué recursos son necesarios para llegar a tus segmentos de clientes y mantener relaciones con ellos? Considera herramientas de comunicación, plataformas de CRM, y contenido y/o materiales promocionales. - Ejemplo: "Necesito una cuenta de negocios en Instagram, una cuenta de WhatsApp Business para gestionar las relaciones con los clientes, y contenido promocional para como historias de WhatsApp e Instagram."\n\nPor favor, responde a cada una de estas preguntas en orden.')
                                                                    
                                                                            st.session_state.recursos_tipos = st.text_input('1. ¿Cuáles son los recursos físicos, intelectuales, humanos y financieros que son cruciales para la operación de tu negocio?', st.session_state.recursos_tipos, key='recursos_tipos_entrada')
                                                                            st.session_state.recursos_clave = st.text_input('2. ¿Qué activos son indispensables para la creación, entrega y mantenimiento de tu propuesta de valor?', st.session_state.recursos_clave, key='recursos_clave_entrada')
                                                                            st.session_state.recursos_necesarios = st.text_input('3. ¿Qué recursos son necesarios para llegar a tus segmentos de clientes y mantener relaciones con ellos? ', st.session_state.recursos_necesarios, key='recursos_necesarios_entrada')

                                                                            if st.session_state.recursos_tipos and st.session_state.recursos_clave and st.session_state.recursos_necesarios:
                                                                                if not st.session_state.resumen_recursos:
                                                                                    resumen_recursos = llamar(
                                                                                        f'Analiza la siguiente información y proporciona un resumen estructurado sobre los recursos claves:\n\n1. Recursos Físicos, Intelectuales, Humanos y Financieros:\n{st.session_state.recursos_tipos}\n\n2. Activos Indispensables para la Creación, Entrega y Mantenimiento de la Propuesta de Valor:\n{st.session_state.recursos_clave}\n\n3. Recursos Necesarios para Llegar a los Segmentos de Clientes y Mantener Relaciones:\n{st.session_state.recursos_necesarios}',
                                                                                        'Eres un experto en desarrollo de negocios y desarrollo de modelos de negocio. Analiza la información proporcionada y realiza un resumen detallado sobre los recursos claves del proyecto con base a lo que escribió el usuario'
                                                                                    )
                                                                                    st.session_state.resumen_recursos = resumen_recursos

                                                                                st.chat_message('assistant').write(f'¡Excelente, {st.session_state.nombre}! 😊 Con esta información, he podido identificar los recursos claves de tu idea de negocio. Aquí los tienes:\n\n{st.session_state.resumen_recursos}\n\n')

                                                                                st.chat_message('assistant').write('Por favor, revisa esta información de forma detallada. Una vez que estés preparada, continuaremos con otras partes del Business Model Canvas. Escribe "lista" para continuar.')

                                                                                if st.text_input('Escribe "lista" para continuar:', key='recursos_canva').lower() == 'lista':
                                                                                    st.chat_message('assistant').write('Aquí tienes el enlace para registrar los recursos claves en tu Canvas:\n\n[Enlace Canva: https://www.canva.com/design/DAGKqOD7Hcw/yENnVLwX2aMJvHFK69zhkA/view?utm_content=DAGKqOD7Hcw&utm_campaign=designshare&utm_medium=link&utm_source=publishsharelink&mode=preview]\n\n¡Vas bien! Felicidades, sigue así. Ahora vamos a pasar a las actividades clave de tu proyecto.')
                                                                                    
                                                                                    # Sección de actividades clave
                                                                                    st.chat_message('assistant').write(f'Tranquila {st.session_state.nombre}, estamos por terminar este apartado. 😪 Ahora vamos a identificar las Actividades Clave que tu negocio debe realizar para funcionar correctamente y cumplir con tu propuesta de valor. Estas actividades son esenciales para asegurar que tu negocio opere de manera eficiente. ¡Escriba "lista" para empezar!')
                                                                                    
                                                                                    if st.text_input('Escribe "lista" para continuar:', key='actividades_preguntas').lower() == 'lista':
                                                                                        st.chat_message('assistant').write('Estás son las últimas preguntas de esta fase 2 para definir las actividades clave de tu negocio (sí, ¡al fin!). 😆 Sé lo más específica posible con tus respuestas para ayudarte a identificar con precisión lo que necesitas hacer. Aquí las preguntas:\n\n1. ¿Cuáles son las actividades más importantes que tu negocio debe realizar para crear y entregar su propuesta de valor? Piensa en actividades de producción, diseño, marketing, ventas, y logística. - Ejemplo: "Necesito desarrollar recetas innovadoras, gestionar la producción de alimentos, y planificar campañas de marketing en redes sociales como Instagram y Facebook."\n\n2. ¿Qué procesos son esenciales para operar tu negocio, desde la producción hasta el marketing y ventas? Considera los procesos diarios, semanales y mensuales que mantienen tu negocio en funcionamiento. - Ejemplo: "Debo asegurarme de la calidad de los productos, realizar inventarios semanales, y coordinar la distribución a los puntos de venta."\n\n3. ¿Qué actividades principales te permiten mantener y fortalecer tus relaciones con los clientes? Incluye actividades de servicio al cliente, gestión de feedback, y programas de fidelización. - Ejemplo: "Es crucial responder rápidamente a las consultas de los clientes por medio de WhatsApp, realizar encuestas de satisfacción usando Google Forms, y ofrecer descuentos exclusivos a los clientes leales."\n\nPor favor, responde a cada una de estas preguntas en orden.')
                                                                                
                                                                                        st.session_state.actividades_importantes = st.text_input('1. ¿Cuáles son las actividades más importantes que tu negocio debe realizar para crear y entregar su propuesta de valor?', st.session_state.actividades_importantes, key='actividades_importantes_entrada')
                                                                                        st.session_state.actividades_esenciales = st.text_input('2. ¿Qué procesos son esenciales para operar tu negocio, desde la producción hasta el marketing y ventas?', st.session_state.actividades_esenciales, key='actividades_esenciales_entrada')
                                                                                        st.session_state.actividades_principales = st.text_input('3. ¿Qué actividades principales te permiten mantener y fortalecer tus relaciones con los clientes?', st.session_state.actividades_principales, key='actividades_principales_entrada')

                                                                                        if st.session_state.actividades_importantes and st.session_state.actividades_esenciales and st.session_state.actividades_principales:
                                                                                            if not st.session_state.resumen_actividades:
                                                                                                resumen_actividades = llamar(
                                                                                                    f'Analiza la siguiente información y proporciona un resumen estructurado sobre las actividades claves:\n\n1. Actividades Importantes para Crear y Entregar la Propuesta de Valor:\n{st.session_state.actividades_importantes}\n\n2. Procesos Esenciales para Operar el Negocio:\n{st.session_state.actividades_esenciales}\n\n3. Actividades para Mantener y Fortalecer Relaciones con los Clientes:\n{st.session_state.actividades_principales}',
                                                                                                    'Eres un experto en desarrollo de negocios y desarrollo de modelos de negocio. Analiza la información proporcionada y realiza un resumen detallado sobre las actividades claves del proyecto con base a lo que escribió el usuario'
                                                                                                )
                                                                                                st.session_state.resumen_actividades = resumen_actividades

                                                                                            st.chat_message('assistant').write(f'¡Vas bien {st.session_state.nombre}! 🫡 Con esta información, he podido identificar las actividades claves de tu idea de negocio. Aquí las tienes:\n\n{st.session_state.resumen_actividades}\n\n')

                                                                                            st.chat_message('assistant').write('Por favor, revisa esta información de forma detallada. Una vez que estés preparada, continuaremos con otras partes del Business Model Canvas. Escribe "lista" para continuar.')

                                                                                            if st.text_input('Escribe "lista" para continuar:', key='actividades_canva').lower() == 'lista':
                                                                                                st.chat_message('assistant').write('Aquí tienes el enlace para registrar las actividades claves en tu Canvas:\n\n[Enlace Canva: https://www.canva.com/design/DAGKqOD7Hcw/yENnVLwX2aMJvHFK69zhkA/view?utm_content=DAGKqOD7Hcw&utm_campaign=designshare&utm_medium=link&utm_source=publishsharelink&mode=preview]\n\n¡Vas bien! Felicidades, sigue así. Ahora vamos a pasar a los socios clave de tu proyecto.')
                                                                                            
                                                                                                # Sección de socios clave
                                                                                                st.chat_message('assistant').write(f'¡Excelente trabajo {st.session_state.nombre}, ya falta el último paso de este apartado! Identificamos ahora a los socios clave de tu negocio. Estos socios son aquellas organizaciones, personas o empresas que te ayudan a que tu negocio funcione y crezca. ¡Vamos a empezar! Para continuar escribe “preparada”.')

                                                                                                if st.text_input('Escribe "preparada" para continuar:', key='socios_preguntas').lower() == 'preparada':
                                                                                                    st.chat_message('assistant').write('Sólo faltan estas preguntas para definir los socios clave de tu negocio, ya casi terminamos esta parte.😅 Intenta ser lo más específica posible con tus respuestas para que podamos identificar con precisión las alianzas y colaboraciones necesarias. Aquí van las preguntas:\n\n1. ¿Quiénes son tus principales socios o aliados estratégicos que te ayudan a cumplir con tu propuesta de valor? Considera proveedores, distribuidores, aliados comerciales, etc. - Ejemplo: "Mi principal proveedor de materias primas, una agencia de marketing digital y una empresa de logística."\n\n2.  ¿Qué recursos claves obtienes de estos socios? Piensa en recursos físicos, financieros, intelectuales o humanos. - Ejemplo: "Obtengo los ingredientes principales de mi proveedor, el diseño de campañas publicitarias de la agencia de marketing y el transporte y entrega de productos de la empresa de logística."\n\n3. ¿Qué actividades clave realizan estos socios que te ayudan a operar tu negocio? Incluye actividades como producción, distribución, ventas, etc. - Ejemplo: "Mi proveedor garantiza el suministro continuo de materias primas, la agencia de marketing gestiona nuestras campañas publicitarias y la empresa de logística maneja la distribución."\n\nPor favor, responde a cada una de estas preguntas en orden.')
                                                                                            
                                                                                                    st.session_state.socios_principales = st.text_input('1. ¿Quiénes son tus principales socios o aliados estratégicos que te ayudan a cumplir con tu propuesta de valor? ', st.session_state.socios_principales, key='socios_principales_entrada')
                                                                                                    st.session_state.socios_clave = st.text_input('2. ¿Qué recursos claves obtienes de estos socios?', st.session_state.socios_clave, key='socios_clave_entrada')
                                                                                                    st.session_state.socios_actividades = st.text_input('3. ¿Qué actividades clave realizan estos socios que te ayudan a operar tu negocio?', st.session_state.socios_actividades, key='socios_actividades_entrada')

                                                                                                    if st.session_state.socios_principales and st.session_state.socios_clave and st.session_state.socios_actividades:
                                                                                                        if not st.session_state.resumen_socios:
                                                                                                            resumen_socios = llamar(
                                                                                                                f'Analiza la siguiente información y proporciona un resumen estructurado sobre los socios clave:\n\n1. Principales Socios o Aliados Estratégicos:\n{st.session_state.socios_principales}\n\n2. Recursos Claves Obtenidos de los Socios:\n{st.session_state.socios_clave}\n\n3. Actividades Clave Realizadas por los Socios:\n{st.session_state.socios_actividades}',
                                                                                                                'Eres un experto en desarrollo de negocios y desarrollo de modelos de negocio. Analiza la información proporcionada y realiza un resumen detallado sobre cuales son los socios clave del proyecto con base a lo que escribió el usuario, recuerda ser especifico y dar buena información'
                                                                                                            )
                                                                                                            st.session_state.resumen_socios = resumen_socios

                                                                                                        st.chat_message('assistant').write(f'¡Muy bien, {st.session_state.nombre}! 🤪 Con la información que me has proporcionado, he creado un perfil detallado de tus socios clave. Aquí tienes:\n\n{st.session_state.resumen_socios}\n\n')

                                                                                                        st.chat_message('assistant').write('Ahora, revisa esta información de forma detallada para agregarla a tu canva. 🤓 Una vez que estés satisfecha, daremos por finalizada con esta parte del Business Model Canvas.')

                                                                                                        st.chat_message('assistant').write('Aquí tienes el enlace para registrar los socios clave en tu Canva:\n\n[Enlace Canva: https://www.canva.com/design/DAGKqOD7Hcw/yENnVLwX2aMJvHFK69zhkA/view?utm_content=DAGKqOD7Hcw&utm_campaign=designshare&utm_medium=link&utm_source=publishsharelink&mode=preview]\n\n')
                                                                                                        
                                                                                                        st.chat_message('assistant').write('Si crees que has terminado escribe "lista" para finalizar.')
                                                                                                        
                                                                                                        if st.text_input('Escribe "lista" para continuar:', key='socios_canva').lower() == 'lista':
                                                                                                            st.chat_message('assistant').write(f'¡Lo lograste, {st.session_state.nombre}! 🥳 Has completado la Fase 2: Desarrolla tu Idea. Tu negocio está tomando forma. Estás a pocos pasos de empezar tu camino como emprendedora y tener un plan detallado para tu negocio. Ten en cuenta: "El obstáculo más grande para emprender son los límites mentales que tenemos" (Simón Borrero, Fundador y CEO de Rappi).')

# Función para la tercera pestaña
def fase3():
    
    # Inicializar el estado de sesión
    if 'nombre' not in st.session_state:
        st.session_state.nombre = ''
    if 'negocio' not in st.session_state:
        st.session_state.negocio = ''
    if 'productos' not in st.session_state:
        st.session_state.productos = []
    if 'producto_seleccionado' not in st.session_state:
        st.session_state.producto_seleccionado = ''
    if 'costo_fabricacion' not in st.session_state:
        st.session_state.costo_fabricacion = 0
    if 'otros_costos' not in st.session_state:
        st.session_state.otros_costos = 0
    if 'precio_venta' not in st.session_state:
        st.session_state.precio_venta = 0
    if 'cantidadEspecifica' not in st.session_state:
        st.session_state.cantidadEspecifica = 0
    if 'inversion' not in st.session_state:
        st.session_state.inversion = 0
    if 'ingresos_valor' not in st.session_state:
        st.session_state.ingresos_valor = ''
    if 'ingresos_pago' not in st.session_state:
        st.session_state.ingresos_pago = ''
    if 'ingresos_manera' not in st.session_state:
        st.session_state.ingresos_manera = ''
    if 'ingresos_metodos' not in st.session_state:
        st.session_state.ingresos_metodos = ''
    if 'ingresos_contribucion' not in st.session_state:
        st.session_state.ingresos_contribucion = ''
    if 'resumen_ingresos' not in st.session_state:
        st.session_state.resumen_ingresos = ''
    if 'user_input' not in st.session_state:
        st.session_state.user_input = ''

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
    st.sidebar.write(f'Valida tu idea')
    ###

    st.title('¡Bienvenida a valida tu idea!')

    # Introducción y nombre del participante
    st.session_state.nombre = st.text_input('Antes de iniciar me gustaría preguntar ¿Cuál es tu nombre?, con esto ya daremos el primer paso para empezar', key='inicio_fase3')

    if st.session_state.nombre:

        st.chat_message('assistant').write(f'¡Hola, {st.session_state.nombre}! Vamos a trabajar en la estructura de costes de tu negocio. Escribe “lista” para continuar.')

        if st.text_input('Escribe "lista" para continuar:', key='start_input').lower() == 'lista':
            st.session_state.negocio = st.text_input('¿Cómo se llama tu negocio y qué productos o servicios ofreces?', key='negocio_input')
            
            if st.session_state.negocio:
                productos = st.text_input('Menciona tres productos principales que ofreces o te gustaría ofrecer:\n\nEjemplo: Si tiene una reposteria, 3 productos serian: pastel de mora, galleta de coco, postre napoleon\n\nDebe seleccionar solo uno y es a ese producto al que se le trabajará la estructura de costos', key='productos_input')
                st.session_state.productos = productos.split(',')

                if len(st.session_state.productos) >= 3:
                    st.chat_message('assistant').write(f'¡Genial! Ahora elige uno de estos productos para detallar más a fondo.')
                    st.session_state.producto_seleccionado = st.selectbox('Selecciona el producto para detallar:', st.session_state.productos)

                    if st.session_state.producto_seleccionado:
                        st.chat_message('assistant').write(f'Perfecto, {st.session_state.nombre}. Vamos a detallar el {st.session_state.producto_seleccionado}.')

                        st.session_state.costo_fabricacion = st.number_input('¿Cuál es el costo de fabricación por unidad de este producto o servicio?', min_value=0, step=1000, key='costo_fabricacion_input')
                        st.session_state.otros_costos = st.number_input('¿Qué otros costos están asociados con la comercialización de este producto?', min_value=0, step=1000, key='otros_costos_input')
                        st.session_state.precio_venta = st.number_input('¿Cuál es el precio de venta de este producto o servicio?', min_value=0, step=1000, key='precio_venta_input')

                        if st.session_state.costo_fabricacion and st.session_state.otros_costos and st.session_state.precio_venta:
                            st.chat_message('assistant').write(f'¡Gracias, {st.session_state.nombre}! Aquí tienes un estimado de la estructura de costes para el {st.session_state.producto_seleccionado}:')
                            st.write(f'1. Costo de Fabricación por Unidad: ${st.session_state.costo_fabricacion}')
                            st.write(f'2. Precio de Venta por Unidad: ${st.session_state.precio_venta}')
                            st.write(f'3. Otros Costos Asociados: ${st.session_state.otros_costos}')

                            if st.text_input('¿Estás lista para ver la rentabilidad y utilidad estimada para 10, 50, y 100 unidades? Escribe "lista" para ver.', key='rentabilidad_input').lower() == 'lista':
                                for cantidad in [10, 50, 100]:
                                    costo_total_fabricacion = st.session_state.costo_fabricacion * cantidad
                                    costo_total_comercializacion = st.session_state.otros_costos * (cantidad / 10)
                                    ingreso_total_ventas = st.session_state.precio_venta * cantidad
                                    utilidad_total = ingreso_total_ventas - costo_total_fabricacion - costo_total_comercializacion
                                    rentabilidad = (utilidad_total / ingreso_total_ventas) * 100

                                    st.chat_message('assistant').write(f'Para {cantidad} unidades:')
                                    st.write(f'● Costo Total de Fabricación: ${costo_total_fabricacion}')
                                    st.write(f'● Costo Total de Comercialización: ${costo_total_comercializacion}')
                                    st.write(f'● Ingreso Total por Ventas: ${ingreso_total_ventas}')
                                    st.write(f'● Utilidad Total: ${utilidad_total}')
                                    st.write(f'● Rentabilidad: {rentabilidad:.2f}%')                               
                                    
                                user_input = st.text_input('¿Quieres calcular de forma específica una cantidad de productos y servicios? Escribe "calcular" para digitar una cifra específica o escribe "no" para continuar.', key='cantidadEspecifica_input').lower()    
                                    
                                if user_input:
                                    if user_input == 'calcular':
                                        st.session_state.cantidadEspecifica = st.number_input('Cantidad de productos o servicios que quieres calcular de forma específica', min_value=0, step=5, key='cantidadEspecifica_number')
                                        if st.session_state.cantidadEspecifica != 0:
                                            for cantidad in [st.session_state.cantidadEspecifica]:
                                                costo_total_fabricacion = st.session_state.costo_fabricacion * cantidad
                                                costo_total_comercializacion = st.session_state.otros_costos * (cantidad / 10)
                                                ingreso_total_ventas = st.session_state.precio_venta * cantidad
                                                utilidad_total = ingreso_total_ventas - costo_total_fabricacion - costo_total_comercializacion
                                                rentabilidad = (utilidad_total / ingreso_total_ventas) * 100

                                                st.chat_message('assistant').write(f'Para {cantidad} unidades:')
                                                st.write(f'● Costo Total de Fabricación: ${costo_total_fabricacion}')
                                                st.write(f'● Costo Total de Comercialización: ${costo_total_comercializacion}')
                                                st.write(f'● Ingreso Total por Ventas: ${ingreso_total_ventas}')
                                                st.write(f'● Utilidad Total: ${utilidad_total}')
                                                st.write(f'● Rentabilidad: {rentabilidad:.2f}%')
                                                
                                                # Control de condicional sobre el mismo final si pasa una cosa o la otra
                                                st.chat_message('assistant').write(f'Perfecto {st.session_state.nombre} ahora vamos a continuar, pero antes de eso, para poder ayudarte mejor necesito saber cuanto estás dispuesta a invertir, por lo que te pregunto ¿Cuánto estás dispuesta a invertir en la producción de este producto o servicio para lanzarte a emprender? Esto nos ayudará a determinar la cantidad óptima para producir con una rentabilidad/utilidad favorable.')
                                                if st.text_input('Piensa por un momento, cuando estés segura de la cantidad escribe "lista" para continuar.', key='inversion_input').lower() == 'lista':
                                                    st.session_state.inversion = st.number_input('Ingresa la cantidad a invertir:', min_value=0, step=100000, key='inversion_number')
                                                    if st.session_state.inversion != 0:
                                                        for cantidad in [st.session_state.inversion]:
                                                            cantidad_optima_produccion = st.session_state.inversion / st.session_state.costo_fabricacion
                                                            costo_total_fabricacion_inversion = st.session_state.costo_fabricacion * cantidad_optima_produccion
                                                            costo_total_comercializacion_inversion = st.session_state.otros_costos * (cantidad_optima_produccion / 10)
                                                            ingreso_total_ventas_inversion = st.session_state.precio_venta * cantidad_optima_produccion
                                                            utilidad_total_inversion = ingreso_total_ventas_inversion - costo_total_fabricacion_inversion  - costo_total_comercializacion_inversion
                                                            rentabilidad_inversion = (utilidad_total_inversion / ingreso_total_ventas_inversion) * 100

                                                            st.chat_message('assistant').write(f'¡Gracias, {st.session_state.nombre}! Con base en tu inversión de ${st.session_state.inversion}, aquí tienes el cálculo óptimo para producir:')

                                                            st.write(f'● Cantidad Óptima a Producir: {cantidad_optima_produccion}')
                                                            st.write(f'● Costo Total de Fabricación: ${costo_total_fabricacion_inversion}')
                                                            st.write(f'● Costo Total de Comercialización: ${costo_total_comercializacion_inversion}')
                                                            st.write(f'● Ingreso Total por Ventas: ${ingreso_total_ventas_inversion}')
                                                            st.write(f'● Utilidad Total: ${utilidad_total_inversion}')
                                                            st.write(f'● Rentabilidad: {rentabilidad_inversion:.2f}%')
                                                            
                                                            if st.text_input('Cuando acabes de analizar los datos con relación a tu posible inversión, escribe "lista" para continuar.', key='finalizacionCostos_input').lower() == 'lista':
                                                                
                                                                st.chat_message('assistant').write('¡Bien! Nuestra Estructura de Costos está lista. Recuerda, entender cómo se distribuyen los costos y recursos claves nos ayudará a mantener un negocio organizado y eficiente! 🏛 Vamos a registrar tu Estructura de Costos en la plantilla del Business Model Canvas. Aquí tienes el enlace para comenzar a llenar tu Canvas: https://www.canva.com/design/DAGKqOD7Hcw/yENnVLwX2aMJvHFK69zhkA/view?utm_content=DAGKqOD7Hcw&utm_campaign=designshare&utm_medium=link&utm_source=publishsharelink&mode=preview')
                                                                st.chat_message('assistant').write(f'NOTA: Recuerda que en cualquier momento puedes subir un poco y ajustar los costos a tu acomodo.')

                                                                if st.text_input('Cuando termines de colocar tus costos en la plantilla del Business Model Canvas, escribe "lista" para continuar.', key='ingresoInicio_input').lower() == 'lista':
                                                                    st.chat_message('assistant').write(f'¡Perfecto, {st.session_state.nombre}! 😊 Ahora vamos a trabajar en el flujo de ingresos de tu negocio. Identificaremos cómo y por qué valor están dispuestos a pagar tus clientes. ¡Vamos a ello!')
                                                                    
                                                                    st.chat_message('assistant').write('Voy a hacerte algunas preguntas clave sobre el flujo de ingresos de tu negocio. Intenta ser lo más específica posible:\n\n1. ¿Cuál es la razón por la cual tus clientes estarían dispuestos a pagar por tus productos o servicios? Piensa en el valor que tu producto o servicio ofrece. - Ejemplo: "Por la calidad y exclusividad de mis productos."\n\n2. ¿Por qué valor crees que pagarán actualmente? Incluye tus estimaciones de precios. - Ejemplo: "Mis productos se venderán a $50 por unidad."\n\n3. ¿Cómo pagarán tus clientes? Considera los métodos de pago que preferirán utilizar. - Ejemplo: "Pagos mediante tarjeta de crédito y transferencias bancarias."\n\n4. ¿Qué método preferirían utilizar para pagar? Pregunta a tus clientes sus preferencias. - Ejemplo: "Pagos móviles y billeteras electrónicas."\n\n5. ¿Cuánto contribuirá cada fuente de ingresos a los ingresos totales? Desglosa tus estimaciones. - Ejemplo: "Ventas directas contribuirán con el 70%, y suscripciones con el 30%." Por favor, responde a cada una de estas preguntas en orden.')
                                                                    
                                                                    st.session_state.ingresos_valor = st.text_input('1. ¿Cuál es la razón por la cual tus clientes estarían dispuestos a pagar por tus productos o servicios?', st.session_state.ingresos_valor, key='ingresos_valor_entrada')
                                                                    st.session_state.ingresos_pago = st.text_input('2. ¿Por qué valor crees que pagarán actualmente?', st.session_state.ingresos_pago, key='ingresos_pago_entrada')
                                                                    st.session_state.ingresos_manera = st.text_input('3. ¿Cómo pagarán tus clientes?', st.session_state.ingresos_manera, key='ingresos_manera_entrada')
                                                                    st.session_state.ingresos_metodos = st.text_input('4. ¿Qué método preferirían utilizar para pagar?', st.session_state.ingresos_metodos, key='ingresos_metodos_entrada')
                                                                    st.session_state.ingresos_contribucion = st.text_input('5. ¿Cuánto contribuirá cada fuente de ingresos a los ingresos totales?', st.session_state.ingresos_contribucion, key='ingresos_contribucion_entrada')
                                                                    
                                                                    
                                                                    
                                                                    if st.session_state.ingresos_valor and st.session_state.ingresos_pago and st.session_state.ingresos_manera and st.session_state.ingresos_metodos and st.session_state.ingresos_contribucion:
                                                                        if not st.session_state.resumen_ingresos:
                                                                            resumen_ingresos = llamar(
                                                                                f'Analiza la siguiente información y proporciona un resumen estructurado sobre el flujo de ingresos:\n\n1. Valor por el que estarán dispuestos a pagar los clientes:\n{st.session_state.ingresos_valor}\n\n2. Valor actual que pagarán los clientes:\n{st.session_state.ingresos_pago}\n\n3. Métodos de pago:\n{st.session_state.ingresos_manera}\n\n4. Métodos de pago preferidos:\n{st.session_state.ingresos_metodos}\n\n5. Contribución de cada fuente de ingresos:\n{st.session_state.ingresos_contribucion}',
                                                                                'Eres un experto en desarrollo de negocios, desarrollo de modelos de negocio y en especial eres experto sacando flujos de ingresos para las empresas. Analiza la información proporcionada y realiza un resumen detallado sobre cual es el flujo de ingreso del proyecto con base a lo que escribió el usuario, recuerda ser especifico y dar buena información'
                                                                            )
                                                                            st.session_state.resumen_ingresos = resumen_ingresos
                                                                        
                                                                        st.chat_message('assistant').write(f'¡Muy bien, {st.session_state.nombre}! 🤪 Con la información que me has proporcionado, he creado un resumen de tu flujo de ingresos. Aquí tienes:\n\n{st.session_state.resumen_ingresos}\n\n')
                                                                        
                                                                        st.chat_message('assistant').write('Ahora, revisa esta información de forma detallada para agregarla a tu canva. 🤓')

                                                                        if st.text_input('Escribe "lista" para continuar, cuando sientas que ya has acabado:', key='ingresos_canva').lower() == 'lista':
                                                                            st.chat_message('assistant').write(f'¡Excelente, {st.session_state.nombre}! El flujo de ingresos está terminado. ¡Ten en cuenta que un negocio con ingresos y costos en orden garantiza viabilidad en las operaciones y proyectos que intentes realizar! 😎 Vamos a registrar tu Flujo de Ingresos en la plantilla del Business Model Canvas. Aquí tienes el enlace para comenzar a llenar tu Canvas: (https://www.canva.com/design/DAGKqOD7Hcw/yENnVLwX2aMJvHFK69zhkA/view?utm_content=DAGKqOD7Hcw&utm_campaign=designshare&utm_medium=link&utm_source=publishsharelink&mode=preview).')
                                                                            
                                                                            if st.text_input('Una vez hayas completado el Business Model Canvas, escribe “terminado” para continuar. 🤩', key='ingresos_final_canva').lower() == 'terminado':
                                                                                st.chat_message('assistant').write(f'¡Lo lograste, {st.session_state.nombre}! 🥳 Has completado la Fase 3: Válida tu Idea. Tu idea de negocio va volando. Estás a una fase de iniciar tu camino como emprendedora y empezar a publicitar tu negocio.')
                                                                            
                                    elif user_input == 'no':                                
                                        st.chat_message('assistant').write(f'Perfecto {st.session_state.nombre} ahora vamos a continuar, pero antes de eso, para poder ayudarte mejor necesito saber cuanto estás dispuesta a invertir, por lo que te pregunto ¿Cuánto estás dispuesta a invertir en la producción de este producto o servicio para lanzarte a emprender? Esto nos ayudará a determinar la cantidad óptima para producir con una rentabilidad/utilidad favorable.')
                                        if st.text_input('Piensa por un momento, cuando estés segura de la cantidad escribe "lista" para continuar.', key='inversion_input').lower() == 'lista':
                                            st.session_state.inversion = st.number_input('Ingresa la cantidad a invertir:', min_value=0, step=100000, key='inversion_number')
                                            if st.session_state.inversion != 0:
                                                for cantidad in [st.session_state.inversion]:
                                                    cantidad_optima_produccion = st.session_state.inversion / st.session_state.costo_fabricacion
                                                    costo_total_fabricacion_inversion = st.session_state.costo_fabricacion * cantidad_optima_produccion
                                                    costo_total_comercializacion_inversion = st.session_state.otros_costos * (cantidad_optima_produccion / 10)
                                                    ingreso_total_ventas_inversion = st.session_state.precio_venta * cantidad_optima_produccion
                                                    utilidad_total_inversion = ingreso_total_ventas_inversion - costo_total_fabricacion_inversion  - costo_total_comercializacion_inversion
                                                    rentabilidad_inversion = (utilidad_total_inversion / ingreso_total_ventas_inversion) * 100

                                                    st.chat_message('assistant').write(f'¡Gracias, {st.session_state.nombre}! Con base en tu inversión de ${st.session_state.inversion}, aquí tienes el cálculo óptimo para producir:')

                                                    st.write(f'● Cantidad Óptima a Producir: {cantidad_optima_produccion}')
                                                    st.write(f'● Costo Total de Fabricación: ${costo_total_fabricacion_inversion}')
                                                    st.write(f'● Costo Total de Comercialización: ${costo_total_comercializacion_inversion}')
                                                    st.write(f'● Ingreso Total por Ventas: ${ingreso_total_ventas_inversion}')
                                                    st.write(f'● Utilidad Total: ${utilidad_total_inversion}')
                                                    st.write(f'● Rentabilidad: {rentabilidad_inversion:.2f}%')
                                                    
                                                    if st.text_input('Cuando acabes de analizar los datos con relación a tu posible inversión, escribe "lista" para continuar.', key='finalizacionCostos_input').lower() == 'lista':
                                                        
                                                        st.chat_message('assistant').write('¡Bien! Nuestra Estructura de Costos está lista. Recuerda, entender cómo se distribuyen los costos y recursos claves nos ayudará a mantener un negocio organizado y eficiente! 🏛 Vamos a registrar tu Estructura de Costos en la plantilla del Business Model Canvas. Aquí tienes el enlace para comenzar a llenar tu Canvas: https://www.canva.com/design/DAGKqOD7Hcw/yENnVLwX2aMJvHFK69zhkA/view?utm_content=DAGKqOD7Hcw&utm_campaign=designshare&utm_medium=link&utm_source=publishsharelink&mode=preview.')
                                                        st.chat_message('assistant').write(f'NOTA: Recuerda que en cualquier momento puedes subir un poco y ajustar los costos a tu acomodo.')

                                                        if st.text_input('Cuando termines de colocar tus costos en la plantilla del Business Model Canvas, escribe "lista" para continuar.', key='ingresoInicio_input').lower() == 'lista':
                                                            st.chat_message('assistant').write(f'¡Perfecto, {st.session_state.nombre}! 😊 Ahora vamos a trabajar en el flujo de ingresos de tu negocio. Identificaremos cómo y por qué valor están dispuestos a pagar tus clientes. ¡Vamos a ello!')
                                                            
                                                            st.chat_message('assistant').write('Voy a hacerte algunas preguntas clave sobre el flujo de ingresos de tu negocio. Intenta ser lo más específica posible:\n\n1. ¿Cuál es la razón por la cual tus clientes estarían dispuestos a pagar por tus productos o servicios? Piensa en el valor que tu producto o servicio ofrece. - Ejemplo: "Por la calidad y exclusividad de mis productos."\n\n2. ¿Por qué valor crees que pagarán actualmente? Incluye tus estimaciones de precios. - Ejemplo: "Mis productos se venderán a $50 por unidad."\n\n3. ¿Cómo pagarán tus clientes? Considera los métodos de pago que preferirán utilizar. - Ejemplo: "Pagos mediante tarjeta de crédito y transferencias bancarias."\n\n4. ¿Qué método preferirían utilizar para pagar? Pregunta a tus clientes sus preferencias. - Ejemplo: "Pagos móviles y billeteras electrónicas."\n\n5. ¿Cuánto contribuirá cada fuente de ingresos a los ingresos totales? Desglosa tus estimaciones. - Ejemplo: "Ventas directas contribuirán con el 70%, y suscripciones con el 30%." Por favor, responde a cada una de estas preguntas en orden.')
                                                            
                                                            st.session_state.ingresos_valor = st.text_input('1. ¿Cuál es la razón por la cual tus clientes estarían dispuestos a pagar por tus productos o servicios?', st.session_state.ingresos_valor, key='ingresos_valor_entrada')
                                                            st.session_state.ingresos_pago = st.text_input('2. ¿Por qué valor crees que pagarán actualmente?', st.session_state.ingresos_pago, key='ingresos_pago_entrada')
                                                            st.session_state.ingresos_manera = st.text_input('3. ¿Cómo pagarán tus clientes?', st.session_state.ingresos_manera, key='ingresos_manera_entrada')
                                                            st.session_state.ingresos_metodos = st.text_input('4. ¿Qué método preferirían utilizar para pagar?', st.session_state.ingresos_metodos, key='ingresos_metodos_entrada')
                                                            st.session_state.ingresos_contribucion = st.text_input('5. ¿Cuánto contribuirá cada fuente de ingresos a los ingresos totales?', st.session_state.ingresos_contribucion, key='ingresos_contribucion_entrada')
                                                            
                                                            
                                                            
                                                            if st.session_state.ingresos_valor and st.session_state.ingresos_pago and st.session_state.ingresos_manera and st.session_state.ingresos_metodos and st.session_state.ingresos_contribucion:
                                                                if not st.session_state.resumen_ingresos:
                                                                    resumen_ingresos = llamar(
                                                                        f'Analiza la siguiente información y proporciona un resumen estructurado sobre el flujo de ingresos:\n\n1. Valor por el que estarán dispuestos a pagar los clientes:\n{st.session_state.ingresos_valor}\n\n2. Valor actual que pagarán los clientes:\n{st.session_state.ingresos_pago}\n\n3. Métodos de pago:\n{st.session_state.ingresos_manera}\n\n4. Métodos de pago preferidos:\n{st.session_state.ingresos_metodos}\n\n5. Contribución de cada fuente de ingresos:\n{st.session_state.ingresos_contribucion}',
                                                                        'Eres un experto en desarrollo de negocios, desarrollo de modelos de negocio y en especial eres experto sacando flujos de ingresos para las empresas. Analiza la información proporcionada y realiza un resumen detallado sobre cual es el flujo de ingreso del proyecto con base a lo que escribió el usuario, recuerda ser especifico y dar buena información'
                                                                    )
                                                                    st.session_state.resumen_ingresos = resumen_ingresos
                                                                
                                                                st.chat_message('assistant').write(f'¡Muy bien, {st.session_state.nombre}! 🤪 Con la información que me has proporcionado, he creado un resumen de tu flujo de ingresos. Aquí tienes:\n\n{st.session_state.resumen_ingresos}\n\n')
                                                                
                                                                st.chat_message('assistant').write('Ahora, revisa esta información de forma detallada para agregarla a tu canva. 🤓')

                                                                if st.text_input('Escribe "lista" para continuar, cuando sientas que ya has acabado:', key='ingresos_canva').lower() == 'lista':
                                                                    st.chat_message('assistant').write(f'¡Excelente, {st.session_state.nombre}! El flujo de ingresos está terminado. ¡Ten en cuenta que un negocio con ingresos y costos en orden garantiza viabilidad en las operaciones y proyectos que intentes realizar! 😎 Vamos a registrar tu Flujo de Ingresos en la plantilla del Business Model Canvas. Aquí tienes el enlace para comenzar a llenar tu Canvas: (https://www.canva.com/design/DAGKqOD7Hcw/yENnVLwX2aMJvHFK69zhkA/view?utm_content=DAGKqOD7Hcw&utm_campaign=designshare&utm_medium=link&utm_source=publishsharelink&mode=preview).')
                                                                    
                                                                    if st.text_input('Una vez hayas completado el Business Model Canvas, escribe “terminado” para continuar. 🤩', key='ingresos_final_canva').lower() == 'terminado':
                                                                        st.chat_message('assistant').write(f'¡Lo lograste, {st.session_state.nombre}! 🥳 Has completado la Fase 3: Válida tu Idea. Tu idea de negocio va volando. Estás a una fase de iniciar tu camino como emprendedora y empezar a publicitar tu negocio.')        
        
# Función para la cuarta pestaña
def fase4():
    
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

    st.session_state.nombre = st.text_input('Antes de iniciar me gustaría preguntar ¿Cuál es tu nombre?, con esto ya daremos el primer paso para empezar', key='inicio_fase4')

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

# Menú de navegación en la barra lateral
opcion = st.sidebar.selectbox("Selecciona una pestaña:", ("Fase 1", "Fase 2", "Fase 3", "Fase 4"))

# Mostrar el contenido basado en la opción seleccionada
if opcion == "Fase 1":
    fase1()
if opcion == "Fase 2":
    fase2()
if opcion == "Fase 3":
    fase3()
if opcion == "Fase 4":
    fase4()
