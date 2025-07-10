def add_missing_cuts_from_internal(level1, level2, level3, level4, level5, level6, x1, x2, y1, y2):
    '''
        1. CASO DONDE EL ULTIMO CORTE NO EXISTE, PERO SI EXISTE CORTES INTERNOS
    '''
    
    # LEVEL 1 CREADO, CASO DONDE EL NIVEL 1 ESTA EN EXTREMO DE LA ALTURA DEL TABLERO Y HAY LEVEL 2 INTERNOS
    for cutLvl2 in level2:
        if float(cutLvl2['y2']) == y2: 
            level1.append({
                "stockNo": "",
                "iCut": "",
                "x1": x1,
                "y1": y1,
                "x2": x2,
                "y2": y2,
                "aLevel": 1
            })
                

    # LEVEL 2 CREADO, CASO DONDE EL NIVEL 2 ESTA EN EXTREMO DEL ANCHO DEL TABLERO EN UNA TIRA Y HAY LEVEL 3 INTERNOS
            ##puede haber un caso donde un lvl2 previo no exista y se deba saber el lvl1 actual para tener el y2, es poco probable porque el optimizador lo consideraria lvl1
    for cutLvl3 in level3:
        if float(cutLvl3['x2']) == x2: 
            lastCutLvl2 = next((cutLvl2 for cutLvl2 in level2 if cutLvl2["x1"] == cutLvl3["x1"] and cutLvl2['y1'] <= cutLvl3['y2'] and cutLvl2['y2'] >= cutLvl3['y2']), None)
            if lastCutLvl2 is not None:
                level2.append({
                    "stockNo": "",
                    "iCut": "",
                    "x1": x2,
                    "y1": lastCutLvl2['y1'],
                    "x2": x2,
                    "y2": lastCutLvl2['y2'],
                    "aLevel": 2
                })
            
    # LEVEL 3 CREADO, CASO DONDE EL NIVEL 3 ESTA EN EXTREMO DEL ALTO DE LA TIRA DONDE SE ENCUENTRA, CONINCIDIENTO CON EL NIVEL 1 PREVIO, Y HAY NIVELES INTERNOS LEVEL 4
            ##puede haber un caso donde un lvl3 previo no exista y se deba saber el lvl1 previo para tener el y1, es poco probable porque el optimizador lo consideraria lvl2
    for cutLvl4 in level4:
        for cutLvl1 in level1:
            if cutLvl4['y2'] == cutLvl1["y2"]: 
                lastCutLvl3 = next((cutLvl3 for cutLvl3 in level3 if cutLvl3["y1"] == cutLvl4["y1"] and cutLvl3['x1'] <= cutLvl4['x1'] and cutLvl3['x2'] >= cutLvl4['x2']), None)
                if lastCutLvl3 is not None:
                    level3.append({
                        "stockNo": "",
                        "iCut": "",
                        "x1": lastCutLvl3['x1'],
                        "y1": cutLvl4['y2'],
                        "x2": lastCutLvl3['x2'],
                        "y2": cutLvl4['y2'],
                        "aLevel": 3
                    })

    # LEVEL 4 CREADO, CASO DONDE EL NIVEL 4 ESTA EN EXTREMO DEL ANCHO, CONINCIDIENTO CON EL NIVEL 2 PREVIO,  Y HAY NIVELES INTERNOS LEVEL 5
            ##puede haber un caso donde un lvl4 previo no exista y se deba saber el lvl2 previo para tener el y1, es poco probable porque el optimizador lo consideraria lvl3
    for cutLvl5 in level5:
        for cutLvl2 in level2:
            if cutLvl5['x2'] == cutLvl2["x2"]: 
                lastCutLvl4 = next((cutLvl4 for cutLvl4 in level4 if cutLvl4["x1"] == cutLvl5["x1"] and cutLvl4['y1'] <= cutLvl5['y1'] and cutLvl4['y2'] >= cutLvl5['y2']), None)
                if lastCutLvl4 is not None:
                    level4.append({
                        "stockNo": "",
                        "iCut": "",
                        "x1": cutLvl5['x2'],
                        "y1": lastCutLvl4['y1'],
                        "x2": cutLvl5['x2'],
                        "y2": lastCutLvl4['y2'],
                        "aLevel": 4
                    })

    # LEVEL 5 CREADO, CASO DONDE EL NIVEL 5 ESTA EN EXTREMO DEL ALTO, CONINCIDIENTO CON EL NIVEL 3 PREVIO,  Y HAY NIVELES INTERNOS LEVEL 6
            ##puede haber un caso donde un lvl5 previo no exista y se deba saber el lvl3 previo para tener el x1 y x2, es poco probable porque el optimizador lo consideraria lvl3
    for cutLvl6 in level6:
        for cutLvl3 in level3:
            if cutLvl6['y2'] == cutLvl3["y2"]: 
                lastCutLvl5 = next((cutLvl5 for cutLvl5 in level5 if cutLvl5["y1"] == cutLvl6["y1"] and cutLvl5['x1'] <= cutLvl6['x1'] and cutLvl5['x2'] >= cutLvl6['x2']), None)
                if lastCutLvl5 is not None:
                    level5.append({
                        "stockNo": "",
                        "iCut": "",
                        "x1": lastCutLvl5['x1'],
                        "y1": cutLvl6['y2'],
                        "x2": lastCutLvl5['x2'],
                        "y2": cutLvl6['y2'],
                        "aLevel": 5
                    })

    #REVISARRRRRRRR
    # LEVEL 6 CREADO, CASO DONDE EL NIVEL 6 ESTA EN EXTREMO DE LA HORIZONTAL, CONINCIDIENTO CON EL NIVEL 4 PREVIO
            ##puede haber un caso donde un lvl5 previo no exista y se deba saber el lvl3 previo para tener el y1, es poco probable porque el optimizador lo consideraria lvl3
    for cutLvl6 in level6:
        for cutLvl5 in level5:
            if cutLvl6['y2'] == cutLvl5["y2"]: 
                lastCutLvl6 = next((cutLvl6 for cutLvl6 in level6 if cutLvl6["y2"] == cutLvl5["y2"] and cutLvl5['x1'] <= cutLvl6['x1'] and cutLvl5['x2'] >= cutLvl6['x2']), None)
                if lastCutLvl6 is not None:
                    level6.append({
                        "stockNo": "",
                        "iCut": "",
                        "x1": cutLvl5['x2'],
                        "y1": lastCutLvl6['y1'],
                        "x2": cutLvl5['x2'],
                        "y2": lastCutLvl6['y2'],
                        "aLevel": 6
                    })

def add_missing_cuts_from_parts(level1, level2, level3, level4, level5, level6, parts, saw_width, x1, x2, y1, y2):
    '''
        2. CASOS DONDE EL CORTE NO EXISTE PORQUE ESTA AL EXTREMO, PERO SACAN PIEZAS DIRECTAMENTE
        Los part['y'] es la coordenada superior izquierda de la pieza neta, es decir sin saneado inicial
    '''
    ## LEVEL 1 CREADO, PORQUE ESTE GENERA UNA PIEZA DIRECTAMENTE
    for part in parts:
        part_length = part['length'] if part['rotated'] == False else part['width']
        if round(part['y'] + part_length + saw_width/2, 2) == round(y2, 2):
            level1.append({
                "stockNo": "",
                "iCut": "",
                "x1": x1,
                "y1": y2,
                "x2": x2,
                "y2": y2,
                "aLevel": 1
            })
        
    # LEVEL 2 CREADO, PORQUE ESTE GENERA UNA PIEZA DIRECTAMENTE
    for part in parts:
        part_width = part['width'] if part['rotated'] == False else part['length']
        part_length = part['length'] if part['rotated'] == False else part['width']
        if round(part['x'] + part_width + saw_width/2, 2) == round(x2, 2):
            level2.append({
                "stockNo": "",
                "iCut": "",
                "x1": x2,
                "y1": round(part['y'] - saw_width/2, 2),
                "x2": x2,
                "y2": round(part['y'] + part_length + saw_width/2, 2),
                "aLevel": 2
            })

    # LEVEL 3 CREADO, PORQUE ESTE GENERA UNA PIEZA DIRECTAMENTE
    for part in parts:
        part_width = part['width'] if part['rotated'] == False else part['length']
        part_length = part['length'] if part['rotated'] == False else part['width']
        for cutLvl2 in level2:
            #garantiza que el corte que genera la pieza no es nivel 2, sino que es nivel 3 y falta crear
            exist_cutLvl3 = any(cut for cut in level3 if cut['x2'] == cutLvl2['x2'] and cut['y1'] > cutLvl2['y1'] and cut['y2'] < cutLvl2['y2'])
            
            if round(part['y'] + part_length + saw_width/2, 2) == round(cutLvl2['y2'], 2) and exist_cutLvl3:
                level3.append({
                    "stockNo": "",
                    "iCut": "",
                    "x1": round(part['x'] - saw_width/2, 2),                                           
                    "y1": cutLvl2['y2'],                                  
                    "x2": round(part['x'] + part_width + saw_width/2, 2),
                    "y2": cutLvl2['y2'],                                  
                    "aLevel": 3
                })

    # LEVEL 4 CREADO, PORQUE ESTE GENERA UNA PIEZA DIRECTAMENTE
    for part in parts:
        part_width = part['width'] if part['rotated'] == False else part['length']
        part_length = part['length'] if part['rotated'] == False else part['width']
        for cutLvl3 in level3:
            #garantiza que el corte que genera la pieza no es nivel 3, sino que es nivel 4 y falta crear
            exist_cutLvl4 = any(cut for cut in level4 if cut['y2'] == cutLvl3['y2'] and cut['x2'] > cutLvl3['x1'] and cut['x2'] < cutLvl3['x2'])
            
            if round(part['x'] + part_width + saw_width/2, 2) == round(cutLvl3['x2'], 2) and exist_cutLvl4:
                level4.append({
                    "stockNo": "",
                    "iCut": "",
                    "x1": cutLvl3['x2'],                                 
                    "y1": round(part['y'] - saw_width/2, 2),                                     
                    "x2": cutLvl3['x2'],                               
                    "y2": round(part['y'] + part_length + saw_width/2, 2), 
                    "aLevel": 4
                })
        
    # LEVEL 5 CREADO, PORQUE ESTE GENERA UNA PIEZA DIRECTAMENTE
    for part in parts:
        part_width = part['width'] if part['rotated'] == False else part['length']
        part_length = part['length'] if part['rotated'] == False else part['width']
        for cutLvl4 in level4:
            #garantiza que el corte que genera la pieza no es nivel 4, sino que es nivel 5 y falta crear
            exist_cutLvl5 = any(cut for cut in level5 if cut['x2'] == cutLvl4['x2'] and cut['y1'] > cutLvl4['y1'] and cut['y2'] < cutLvl4['y2'])
            
            if round(part['y'] + part_length + saw_width/2, 2) == round(cutLvl4['y2'], 2) and exist_cutLvl5:
                level5.append({
                    "stockNo": "",
                    "iCut": "",
                    "x1": round(part['x'] - saw_width/2, 2),                                      
                    "y1": cutLvl4['y2'],                            
                    "x2": round(part['x'] + part_width + saw_width/2, 2), 
                    "y2": cutLvl4['y2'],                          
                    "aLevel": 5
                })

    # LEVEL 6 CREADO, PORQUE ESTE GENERA UNA PIEZA DIRECTAMENTE
    for part in parts:
        part_width = part['width'] if part['rotated'] == False else part['length']
        part_length = part['length'] if part['rotated'] == False else part['width']
        for cutLvl5 in level5:
            #garantiza que el corte que genera la pieza no es nivel 4, sino que es nivel 5 y falta crear
            exist_cutLvl6 = any(cut for cut in level6 if cut['y2'] == cutLvl5['y2'] and cut['x2'] > cutLvl5['x1'] and cut['x2'] < cutLvl5['x2'])
            
            if round(part['x'] + part_width + saw_width/2, 2) == round(cutLvl5['x2'], 2) and exist_cutLvl6:
                level6.append({
                    "stockNo": "",
                    "iCut": "",
                    "x1": cutLvl5['x2'],                           
                    "y1": round(part['y'] - saw_width/2, 2),                                
                    "x2": cutLvl5['x2'],                             
                    "y2": round(part['y'] + part_length + saw_width/2, 2),
                    "aLevel": 6
                })
        
def generate_cut_sequential(level1, level2, level3, level4, level5, level6):
    '''
        AGREGANDO iCut a los cortes creados, combinando todos los niveles y asignar iCut secuencial
    '''
    all_cuts = level1 + level2 + level3 + level4 + level5 + level6
    for i, cut in enumerate(all_cuts):
        cut['iCut'] = i


def process_sanitation_cuts(cuts, parts, width, height, trim, saw_width):
    """
    Procesa los datos de corte y sanea los cortes faltantes

    Args:
        cuts: Json de diccionario con datos del tablero
        saw_width: Ancho de la sierra
        trim: Margen de recorte
        width: Ancho del tablero
        height: Alto del tablero
    
    Returns:
        list: Lista de todos los cortes (level1 + level2 + level3 + level4 + level6 + level6)
    """
    x1 = round(trim - saw_width/2, 2)
    x2 = round(width - trim + saw_width/2, 2)
    y1 = round(trim - saw_width/2, 2)
    y2 = round(height - trim + saw_width/2, 2)
    
    parts = [ {
        **part,
        "stockNo": float(part["stockNo"]),
        "part": float(part["part"]),
        "x": float(part["x"]),
        "y": float(part["y"]),
        "length": float(part["length"]),
        "width": float(part["width"]),
        "rotated": False if part["rotated"] == 'False' else True
        } for part in parts
    ]
    
    cuts = [ {
        "stockNo": cut["stockNo"],
        "iCut": cut["iCut"],
        "x1": float(cut["x1"]),
        "y1": float(cut["y1"]),
        "x2": float(cut["x2"]),
        "y2": float(cut["y2"]),
        "aLevel": int(cut["aLevel"]) + 1
        } for cut in cuts
    ]

    # print(cuts)

    level1 = [ cut for cut in cuts if cut['aLevel'] == 1 ]
    level2 = [ cut for cut in cuts if cut['aLevel'] == 2 ]
    level3 = [ cut for cut in cuts if cut['aLevel'] == 3 ]
    level4 = [ cut for cut in cuts if cut['aLevel'] == 4 ]
    level5 = [ cut for cut in cuts if cut['aLevel'] == 5 ]
    level6 = [ cut for cut in cuts if cut['aLevel'] == 6 ]

    # print({'level1': level1, 'level2': level2, 'level3': level3, 'level4': level4, 'level5': level5, 'level6': level6})
    
    add_missing_cuts_from_internal(level1, level2, level3, level4, level5, level6, x1, x2, y1, y2)
   
    add_missing_cuts_from_parts(level1, level2, level3, level4, level5, level6, parts, saw_width, x1, x2, y1, y2)

    generate_cut_sequential(level1, level2, level3, level4, level5, level6)
    
    return level1, level2, level3, level4, level5, level6, parts