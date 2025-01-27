# SnapIt

SnapIt is a user-friendly web-based image filter application built using **Streamlit**. It allows users to upload images, apply various filters, and download the customized images instantly. Perfect for enhancing your pictures with unique and attractive effects!

## Features

- **Upload Your Image**: Supports JPG, PNG, and JPEG file formats.
- **Filters Available**:
  - Original (No Filter)
  - Grayscale
  - Sepia
  - Blur
  - Contrast
- **Real-Time Preview**: Instantly preview your edited image after applying filters.
- **Download Filtered Images**: Save your filtered images directly to your device.
- **Customizable Background**: An aesthetic app design with a spring-season-themed background.

## Getting Started

Follow these instructions to run SnapIt on your local machine for development and testing purposes.

### Prerequisites

- Python (>= 3.7)
- pip (Python package manager)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/snapit.git
   cd snapit
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Run the App

1. Start the Streamlit server:
   ```bash
   streamlit run app.py
   ```
2. Open the URL displayed in the terminal (usually `http://localhost:8501`) in your web browser to access SnapIt.

## Usage

1. Open the SnapIt web interface.
2. Upload an image file (JPG, PNG, or JPEG).
3. Choose your desired filter from the sidebar.
4. Preview the filtered image.
5. Click the **Download** button in the sidebar to save the edited image.

## Example



## Technologies Used

- **Streamlit**: For building the web app
- **Pillow (PIL)**: For image processing
- **Python**: The backbone of the project

## Customization

To update the app appearance or behavior:

- Modify the `st.markdown` CSS styles in the app source code.
- Add additional filters or image enhancement techniques in the sidebar section.

## Contributing

Contributions are welcome! Follow these steps to contribute:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/new-feature
   ```
3. Make changes and commit them:
   ```bash
   git commit -m "Add some new feature"
   ```
4. Push the branch:
   ```bash
   git push origin feature/new-feature
   ```
5. Open a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- Inspired by the beauty of spring and creative image processing
