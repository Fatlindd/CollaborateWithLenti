import streamlit as st
import pandas as pd
import requests
from typing import Dict
import io


class SearchApp:
    def __init__(self) -> None:
        """Initialize the SearchApp with static data."""
        # Sample dataset for keyword-based job search
        self.search_by_keyword = pd.DataFrame([
            {"Keyword": "Python Developer", "Location": "New York", "URL": "https://example.com/job1"},
            {"Keyword": "Data Analyst", "Location": "San Francisco", "URL": "https://example.com/job2"},
            {"Keyword": "Machine Learning Engineer", "Location": "Austin", "URL": "https://example.com/job3"},
            {"Keyword": "Web Developer", "Location": "Los Angeles", "URL": "https://example.com/job4"},
        ])

        # Sample dataset for URL-based job contact information search
        self.search_by_url = pd.DataFrame([
            {"Category": "IT", "Contact": "John Doe", "Email": "john@example.com", "Phone Number": "+1-555-1234", "URL": "https://example.com/it-job1"},
            {"Category": "Finance", "Contact": "Jane Smith", "Email": "jane@example.com", "Phone Number": "+1-555-5678", "URL": "https://example.com/finance-job2"},
            {"Category": "Marketing", "Contact": "Alice Brown", "Email": "alice@example.com", "Phone Number": "+1-555-8765", "URL": "https://example.com/marketing-job3"},
            {"Category": "Engineering", "Contact": "Bob Johnson", "Email": "bob@example.com", "Phone Number": "+1-555-4321", "URL": "https://example.com/engineering-job4"},
        ])
    
    def render_header(self) -> None:
        """Render the title of the app."""
        st.title(":iphone: Application for searching")

    def render_search_by_keyword(self) -> None:
        """Render the Search by Keyword tab."""
        st.warning(":zap: Give keyword and location to get list of urls!")

        keyword = st.text_input("Enter keyword:")
        location = st.text_input("Enter location:")

        if st.button("Search", key="search_keyword", help="Click to search to display 100 results from google, you can extract them in a csv file."):
            st.info("Feature under development.")
        
        self.show_results(self.search_by_keyword)

        # Add "Extract to CSV" button with a unique key
        self.add_download_button(self.search_by_keyword, key="keyword_csv_button")

    def render_search_by_url(self) -> None:
        """Render the Search by URL tab."""
        st.warning(":zap: Enter url get information like category, email, contact and phone number!")


        url = st.text_input("Enter URL:")

        if st.button("Search", key="search_url",  help="Click to search to display 100 results from google, you can extract them in a csv file."):
            if url:
                # Instead of scraping, mock data for the URL search
                scraped_data = {
                    "Contact": "Extracted Contact Name",
                    "Email": "contact@example.com",
                    "Phone Number": "+1-123-456-7890"
                }
                # Convert mock scraped data into a DataFrame for display consistency
                self.search_by_url = pd.DataFrame([scraped_data])
            else:
                st.warning("Please enter a valid URL.")
        
        self.show_results(self.search_by_url)
        
        # Display suggested improvements to the user
        self.show_suggestions()

        # Add "Extract to CSV" button with a unique key
        self.add_download_button(self.search_by_url, key="url_csv_button")

    def add_download_button(self, df: pd.DataFrame, key: str) -> None:
        """Add a button to download the DataFrame as a CSV."""
        # Convert DataFrame to CSV
        csv = df.to_csv(index=False)

        # Create a download button with a unique key
        st.download_button(
            label="Extract to CSV",
            data=csv,
            file_name="data.csv",
            mime="text/csv",
            key=key  # Unique key for each download button
        )

    def show_suggestions(self) -> None:
        """Show suggested improvements in a well-styled text area."""
        improvement_text = """
        - Ensure the contact information is up-to-date and correctly formatted.
        - Add more contact channels (LinkedIn, Twitter, WhatsApp).
        - Improve the website’s "Contact Us" page for better accessibility.
        - Verify email deliverability to avoid bounced emails.
        """
        st.text_area("Improvements", improvement_text, height=150, disabled=True)

    def scrape_contact_info(self, url: str) -> Dict[str, str]:
        """Mock method to simulate scraping without BeautifulSoup."""
        # For the purposes of this example, let's return mock data instead of scraping.
        # You can replace this with any other method you prefer.
        return {
            "Email": "contact@example.com",
            "Phone": "+1-123-456-7890",
        }

    def show_results(self, df: pd.DataFrame) -> None:
        """Display results in a well-formatted table."""
        st.divider()
        st.subheader("Results")

        # Start row numbering from 1
        df.index = df.index + 1
        
        # Apply custom CSS for better table styling
        st.markdown(
            """
            <style>
            table {
                border-collapse: collapse;
                width: 100%;
            }
            thead th {
                background-color: #574964 !important;
                color: white !important;
                text-align: left;
                padding: 10px;
            }
            tbody td {
                padding: 10px;
                border: 1px solid #ddd;
            }
            </style>
            """,
            unsafe_allow_html=True,
        )

        # Display the DataFrame as a table
        st.table(df)

    def run(self) -> None:
        """Run the entire Streamlit app."""
        self.render_header()

        # Create tabs for different search functionalities
        tab1, tab2 = st.tabs(["Search By Keyword", "Search By URL"])

        with tab1:
            self.render_search_by_keyword()
        with tab2:
            self.render_search_by_url()


# Entry point to run the Streamlit app
if __name__ == "__main__":
    app = SearchApp()
    app.run()
