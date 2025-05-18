import os

def generate_files():
    # --- CONFIGURATION ---
    TARGET_FOLDER = r"D:\Creations\Other projects\git reps\contestmoji\list" # ← CHANGE TO YOUR FOLDER
    CSS_OUTPUT = ".emoji_css.txt"
    HTML_OUTPUT = ".emoji_html.txt"
    
    # --- SAFETY CHECKS ---
    if not os.path.exists(TARGET_FOLDER):
        print(f"❌ Error: Folder doesn't exist: {TARGET_FOLDER}")
        return
    
    # Get SVG files
    svg_files = [
        f for f in os.listdir(TARGET_FOLDER)
        if f.lower().endswith('.svg') 
        and os.path.isfile(os.path.join(TARGET_FOLDER, f))
    ]
    
    if not svg_files:
        print("❌ No SVG files found in the folder!")
        return
    
    # --- GENERATE CSS FILE ---
    css_path = os.path.join(TARGET_FOLDER, CSS_OUTPUT)
    with open(css_path, 'w', encoding='utf-8') as css_file:
        for filename in svg_files:
            name = os.path.splitext(filename)[0]
            css_rule = f"""i.md-e-{name.lower()} {{\n    background-image: url('https://macestudios.ru/contestmoji/list/{name}.svg');\n}}\n"""
            css_file.write(css_rule)
    
    # --- GENERATE HTML FILE ---
    html_path = os.path.join(TARGET_FOLDER, HTML_OUTPUT)
    with open(html_path, 'w', encoding='utf-8') as html_file:
        for filename in svg_files:
            name = os.path.splitext(filename)[0]
            html_entry = f'<div class="md-e-div"><p><i class="md-e md-e-{name.lower()}"></i> - {name.lower()}</p></div>\n'
            html_file.write(html_entry)
    
    # --- RESULTS ---
    print(f"✅ Successfully generated:")
    print(f"CSS: {css_path}")
    print(f"HTML: {html_path}")
    print(f"Processed {len(svg_files)} emoji files")

if __name__ == "__main__":
    generate_files()