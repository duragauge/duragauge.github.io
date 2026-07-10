#!/usr/bin/env python3
"""
Hugo Image Audit Script - Final HTML Scanner (per-path)
For each image under static/img, search if its web path appears anywhere in the HTML.
"""

import os

# Configuration
PROJECT_ROOT = r"C:\Users\Nolan Mitchell\Documents\GitHub\duragauge.github.io"
DOCS_DIR = os.path.join(PROJECT_ROOT, "docs")      # Hugo output directory
STATIC_IMG_DIR = os.path.join(PROJECT_ROOT, "static", "img")

IMAGE_EXTENSIONS = {".svg", ".jpg", ".jpeg", ".png", ".gif", ".webp"}


def get_all_images_in_directory(img_dir):
    """
    Get all image files in static/img and subdirectories.
    Each entry is keyed by its relative path under static/img, e.g. 'ch1/example.png'.
    """
    images = {}
    if not os.path.exists(img_dir):
        print(f"Warning: {img_dir} does not exist")
        return images

    for root, dirs, files in os.walk(img_dir):
        for filename in files:
            ext = os.path.splitext(filename)[1].lower()
            if ext in IMAGE_EXTENSIONS:
                rel_path = os.path.relpath(os.path.join(root, filename), img_dir)
                rel_path = rel_path.replace(os.sep, "/")  # web uses forward slashes
                key = rel_path.lower()
                images[key] = {
                    "relative_path": rel_path,   # e.g. 'ch1/example.png'
                    "filename": filename.lower(),
                    "used": False,
                    "used_by_basename_only": False,  # in case only basename match is found
                }
    return images


def load_all_html(docs_dir):
    """Load all HTML files into one giant string (lowercased for searching)."""
    all_html = []
    file_count = 0

    for root, dirs, files in os.walk(docs_dir):
        for file in files:
            if file.endswith(".html"):
                file_count += 1
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                        all_html.append(f.read())
                except Exception as e:
                    print(f"Error reading {filepath}: {e}")

    html_text = "\n".join(all_html)
    return html_text.lower(), file_count


def main():
    print("=" * 70)
    print("HUGO IMAGE AUDIT - FINAL HTML SCANNER (PER-PATH)")
    print("=" * 70)
    print()

    # Gather images
    print(f"Scanning images in: {STATIC_IMG_DIR}")
    images = get_all_images_in_directory(STATIC_IMG_DIR)
    print(f"Found {len(images)} image files in static/img\n")

    # Load HTML
    print(f"Loading HTML files from: {DOCS_DIR}")
    all_html_lower, html_file_count = load_all_html(DOCS_DIR)
    print(f"Found {html_file_count} HTML files\n")

    # First pass: look for full /img/<relative-path> usage
    print("Searching for images in HTML...")
    for key, data in images.items():
        rel_path = data["relative_path"].lower()  # 'ch1/example.png'
        # typical Hugo static path: '/img/ch1/example.png' or 'img/ch1/example.png'
        needle1 = f"/img/{rel_path}"
        needle2 = f"img/{rel_path}"

        if needle1 in all_html_lower or needle2 in all_html_lower:
            data["used"] = True

    # Optional second pass: basename search for images that still look unused.
    # This can catch cases where Hugo transforms the filename (e.g. fingerprints),
    # but may give false positives if you reuse filenames in different folders.
    for key, data in images.items():
        if data["used"]:
            continue
        basename = data["filename"]  # just 'example.png'
        if basename and basename in all_html_lower:
            data["used"] = True
            data["used_by_basename_only"] = True

    used_images = [img for img in images.values() if img["used"]]
    unused_images = [img for img in images.values() if not img["used"]]

    print()
    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(f"Total images in static/img: {len(images)}")
    print(f"Images found in HTML: {len(used_images)}")
    print(f"Unused images: {len(unused_images)}")
    if images:
        print(f"Usage rate: {len(used_images) / len(images) * 100:.1f}%")
        print(f"Math check: {len(images)} - {len(used_images)} = {len(unused_images)}")
    print()

    # Group unused images by top-level folder
    export_file = os.path.join(PROJECT_ROOT, "unused_images.txt")
    if unused_images:
        print("=" * 70)
        print("UNUSED IMAGES")
        print("=" * 70)
        print()

        folder_images = {}
        for img_data in unused_images:
            path = img_data["relative_path"]  # 'ch1/example.png'
            parts = path.split("/")
            folder = parts[0] if len(parts) > 1 else "(root)"
            folder_images.setdefault(folder, []).append(path)

        with open(export_file, "w", encoding="utf-8") as f:
            f.write("UNUSED IMAGES (Based on HTML search)\n")
            f.write("=" * 70 + "\n\n")
            f.write(f"Total unused: {len(unused_images)}\n\n")

            for folder in sorted(folder_images.keys()):
                images_in_folder = sorted(folder_images[folder])
                f.write(f"{folder}/ ({len(images_in_folder)} files):\n")
                for img_path in images_in_folder:
                    f.write(f"  - {img_path}\n")
                f.write("\n")

        # Print a preview to console
        for folder in sorted(folder_images.keys()):
            images_in_folder = sorted(folder_images[folder])
            print(f"{folder}/ ({len(images_in_folder)} files):")
            for img_path in images_in_folder[:10]:
                print(f"  - {img_path}")
            if len(images_in_folder) > 10:
                print(f"  ... and {len(images_in_folder) - 10} more")
            print()

        print("=" * 70)
        print(f"Full list exported to: {export_file}")
        print()
    else:
        print("No unused images found!\n")


if __name__ == "__main__":
    main()
