import os
import json
import shutil
from pathlib import Path
from PIL import Image
from tqdm import tqdm

# --- CONFIGURATION ---
PROJECT_ROOT = Path(__file__).resolve().parent
GALLERY_DIR = PROJECT_ROOT / "public" / "assets" / "gallery"
ARCHIVE_DIR = PROJECT_ROOT / "archive"
WEBP_QUALITY = 80

VALID_EXTENSIONS = {".jpg", ".jpeg", ".png", ".bmp", ".tiff"}

def optimize_gallery():
    if not GALLERY_DIR.exists():
        print(f"❌ Error: Gallery directory '{GALLERY_DIR}' does not exist.")
        return

    # Find all year folders (4 digits)
    year_folders = [
        d for d in GALLERY_DIR.iterdir()
        if d.is_dir() and d.name.isdigit() and len(d.name) == 4
    ]

    if not year_folders:
        print("ℹ️ No year folders found in the gallery.")
        return

    print(f"📂 Found years: {', '.join(sorted([d.name for d in year_folders]))}")

    # Gather all albums
    albums = []
    for year_folder in year_folders:
        for album_folder in year_folder.iterdir():
            if album_folder.is_dir() and not album_folder.name.startswith("."):
                albums.append(album_folder)

    if not albums:
        print("ℹ️ No albums found in the year folders.")
        return

    print(f"🚀 Found {len(albums)} albums. Scanning for images...\n")

    total_optimized = 0
    total_failed = 0

    for album_path in albums:
        year_name = album_path.parent.name
        album_name = album_path.name
        print(f"📁 Scanning album: {year_name}/{album_name}")

        # Gather all valid images in this album (ignoring .webp)
        image_files = [
            f for f in album_path.iterdir()
            if f.is_file() and f.suffix.lower() in VALID_EXTENSIONS
        ]

        if not image_files:
            print(f"  ℹ️ No images to optimize in this album.")
            continue

        # Prepare archive path for this album
        # Mirroring the public/assets/gallery structure in the project root archive folder
        album_archive_dir = ARCHIVE_DIR / "assets" / "gallery" / year_name / album_name
        album_archive_dir.mkdir(parents=True, exist_ok=True)

        print(f"  ⚡ Optimizing {len(image_files)} images...")
        processed_stems = set()

        for file_path in tqdm(image_files, desc=f"  Optimizing {album_name}", unit="img", leave=False):
            try:
                # 1. Open the original image
                with Image.open(file_path) as img:
                    # Convert RGBA/Palette images to RGB if saving to WebP to maintain compatibility
                    if img.mode in ("RGBA", "P"):
                        img = img.convert("RGB")
                    
                    # Define the new WebP path in the same folder
                    output_path = album_path / f"{file_path.stem}.webp"
                    
                    # 2. Save as optimized WebP
                    img.save(output_path, "WEBP", quality=WEBP_QUALITY, optimize=True)
                
                # Record successful stem conversion
                processed_stems.add(file_path.name.lower())

                # 3. Move the original file to the archive folder
                shutil.move(str(file_path), album_archive_dir / file_path.name)
                total_optimized += 1

            except Exception as e:
                print(f"\n  ❌ Failed to process {file_path.name}: {e}")
                total_failed += 1

        # 4. Update info.json if it exists
        json_path = album_path / "info.json"
        if json_path.exists():
            try:
                with open(json_path, "r", encoding="utf-8") as f:
                    meta = json.load(f)

                if "cover" in meta and meta["cover"]:
                    cover_filename = meta["cover"].strip()
                    # Check if the cover matches one of the processed files or has a valid extension
                    cover_path = Path(cover_filename)
                    if cover_path.suffix.lower() in VALID_EXTENSIONS:
                        new_cover = str(cover_path.with_suffix(".webp"))
                        meta["cover"] = new_cover
                        
                        with open(json_path, "w", encoding="utf-8") as f:
                            json.dump(meta, f, indent=2, ensure_ascii=False)
                        print(f"  ✏️ Updated info.json cover from '{cover_filename}' to '{new_cover}'")
            except Exception as e:
                print(f"  ❌ Error updating {json_path.name}: {e}")

    print(f"\n🎉 Done! Total optimized: {total_optimized}, Failed: {total_failed}")
    print(f"📦 Originals have been moved to '{ARCHIVE_DIR}'.")

if __name__ == "__main__":
    optimize_gallery()
