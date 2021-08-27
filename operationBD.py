from typing import ItemsView
import os
import pymysql
import json
from datetime import date
from datetime import datetime

DB_HOST='remotemysql.com'  # por favor modifique aca ingeniero
DB_USER='MAHdOtn0ov'       # por favor modifique aca ingeniero
DB_PASS='pmO6HIjNSu'       # por favor modifique aca ingeniero
DB_NAME='MAHdOtn0ov'       # por favor modifique aca ingeniero
class koha():

    def run_query(self,query ): 
        conn = pymysql.connect(host= DB_HOST,user=  DB_USER, passwd= DB_PASS, db = DB_NAME) # Conectar a la base de datos 
        cursor = conn.cursor()        
        cursor.execute(query)         
        if query.upper().startswith('SELECT'): 
            data = cursor.fetchall()   
        else: 
            conn.commit()              
            data = None       
        cursor.close()   
        conn.close()   
        return data

    
    def insertJson(self, data ):
        query = "SELECT max(biblionumber) FROM biblio" 
        result = self.run_query(query) 
        resultado = result[0][0] + 1
        biblio = data['biblio']
        biblioItems = data['biblioItems']
        items = data['items']
        campo = data['campos'] 
        biblio['biblionumber'] = resultado
        
        codigoCatalogador = campo['codigoCatalogador']
        horaCampoCinco = campo['horaCampoCinco'] 
        tema650 = campo['tema650'] 
        biblionumber = str(resultado) 
        numeroClasificacion =  campo['numeroClasificacion'] 
        numeroClasificacionOpcional =  campo['numeroClasificacionOpcional']
        lugarProduccion = campo['lugarProduccion'] 
        entidadProductora =  campo['entidadProductora'] 
        anoProduccion = campo['anoProduccion'] 
        fechaAccion = campo['fechaAccion']
        palabraClave = campo['palabraClave']
        textoEnlace = campo['textoEnlace']
        urlArchivoa = campo['urlArchivoa']
        encabezamiento =  campo['encabezamiento']
        descripcionFisicaFijo = campo['descripcionFisicaFijo']
        longitudFija = campo['longitudFija']
        autorPersona = campo['autorPersona']
        autorEntidad = campo['autorEntidad']
        autorEvento = campo['autorEvento']
        tituloUniforme = campo['tituloUniforme']
        titulo = biblio['title']
        autorTitulo = campo['autorTitulo'] 
        duracion = campo['duracion']
        tipoContenidoA = campo['tipoContenidoA']
        tipoContenidoB = campo['tipoContenidoB']
        tipoMedioA = campo['tipoMedioA']
        tipoMedioB = campo['tipoMedioB']
        coleccion = campo['coleccion']
        notaGeneral = campo['notaGeneral']
        notaContenido = biblio['notes']  
        notaCreditos = campo['notaCreditos']
        notaElenco = campo['notaElenco']
        descripcionFisicaA = campo['descripcionFisicaA']
        descripcionFisicaB = campo['descripcionFisicaB']
        descripcionFisicaC = campo['descripcionFisicaC']
        tipoItem = campo['tipoItem']
        urlArchivo = campo['urlArchivo'] 
        tipoAoV = campo['tipoAoV'] 
        campoSeiscientos = campo['campoSeiscientos']
        caracteristicaseis = campo['caracteristicaseis']
        genero = campo['genero']
        forma = campo['forma']
        autorPersonad = campo['autorPersonad']
        autorPersonae = campo['autorPersonae']
        autorEventod = campo['autorEventod']
        autorEventoe = campo['autorEventoe']
        autorEntidadd = campo['autorEntidadd']
        autorEntidade = campo['autorEntidade']

        xml = """<?xml version="1.0" encoding="UTF-8"?>\n<record\n    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"\n    xsi:schemaLocation="http://www.loc.gov/MARC21/slim http://www.loc.gov/standards/marcxml/schema/MARC21slim.xsd"\n    xmlns="http://www.loc.gov/MARC21/slim">\n\n  
        <leader>"""+encabezamiento+"""</leader>\n  
        <datafield tag="999" ind1=" " ind2=" ">\n    <subfield code="c">"""+biblionumber+"""</subfield>\n    <subfield code="d">"""+biblionumber+"""</subfield>\n  </datafield>\n
        <controlfield tag="001"></controlfield>\n  
        <controlfield tag="003">CO-BoRTV</controlfield>\n  
        <controlfield tag="005">"""+horaCampoCinco+"""</controlfield>\n
        <controlfield tag="006">"""+caracteristicaseis+"""</controlfield>\n
        <controlfield tag="007">"""+descripcionFisicaFijo+"""</controlfield>\n  
        <controlfield tag="008">"""+longitudFija+"""</controlfield>\n  
        <datafield tag="010" ind1=" " ind2=" ">\n    <subfield code="a">CO-BoRTV</subfield>\n  </datafield>\n  
        <datafield tag="040" ind1=" " ind2=" ">\n    <subfield code="a">CO-BoRTV</subfield>\n    <subfield code="b">spa</subfield>\n  </datafield>\n 
        <datafield tag="041" ind1=" " ind2=" ">\n    <subfield code="a">spa</subfield>\n  </datafield>\n   
        <datafield tag="084" ind1=" " ind2=" ">\n    <subfield code="a">"""+numeroClasificacion+"""</subfield>\n  </datafield>\n  
        <datafield tag="090" ind1=" " ind2=" ">\n    <subfield code="a">"""+numeroClasificacionOpcional+"""</subfield>\n  </datafield>\n  
        <datafield tag="100" ind1="1" ind2=" ">\n    <subfield code="a">"""+autorPersona+"""</subfield>\n    <subfield code="d">"""+autorPersonad+"""</subfield>\n    <subfield code="e">"""+autorPersonae+"""</subfield>\n  </datafield>\n  
        <datafield tag="110" ind1="2" ind2=" ">\n    <subfield code="a">"""+autorEntidad+"""</subfield>\n    <subfield code="d">"""+autorEntidadd+"""</subfield>\n    <subfield code="e">"""+autorEntidade+"""</subfield>\n  </datafield>\n  
        <datafield tag="111" ind1="2" ind2=" ">\n    <subfield code="a">"""+autorEvento+"""</subfield>\n    <subfield code="d">"""+autorEventod+"""</subfield>\n    <subfield code="e">"""+autorEventoe+"""</subfield>\n  </datafield>\n  
        <datafield tag="243" ind1="1" ind2="0">\n    <subfield code="a">"""+tituloUniforme+"""</subfield>\n  </datafield>\n  
        <datafield tag="245" ind1="1" ind2="0">\n    <subfield code="a">"""+titulo+"""</subfield>\n    <subfield code="c">"""+autorTitulo+"""</subfield>\n  </datafield>\n  
        <datafield tag="264" ind1=" " ind2="0">\n    <subfield code="a">"""+lugarProduccion+"""</subfield>\n    <subfield code="b">"""+entidadProductora+"""</subfield>\n    <subfield code="c">"""+anoProduccion+"""</subfield>\n  </datafield>\n  
        <datafield tag="300" ind1=" " ind2=" ">\n    <subfield code="a">"""+descripcionFisicaA+"""</subfield>\n    <subfield code="b">"""+descripcionFisicaB+"""</subfield>\n    <subfield code="c">"""+descripcionFisicaC+"""</subfield>\n      </datafield>\n  
        <datafield tag="306" ind1=" " ind2=" ">\n    <subfield code="a">"""+duracion+"""</subfield>\n  </datafield>\n  
        <datafield tag="336" ind1=" " ind2=" ">\n    <subfield code="a">"""+tipoContenidoA+"""</subfield>\n    <subfield code="b">"""+tipoContenidoB+"""</subfield>\n    <subfield code="2">rdacontenido</subfield>\n  </datafield>\n  
        <datafield tag="337" ind1=" " ind2=" ">\n    <subfield code="a">"""+tipoMedioA+"""</subfield>\n    <subfield code="b">"""+tipoMedioB+"""</subfield>\n  <subfield code="2">rdamedio</subfield>\n  </datafield>\n  
        <datafield tag="338" ind1=" " ind2=" ">\n    <subfield code="a">recurso en línea</subfield>\n    <subfield code="b">cr</subfield>\n    <subfield code="2">rdasoporte</subfield>\n  </datafield>\n  
        <datafield tag="490" ind1="0" ind2=" ">\n    <subfield code="a">"""+coleccion+"""</subfield>\n  </datafield>\n  
        <datafield tag="500" ind1="0" ind2=" ">\n    <subfield code="a">"""+notaGeneral+"""</subfield>\n  </datafield>\n  
        <datafield tag="505" ind1="0" ind2=" ">\n    <subfield code="a">"""+notaContenido+"""</subfield>\n  </datafield>\n  
        <datafield tag="506" ind1="1" ind2=" ">\n    <subfield code="a">Sin especificar</subfield>\n    <subfield code="f">Acceso online con previa autorización</subfield>\n  </datafield>\n  
        <datafield tag="508" ind1=" " ind2=" ">\n    <subfield code="a">"""+notaCreditos+"""</subfield>\n  </datafield>\n  
        <datafield tag="511" ind1="0" ind2=" ">\n    <subfield code="a">"""+notaElenco+"""</subfield>\n  </datafield>\n  
        <datafield tag="583" ind1=" " ind2=" ">\n    <subfield code="a">Catalogacion</subfield>\n    <subfield code="c">"""+fechaAccion+"""</subfield>\n    <subfield code="i">Se realiza el registro mínimo de metadatos de identificación y contenido del documento en el software bibliográfico Koha, estructurado bajo el formato MARC21, utilizando las normas AACR2, IASA, RDA y en concordancia con el manual interno de catalogación de Señal Memoria, establecido por el área de Gestión de Colecciones.</subfield>\n
        """+campoSeiscientos+"""
        <datafield tag="610" ind1=" " ind2=" ">\n    <subfield code="a"></subfield>\n    <subfield code="2"></subfield>\n  </datafield>\n    
        <subfield code="l">El archivo esta procesable</subfield>\n    <subfield code="k">"""+codigoCatalogador+"""</subfield>\n  </datafield>\n  
        <datafield tag="650" ind1=" " ind2="7">\n    <subfield code="a">"""+tema650+"""</subfield>\n    <subfield code=" "></subfield>\n  </datafield>\n  
        <datafield tag="653" ind1="0" ind2="2">\n    <subfield code="a">"""+palabraClave+"""</subfield>\n  </datafield>\n  
        <datafield tag="655" ind1=" " ind2="7">\n    <subfield code="2">Tesauro de Señal Memoria, RTVC</subfield>\n    <subfield code="a">"""+genero+"""</subfield>\n    <subfield code="v">"""+forma+"""</subfield>\n  </datafield>\n  
        <datafield tag="700" ind1="1" ind2=" ">\n    <subfield code="a"></subfield>\n    <subfield code="d"></subfield>\n    <subfield code="e"></subfield>\n  </datafield>\n
        <datafield tag="710" ind1="2" ind2=" ">\n    <subfield code="a"></subfield>\n    <subfield code="e"></subfield>\n  </datafield>\n
        <datafield tag="810" ind1="2" ind2=" ">\n    <subfield code="a"></subfield>\n  </datafield>\n
        <datafield tag="856" ind1="4" ind2="1">\n    <subfield code="u">"""+urlArchivo+"""</subfield>\n    <subfield code="y">"""+textoEnlace+"""</subfield>\n    <subfield code="a">"""+urlArchivoa+"""</subfield>\n    <subfield code="q">"""+tipoAoV+"""</subfield>\n  </datafield>\n
        <datafield tag="852" ind1="8" ind2="2">\n    <subfield code="a"></subfield>\n    <subfield code="h"></subfield>\n  </datafield>\n
        <datafield tag="856" ind1="4" ind2="1">\n    <subfield code="u"></subfield>\n    <subfield code="y"></subfield>\n    <subfield code="a"></subfield>\n    <subfield code="q"></subfield>\n  </datafield>\n  
        <datafield tag="942" ind1=" " ind2=" ">\n    <subfield code="2">z</subfield>\n    <subfield code="c">"""+tipoItem+"""</subfield>\n  </datafield>\n</record>
        """

        query1 = """INSERT INTO `biblio` (`biblionumber`, `frameworkcode`, `author`, `title`, `unititle`, `notes`, 
        `serial`, `seriestitle`, `copyrightdate`, `timestamp`, `datecreated`, `abstract`)
        VALUES ( %s, '%s', '%s', '%s', '%s', '%s', %i , '%s', %i, CURRENT_TIMESTAMP, '%s', '%s');
        """ % (biblio['biblionumber'], biblio['frameworkcode'],biblio['author'],biblio['title'], biblio['unititle'], biblio['notes'],
        biblio['serial'],biblio['seriestitle'],biblio['copyrightdate'], biblio['datecreated'], biblio['abstract'] )

        query2 = """INSERT INTO `biblioitems` (`biblioitemnumber`, `biblionumber`, `volume`, `number`, `itemtype`, 
        `isbn`, `issn`, `ean`, `publicationyear`, `publishercode`, `volumedate`, `volumedesc`, `collectiontitle`, `collectionissn`, `collectionvolume`, `editionstatement`, `editionresponsibility`, 
        `timestamp`,`illus`, `pages`, `notes`, `size`, `place`, `lccn`, `url`, `cn_source`, `cn_class`, `cn_item`, `cn_suffix`, `cn_sort`, `agerestriction`, `totalissues`,`marcxml`) 
        VALUES (%i, %i,'%s','%s','%s',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,
        CURRENT_TIMESTAMP,'%s','%s',NULL,'%s',NULL,NULL,'%s','%s', NULL, NULL, NULL ,'%s', NULL,NULL,'%s');
        """ % (resultado,resultado,biblioItems['volume'],biblioItems['number'],biblioItems['itemtype'],
        biblioItems['illus'],biblioItems['pages'],biblioItems['size'],biblioItems['url'],biblioItems['cn_source'],biblioItems['cn_sort'], xml)


        query3 = """ INSERT INTO `items` (`itemnumber`, `biblionumber`, `biblioitemnumber`, `barcode`, `dateaccessioned`, `booksellerid`, `homebranch`, `price`, `replacementprice`, `replacementpricedate`, 
        `datelastborrowed`, `datelastseen`, `stack`, `notforloan`, `damaged`, `itemlost`, `itemlost_on`, `withdrawn`, `withdrawn_on`, `itemcallnumber`, 
        `coded_location_qualifier`, `issues`, `renewals`, `reserves`, `restricted`, `itemnotes`, `itemnotes_nonpublic`, `holdingbranch`, `paidfor`, `timestamp`, 
        `location`, `permanent_location`, `onloan`, `cn_source`, `cn_sort`, `ccode`, `materials`, `uri`, `itype`, `more_subfields_xml`, 
        `enumchron`, `copynumber`, `stocknumber`, `new_status`) 
        VALUES (%i, %i, %i, NULL, '%s', '%s', NULL, NULL, NULL, '%s',
        NULL, '%s', NULL, %i, %i, %i, NULL, %i , NULL,'%s',
        NULL,NULL , NULL, NULL, NULL, NULL, NULL, NULL ,NULL,CURRENT_TIMESTAMP,
        '%s', '%s', NULL, '%s', '%s', NULL, NULL, NULL,'%s',NULL,
        NULL,NULL,NULL,NULL);
        """ % (resultado,resultado, resultado, items['dateaccessioned'], items['booksellerid'],  items['replacementpricedate'], 
        items['datelastseen'], items['notforloan'], items['damaged'], items['itemlost'], items['withdrawn'], items['itemcallnumber'],
        items['location'], items['permanent_location'], items['cn_source'] , items['cn_sort'], items['itype']  
        )


        queryInfo ="SELECT `biblionumber` FROM `biblio` WHERE 1"
        consulta = self.run_query(queryInfo)
        numbers =list(consulta)
        l= len(numbers) -1
        esta= True
        while l >= 0:
            if biblio['biblionumber'] in list(numbers[l]):
                esta = False
            l= l-1
        if esta:
            self.run_query(query1)
            self.run_query(query2)
            self.run_query(query3)
            proces = {"se agrego la ficha":resultado}
            return proces
        else:
            res = {"error":"el id de la ficha ya existe","codigo":403,"numero id de la ficha a insertar": biblio['biblionumber']}
            return res

        
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------


    def getJson(self, miniJson):
        num= miniJson['numero']
        queryInfo ="SELECT `biblionumber` FROM `biblio` WHERE 1"
        consulta = self.run_query(queryInfo)
        numbers =list(consulta)
        l= len(numbers) -1
        esta= False
        while l >= 0:
            if num in list(numbers[l]):
                esta = True
            l= l-1
        if esta:
            queryA = "SELECT * FROM `biblio` WHERE `biblionumber` = %i;"% num
            queryB = "SELECT * FROM `biblioitems` WHERE `biblionumber` = %i;"% num
            queryC = "SELECT * FROM `items` WHERE `biblionumber` = %i;"% num
            resultA = self.run_query(queryA)
            resultB = self.run_query(queryB)
            resultC = self.run_query(queryC)
            devJson = {
                "biblio":{    
                    "biblionumber": resultA[0][0],           
                    "frameworkcode": resultA[0][1],
                    "author": resultA[0][2],
                    "title": resultA[0][3] ,
                    "unititle": resultA[0][4],
                    "notes" : resultA[0][5],
                    "serial": resultA[0][6],
                    "seriestitle" : resultA[0][7],
                    "copyrightdate" : resultA[0][8],
                    "timestamp" : resultA[0][9],
                    "datecreated" : resultA[0][10],
                    "abstract" : resultA[0][11]      
                },

                        
                "biblioItems":{
                    "biblioitemnumber": resultB[0][0],
                    "biblionumber": resultB[0][1],
                    "volume": resultB[0][2],
                    "number": resultB[0][3],
                    "itemtype": resultB[0][4],
                    "isbn": resultB[0][5],
                    "issn": resultB[0][6],
                    "ean": resultB[0][7],
                    "publicationyear": resultB[0][8],
                    "publishercode": resultB[0][9],
                    "volumedate": resultB[0][10],
                    "volumedesc":resultB[0][11],
                    "collectiontitle": resultB[0][12],
                    "collectionissn": resultB[0][13],
                    "collectionvolume": resultB[0][14],
                    "editionstatement": resultB[0][15],
                    "editionresponsibility": resultB[0][16],
                    "timestamp": resultB[0][17],
                    "illus": resultB[0][18],
                    "pages":resultB[0][19],
                    "notes": resultB[0][20],
                    "size": resultB[0][21],
                    "place": resultB[0][22],
                    "lccn": resultB[0][23],
                    "marc": resultB[0][24],
                    "url": resultB[0][25],
                    "cn_source": resultB[0][26],
                    "cn_class": resultB[0][27],
                    "cn_item": resultB[0][28],
                    "cn_suffix": resultB[0][29],
                    "cn_sort": resultB[0][30],
                    "agerestriction": resultB[0][31],
                    "totalissues": resultB[0][32],
                    "marcxml": resultB[0][33]
                },
                
                "items": {
                    "itemnumber": resultC[0][0], 
                    "biblionumber": resultC[0][1],
                    "biblioitemnumber": resultC[0][2],
                    "barcode": resultC[0][3],
                    "dateaccessioned": resultC[0][4],
                    "booksellerid": resultC[0][5],
                    "homebranch": resultC[0][6],
                    "price": resultC[0][7],
                    "replacementprice": resultC[0][8],
                    "replacementpricedate": resultC[0][9],
                    "datelastborrowed": resultC[0][10],
                    "datelastseen": resultC[0][11],
                    "stack": resultC[0][12],
                    "notforloan": resultC[0][13],
                    "damaged": resultC[0][14],
                    "itemlost": resultC[0][15],
                    "itemlost_on": resultC[0][16],
                    "withdrawn": resultC[0][17],
                    "withdrawn_on": resultC[0][18],
                    "itemcallnumber": resultC[0][19],
                    "coded_location_qualifier": resultC[0][20],
                    "issues": resultC[0][21],
                    "renewals": resultC[0][22],
                    "reserves": resultC[0][23],
                    "restricted": resultC[0][24],
                    "itemnotes": resultC[0][25],
                    "itemnotes_nonpublic": resultC[0][26],
                    "holdingbranch": resultC[0][27],
                    "paidfor": resultC[0][28],
                    "timestamp": resultC[0][29],
                    "location": resultC[0][30],
                    "permanent_location": resultC[0][31],
                    "onloan": resultC[0][32],
                    "cn_source": resultC[0][33],
                    "cn_sort": resultC[0][34],
                    "ccode": resultC[0][35],
                    "materials": resultC[0][36],
                    "uri": resultC[0][37],
                    "itype": resultC[0][38],
                    "more_subfields_xml": resultC[0][39],
                    "enumchron": resultC[0][40],
                    "copynumber": resultC[0][41],
                    "stocknumber": resultC[0][42],
                    "new_status": resultC[0][43]
                }
            }
            return devJson
        else:
            res = {"error":"el numero del id de la ficha buscada no esta","codigo":403,"numero Buscado ":num}
            return res



#----------------------------------------------------------------------------
#----------------------------------
#----------------------------------------------------------------------
    def actualizar(self,datosActualizar):
        for key, value in datosActualizar.items():
            if key == "biblionumber":
                biblionumber = value
        try:
            stringXml = self.run_query('SELECT `marcxml` FROM `biblioitems` WHERE `biblioitems`.`biblionumber` = '+biblionumber)
        except:
            return {"error":"debe diligenciar el parametro de biblionumber"}
        try:
            xml = stringXml[0][0]
        except:
            return {"error":"el campo no existe, el biblionumber esta fuera de rango"}
        try:
            result = xml.find('<leader>')
            nuevo = xml[result:]
            result2 = nuevo.find('</leader>')
            for key, value in datosActualizar.items():
                if key == "encabezamiento":
                    nuevoXml = xml[0:result]+'<leader>'+ value +xml[result+result2:]
                    xml = nuevoXml  
        except:
            pass
        try:
            result = xml.find('tag="006">')
            nuevo = xml[result:]
            result2 = nuevo.find('</')
            for key, value in datosActualizar.items():
                if key == "caracteristicaseis":
                    nuevoXml = xml[0:result]+'tag="006">'+ value +xml[result+result2:]
                    xml = nuevoXml  
        except:
            pass
        try:
            result = xml.find('tag="007">')
            nuevo = xml[result:]
            result2 = nuevo.find('<')
            for key, value in datosActualizar.items():
                if key == "descripcionFisicaFijo":
                    nuevoXml = xml[0:result]+'tag="007">'+ value +xml[result+result2:]
                    xml = nuevoXml  
        except:
            pass
        try:
            result = xml.find('tag="008">')
            nuevo = xml[result:]
            result2 = nuevo.find('<')
            for key, value in datosActualizar.items():
                if key == "longitudFija":
                    nuevoXml = xml[0:result]+'tag="008">'+ value +xml[result+result2:]
                    xml = nuevoXml
        except:
            pass
        try:
            result = xml.find('tag="084"')
            nuevo = xml[result:]
            result2 = nuevo.find('</subfield>')
            for key, value in datosActualizar.items():
                if key == "numeroClasificacion":
                    nuevoXml = xml[0:result]+'tag="084" ind1=" " ind2=" ">\n    <subfield code="a">'+ value +xml[result+result2:]
                    xml = nuevoXml  
        except:
            pass
        try:
            result = xml.find('tag="243"')
            nuevo = xml[result:]
            result2 = nuevo.find('</subfield>')
            for key, value in datosActualizar.items():
                if key == "tituloUniforme":
                    nuevoXml = xml[0:result]+'tag="243" ind1="1" ind2="0">\n    <subfield code="a">'+ value +xml[result+result2:]
                    xml = nuevoXml  
        except:
            pass  
        try:
            result = xml.find('tag="245"')
            nuevo = xml[result:]
            result2 = nuevo.find('</subfield>')
            for key, value in datosActualizar.items():
                if key == "title":
                    nuevoXml = xml[0:result]+'tag="245" ind1="1" ind2="0">\n    <subfield code="a">'+ value +xml[result+result2:]
                    xml = nuevoXml  
        except:
            pass
        try:
            result = xml.find('tag="264"')
            nuevo = xml[result:]
            result2 = nuevo.find('</subfield>')
            for key, value in datosActualizar.items():
                if key == "lugarProduccion":
                    nuevoXml = xml[0:result]+'tag="264" ind1=" " ind2="0">\n    <subfield code="a">'+ value +xml[result+result2:]
                    xml = nuevoXml
        except:
            pass
        try:
            result = xml.find('tag="300"')
            nuevo = xml[result:]
            result2 = nuevo.find('</subfield>')
            for key, value in datosActualizar.items():
                if key == "descripcionFisica":
                    nuevoXml = xml[0:result]+'tag="300" ind1=" " ind2=" ">\n    <subfield code="a">'+ value +xml[result+result2:]
                    xml = nuevoXml
        except:
            pass
        try:
            result = xml.find('tag="336"')
            nuevo = xml[result:]
            result2 = nuevo.find('</subfield>')
            for key, value in datosActualizar.items():
                if key == "tipoContenido":
                    nuevoXml = xml[0:result]+'tag="336" ind1=" " ind2=" ">\n    <subfield code="a">'+ value +xml[result+result2:]
                    xml = nuevoXml
        except:
            pass
        try:
            result = xml.find('tag="490"')
            nuevo = xml[result:]
            result2 = nuevo.find('</subfield>')
            for key, value in datosActualizar.items():
                if key == "coleccion":
                    nuevoXml = xml[0:result]+'tag="490" ind1="0" ind2=" ">\n    <subfield code="a">'+ value +xml[result+result2:]
                    xml = nuevoXml
        except:
            pass
        try:
            result = xml.find('tag="500"')
            nuevo = xml[result:]
            result2 = nuevo.find('</subfield>')
            for key, value in datosActualizar.items():
                if key == "notaGeneral":
                    nuevoXml = xml[0:result]+'tag="500" ind1="0" ind2=" ">\n    <subfield code="a">'+ value +xml[result+result2:]
                    xml = nuevoXml
        except:
            pass
        try:
            result = xml.find('tag="505"')
            nuevo = xml[result:]
            result2 = nuevo.find('</subfield>')
            for key, value in datosActualizar.items():
                if key == "notaContenido":
                    nuevoXml = xml[0:result]+'tag="505" ind1="0" ind2=" ">\n    <subfield code="a">'+ value +xml[result+result2:]
                    xml = nuevoXml
        except:
            pass
        try:
            result = xml.find('tag="508"')
            nuevo = xml[result:]
            result2 = nuevo.find('</subfield>')
            for key, value in datosActualizar.items():
                if key == "notaCreditos":
                    nuevoXml = xml[0:result]+'tag="508" ind1=" " ind2=" ">\n    <subfield code="a">'+ value +xml[result+result2:]
                    xml = nuevoXml
        except:
            pass
        try:
            result = xml.find('tag="511"')
            nuevo = xml[result:]
            result2 = nuevo.find('</subfield>')
            for key, value in datosActualizar.items():
                if key == "notaElenco":
                    nuevoXml = xml[0:result]+'tag="511" ind1="0" ind2=" ">\n    <subfield code="a">'+ value +xml[result+result2:]
                    xml = nuevoXml
        except:
            pass
        try:
            result = xml.find('tag="650"')
            nuevo = xml[result:]
            result2 = nuevo.find('</subfield>')
            for key, value in datosActualizar.items():
                if key == "tema650":
                    nuevoXml = xml[0:result]+'tag="650" ind1=" " ind2="7">\n    <subfield code="a">'+ value +xml[result+result2:]
                    xml = nuevoXml
        except:
            pass
        try:
            result = xml.find('tag="653"')
            nuevo = xml[result:]
            result2 = nuevo.find('</subfield>')
            for key, value in datosActualizar.items():
                if key == "palabraClave" :
                    nuevoXml = xml[0:result]+'tag="653" ind1="0" ind2="2">\n    <subfield code="a">'+ value +xml[result+result2:]
                    xml = nuevoXml
        except:
            pass
        try:
            result = xml.find('<datafield tag="655" ind1=" " ind2="7">\n    <subfield code="2">Tesauro de Señal Memoria, RTVC</subfield>\n    <subfield code="a">')
            nuevo = xml[result:]
            result2 = nuevo.find('</subfield>')
            for key, value in datosActualizar.items():
                if key == "genero" :
                    nuevoXml = xml[0:result]+'<datafield tag="655" ind1=" " ind2="7">\n    <subfield code="2">Tesauro de Señal Memoria, RTVC</subfield>\n    <subfield code="a">'+ value +xml[result+result2:]
                    xml = nuevoXml
        except:
            pass
        try:
            result = xml.find('tag="856"')
            nuevo = xml[result:]
            result2 = nuevo.find('</subfield>')
            for key, value in datosActualizar.items():
                if key == "urlArchivo" :
                    nuevoXml = xml[0:result]+'tag="856" ind1="4" ind2="1">\n    <subfield code="u">'+ value +xml[result+result2:]
                    xml = nuevoXml
        except:
            pass

        query = ""

        for key, value in datosActualizar.items():
            queryEnviar = query
            queryEnviar = "UPDATE `biblio` SET "
            queryEnviar += "`{}`='{}'".format(key, value)
            queryEnviar += " WHERE `biblio`.`biblionumber` = "
            queryEnviar += datosActualizar['biblionumber']
            queryEnviar += ";"
            try:
                self.run_query(queryEnviar)
            except:
                pass
        
            
        for key, value in datosActualizar.items():
            queryEnviar = query
            queryEnviar = "UPDATE `biblioitems` SET `marcxml` = '"
            queryEnviar += xml
            queryEnviar += "' WHERE `biblioitems`.`biblionumber` = "
            queryEnviar += datosActualizar['biblionumber']
            queryEnviar += ";"
            try:
                self.run_query(queryEnviar)
            except:
                pass
        return {"ficha actualizada": biblionumber} 

