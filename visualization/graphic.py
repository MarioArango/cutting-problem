import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.lines as mlines

def draw_cut_lines(ax, cuts, scale=1.0, saw_width=4.4):
    offset = (saw_width / 2) * scale

    def draw_single_cut(x1, y1, x2, y2, is_retal=False):
        base_color = 'blue' if is_retal else 'black'
        aux_color = 'blue' if is_retal else 'gray'

        ax.plot([x1, x2], [y1, y2], linestyle='--', color=base_color, linewidth=0.5)

        if x1 == x2:  # vertical
            ax.plot([x1 + offset, x2 + offset], [y1, y2], linestyle='-', color=aux_color, linewidth=0.4, alpha=0.5)
            ax.plot([x1 - offset, x2 - offset], [y1, y2], linestyle='-', color=aux_color, linewidth=0.4, alpha=0.5)
        elif y1 == y2:  # horizontal
            ax.plot([x1, x2], [y1 + offset, y2 + offset], linestyle='-', color=aux_color, linewidth=0.4, alpha=0.5)
            ax.plot([x1, x2], [y1 - offset, y2 - offset], linestyle='-', color=aux_color, linewidth=0.4, alpha=0.5)

    def recursive_draw(cut_list):
        for cut in cut_list:
            is_retal = cut.get("type", "").lower() == "retal"

            x1 = cut["x1"] * scale
            y1 = cut["y1"] * scale
            x2 = cut["x2"] * scale
            y2 = cut["y2"] * scale

            draw_single_cut(x1, y1, x2, y2, is_retal=is_retal)

            # Si es retal y tiene aLevel, dibuja el texto
            if is_retal and "aLevel" in cut:
                cx = (x1 + x2) / 2
                cy = (y1 + y2) / 2
                ax.text(cx, cy, str(cut["aLevel"]), fontsize=8, ha='center', va='center', color='blue', weight='bold')

            if "level2" in cut:
                recursive_draw(cut["level2"])
            if "level3" in cut:
                recursive_draw(cut["level3"])

    recursive_draw(cuts)

def visualize_cutting_plan(data, saw_width, plano_index=0, scale=0.3):
    # Paleta de colores fija
    custom_colors = [
        '#d1ffd6', '#ffc759', '#e8ffc7', '#ffdb52', '#ebffb5', '#ffd67a', '#ffc7a8', '#ffedbd',
        '#cfffe6', '#ffba91', '#e0ff96', '#ffdec2', '#fff08c', '#d7ffd7', '#edffe6', '#fde2cd',
        '#d1eaf9', '#d0f3ee', '#dcd9f8', '#f7d8c3', '#d7ffff', '#ffc8c3', '#a9e5e3', '#fae087',
        '#d8f79a', '#e8ba86', '#a2edce', '#afd7ff', '#afffaf', '#d0f3ee', '#f4d1f4', '#fafda4',
        '#ded6f8', '#fdd1fd', '#fcf0e4', '#d9edf6', '#d787af', '#d787d7', '#d7af5f', '#d7af87',
        '#d7afaf', '#d7d787', '#d7d7ff', '#d7ffff', '#ffe870', '#ffd7af', '#ffd7ff', '#ffff87', '#ffffd7'
    ]

    for group in data:  # Recorre cada material/color
        planos = group['layout']
        saw_width_local = float(group['layoutResume']['sawWidth']) if group['layoutResume']['sawWidth'] is not None else saw_width

        for plano_index, plano in enumerate(planos):
            parts = plano['part']
            cuts = plano.get('cuts', [])
            width = float(plano['sheetW']) * scale
            height = float(plano['sheetH']) * scale

            unique_nitems = sorted(set(p['nItem'] for p in parts))
            color_by_nitem = {n: custom_colors[i % len(custom_colors)] for i, n in enumerate(unique_nitems)}

            fig, ax = plt.subplots(figsize=(12, 8))
            ax.set_xlim(0, width)
            ax.set_ylim(height, 0)
            ax.set_aspect('equal')
            ax.set_title(f"Plano {plano_index + 1} - Material: {plano['material']}", fontsize=10, pad=15)

            ax.add_patch(patches.Rectangle((0, 0), width, height, fill=False, edgecolor='black', linewidth=1))

            for part in parts:
                x = float(part['x']) * scale
                y = float(part['y']) * scale
                w = (float(part['width']) if part['rotated'] is False else float(part['length'])) * scale
                h = (float(part['length']) if part['rotated'] is False else float(part['width'])) * scale

                type_value = part.get('type', '').lower()
                nItem = part.get('nItem', 0)

                # Determinar color
                if type_value == 'retal':
                    color = '#d3d3d3'  # Gris claro
                else:
                    color = color_by_nitem.get(nItem, '#ffffff')  # Fallback blanco

                # Dibujar pieza
                ax.add_patch(patches.Rectangle((x, y), w, h, linewidth=0.5, edgecolor='black', facecolor=color))

                # Texto principal centrado
                label_text = "R" if type_value == 'retal' else f"{nItem}"
                ax.text(x + w / 2, y + h / 2, label_text, ha='center', va='center', fontsize=10, weight='bold')

                # Texto dimensiones siempre
                ax.text(x + 2, y + 10, f"{int(h / scale)} x {int(w / scale)}", ha='left', va='top', fontsize=6)

            draw_cut_lines(ax, cuts, scale=scale, saw_width=saw_width_local)

            ax.axis('off')
            ax.text(
                width / 2, -10,
                f"{int(width / scale)} mm x {int(height / scale)} mm",
                ha='center', va='top', fontsize=9, weight='bold'
            )

            plt.tight_layout()
            plt.show()