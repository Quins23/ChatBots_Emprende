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

st.session_state.nombre = st.text_input('Antes de iniciar me gustaría preguntar ¿Cuál es tu nombre?, con esto ya daremos el primer paso para empezar', '')

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




