from algorithms import process_sanitation_cuts, add_piece_by_cut, build_nested_structure, sort_level1_by_strip_height, sort_level2_by_strip_width
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
            width = float(board['sheetW'])
            height = float(board['sheetH'])
            cuts = board['cuts']
            parts = board['part']
    
            # Uso:
            # 1. Crear estructura cortes saneados
            level1, level2, level3, level4, level5, level6, parts = process_sanitation_cuts(cuts, parts, width, height, trim, saw_width)
            # print({'level1': level1, 'level2': level2, 'level3': level3, 'level4': level4, 'level5': level5, 'level6': level6})
            
            # 2. Agregar pieza por corte
            level1, level2, level3, level4, level5, level6 = add_piece_by_cut(level1, level2, level3, level4, level5, level6, parts, trim, saw_width)
            print({'level1': level1, 'level2': level2, 'level3': level3, 'level4': level4, 'level5': level5, 'level6': level6})

            # 3. Crear estructura anidada
            nested_structure = build_nested_structure(level1, level2, level3, level4, level5, level6)

            # 4. Ordenar y recalcular coordenadas en nivel 1
            # sorted_structure_level1 = sort_level1_by_strip_height(nested_structure, parts, trim, saw_width, 'asc')

            # 5. Ordenar y recalcular coordenadas en nivel 2
            # sorted_structure_level2 = sort_level2_by_strip_width(sorted_structure_level1, parts, trim, saw_width, 'asc')
            
            healthy_boards.append({
                **board,
                'cuts': nested_structure,
                'part': parts
            })
        
        healthy_material.append({
            **material,
            'layout': healthy_boards,
        })
        
    return healthy_material

if __name__ == "__main__":

    trim = 10
    saw_width = 4.4
    
    # result_optimization_path = os.path.join(os.path.dirname(__file__), 'data_apilado.json') # N:2318 - id:2690
    # result_optimization_path = os.path.join(os.path.dirname(__file__), 'data_order1.json') #N:2288 - id:2659
    result_optimization_path = os.path.join(os.path.dirname(__file__), 'data_order2.json') #N:2277 - id:2648
    # result_optimization_path = os.path.join(os.path.dirname(__file__), 'prueba3.json')
    
    with open(result_optimization_path, 'r') as json_file:
        result_optimization = json.load(json_file)
        healthy_material = generate_cuts_ordered(result_optimization, trim, saw_width)
        visualize_cutting_plan(healthy_material, saw_width)

        output_path = os.path.join(os.path.dirname(__file__), 'sorted_structure.json')
        try:
            json_str = json.dumps(healthy_material, indent=2, default=str)
            with open(output_path, 'w') as f:
                f.write(json_str)
                print("✅ JSON guardado correctamente.")
        except Exception as e:
            print("❌ Fallo en escritura:", e)