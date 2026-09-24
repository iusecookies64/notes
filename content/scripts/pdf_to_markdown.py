from pathlib import Path
from marker.converters.pdf import PdfConverter
from marker.models import create_model_dict
from marker.output import text_from_rendered

def convert_slide_pdf(pdf_path: str, output_dir: str):
    source_path = Path(pdf_path)
    vault_dest = Path(output_dir)
    vault_dest.mkdir(parents=True, exist_ok=True)

    # Load neural models for layout detection, OCR, and LaTeX equation recognition
    artifact_dict = create_model_dict()
    converter = PdfConverter(artifact_dict=artifact_dict, config={"disable_ocr": True})

    # Render PDF into structured elements
    print(f"Converting {source_path.name}...")
    rendered = converter(str(source_path))
    
    # Extract markdown text, metadata, and embedded images
    markdown_text, metadata, images = text_from_rendered(rendered)

    # Save extracted slide diagrams/figures
    for img_name, img in images.items():
        img_save_path = vault_dest / img_name
        img.save(img_save_path)

    # Save the final Markdown file
    md_file_path = vault_dest / f"{source_path.stem}.md"
    with open(md_file_path, "w", encoding="utf-8") as f:
        f.write(markdown_text)

    print(f"Conversion complete: {md_file_path} ({len(images)} images extracted)")

if __name__ == "__main__":
    # Point to your downloaded DDCA slide deck and target vault folder
    PDF_FILE = "./PDF Notes/l1.pdf"
    OUTPUT_FOLDER = "./Marker Converted"
    convert_slide_pdf(PDF_FILE, OUTPUT_FOLDER)