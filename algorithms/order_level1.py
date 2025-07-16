'''
  5. ORDENAMIENTO POR NIVEL 1
  FORMULA: Y2xf = (Y2xi - Y2(x-1)i) + Suma(Dprecedente_nuevo_orden) + SaneadoInicial, donde Htira_bruto = (Y2xi - Y2(x-1)i)
  ALGORITMO: Trata de identificar el y2 inicial y el y2 inicial de la pieza debajo de la actual, 
  luego una vez ordenado calcular la suma de alturas de las pizas antes de la actual
'''
def update_icuts(level, current_level = 1, index = 0):
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
          

def clear_fields_created(level1_sorted):
    """
    Limpia los campos creados en el proceso de ordenamiento
    """
    for cut in level1_sorted:
        del cut['previous_y2']
        del cut['height']

def recalculate_all_coordinates(level1_sorted, parts, trim, saw_width):
    """
    Recalcula coordenadas Y usando la fórmula y actualiza todos los cortes anidados
    """
    accumulated_heights = 0
    
    for cut1 in level1_sorted:
        # Aplicar fórmula
        new_y2 = round(cut1['height'] + accumulated_heights + (trim - saw_width/2), 2)
        old_y2 = cut1['y2']
        cut1['y1'] = new_y2
        cut1['y2'] = new_y2
        
        if cut1['nItem'] != 0: #ACA SOLO ACTUALIZARA LA PRIMERA PIEZA, SI HAY PIEZAS IGUALES EN EL MISMO TABLERO, ESTAS TIENEN DISTINTAS CORRDENADAS E IGUAL NUMERO DE ITEM, debe validarse tambien por antigua coordenada
          part = next((part for part in parts if part['nItem'] == cut1['nItem'] and round(part['y'] + part['height'] + saw_width/2, 2) == round(old_y2, 2)), None)
          part_height = part['length'] if part['rotated'] is False else part['width']
          part['y'] = round(new_y2 - part_height - saw_width/2, 2)
        
        # Actualizar todos los cortes anidados con la fórmula completa
        update_nested_coordinates_recursive(cut1, cut1, parts, accumulated_heights, trim, saw_width)
        
        accumulated_heights += cut1['height']
        
def update_nested_coordinates_recursive(cut_dict, cut_dict_nivel1, parts, accumulated_heights, trim, saw_width):
    """
    Actualiza recursivamente coordenadas Y1 y Y2 de los niveles hijos
    """
    for level_key in ['level2', 'level3', 'level4', 'level5', 'level6']:
        if level_key in cut_dict:
            for cut in cut_dict[level_key]:
                # Aplicar la fórmula
                height_strip_y1 = cut['y1'] - cut_dict_nivel1['previous_y2']
                height_strip_y2 = cut['y2'] - cut_dict_nivel1['previous_y2']
                
                new_y1 = round(height_strip_y1 + accumulated_heights + (trim - saw_width/2), 2)
                new_y2 = round(height_strip_y2 + accumulated_heights + (trim - saw_width/2), 2)
                
                old_y2 = cut['y2']
                
                cut['y1'] = new_y1
                cut['y2'] = new_y2
                
                if cut['nItem'] != 0:
                  part = next((part for part in parts 
                               if part['nItem'] == cut['nItem']
                               and (round(part['y'] + (part['length'] if part['rotated'] is False else part['width']) + saw_width/2, 2) if level_key == 'level3' or level_key == 'level5' else round(part['x'] + (part['width'] if part['rotated'] is False else part['length']) + saw_width/2, 2)) == round(old_y2 if level_key == 'level3' or level_key == 'level5' else cut['x2'], 2)
                              ), None)
                  part_height = part['length'] if part['rotated'] is False else part['width']
                  part['y'] = round(new_y2 - part_height - saw_width/2, 2)
                
                # Recursión para niveles más profundos
                update_nested_coordinates_recursive(cut, cut_dict_nivel1, parts, accumulated_heights, trim, saw_width)  



def sort_level1_by_strip_height(nested_structure, parts, trim, saw_width, order='asc'):
  """
  Ordena nivel 1 por altura de tiras y recalcula todas las coordenadas
  """
    
  # 1. Calcular altura real de cada tira usando orden original
  for i, cut in enumerate(nested_structure):
    if i == 0:
      previous_y2 = round(trim - saw_width/2, 2)  # Primera tira no tiene precedente, pero si una coord inicio
    else:
      previous_y2 = nested_structure[i-1]['y2']  # Y2 de la tira anterior
        
    cut['previous_y2'] = previous_y2
    cut['height'] = round(cut['y2'] - previous_y2, 2) #height bruto = height_pieza + sawWidth_extremos_verticales
    
  # 2. Ordenar por altura de tira
  reverse_order = order.lower() == 'desc'

  level1_sorted = sorted(nested_structure, key=lambda cut: cut['height'], reverse=reverse_order)

  # 3. Recalcular todas las coordenadas de los cortes y piezas
  recalculate_all_coordinates(level1_sorted, parts, trim, saw_width)
  
  clear_fields_created(level1_sorted)
  
  update_icuts(level1_sorted, current_level=1, index=0)
    
  return level1_sorted

