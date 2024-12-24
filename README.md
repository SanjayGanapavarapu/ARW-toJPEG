# ARW-toJPEG
Phyton code to convert Sony's ARW picture file type to JPEG

This lightweight code is designed to automate the conversion of Sony .ARW (RAW) image files into .JPEG files in batch from a local file location, instead of uploading and downloading the photos from sketchy websites.
## Features
- Converts Sony `.ARW` files to `.JPEG` format.
- Batch processing for multiple files in a directory.
- Utilizes `rawpy` for RAW image decoding.
- Leverages `Pillow` for efficient `.JPEG` image creation.

---

## Installation

### Prerequisites
Ensure you have Python installed. You can download it from [python.org](https://www.python.org/).

### Clone the Repository
```bash
git clone git clone https://github.com/SanjayGanapavarapu/ARW-toJPEG.git
cd ARW-toJPEG
```

### Install Dependencies
```bash
pip install -r requirements.txt
```
or 
```bash

pip install rawpy pillow
```
---

## Usage

### Command Line
Run the following command to convert `.ARW` files in a specified folder:

```bash
python ARW_toJPEG.py
--input <input_folder>
--output <output_folder>
```

### Example
```bash
python ARW_toJPEG.py
```
```
--input C:\Users\"Name"\Pictures\RAW
--output C:\Users\"Name"\Pictures\JPEG
```

### Arguments
- `--input`: Path to the folder containing `.ARW` files.
- `--output`: Path to the folder where `.JPEG` files will be saved.

---

## Libraries and Extensions Used

### Libraries
1. **rawpy**  
   - Used for decoding `.ARW` files.  
   - License: [MIT License](https://github.com/letmaik/rawpy/blob/main/LICENSE)

2. **Pillow**  
   - Used for processing and saving `.JPEG` files.  
   - License: [Pillow License](https://github.com/python-pillow/Pillow/blob/main/LICENSE)

### File Extensions
- **Input:** `.ARW`
- **Output:** `.JPEG`

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Contributions
Contributions are welcome! Please follow these steps to contribute:
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m 'Add feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Open a pull request.

---

## Citations
This project is built upon open-source tools. Special thanks to:
- The [rawpy library](https://github.com/letmaik/rawpy)
- The [Pillow library](https://python-pillow.org/)

---

## Disclaimer
This tool is designed for educational and non-commercial purposes. Please ensure compliance with all applicable software and image licensing agreements.

---

## Support
If you encounter any issues or have questions, feel free to open an [issue](https://github.com/SanjayGanapavarapu/ARW-toJPEG/issues) in this repository.

## TLDR;
Lightweight code to convert Sony's `.ARW` to `.JPEG`

follow above steps or manual below:

* Ensrue python is installed and all other needed dependencies. (Version used 13.13.1)
* check the "requirments.txt" for libraries needed and install using follwing code.
```bash

pip install rawpy pillow
```
* Download "ARW_toJPEG.py" .
* Open CMD and cd to directory with `.py` file.
* Follow  "Usage" commands to run. 


