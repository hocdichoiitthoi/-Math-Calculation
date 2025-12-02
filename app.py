import streamlit as st
import math

# Web app configuration
st.set_page_config(page_title="Calculator Online", page_icon="🧮")

st.title("🧮 Calculator Online")

# Initialize session state for history
if 'calculation_count' not in st.session_state:
    st.session_state.calculation_count = 0
if 'history' not in st.session_state:
    st.session_state.history = []

# Create 2 columns for better layout
col1, col2 = st.columns(2)

with col1:
    num1 = st.number_input("Enter the first number (a)", value=0.0)
with col2:
    num2 = st.number_input("Enter the second number (b)", value=0.0)

# Choose operation
operation = st.selectbox(
    "Choose operation",
    ("Add (+)", "Subtract (-)", "Multiply (*)", "Divide (/)",
     "Power (a^2)", "Power (a^3)", "Power (a^b)", 
     "Square root of a", "Cube root of a", "bth root of a",
     "Sin(a)", "Cos(a)", "Tan(a)", "Cot(a)")
)

result = None

# Handle calculation when button is pressed
if st.button("Calculate"):
    try:
        if operation == "Add (+)":
            result = num1 + num2
        elif operation == "Subtract (-)":
            result = num1 - num2
        elif operation == "Multiply (*)":
            result = num1 * num2
        elif operation == "Divide (/)":
            if num2 != 0:
                result = num1 / num2
            else:
                st.error("Error: Cannot divide by zero")
        elif operation == "Power (a^2)":
            result = math.pow(num1, 2)  
        elif operation == "Power (a^3)":
            result = math.pow(num1, 3)          
        elif operation == "Power (a^b)":
            result = math.pow(num1, num2)
        elif operation == "Square root of a":
            if num1 >= 0:
                result = math.sqrt(num1)
            else:
                st.error("Error: Cannot calculate the square root of a negative number")
        elif operation == "Cube root of a":
            result = num1 ** (1/3)
        elif operation == "bth root of a":
            if num2 != 0 and (num2 % 2 != 0 or num1 >= 0):
                result = num1 ** (1/num2)
            elif num2!= 0 and num2 % 2 == 0 and num1 <0:
                st.error("Error: Cannot calculate even root of a negative number")    
            else:
                st.error("Error: Cannot calculate the zeroth root")    
        elif operation == "Sin(a)":
            # Convert degrees to radians
            radians = math.radians(num1)
            result = math.sin(radians)
        elif operation == "Cos(a)":
            # Convert degrees to radians
            radians = math.radians(num1)
            result = math.cos(radians)
        elif operation == "Tan(a)":
            # Convert degrees to radians
            radians = math.radians(num1)
            result = math.tan(radians)
        elif operation == "Cot(a)":
            # Convert degrees to radians
            radians = math.radians(num1)
            if math.tan(radians) != 0:
                result = 1 / math.tan(radians)
            else:
                st.error("Error: Cotangent is undefined for this input")
        # Show result
        if result is not None:
            # Round to 10 decimal places to avoid floating point precision issues
            rounded_result = round(result, 10)
            st.success(f"Result: {rounded_result}")
            st.session_state.history.insert(0, expression := f"{operation.replace('(a)', f'({num1})').replace('(b)', f'({num2})')} = {rounded_result}")
            st.session_state.calculation_count += 1

    except Exception as e:
        st.error(f"An error occurred: {e}")

st.divider() # Draw a horizontal line
st.subheader("📜 History of recent calculations")

if len(st.session_state.history) > 0:
    for item in st.session_state.history:
        st.text(item) # Print each history item
else:
    st.write("No calculations yet.")

st.write(f"Total calculations performed: {st.session_state.calculation_count}")