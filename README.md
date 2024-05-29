# ModelMatch

ModelMatch is a web-based application that recommends AI/ML models based on user requirements. By leveraging data scraped from Hugging Face, the application filters and suggests models that best match the user’s needs.

## Features

- **Personalized Recommendations:** Provides tailored model suggestions based on specific user input.
- **Detailed Metadata:** Displays comprehensive model information including downloads, author, creation date, and more.
- **User-Friendly Interface:** An intuitive web interface for easy input and viewing of recommendations.
- **Direct Links:** Facilitates direct access to recommended models on Hugging Face.
- **Extensive Filtering:** Ensures high-quality recommendations by sorting based on downloads and other criteria.

## Data Collection

The data for the models is collected using web scraping with Beautiful Soup from Hugging Face. Exploratory Data Analysis (EDA) is performed on the dataset to understand model specifications and distributions.

## Recommendation System

The recommendation system uses cosine similarity to match user requirements with model specifications. The top 10 models are suggested based on the similarity score and filtered by downloads in descending order.

## Challenges Addressed

1.**Model Overload**: Filters and recommends models based on user input, reducing the overwhelming number of choices.

2.**Time-Consuming Research**: Automates the process of gathering and comparing model specifications.

3.**Inconsistent Model Information**: Consolidates metadata in one place, providing a uniform view.

4.**Lack of Model Comparison Tools**: Includes a comparison feature to help developers make informed decisions.


## Benefits for Developers

1.**Enhanced Productivity**: Automates the recommendation and comparison process, allowing developers to focus on building.
   
2.**Centralized Information**: Reduces the need to visit multiple sites to gather information.

3.**Educational Tool**: Exposes developers to a variety of models and applications.

4.**Scalable and Adaptable**: Easily updated with new models and datasets.

## Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/Adarshh9/ModelMatch.git
    cd ModelMatch
    ```

2. **Set up a virtual environment:**
    ```sh
    conda create --name modelmatch python=3.12
    conda activate modelmatch
    ```

3. **Install the required packages:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Download the `vector_db.pickle` file:**
    - Download the `vector_db.pickle` file from [Google Drive](https://drive.google.com/file/d/1ZBlk3g-x50AUOff4gXqJ4oR21RMyE0cM/view?usp=sharing) and place it in the 'Data' directory of the project.

## Usage

1. **Run the Flask application:**
    ```sh
    python app.py
    ```

2. **Access the application in your browser:**
    ```
    http://127.0.0.1:5000/
    ```

3. **Provide your requirements** by selecting the following fields:
   - **Task Type**, **Task**, **Model Type**, **Framework**

   Click "Get Recommendations" to view the suggested models.

## Project Structure

- `app.py`: Main application script using Flask.
- `utils.py`: Helper functions for loading data and recommending models.
- `templates/index.html`: HTML template, CSS styles, JavaScript for handling form submission and displaying recommendations for the web interface.
- `vector_db.pickle`: The vector database file needed for recommendations (download from Google Drive).

## Example

### Input:
Provide inputs in the following fields:
- **Task Type** (e.g., "Natural Language Processing")
- **Task** (e.g., "Text Classification")
- **Model Type** (e.g., "Transformer")
- **Framework** (e.g., "PyTorch")

### Output:
List of recommended models with the following details:
- **Model ID**
- **Author**
- **Downloads**
- **Likes**
- **Created At**
- **Tags (first 5 words)**
- **Direct link to the model on Hugging Face**

## Demo

Check out a live demonstration of the ModelMatch application on YouTube: [ModelMatch Demo](https://youtu.be/4Rfqje5_KHw)

[![ModelMatch Demo](https://img.youtube.com/vi/4Rfqje5_KHw/0.jpg)](https://youtu.be/4Rfqje5_KHw)

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the [GNU](LICENSE) License.

## Acknowledgements

- [Hugging Face](https://huggingface.co/) for providing the models and APIs.
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/) for web scraping.
- [Flask](https://flask.palletsprojects.com/) for the web framework.

---

### Contact

For any questions or suggestions, please contact at [email](akesherwani900@gmail.com).
