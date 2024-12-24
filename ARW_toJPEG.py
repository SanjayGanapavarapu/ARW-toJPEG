import os
import rawpy
from PIL import Image


def convert_arw_to_jpeg(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith('.arw'):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + '.jpeg')

            try:
                # Load the RAW file
                with rawpy.imread(input_path) as raw:
                    rgb_image = raw.postprocess()

                # Convert to JPEG and save
                image = Image.fromarray(rgb_image)
                image.save(output_path, 'JPEG', quality=90)
                print(f"Converted: {filename} -> {output_path}")
            except Exception as e:
                print(f"Error converting {filename}: {e}")


if __name__ == "__main__":
    input_folder = input("Enter the path to the folder containing .ARW files: ")
    output_folder = input("Enter the path to the folder where .JPEG files will be saved: ")

    convert_arw_to_jpeg(input_folder, output_folder)
    print("Conversion completed, Please check the inserted output directory")
