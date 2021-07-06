from typing import ItemsView
import os
import pymysql
import json

DB_HOST='remotemysql.com'
DB_USER='utF3rRuKY4'
DB_PASS='MuJSiLkxOz'
DB_NAME='utF3rRuKY4'
  


class koha():

    def run_query(self,query ): 
        conn = pymysql.connect(host= DB_HOST,user=  DB_USER, passwd= DB_PASS, db = DB_NAME) # Conectar a la base de datos 
        cursor = conn.cursor()         # Crear un cursor
        cursor.execute(query)          # Ejecutar una consulta
        if query.upper().startswith('SELECT'): 
            data = cursor.fetchall()   # Traer los resultados de un select 
        else: 
            conn.commit()              # Hacer efectiva la escritura de datos 
            data = None       
        cursor.close()                 # Cerrar el cursor 
        conn.close()                   # Cerrar la conexión 
        return data


    def insertJson(self, data: json):
        biblio = data['biblio']
        biblioItems = data['biblioItems']
        items = data['items']
        queryInfo ="SELECT `biblionumber` FROM `biblio` WHERE 1"
        consulta = self.run_query(queryInfo)
        numbers =list(consulta)
        l= len(numbers) -1
        noEsta= True
        while l >= 0:
            if biblio['biblionumber'] in list(numbers[l]):
                noEsta = False
            l= l-1
        if noEsta:
            query1 = """INSERT INTO `biblio` (`biblionumber`, `frameworkcode`, `author`, `title`, `unititle`, `notes`, 
            `serial`, `seriestitle`, `copyrightdate`, `timestamp`, `datecreated`, `abstract`)
            VALUES ( %i, '%s', '%s', '%s', '%s', '%s', %i , '%s', %i, '%s', '%s', '%s');
            """ % (biblio['biblionumber'], biblio['frameworkcode'],biblio['author'],biblio['title'], biblio['unititle'], biblio['notes'],
            biblio['serial'],biblio['seriestitle'],biblio['copyrightdate'],biblio['timestamp'], biblio['datecreated'], biblio['abstract'] )

            query2 = """INSERT INTO `biblioitems` (`biblioitemnumber`, `biblionumber`, `volume`, `number`, `itemtype`, `isbn`, `issn`, `ean`, `publicationyear`, `publishercode`, 
            `volumedate`, `volumedesc`, `collectiontitle`, `collectionissn`, `collectionvolume`, `editionstatement`, `editionresponsibility`, `timestamp`, `illus`, `pages`, 
            `notes`, `size`, `place`, `lccn`, `marc`, `url`, `cn_source`, `cn_class`, `cn_item`, `cn_suffix`, 
            `cn_sort`, `agerestriction`, `totalissues`, `marcxml`)       
            VALUES (%i, %i,'%s','%s','%s','%s','%s','%s','%s','%s',
            '%s','%s','%s','%s','%s','%s','%s','%s','%s','%s',
            '%s','%s','%s','%s','%s','%s','%s','%s','%s','%s',
            '%s', '%s', %i, %s);
            """ % (biblioItems['biblioitemnumber'], biblioItems['biblionumber'],biblioItems['volume'],biblioItems['number'],biblioItems['itemtype'],biblioItems['isbn'],biblioItems['issn'],biblioItems['ean'],biblioItems['publicationyear'],biblioItems['publishercode'],
            biblioItems['volumedate'],biblioItems['volumedesc'],biblioItems['collectiontitle'],biblioItems['collectionissn'],biblioItems['collectionvolume'], biblioItems['editionstatement'],biblioItems['editionresponsibility'],biblioItems['timestamp'], biblioItems['illus'],biblioItems['pages'],
            biblioItems['notes'],biblioItems['size'],biblioItems['place'],biblioItems['lccn'], biblioItems['marc'], biblioItems['url'],biblioItems['cn_source'],biblioItems['cn_class'],biblioItems['cn_item'],biblioItems['cn_suffix'],
            biblioItems['cn_sort'],biblioItems['agerestriction'],biblioItems['totalissues'],biblioItems['marcxml'] )

            query3 = """ INSERT INTO `items` (`itemnumber`, `biblionumber`, `biblioitemnumber`, `barcode`, `dateaccessioned`, `booksellerid`, `homebranch`, `price`, `replacementprice`, `replacementpricedate`, 
            `datelastborrowed`, `datelastseen`, `stack`, `notforloan`, `damaged`, `itemlost`, `itemlost_on`, `withdrawn`, `withdrawn_on`, `itemcallnumber`, 
            `coded_location_qualifier`, `issues`, `renewals`, `reserves`, `restricted`, `itemnotes`, `itemnotes_nonpublic`, `holdingbranch`, `paidfor`, `timestamp`, 
            `location`, `permanent_location`, `onloan`, `cn_source`, `cn_sort`, `ccode`, `materials`, `uri`, `itype`, `more_subfields_xml`, 
            `enumchron`, `copynumber`, `stocknumber`, `new_status`) 
            VALUES (%i, %i, %i, '%s', '%s', '%s', '%s', %i, %i, '%s',
            '%s', '%s', %i, %i, %i, %i, '%s', %i,'%s','%s',
            '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s','%s','%s',
            '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s','%s','%s',
            '%s','%s', '%s','%s');
            """ % (items['itemnumber'], items['biblionumber'],items['biblioitemnumber'],items['barcode'],items['dateaccessioned'], items['booksellerid'], items['homebranch'], items['price'], items['replacementprice'], items['replacementpricedate'], 
            items['datelastborrowed'], items['datelastseen'], items['stack'] , items['notforloan'], items['damaged'], items['itemlost'] , items['itemlost_on'], items['withdrawn'], items['withdrawn_on'], items['itemcallnumber'],
            items['coded_location_qualifier'], items['issues'] ,    items['renewals'], items['reserves'], items['restricted'], items['itemnotes'], items['itemnotes_nonpublic'], items['holdingbranch'],items['paidfor'], items['timestamp'], 
            items['location'], items['permanent_location'], items['onloan'], items['cn_source'] , items['cn_sort'],  items['ccode'],  items['materials'], items['uri'], items['itype'], items['more_subfields_xml'], 
            items['enumchron'], items['copynumber'],items['stocknumber'], items['new_status'] )

            self.run_query(query1)
            self.run_query(query2)
            self.run_query(query3)

            proces = {"proceso":"la ficha a sido agregaada correctamente"}
            return proces
        else:
            res = {"error":"el id de la ficha ya existe","codigo":403,"numero id de la ficha a insertar": biblio['biblionumber']}
            return res
        
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------


    def getJson(self, miniJson : json):
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

#--------------------------------------------------------------------
#--------------------------------------------------------------------
        
    def updateJson(self, actual: json):
        biblio = actual['biblio']
        biblioItems = actual['biblioItems']
        items = actual['items']
        num = biblio['biblionumber']
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
            queryP = """
            UPDATE `biblio`
            SET `frameworkcode`= '%s' ,`author`='%s',`title`='%s' ,`unititle`= '%s',`notes`='%s',        
            `serial`= %i,`seriestitle`='%s',`copyrightdate`= %i,`timestamp`= '%s',`datecreated`= '%s',`abstract`='%s'
            WHERE `biblionumber`= %i
            """% (    
                biblio['frameworkcode'],biblio['author'],biblio['title'], biblio['unititle'], biblio['notes'],
                biblio['serial'],biblio['seriestitle'],biblio['copyrightdate'],biblio['timestamp'], biblio['datecreated'], biblio['abstract'] ,
                num
            )
            queryS = """
            UPDATE `biblioitems`
            SET `biblioitemnumber`=%i,`volume`='%s',`number`='%s',`itemtype`='%s',
            `isbn`='%s',`issn`='%s',`ean`='%s',`publicationyear`='%s',`publishercode`='%s',
            `volumedate`='%s',`volumedesc`='%s',`collectiontitle`='%s',`collectionissn`='%s',`collectionvolume`='%s',
            `editionstatement`='%s',`editionresponsibility`='%s',`timestamp`='%s',`illus`='%s',`pages`='%s',
            `notes`='%s',`size`='%s',`place`='%s',`lccn`= '%s',`marc`= '%s',
            `url`= '%s',`cn_source`= '%s',`cn_class`= '%s',`cn_item`= '%s',`cn_suffix`= '%s',
            `cn_sort`= '%s' ,`agerestriction`= '%s' ,`totalissues`=%i,`marcxml`= '%s'
            WHERE `biblionumber`= %i
            """% (biblioItems['biblioitemnumber'], biblioItems['volume'],biblioItems['number'],biblioItems['itemtype'],biblioItems['isbn'],biblioItems['issn'],biblioItems['ean'],biblioItems['publicationyear'],biblioItems['publishercode'],
            biblioItems['volumedate'],biblioItems['volumedesc'],biblioItems['collectiontitle'],biblioItems['collectionissn'],biblioItems['collectionvolume'], biblioItems['editionstatement'],biblioItems['editionresponsibility'],biblioItems['timestamp'], biblioItems['illus'],biblioItems['pages'],
            biblioItems['notes'],biblioItems['size'],biblioItems['place'],biblioItems['lccn'], biblioItems['marc'], biblioItems['url'],biblioItems['cn_source'],biblioItems['cn_class'],biblioItems['cn_item'],biblioItems['cn_suffix'],
            biblioItems['cn_sort'],biblioItems['agerestriction'],biblioItems['totalissues'],biblioItems['marcxml'], num )

            
            queryT = """
            UPDATE `items` 
            SET `itemnumber`= %i,`biblioitemnumber`= %i,`barcode`='%s',`dateaccessioned`='%s',
            `booksellerid`='%s',`homebranch`='%s',`price`=%i,`replacementprice`=%i,`replacementpricedate`='%s',
            `datelastborrowed`='%s',`datelastseen`='%s',`stack`=%i,`notforloan`=%i,`damaged`=%i,
            `itemlost`= %i,`itemlost_on`='%s',`withdrawn`= %i,`withdrawn_on`='%s',`itemcallnumber`='%s',
            `coded_location_qualifier`='%s',`issues`='%s',`renewals`='%s',`reserves`='%s',`restricted`='%s',
            `itemnotes`='%s',`itemnotes_nonpublic`='%s',`holdingbranch`='%s',`paidfor`='%s',`timestamp`='%s',
            `location`='%s',`permanent_location`='%s',`onloan`='%s',`cn_source`='%s',`cn_sort`='%s',
            `ccode`='%s',`materials`='%s',`uri`='%s',`itype`='%s',`more_subfields_xml`='%s',
            `enumchron`='%s',`copynumber`='%s',`stocknumber`='%s',`new_status`='%s' 
            WHERE `biblionumber`= %i      
            """ % (items['itemnumber'],items['biblioitemnumber'],items['barcode'],items['dateaccessioned'], items['booksellerid'], items['homebranch'], items['price'], items['replacementprice'], items['replacementpricedate'], 
            items['datelastborrowed'], items['datelastseen'], items['stack'] , items['notforloan'], items['damaged'], items['itemlost'] , items['itemlost_on'], items['withdrawn'], items['withdrawn_on'], items['itemcallnumber'],
            items['coded_location_qualifier'], items['issues'] ,    items['renewals'], items['reserves'], items['restricted'], items['itemnotes'], items['itemnotes_nonpublic'], items['holdingbranch'],items['paidfor'], items['timestamp'], 
            items['location'], items['permanent_location'], items['onloan'], items['cn_source'] , items['cn_sort'],  items['ccode'],  items['materials'], items['uri'], items['itype'], items['more_subfields_xml'], 
            items['enumchron'], items['copynumber'],items['stocknumber'], items['new_status'], num)

            self.run_query(queryP)
            self.run_query(queryS)
            self.run_query(queryT)
            return {"proceso":"informacion actualizada exitosamente"}
        else:
            res = {"error":"la ficha a actualizar no se encuenta anteriormente registrada","codigo":403,"numero id buscado":num}
            return res
            
        
    def crearTabla (self):
        queryC = """
        CREATE TABLE biblio (
        biblionumber int NOT NULL,
        frameworkcode varchar(255) NOT NULL,
        author varchar(255) DEFAULT NULL,
        title varchar(255) DEFAULT NULL,
        unititle varchar(255) DEFAULT NULL,
        notes varchar(255) DEFAULT NULL,
        serial int DEFAULT NULL,
        seriestitle varchar(255) DEFAULT NULL,
        copyrightdate int(255) DEFAULT NULL,
        timestamp varchar(255) DEFAULT NULL,
        datecreated varchar(255) DEFAULT NULL,
        abstract varchar(255) DEFAULT NULL
        );

        CREATE TABLE biblioitems (
        biblioitemnumber int DEFAULT NULL,
        biblionumber int DEFAULT NULL,
        volume varchar(255) DEFAULT NULL,
        number varchar(255) DEFAULT NULL,
        itemtype varchar(255) DEFAULT NULL,
        isbn varchar(255) DEFAULT NULL,
        issn varchar(255) DEFAULT NULL,
        ean varchar(255) DEFAULT NULL,
        publicationyear varchar(255) DEFAULT NULL,
        publishercode varchar(255) DEFAULT NULL,
        volumedate varchar(255) DEFAULT NULL,
        volumedesc varchar(255) DEFAULT NULL,
        collectiontitle varchar(255) DEFAULT NULL,
        collectionissn varchar(255) DEFAULT NULL,
        collectionvolume varchar(255) DEFAULT NULL,
        editionstatement varchar(255) DEFAULT NULL,
        editionresponsibility varchar(255) DEFAULT NULL,
        timestamp varchar(255) DEFAULT NULL,
        illus varchar(255) DEFAULT NULL,
        pages varchar(255) DEFAULT NULL,
        notes varchar(255) DEFAULT NULL,
        size varchar(255) DEFAULT NULL,
        place varchar(255) DEFAULT NULL,
        lccn varchar(255) DEFAULT NULL,
        marc varchar(255) DEFAULT NULL,
        url varchar(255) DEFAULT NULL,
        cn_source varchar(255) DEFAULT NULL,
        cn_class varchar(255) DEFAULT NULL,
        cn_item varchar(255) DEFAULT NULL,
        cn_suffix varchar(255) DEFAULT NULL,
        cn_sort varchar(255) DEFAULT NULL,
        agerestriction varchar(255) DEFAULT NULL,
        totalissues int DEFAULT NULL,
        marcxml varchar(255) DEFAULT NULL
        );


        CREATE TABLE items (
        itemnumber int DEFAULT NULL,
        biblionumber int DEFAULT NULL,
        biblioitemnumber int DEFAULT NULL,
        barcode varchar(255) DEFAULT NULL,
        dateaccessioned varchar(255) DEFAULT NULL,
        booksellerid varchar(255) DEFAULT NULL,
        homebranch varchar(255) DEFAULT NULL,
        price int DEFAULT NULL,
        replacementprice int DEFAULT NULL,
        replacementpricedate varchar(255) DEFAULT NULL,
        datelastborrowed varchar(255) DEFAULT NULL,
        datelastseen varchar(255) DEFAULT NULL,
        stack int DEFAULT NULL,
        notforloan int DEFAULT NULL,
        damaged int DEFAULT NULL,
        itemlost int DEFAULT NULL,
        itemlost_on varchar(255) DEFAULT NULL,
        withdrawn int DEFAULT NULL,
        withdrawn_on varchar(255) DEFAULT NULL,
        itemcallnumber varchar(255) DEFAULT NULL,
        coded_location_qualifier varchar(255) DEFAULT NULL,
        issues varchar(255) DEFAULT NULL,
        renewals varchar(255) DEFAULT NULL,
        reserves varchar(255) DEFAULT NULL,
        restricted varchar(255) DEFAULT NULL,
        itemnotes varchar(255) DEFAULT NULL,
        itemnotes_nonpublic varchar(255) DEFAULT NULL,
        holdingbranch varchar(255) DEFAULT NULL,
        paidfor varchar(255) DEFAULT NULL,
        timestamp varchar(255) DEFAULT NULL,
        location varchar(255) DEFAULT NULL,
        permanent_location varchar(255) DEFAULT NULL,
        onloan varchar(255) DEFAULT NULL,
        cn_source varchar(255) DEFAULT NULL,
        cn_sort varchar(255) DEFAULT NULL,
        ccode varchar(255) DEFAULT NULL,
        materials varchar(255) DEFAULT NULL,
        uri varchar(255) DEFAULT NULL,
        itype varchar(255) DEFAULT NULL,
        more_subfields_xml varchar(255) DEFAULT NULL,
        enumchron varchar(255) DEFAULT NULL,
        copynumber varchar(255) DEFAULT NULL,
        stocknumber varchar(255) DEFAULT NULL,
        new_status varchar(255) DEFAULT NULL
        ) ; """
        self.run_query(queryC)
        print("listo")
        return 0




