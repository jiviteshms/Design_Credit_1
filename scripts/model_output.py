import os
import json
from IndicPhotoOCR.ocr import OCR

# Initialize OCR system
ocr_system = OCR(verbose=True, identifier_lang="auto", device="cpu")

folder_path = "test_images/tamil"
valid_exts = {".jpg", ".jpeg", ".png", ".bmp", ".tiff"}

# Final JSON dictionary
ocr_results = {}

for filename in os.listdir(folder_path):
    if os.path.splitext(filename)[1].lower() in valid_exts:

        image_path = os.path.join(folder_path, filename)
        print(f"\n🔹 Processing: {filename}")

        result = ocr_system.ocr(image_path)

        words_raw, langs_raw = result  # unpack tuple

        # Flatten nested lists
        words = [w[0] for w in words_raw]
        langs = [l[0] for l in langs_raw]

        # Build word → lang mapping
        word_lang_map = {word: lang for word, lang in zip(words, langs)}

        # Add to global dictionary
        ocr_results[filename] = word_lang_map

        print(" OCR Output:", result)
        print("-" * 60)

# Save JSON
output_path = "ocr_output.json"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(ocr_results, f, ensure_ascii=False, indent=4)

print("\n✅ Saved OCR results to:", output_path)
 