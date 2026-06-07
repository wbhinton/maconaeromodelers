import os
import json
import shutil
from pathlib import Path
from PIL import Image, ImageOps
from tqdm import tqdm

# --- CONFIGURATION ---
PROJECT_ROOT = Path(__file__).resolve().parent
GALLERY_DIR = PROJECT_ROOT / "public" / "assets" / "gallery"
ARCHIVE_DIR = PROJECT_ROOT / "archive"
WEBP_QUALITY = 80

VALID_EXTENSIONS = {".jpg", ".jpeg", ".png", ".bmp", ".tiff"}

def process_single_image(file_path: Path, output_path: Path):
    """Opens an image, corrects orientation based on EXIF, and saves as WebP."""
    with Image.open(file_path) as img:
        # Correct orientation using EXIF data (fixes rotated images)
        img = ImageOps.exif_transpose(img)
        
        # Convert RGBA/Palette images to RGB if saving to WebP to maintain compatibility
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")
        
        # Save as optimized WebP
        img.save(output_path, "WEBP", quality=WEBP_QUALITY, optimize=True)

def reprocess_archive():
    """Reprocesses already-archived original images to apply orientation fixes."""
    archive_gallery = ARCHIVE_DIR / "assets" / "gallery"
    if not archive_gallery.exists():
        print("ℹ️ No archived originals found to reprocess.")
        return

    print("🔄 Reprocessing already-archived original images to fix orientation...")
    
    # Find all year folders in archive
    year_folders = [
        d for d in archive_gallery.iterdir()
        if d.is_dir() and d.name.isdigit() and len(d.name) == 4
    ]

    total_reprocessed = 0
    total_failed = 0

    for year_folder in year_folders:
        year_name = year_folder.name
        for album_folder in year_folder.iterdir():
            if not album_folder.is_dir() or album_folder.name.startswith("."):
                continue
            
            album_name = album_folder.name
            target_album_path = GALLERY_DIR / year_name / album_name
            target_album_path.mkdir(parents=True, exist_ok=True)
            
            # Find all original images in archive
            image_files = [
                f for f in album_folder.iterdir()
                if f.is_file() and f.suffix.lower() in VALID_EXTENSIONS
            ]
            
            if not image_files:
                continue
            
            print(f"📁 Reprocessing {year_name}/{album_name}...")
            for file_path in tqdm(image_files, desc=f"  Fixing {album_name}", unit="img", leave=False):
                try:
                    output_path = target_album_path / f"{file_path.stem}.webp"
                    process_single_image(file_path, output_path)
                    total_reprocessed += 1
                except Exception as e:
                    print(f"\n  ❌ Failed to reprocess {file_path.name}: {e}")
                    total_failed += 1

    print(f"\n🎉 Finished re-orienting archived files! Total fixed: {total_reprocessed}, Failed: {total_failed}\n")

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

    print(f"🚀 Found {len(albums)} albums. Scanning for new images...\n")

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
            print(f"  ℹ️ No new images to optimize in this album.")
            continue

        # Prepare archive path for this album
        album_archive_dir = ARCHIVE_DIR / "assets" / "gallery" / year_name / album_name
        album_archive_dir.mkdir(parents=True, exist_ok=True)

        print(f"  ⚡ Optimizing {len(image_files)} images...")

        for file_path in tqdm(image_files, desc=f"  Optimizing {album_name}", unit="img", leave=False):
            try:
                # Define the new WebP path in the same folder
                output_path = album_path / f"{file_path.stem}.webp"
                
                # 1. Process and save
                process_single_image(file_path, output_path)
                
                # 2. Move the original file to the archive folder
                shutil.move(str(file_path), album_archive_dir / file_path.name)
                total_optimized += 1

            except Exception as e:
                print(f"\n  ❌ Failed to process {file_path.name}: {e}")
                total_failed += 1

        # 3. Update info.json if it exists
        json_path = album_path / "info.json"
        if json_path.exists():
            try:
                with open(json_path, "r", encoding="utf-8") as f:
                    meta = json.load(f)

                if "cover" in meta and meta["cover"]:
                    cover_filename = meta["cover"].strip()
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
    # First, run reprocessing to fix any orientation issues on already-archived images
    reprocess_archive()
    
    # Then, run standard optimization for any new files
    optimize_gallery()
