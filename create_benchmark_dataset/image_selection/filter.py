import csv
import os
import shutil

def copy_images_from_csv(csv_file_path, destination_folder, column_index=0):
    """
    Copies image files listed in a CSV file to a specified destination folder.

    Args:
        csv_file_path (str): Path to the CSV file containing image paths.
        destination_folder (str): Folder where images will be copied.
        column_index (int): Which column of the CSV contains the file paths.
                            Default is 0 (first column).
    """

    # Create the destination folder if it doesn't exist
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
        print(f"Created folder: {destination_folder}")

    missing = 0
    copied = 0

    with open(csv_file_path, "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)

        for row in reader:
            if len(row) <= column_index:
                continue
            
            image_path = "images/" + row[column_index].strip()

            if os.path.isfile(image_path):
                try:
                    shutil.copy(image_path, destination_folder)
                    copied += 1
                except Exception as e:
                    print(f"Error copying {image_path}: {e}")
            else:
                print(f"File not found: {image_path}")
                missing += 1

    print("\nSummary:")
    print(f"Copied: {copied} images")
    print(f"Missing: {missing} images")


# ---------- Example Usage ----------
csv_path = "client_33.csv"  # CSV file containing image paths
output_folder = "copied_images"  # Folder to save copied images

copy_images_from_csv(csv_path, output_folder)
