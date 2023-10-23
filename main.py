import streamlit as st
import sys
sys.path.append("C:\\Abel\\Trabajo\Proyectos Ciencia de Datos\\XML to txt Puertos TCP Nmap\\src")
import xml_to_txt

def main():
    st.title('Cargador de archivos XML')

    # Solicitar la carga del archivo XML
    uploaded_file = st.file_uploader("Por favor, sube un archivo XML", type="xml")
    
    if uploaded_file is not None:
        st.success('Archivo cargado exitosamente!')
        xml_to_txt.xml_to_txt(uploaded_file)

    
if __name__ == "__main__":
    main()