def crearPDFPorHTML(html, ruta_destino):
    try:
        from fpdf import FPDF, HTMLMixin
        class MyFPDF(FPDF, HTMLMixin):
            pass
        pdf = MyFPDF()
        pdf.add_page()
        pdf.write_html(html)
        pdf.output(ruta_destino, 'F')
        return True
    except:
        return False

def obtenerPlantilla1(titulo=None, cuerpo=None, titulo_lista=None, lista=None, titulo_tabla=None,tabla=None):
    html = ""
    if titulo != None:
        html += """<H1 align="center">"""+str(titulo)+"""</H1>"""
    if cuerpo != None:
        html +="""<p>"""+str(cuerpo)+"""</p>"""
    
    if titulo_lista != None:
        html += """"<h3>"""+str(titulo_lista)+"""</h3>"""

    if lista != None:
        html += "<ul>"
        for fila in lista:
            html += "<li>"+str(fila)+"</li>"
        html += "</ul>"
    
    if titulo_tabla != None:
        html += """"<h3>"""+str(titulo_tabla)+"""</h3>"""

    if tabla != None:
        if len(tabla) > 0:
            html += """<table border="0" align="center" width="100%">"""
            for index, element in enumerate(tabla):
                if index == 0:
                    html += "<thead><tr>"
                    for colum in element:
                        html += """<th width=\""""+str(int(100/len(element)))+"""%">"""+str(colum)+"""</th>"""
                    html += "</thead></tr>"
                    break
            if len(tabla) > 1:
                html += """<tbody>"""
                for index, element in enumerate(tabla):
                    if index > 0:
                        html += "<tr>"
                        for colum in element:
                            html += """<td>"""+str(colum)+"""</td>"""
                        html += "</tr>"
                html += """</tbody>"""
            html += """</table>"""
    return html