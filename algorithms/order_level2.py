from functools import cmp_to_key, partial

'''
  5. ORDENAMIENTO POR NIVEL 1
  FORMULA: Y2xf = (Y2xi - Y2(x-1)i) + Suma(Dprecedente_nuevo_orden) + SaneadoInicial, donde Htira_bruto = (Y2xi - Y2(x-1)i)
  ALGORITMO: Trata de identificar el y2 inicial y el y2 inicial de la pieza debajo de la actual, 
  luego una vez ordenado calcular la suma de alturas de las pizas antes de la actual
'''
def update_icuts(level, current_level, index = 0):
    """
    Actualiza recursivamente los iCuts
    """
    current_index = index
    for cut in level:
      cut['iCut'] = current_index
      name_next_level = f'level{current_level + 1}'
      if name_next_level in cut:
        idx = update_icuts(cut[name_next_level], current_level=current_level + 1, index=current_index + 1)
        current_index = idx + 1
    return current_index
          

def clear_fields_created(level2_sorted):
    """
    Limpia los campos creados en el proceso de ordenamiento
    """
    for cut in level2_sorted:
        del cut['previous_x2']
        del cut['width']

def recalculate_all_coordinates(level2_sorted, parts, trim, saw_width):
    """
    Recalcula coordenadas Y usando la fórmula y actualiza todos los cortes anidados
    """
    accumulated_widths = 0
    
    for cut2 in level2_sorted:
        # Aplicar fórmula
        new_x2 = round(cut2['width'] + accumulated_widths + (trim - saw_width/2), 2)
        old_x2 = cut2['x2']
        cut2['x1'] = new_x2
        cut2['x2'] = new_x2
        
        if cut2['nItem'] != 0: #ACA SOLO ACTUALIZARA LA PRIMERA PIEZA, SI HAY PIEZAS IGUALES EN EL MISMO TABLERO, ESTAS TIENEN DISTINTAS CORRDENADAS E IGUAL NUMERO DE ITEM, debe validarse tambien por antigua coordenada
          part = next((part for part in parts if part['nItem'] == cut2['nItem'] and round(part['x'] + part['width'] + saw_width/2, 2) == round(old_x2, 2)), None)
          part_width = part['width'] if part['rotated'] is False else part['length']
          part['x'] = round(new_x2 - part_width - saw_width/2, 2)
        
        # Actualizar todos los cortes anidados con la fórmula completa
        update_nested_coordinates_recursive(cut2, cut2, parts, accumulated_widths, trim, saw_width)
        
        accumulated_heights += cut2['width']
        
def update_nested_coordinates_recursive(cut_dict, cut_dict_nivel2, parts, accumulated_widths, trim, saw_width):
    """
    Actualiza recursivamente coordenadas Y1 y Y2 de los niveles hijos
    """
    for level_key in ['level3', 'level4', 'level5', 'level6']:
        if level_key in cut_dict:
            for cut in cut_dict[level_key]:
                # Aplicar la fórmula
                width_strip_x1 = cut['x1'] - cut_dict_nivel2['previous_x2']
                width_strip_x2 = cut['x2'] - cut_dict_nivel2['previous_x2']
                
                new_x1 = round(width_strip_x1 + accumulated_widths + (trim - saw_width/2), 2)
                new_x2 = round(width_strip_x2 + accumulated_widths + (trim - saw_width/2), 2)
                
                old_x2 = cut['x2']
                
                cut['x1'] = new_x1
                cut['x2'] = new_x2
                
                if cut['nItem'] != 0:
                  part = next((part for part in parts 
                               if part['nItem'] == cut['nItem']
                               and (round(part['x'] + part['width'] + saw_width/2, 2) if level_key == 'level4' or level_key == 'level6' else round(part['y'] + part['length'] + saw_width/2, 2)) == round(old_x2 if level_key == 'level4' or level_key == 'level6' else cut['y2'], 2)
                              ), None)
                  part_width = part['width'] if part['rotated'] is False else part['length']
                  part['x'] = round(new_x2 - part_width - saw_width/2, 2)
                
                # Recursión para niveles más profundos
                update_nested_coordinates_recursive(cut, cut_dict_nivel2, parts, accumulated_widths, trim, saw_width)  


def get_max_level_inner(cutLvl2):
    count_level = 2
    for level_key in ['level3', 'level4', 'level5', 'level6']:
        if level_key in cutLvl2:
            count_level += 1
    return count_level
            
    

def compare_cuts_lvl2(currentCut, nextCut, reverse_order):
    """Función de comparación personalizada"""
    
    # Cortes nivel 2 consecutivos que sacan pieza
    if currentCut['nItem'] != 0 and nextCut['nItem'] != 0:
        return nextCut['width'] - currentCut['width'] if reverse_order else currentCut['width'] - nextCut['width'];

    
    # Corte nivel 2 consecutivos, donde el primero saca pieza, pero el siguiente no
    if currentCut['nItem'] != 0 and nextCut['nItem'] == 0:
        return -1
    
    # Corte nivel 2 consecutivos, donde el primero no saca pieza, pero el siguiente sí
    if currentCut['nItem'] == 0 and nextCut['nItem'] != 0:
        return 1
    
    # Corte nivel 2 consecutivos que NO sacan piezas
    if currentCut['nItem'] == 0 and nextCut['nItem'] == 0:
        max_level_inner_current = get_max_level_inner(currentCut)
        
        max_level_inner_next = get_max_level_inner(nextCut)
        
        # Cortes internos del primero > segundo
        if max_level_inner_current > max_level_inner_next:
            return 1
        
        # Cortes internos del primero < segundo
        if max_level_inner_current < max_level_inner_next:
            return -1
        
        # Cortes internos iguales, orden por medida decreciente
        if max_level_inner_current == max_level_inner_next:
            return nextCut['width'] - currentCut['width'] if reverse_order else currentCut['width'] - nextCut['width'];
    
    return 0

def sort_level2_by_strip_width(nested_structure, parts, trim, saw_width, order='asc'):
    """
        Ordena nivel 2 por ancho de tiras horizontles y recalcula todas las coordenadas (tira igual partes en la horizontal)
    """
    # 1. Calcular ancho real de cada tira usando orden original
    for cutLvl1 in enumerate(nested_structure):
        if(cutLvl1['level2']):
            for i, cut in cutLvl1['level2']:
                if i == 0:
                    previous_x2 = round(trim - saw_width/2, 2)  # Primera tira no tiene precedente, pero si una coord inicio
                else:
                    previous_x2 = nested_structure[i-1]['x2']  # x1 de la tira anterior
                
                cut['previous_x2'] = previous_x2
                cut['width'] = round(cut['x2'] - previous_x2, 2) #width bruto = width_pieza + sawWidth_extremos_horizontales
            
            # 2. Ordenar por ancho de tira
            reverse_order = order.lower() == 'desc'
            
            comparator = partial(compare_cuts_lvl2, reverse_order)
            level2_sorted = sorted(cutLvl1['level2'], key=cmp_to_key(comparator))

            # 3. Recalcular todas las coordenadas de los cortes y piezas
            recalculate_all_coordinates(level2_sorted, parts, trim, saw_width)
        
            clear_fields_created(level2_sorted)
        
            update_icuts(level2_sorted, current_level=2, index=0)
            
            cutLvl1['level2'] = level2_sorted

    return nested_structure
