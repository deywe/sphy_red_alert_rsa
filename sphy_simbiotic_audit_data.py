import py5
import pandas as pd
import numpy as np
import hashlib

# --- CONFIGURAÇÕES DE ESTADO ---
df = None
current_frame = 0
max_frames = 0
found_keys = []
zoom = -800
rot_x, rot_y = 0.5, 0.0
pan_x, pan_y = 0, 0

def settings():
    py5.size(1920, 1080, py5.P3D)

def setup():
    global df, max_frames
    py5.get_surface().set_resizable(True)
    try:
        # Carrega o dataset gerado pelo script 1
        df = pd.read_parquet("sphy_audit_data.parquet")
        max_frames = df['frame'].max()
        print(f"Dataset carregado: {max_frames + 1} frames prontos para auditoria.")
    except Exception as e:
        print(f"Erro ao carregar Parquet: {e}")
        py5.exit_sketch()
    
    py5.frame_rate(60)

def draw():
    global current_frame, rot_y
    py5.background(5, 5, 10)
    
    # --- SISTEMA DE CÂMERA INTERATIVA ---
    py5.translate(py5.width/2 + pan_x, py5.height/2 + pan_y, zoom)
    py5.rotate_x(rot_x)
    py5.rotate_y(rot_y + (current_frame * 0.003)) # Rotação base lenta
    
    # Iluminação Nítida
    py5.ambient_light(60, 60, 70)
    py5.point_light(255, 255, 255, 500, -500, 500)

    # 1. NÚCLEO (A TERRA)
    py5.push_matrix()
    py5.no_stroke()
    py5.fill(0, 100, 255)
    py5.sphere(150)
    py5.pop_matrix()

    # 2. CAMPO ELETROMAGNÉTICO (WIRE)
    py5.no_fill()
    py5.stroke(0, 255, 255, 60) # Wireframe ciano nítido
    py5.stroke_weight(1.5)
    py5.sphere(350) 

    # 3. PROCESSAMENTO DE DADOS DO PARQUET
    frame_data = df[df['frame'] == current_frame]
    valid_hash = validate_frame(frame_data)
    
    for _, row in frame_data.iterrows():
        # Coordenadas extraídas do dataset
        x, y, z = row['x']*350, row['y']*350, row['z']*350
        
        py5.push_matrix()
        py5.translate(x, y, z)
        py5.no_stroke()
        
        if row['rsa_factor'] == 1:
            # Qubit em ressonância (Fator RSA encontrado no dataset)
            py5.fill(255, 255, 0)
            py5.emissive(255, 255, 0)
            py5.sphere(22)
            if row['rsa_key_found'] not in found_keys:
                found_keys.insert(0, row['rsa_key_found'])
        else:
            # Qubits de busca estáveis
            py5.fill(0, 255, 255)
            py5.emissive(0, 100, 100)
            py5.sphere(10)
            
        py5.pop_matrix()
        py5.stroke(0, 255, 255, 35)
        py5.line(0, 0, 0, x, y, z) # Conexão ao núcleo

    # 4. INTERFACE DE SOBERANIA (HUD)
    draw_ui(valid_hash)
    
    # Avanço do log de frames
    if current_frame < max_frames:
        current_frame += 1
    else:
        current_frame = 0

def validate_frame(f_data):
    """Re-calcula o SHA-256 para auditar a integridade do Parquet em tempo real."""
    stored_hash = f_data['sha256_audit'].iloc[0]
    base_data = f_data.drop(columns=['sha256_audit']).to_dict('records')
    calc_hash = hashlib.sha256(str(base_data).encode()).hexdigest()
    return calc_hash == stored_hash

def draw_ui(is_valid):
    py5.hint(py5.DISABLE_DEPTH_TEST)
    py5.camera()
    
    # Banner Q-DAY Pulsante (Fonte 40, Nítida)
    pulse = (np.sin(py5.millis() * 0.003) + 1) / 2
    py5.fill(0)
    py5.rect(0, 0, py5.width, 100)
    py5.fill(255 * pulse, 255 * pulse, 0)
    py5.text_align(py5.CENTER)
    py5.text_size(40)
    py5.text("Q-DAY HAS ARRIVED, THIS IS A REAL ALERT", py5.width/2, 65)
    
    # Painel de Auditoria Lateral (Chaves em Fonte 26)
    py5.fill(0, 0, 0, 220)
    py5.stroke(0, 255, 255)
    py5.stroke_weight(3)
    py5.rect(py5.width - 600, 150, 550, 800)
    
    py5.fill(255, 255, 0)
    py5.text_size(36)
    py5.text("RSA KEYS RECOVERED", py5.width - 325, 205)
    py5.line(py5.width - 550, 225, py5.width - 100, 225)
    
    py5.text_align(py5.LEFT)
    py5.text_size(26)
    for i, key in enumerate(found_keys[:15]):
        py5.fill(255, 255, 0)
        py5.text(f"KEY: {key}", py5.width - 550, 280 + (i * 45))
        
    # Rodapé de Integridade
    py5.fill(0, 255, 150) if is_valid else py5.fill(255, 0, 0)
    py5.text_size(20)
    status = "AUDIT: SHA-256 VERIFIED" if is_valid else "AUDIT: CORRUPTED DATA!"
    py5.text(f"FRAME: {current_frame} | {status} | FIELD: rsa_factor", 50, py5.height - 50)
    
    py5.hint(py5.ENABLE_DEPTH_TEST)

# --- CONTROLES INTERATIVOS ---
def mouse_dragged():
    global rot_x, rot_y, pan_x, pan_y
    if py5.mouse_button == py5.LEFT:
        rot_y += (py5.mouse_x - py5.pmouse_x) * 0.01
        rot_x -= (py5.mouse_y - py5.pmouse_y) * 0.01
    elif py5.mouse_button == py5.CENTER:
        pan_x += (py5.mouse_x - py5.pmouse_x)
        pan_y += (py5.mouse_y - py5.pmouse_y)

def mouse_wheel(event):
    global zoom
    zoom -= event.get_count() * 70

def mouse_dragged_extra():
    global zoom
    if py5.mouse_button == py5.RIGHT:
        zoom += (py5.mouse_y - py5.pmouse_y) * 5

py5.mouse_dragged = mouse_dragged

if __name__ == "__main__":
    py5.run_sketch()
