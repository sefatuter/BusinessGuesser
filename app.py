import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import streamlit as st

@st.cache_data
def train_model(data):
    # Load and process data
    data['NumCompaniesWorked'].fillna(data['NumCompaniesWorked'].mean(), inplace=True)
    data['TotalWorkingYears'].fillna(data['TotalWorkingYears'].mean(), inplace=True)
    
    X = data.drop(['Attrition', 'EmployeeID'], axis=1)
    X = pd.get_dummies(X)  # Convert categorical variables to dummy variables
    y = data['Attrition'].apply(lambda x: 1 if x == 'Yes' else 0)  # Convert target variable to binary format
    
    # Split into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Create and train the model
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)
    
    return model, X.columns.tolist()

def main():
    st.markdown("# Employee Attrition Prediction")
    st.markdown("Upload your CSV file to train the model.")
    
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        model, feature_columns = train_model(data)
        st.write("Model trained successfully!")
        st.write(f"Features used: {feature_columns}")

if __name__ == '__main__':
    main()
