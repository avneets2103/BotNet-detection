import streamlit as st 
import pickle
# import keras
import pandas as pd
from matplotlib import pyplot as plt
# import dangerDetection
dfx = pd.read_csv("TestDx.csv")
dfy = pd.read_csv("TestDy.csv")
plt.style.use("ggplot")

df_master = ["Danger Detection", "Type Detection"]
col_master = st.sidebar.selectbox("Select a Differentiator: ",df_master)

if(col_master == "Danger Detection"):
    df = ["ANN", "Random Forest", "RNN", "SVM", "XGBoost"]
    col = st.sidebar.selectbox("Select a model: ",df)
    
    if(col == "ANN"):
        st.markdown("# Artificial Neural Network")
        st.markdown(""" This page shows the predictions on test data split. The predictions are made on
     randomly generated data subsets. Choose the models you would like to view accuracy
     for: """)
        st.subheader("")
        ANN_test = st.slider('ANN Test Data ', 1, 10, 1) 
        
        if st.button("Predict ANN Danger"):
            
            with open('ANNDanger.pkl','rb') as file:
                ann = pickle.load(file)
            # clf = joblib.load("ANNDanger.joblib")
            sampled_df = dfx.sample(ANN_test) 
            predictions = ann.predict(sampled_df)
                
            # st.dataframe(dataframe, width = 1800)
            st.table(predictions)
        
        
        
        
    # if(col == "Random Forest"):
    #     rfDanger.rfDanger()
    # if(col == "RNN"):
    #     rnnDanger.rnnDanger()
    # if(col == "SVM"):
    #     svmDanger.svmDanger()
    # if(col == "XGBoost"):
    #     xgbDanger.xgbDanger()



# if(col == "Ensembling Models"):
#     st.title("Ensembling Models")
#     st.text(""" This page shows the predictions on test data split. The predictions are made on
#  randomly generated data subsets. Choose the models you would like to view accuracy
#  for: """)
#     st.subheader("")

#  # st.header(“Plant Features”)
#     col1, col2 = st.columns(2)
#     with col1:
#         st.markdown("**ANN**")
#         ANN_test = st.slider('ANN Test Data (%)', 5, 50, 1)
    
#     with col2:
#         st.markdown("**Random Forest**")
#         RF_test = st.slider('RF Test Data (%)', 5, 50, 1)
    
#     col3, col4 = st.columns(2)
#     with col3:
#         st.markdown("**RNN**")
#         ANN_test = st.slider('RNN Test Data (%)', 5, 50, 1)
    
#     with col4:
#         st.markdown("**SVM**")
#         RF_test = st.slider('SVM Test Data (%)', 5, 50, 1)
        
#     st.markdown("**XGBoost**")
#     SGB_test = st.slider('XGBoost Test Data (%)', 5, 50, 1)
      

# if(col == "Confusion Matrices"):
#     st.title("Confusion Matrices")
#     st.markdown("""  The confusion matrix provides a summary of the predictions made by a classification model, comparing them to the actual true values. This information is useful in calculation precision and recall of our model. This matrix gives us an idea about how accurate our model is working when trained on a given dataset.""")
    
#     st.markdown("### **ANN**")
#     # image_path = "./Images In Paper/9. Danger ANN confusion matrix.png"
#     image_path = "dog.jpg"
#     st.image(image_path, use_column_width=True)
    
    
#     data = {
#         'Index': [1,2,3,4],
#         'Attributes': ['True Positive (TP)', 'True Negative (TN)', 'False Positive (FP)', 'False Negative (FN)'],
#         'Count': [1.5e5, 1.5e5, 23, 50]
#     }

#     # Create DataFrame
#     df = pd.DataFrame(data).set_index('Index')

#     # Display as a table
#     st.table(df)
        
    
# #     st.text(''' true positive (TP): 1.5e+05
# #  true negative (TN): 1.5e+05
# #  false positive (FP): 23
# #  false negative (FN): 50''')
#     st.markdown("<br>", True)
    
#     st.markdown("### **Random Forest**")
#     # image_path = "./Images In Paper/9. Danger ANN confusion matrix.png"
#     image_path = "dog.jpg"
#     st.image(image_path, use_column_width=True)
    
#     data = {
#         'Index': [1,2,3,4],
#         'Attributes': ['True Positive (TP)', 'True Negative (TN)', 'False Positive (FP)', 'False Negative (FN)'],
#         'Count': [1.5e+05, 1.5e+05, 45, 77]
#     }

#     # Create DataFrame
#     df = pd.DataFrame(data).set_index('Index')

#     # Display as a table
#     st.table(df)
    
#     st.markdown("<br>", True)
    
#     st.markdown("### **RNN**")
#     # image_path = "./Images In Paper/9. Danger ANN confusion matrix.png"
#     image_path = "dog.jpg"
#     st.image(image_path, use_column_width=True)
#     st.markdown("<br>", True)
    
#     st.markdown("### **SVM**")
#     # image_path = "./Images In Paper/9. Danger ANN confusion matrix.png"
#     image_path = "dog.jpg"
#     st.image(image_path, use_column_width=True)
#     st.markdown("<br>", True)
    
#     st.markdown("### **XGBoost**")
#     # image_path = "./Images In Paper/9. Danger ANN confusion matrix.png"
#     image_path = "dog.jpg"
#     st.image(image_path, use_column_width=True)
#     st.markdown("<br>", True)
    
#     # col1, col2 = st.columns(2)
    
#     # with col1:
#     #     st.markdown("**ANN**")
#     #     # image_path = "./Images In Paper/9. Danger ANN confusion matrix.png"
#     #     image_path = "dog.jpg"
#     #     st.image(image_path, use_column_width=True)
    
#     with col2:
#         st.markdown("**Random Forest**")
        
    
#     col3, col4 = st.columns(2)
#     with col3:
#         st.markdown("**RNN**")
        
    
#     with col4:
#         st.markdown("**SVM**")
        
        
#     st.markdown("**XGBoost**")
    
       

