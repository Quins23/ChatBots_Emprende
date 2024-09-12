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
st.session_state.nombre = st.text_input('Antes de iniciar me gustaría preguntar ¿Cuál es tu nombre?, con esto ya daremos el primer paso para empezar', '')

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
