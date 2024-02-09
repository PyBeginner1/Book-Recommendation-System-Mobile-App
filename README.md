# Book Recommendation System Mobile App

## Overview

This mobile app empowers bookworms to discover their next great read with the help of a **powerful recommendation system**. Utilizing the **Nearest Neighbors algorithm**, the app analyzes your input (book title or selection from a list) and suggests similar books based on your preferences. Streamlit provides a user-friendly interface for a smooth and engaging experience.

## Features:

* **Nearest Neighbors Algorithm:** Leverages the power of this AI technique to uncover hidden gems and familiar favorites aligned with your reading taste.
* **Intuitive Interface:** Streamlit makes interacting with the app effortless, allowing you to search, browse, and explore recommendations seamlessly.
* **Mobile-Friendly:** Enjoy personalized recommendations anytime, anywhere on your mobile device.

## Getting Started:

### Prerequisites:

1. **Python Installation:** Ensure you have Python installed on your system. You can check this by running `python --version` in your terminal. If not installed, download and install it from https://www.python.org/downloads/.
2. **Dependency Installation:** Once Python is set up, run the following command in your terminal to install the necessary libraries:

```bash
pip install -r requirements.txt
```


This command will install all the Python packages needed for the app to function properly, including Streamlit and other relevant libraries.

## Next Steps:

1. **Run the App:** Navigate to the directory containing your app's code and run the main script using the following command:

```bash
streamlit run app.py
```

Replace `app.py` with the actual name of your main script if it's different.

2. **Explore Recommendations:** Open your web browser and access `http://localhost:8501` to launch the app. Type in a book title or select one from the dropdown list, then click "Show Recommendations" to discover your personalized suggestions!

## Dependencies

* Python
* Streamlit
* **Other:** Please refer to `requirements.txt` for a complete list of necessary dependencies.

## Acknowledgments: 

* **Scikit-learn:** We are grateful to the Scikit-learn team for providing the powerful Nearest Neighbors algorithm, enabling us to offer accurate and personalized book recommendations. (https://scikit-learn.org/)
* **Streamlit:** A big thank you to the Streamlit developers for creating such a user-friendly and efficient framework for building our mobile app's interface. Their work has made it possible to deliver a smooth and enjoyable experience for bookworms exploring new reads. (https://streamlit.io/)