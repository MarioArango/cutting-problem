from algorithms import clean_optimization, process_sanitation_cuts, add_piece_by_cut, build_nested_structure, destroy_nested_build, rearrange_pieces, sort_level1_by_strip_height, sort_level2_by_strip_width, add_retal_cut_pieces
from visualization import visualize_cutting_plan
import json
import os


def generate_cuts_ordered(result_optimization, trim, saw_width):
    healthy_material = []    
    for material in result_optimization:

        lTrim_value = material.get('layoutResume', {}).get('lTrim', trim)
        trim = float(lTrim_value) if lTrim_value is not None else trim

        saw_width_value = material.get('layoutResume', {}).get('sawWidth', saw_width)
        saw_width = float(saw_width_value) if saw_width_value is not None else saw_width
        
        healthy_boards = []
        for board in material['layout']:
    
            # Uso:
            # 1. Extraer las medidas, cortes y piezas del tablero
            level1, level2, level3, level4, level5, level6, parts, x1, x2, y1, y2 = clean_optimization(board, trim, saw_width)
            print(parts)
            # 2. Crear estructura cortes saneados
            level1, level2, level3, level4, level5, level6, parts = process_sanitation_cuts(level1, level2, level3, level4, level5, level6, parts, saw_width, x1, x2, y1, y2)
            # print({'level1': level1, 'level2': level2, 'level3': level3, 'level4': level4, 'level5': level5, 'level6': level6})
            
            # 3. Agregar pieza por corte
            level1, level2, level3, level4, level5, level6 = add_piece_by_cut(level1, level2, level3, level4, level5, level6, parts, trim, saw_width)
            # print({'level1': level1, 'level2': level2, 'level3': level3, 'level4': level4, 'level5': level5, 'level6': level6})

            # 4. Crear estructura anidada
            nested_structure = build_nested_structure(level1, level2, level3, level4, level5, level6)

            # 5. Ordenar y recalcular coordenadas en nivel 1
            # sorted_structure_level1, parts = sort_level1_by_strip_height(nested_structure, parts, trim, saw_width, 'asc')
            # print(sorted_structure_level1)
            
            # 6. Ordenar y recalcular coordenadas en nivel 2
            # sorted_structure_level2, parts = sort_level2_by_strip_width(sorted_structure_level1, parts, trim, saw_width, 'asc')
            # print(sorted_structure_level2)
            
            # 7. Agregar piezas y cortes de retal
            sorted_structure_with_retal = add_retal_cut_pieces(nested_structure, parts, saw_width, x1, x2, y1, y2)
            
            healthy_boards.append({
                **board,
                'cuts': sorted_structure_with_retal,
                'part': parts
            })
        
        healthy_material.append({
            **material,
            'layout': healthy_boards,
        })
        
    return healthy_material

def generate_rearrange_pieces(result_optimization, trim, saw_width):
    healthy_material = []    
    for material in result_optimization:

        lTrim_value = material.get('layoutResume', {}).get('lTrim', trim)
        trim = float(lTrim_value) if lTrim_value is not None else trim

        saw_width_value = material.get('layoutResume', {}).get('sawWidth', saw_width)
        saw_width = float(saw_width_value) if saw_width_value is not None else saw_width
        
        healthy_boards = []
        for board in material['layout']:
            # 1. Extraer las medidas, cortes y piezas del tablero
            level1, level2, level3, level4, level5, level6, parts, x1, x2, y1, y2 = clean_optimization(board, trim, saw_width)
                    
            # 1. Mejorar el acodo de piezas que  pueden entrar en un retal
            structure_rearrange = rearrange_pieces(result_optimization, parts, saw_width, x1, x2, y1, y2)

if __name__ == "__main__":

    trim = 10
    saw_width = 4.4
    
    # result_optimization_path = os.path.join(os.path.dirname(__file__), 'data_order1.json') #N:2288 - id:2659
    # result_optimization_path = os.path.join(os.path.dirname(__file__), 'data_order2.json') #N:2277 - id:2648
    
    result_optimization_path = os.path.join(os.path.dirname(__file__), 'prueba1.json')
    # result_optimization_path = os.path.join(os.path.dirname(__file__), 'prueba1_vertical.json')
    
    # result_optimization_path = os.path.join(os.path.dirname(__file__), 'prueba2.json')
    # result_optimization_path = os.path.join(os.path.dirname(__file__), 'prueba2_vertical.json')
    
    
    # result_optimization_path = os.path.join(os.path.dirname(__file__), 'prueba3.json')
    # result_optimization_path = os.path.join(os.path.dirname(__file__), 'prueba3_vertical.json')
    
    # result_optimization_path = os.path.join(os.path.dirname(__file__), 'prueba4.json')
    # result_optimization_path = os.path.join(os.path.dirname(__file__), 'prueba4_vertical.json')
    
    # result_optimization_path = os.path.join(os.path.dirname(__file__), 'prueba5.json')
    # result_optimization_path = os.path.join(os.path.dirname(__file__), 'prueba5_vertical.json')
    
    # result_optimization_path = os.path.join(os.path.dirname(__file__), 'prueba6.json')
    # result_optimization_path = os.path.join(os.path.dirname(__file__), 'prueba6_vertical.json')
    
    # result_optimization_path = os.path.join(os.path.dirname(__file__), 'prueba7.json')
    # result_optimization_path = os.path.join(os.path.dirname(__file__), 'prueba7_vertical.json')
    
    # result_optimization_path = os.path.join(os.path.dirname(__file__), 'prueba8.json')
    # result_optimization_path = os.path.join(os.path.dirname(__file__), 'prueba8_vertical.json')
    
    # result_optimization_path = os.path.join(os.path.dirname(__file__), 'prueba9.json')
    # result_optimization_path = os.path.join(os.path.dirname(__file__), 'prueba10.json')
    # result_optimization_path = os.path.join(os.path.dirname(__file__), 'prueba11.json')
    # result_optimization_path = os.path.join(os.path.dirname(__file__), 'prueba12.json')
    # result_optimization_path = os.path.join(os.path.dirname(__file__), 'prueba13.json')
    # result_optimization_path = os.path.join(os.path.dirname(__file__), 'prueba14.json')
    # result_optimization_path = os.path.join(os.path.dirname(__file__), 'prueba15.json')#apilado 2
    
    # result_optimization_path = os.path.join(os.path.dirname(__file__), 'prueba16.json')#apilado 3
    # result_optimization_path = os.path.join(os.path.dirname(__file__), 'prueba16_sin_alg_apilado.json')#apilado 3
    
    with open(result_optimization_path, 'r') as json_file:
        result_optimization = json.load(json_file)
        
        # healthy_material = generate_cuts_ordered(result_optimization, trim, saw_width)
        
        healthy_material = generate_rearrange_pieces(result_optimization, trim, saw_width)
        
        visualize_cutting_plan(healthy_material, saw_width)

        output_path = os.path.join(os.path.dirname(__file__), 'sorted_structure.json')
        try:
            json_str = json.dumps(healthy_material, indent=2, default=str)
            with open(output_path, 'w') as f:
                f.write(json_str)
                print("✅ JSON guardado correctamente.")
        except Exception as e:
            print("❌ Fallo en escritura:", e)