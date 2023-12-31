'''
Explicacion de la codificacion, esto se hace porque con la aplicacion en linea la manera de acceder al txt generado es a traves de un link de descarga

Codificación Base64: b64 = base64.b64encode(text.encode()).decode()

Esta línea de código convierte el texto del archivo en una cadena codificada en base64, que se puede incluir en un enlace de descarga. Aquí está lo que hace cada parte:

text.encode(): Convierte la cadena de texto en bytes, porque la función base64.b64encode necesita bytes como entrada.
base64.b64encode(...): Codifica los bytes en una cadena base64. Esta función devuelve bytes.
.decode(): Convierte los bytes de la cadena base64 en una cadena normal (decodifica los bytes a una cadena UTF-8).
Creación del enlace de descarga: linko= f'<a href="data:file/txt;base64,{b64}" download="txt_generado_del_xml.txt">Descargar archivo TXT</a>'

Esta línea de código crea un enlace de descarga para el archivo de texto. Aquí está lo que hace cada parte:

'data:file/txt;base64,{b64}': Esto es un URI de datos, que permite incrustar pequeños archivos de datos en línea en el documento. Está formado por el tipo de medio (file/txt), la codificación (base64) y los datos codificados ({b64}).
download="txt_generado_del_xml.txt": Esto hace que al hacer clic en el enlace, los datos se descarguen como un archivo llamado “txt_generado_del_xml.txt”.
Descargar archivo TXT: Este es el texto que se mostrará para el enlace.
'''
import os
import streamlit as st
import sys
cwd = os.getcwd()
# Agregar la ruta relativa `src` al directorio actual
sys.path.append(os.path.join(cwd, "src"))
import xml_to_txt
import txt_to_IP
import txt_to_port
import base64

def main():
    """
    Función principal que se ejecuta cuando se inicia el script. Utiliza la biblioteca Streamlit para crear una interfaz de usuario interactiva en la web.

    La interfaz de usuario solicita al usuario que cargue un archivo XML. Una vez cargado, el archivo se procesa utilizando la función `xml_to_txt`, 
    que extrae el texto de cada elemento del archivo XML y lo devuelve como una cadena de texto.

    El usuario tiene la opción de descargar este texto como un archivo .txt. Además, el usuario puede presionar un botón para procesar este texto con la función `txt_to_IP`, 
    que busca direcciones IP y detalles de puertos TCP abiertos en el texto y escribe esta información en un archivo de salida.

    Finalmente, el usuario puede presionar otro botón para procesar el archivo de salida de `txt_to_IP` con las funciones `parse_txt` y `write_to_txt`, 
    que crean un resumen de los puertos abiertos y las direcciones IP asociadas y escriben esta información en otro archivo de salida.

    Parámetros:
    Ninguno

    Devuelve:
    Ninguno
    """
    st.title('Cargador de archivos XML')

    # Solicitar la carga del archivo XML
    uploaded_file = st.file_uploader("Por favor, sube un archivo XML", type="xml")
    
    if uploaded_file is not None:
        st.success('Archivo cargado exitosamente!')
        text = xml_to_txt.xml_to_txt(uploaded_file,'txt_generado_del_xml.txt')
        b64 = base64.b64encode(text.encode()).decode()  # Codificacion de cadenas de bytes
        linko= f'<a href="data:file/txt;base64,{b64}" download="txt_generado_del_xml.txt">Descargar archivo TXT</a>'
        st.markdown(linko, unsafe_allow_html=True)
        button = st.button("Listado de puertos TCP abiertos en cada IP")
        output_file = txt_to_IP.txt_to_IP(text, 'IP_con_puertos_abiertos.txt')
        if button:
            
            with open(output_file, 'r') as f:
                contenido_txt_from_XML = f.read()
            st.download_button(
            label="Descargar archivo TXT",
            data=contenido_txt_from_XML,
            file_name="IP_con_puertos_abiertos.txt",
            mime="text/plain",
            )
        button2 = st.button("Ver resumen de puertos abiertos y los IP")
        if button2:
            # Llama a parse_txt y write_to_txt con el archivo de salida de txt_to_IP
            ip_dict = txt_to_port.parse_txt(output_file)
            if ip_dict == {'default': []}:
                st.write("No existen puertos TCP abiertos en la red")
            txt_to_port.write_to_txt(ip_dict, 'IP_por_cada_puerto_abierto.txt')
            
            with open('IP_por_cada_puerto_abierto.txt', 'r') as f:
                contenido_IP_por_puerto = f.read()
            st.download_button(
            label="Descargar archivo TXT",
            data=contenido_IP_por_puerto,
            file_name="IP_por_cada_puerto_abierto.txt",
            mime="text/plain",
            )       


    
if __name__ == "__main__":
    main()