
# MicrobiotaDB  

MicrobiotaDB is a Django-based web application designed to manage and visualize data on the impact of plants, bioactive compounds, and extracts on microorganisms. The platform offers powerful search, filtering, and detailed data exploration features to support research and analysis in microbiology and phytochemistry.

---

## Features  

- **Plants Database**:  
  - View and explore plant records.  
  - Search by common name, scientific name, or microorganism name.  
  - Display counts of associated microorganism records.  
  - Detailed side-frame views for individual plants.  

- **Compounds Database**:  
  - Search for compounds by name or microorganism.  
  - Table view with key information.  
  - Detailed view of compound impact on microorganisms.  

- **Extracts Database**:  
  - Search and browse extracts.  
  - Display all available fields in the database with clean formatting.  

- **Pagination**:  
  - Infinite scroll via a "Load More" button for seamless navigation.  

- **Null Value Handling**:  
  - Fields with null values are displayed as "Not Defined" for better readability.  

- **Contact Us**:  
  - Page with supervisor details:  
    - **DSc, Prof. Nadiya Boyko**  
    - **Email**: nadiya.boyko@uzhnu.edu.ua  

---

## Technology Stack  

- **Frontend**: HTML, CSS, Django Templates  
- **Backend**: Django  
- **Database**: SQLite (or replace as needed)  
- **Additional Tools**: Bootstrap for styling  

---

## Setup  

Follow these steps to set up the project locally:  

### Prerequisites  
1. Python 3.x  
2. Django 4.x  
3. Virtual Environment (Recommended)  

### Installation  

1. Clone the repository:  
   ```bash  
   git clone https://github.com/obsessixnv/microbiotadb.git  
   cd microbiotadb  
   ```  

2. Set up a virtual environment:  
   ```bash  
   python3 -m venv venv  
   source venv/bin/activate   # On Windows: venv\Scripts\activate  
   ```  

3. Install dependencies:  
   ```bash  
   pip install -r requirements.txt  
   ```  

4. Apply migrations:  
   ```bash  
   python manage.py migrate  
   ```  

5. Load initial data (optional):  
   ```bash  
   python manage.py loaddata initial_data.json  
   ```  

6. Run the development server:  
   ```bash  
   python manage.py runserver  
   ```  

7. Visit the app at:  
[http://localhost:8000][(](https://microbiotadb-a6d80522104e.herokuapp.com/))]([http://localhost:8000][(](https://microbiotadb-a6d80522104e.herokuapp.com/)))  

---

## Usage  

- Navigate to `/plants`, `/compounds`, or `/extracts` to explore respective datasets.  
- Use the search bar for filtering data.  
- Click on a record to view detailed information in a side-frame (if applicable).  
- View contact information in the "Contact Us" section.  

---

## Contribution  

Contributions are welcome! Please follow these steps:  

1. Fork the repository.  
2. Create a new branch:  
   ```bash  
   git checkout -b feature-branch-name  
   ```  
3. Commit your changes:  
   ```bash  
   git commit -m "Add feature or fix description"  
   ```  
4. Push to the branch:  
   ```bash  
   git push origin feature-branch-name  
   ```  
5. Open a Pull Request.  

---

## License  

This project is licensed under the [MIT License](LICENSE).  

---

## Acknowledgments  

This project is supervised by:  
- **DSc, Prof. Nadiya Boyko**  

For further inquiries, contact **nadiya.boyko@uzhnu.edu.ua**.  

---  
